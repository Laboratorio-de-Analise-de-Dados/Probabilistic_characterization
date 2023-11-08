# FROM python:3.10.12
FROM gfsilveira/env_docker:v1.8.1

LABEL maintainer="Guilherme F Silveira"

WORKDIR /usr/src/myapp

COPY ./python_req.txt /usr/src/myapp

RUN pip install --upgrade pip && \
    pip install -r python_req.txt

RUN apt-get update -y
RUN apt-get install -y pandoc
RUN apt-get install -y texlive-xetex texlive-fonts-recommended texlive-plain-generic

COPY . /usr/src/myapp

COPY ./JupyterLab-configs/tracker.jupyterlab-settings /root/.jupyter/lab/user-settings/@jupyterlab/notebook-extension/tracker.jupyterlab-settings
COPY ./JupyterLab-configs/themes.jupyterlab-settings /root/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/themes.jupyterlab-settings
COPY ./JupyterLab-configs/plugin.jupyterlab-settings /root/.jupyter/lab/user-settings/@jupyterlab/docmanager-extension/plugin.jupyterlab-settings

EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root"]