import os
import pandas as pd
pd.options.plotting.backend = "plotly"

import seaborn as sns

import matplotlib.pyplot as plt
from scipy.stats.stats import spearmanr, pearsonr

from util import mask_corr_graphic

class GraficoCorrelacao:

    def __init__(self, x: str, y: str, df_to_plot: pd.DataFrame) -> None:
        self.__x = x
        self.__y = y
        self.__df_to_plot = df_to_plot

    def __grafico_correla_geral(self, hue_df: str) -> sns.axisgrid.JointGrid:
        ''' Gráfico geral '''
        g = sns.jointplot(
                x=self.__x,
                y=self.__y,
                hue=hue_df,
                height=10,
                data=self.__df_to_plot
        )
        # print(type(g))
        return g

    def __grafico_correla_resalta(
        self,
        instance_to_highlight: str,
        color: str,
        graph: sns.JointGrid) -> None:
        ''' Resaltando o melhor valor encontrado no notebook 01-daods_infra '''
        highlight_x = self.__df_to_plot.loc[instance_to_highlight, self.__x]
        highlight_y = self.__df_to_plot.loc[instance_to_highlight, self.__y]
        graph.ax_joint.scatter(
            highlight_x,
            highlight_y,
            color=color,
            s=200
        )

    def __grafico_correla_reg(self, graph: sns.JointGrid) -> None:
        ''' Inserindo a regressão linera '''
        sns.regplot(
                x=self.__x,
                y=self.__y,
                data=self.__df_to_plot,
                ax=graph.ax_joint,
                scatter=False
        )
    
    def __grafico_correla_add_componentes(
        self,
        title: str,
        labels: tuple,
        graph: sns.JointGrid) -> None:
        ''' Componentes adicionais ao gráfico '''
        graph.fig.suptitle(title)
        graph.fig.tight_layout()
        graph.set_axis_labels(labels[0], labels[1])
    
    def __grafico_correla_calcula_statistica(self) -> list:
        ''' Análise estatistica das Séries de dados '''
        df_to_plot_copy = self.__df_to_plot.dropna()
        x_select = df_to_plot_copy[self.__x]
        y_select = df_to_plot_copy[self.__y]
        r, p = pearsonr(x_select, y_select)
        r = round(r, 3)
        p = round(p, 3)
        if p < 0.01:
            values_legend = [f"R² = {r}\np < 0,01"]
        else:
            values_legend = [f"R² = {r}\np = {p}"]
        return values_legend
    
    def __grafico_correla_plota_statistica(self) -> None:
        ''' Plotando a legenda com as 
        análises estatístcias de correlação '''
        values_legend = self.__grafico_correla_calcula_statistica()
        leg = plt.legend(
                values_legend,
                bbox_to_anchor=(-0.1, 1.225),
                loc='upper left',
                handletextpad=0,
                handlelength=0
        )
        for item in leg.legendHandles:
            item.set_visible(False)
    
    def __save_figure(self, file_name: str) -> None:
        dir_name = "./results/"
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        plt.savefig(
            dir_name+file_name,
            format="png",
            dpi=600,
            bbox_inches="tight"
        )
    
    def grafico_correla(
        self,
        title: str,
        labels: tuple,
        instance_to_highlight: str = "",
        color: str = "",
        hue_df: str = None,
        file_name: str = None,
        save_file: bool = False) -> None:
        ''' Plotagem do Gráfico de Correlação '''
        sns.set(rc={"figure.figsize": (15,15)}, font_scale=1.5)
        
        # Gráfico geral
        g = self.__grafico_correla_geral(hue_df=hue_df)
        
        # Inserindo a regressão linera
        self.__grafico_correla_reg(graph=g)
        
        if color != "":
            self.__grafico_correla_resalta(
                instance_to_highlight=instance_to_highlight,
                color=color,
                graph=g
            )
        
        # Componentes adicionais ao gráfico
        self.__grafico_correla_add_componentes(
            title=title,
            labels=labels,
            graph=g
        )
        
        # Análise estatistica das Séries de dados
        self.__grafico_correla_plota_statistica()
        
        if save_file:
            self.__save_figure(file_name=file_name)
        
        # Plotagem final do gráfico
        plt.show(g)

    def grafico_heatmap(self, title: str) -> None:
        sns.set(rc={"figure.figsize": (5,5)}, font_scale=1)
        
        correlation = self.__df_to_plot.corr()

        g = sns.heatmap(
            correlation,
            cmap="YlGnBu",
            annot=True,
            mask=mask_corr_graphic(len(correlation)),
            vmax=1,
            vmin=-1
        )
        g.set_title(title)
        
        plt.show(g)
    
    def grafico_boxplot(self) -> None:
        
        g = self.__df_to_plot[[self.__x,self.__y]].boxplot()

        plt.show(g)