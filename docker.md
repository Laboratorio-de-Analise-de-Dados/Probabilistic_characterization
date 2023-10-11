# Instalação

## Instalação docker

> curl -fsSL https://get.docker.com | sh

## Instalação docker-compose

> sudo apt-get update && sudo apt-get install -y docker-compose

## Permitir acesso ao docker de usuário sudo

> sudo usermod -aG docker `<nome do usuário>`
> su - `<nome do usuário>`
> id -nG

# Comandos básicos de construção

## Baixar uma imagem

> docker pull `<nome da imagem>:<versão>`

## Construção de imagem com base no Dockerfile.

> docker build -t `<nome tag da imagem>` .

## Construir um container com base na imagem

> docker run --name `<nome do container>` `<nome tag da imagem>`

## Construir um container interativo (-it)

* -it -> interação pelo terminal
* --rm -> remover após a execusão
* --name -> nome do container
* -v -> volumes no mapeados no container
* -w -> diretório de trabalho no container
* -p -> portas mapeadas no container
* -P -> portas aleatórias mapeadas no container
* -e -> variável de ambiente

> docker run -it --rm --name `<nome do container>` -v ${pwd}:/local/no/container -w /local/no/container -p `<porta saída>`:`<porta saída>` -e AUTHOR="GFS" `<nome da imagem>`/bin/bash

## Usar o bash de em um container, removendo após o uso

> docker run -it --rm `<nome tag da imagem>` /bin/bash

## Ativar um container

> docker start `<nome do container>`

## Interagir com um container sem iniciar antes

> docker start -a -i `<nome do container>`

## Executar o bash de um container ativo

> docker exec -it `<nome do container>` /bin/bash

## Executar um arquivo com o container ativo

> docker exec `<nome do container>` `<nome do programa>` `<nome do arquivo>`

## Contruindo imagens com docker-compose

> docker-compose build

## Contruindo containers com docker-compose

> docker-compose up

## Verificando containers com docker-compose

> docker-compose ps

# Comandos básicos de acesso

## Imagens

### Lista das images

> docker images

### Lista ids das images

> docker images -q

## Containers

### Lista dos containers rodando

> docker ps

### Lista os ids dos containers rodando

> docker ps -q

### Lista todos os containers

> docker ps -a

### Lista todos os ids de todos os containers

> docker ps -a -q

## Informações sobre o container

> docker inspect `<nome do container>`

# Comandos básicos de função

## Imagens

### Remove imagem

> docker rmi -f `<nome da imagem>`

### Remove todas as imagens

> docker rmi -f $(docker images -q)

## Containers

### Inicia container inativo

> docker start `<nome do container>`

### Inicia todos os containers inativos

> docker start $(docker ps -a -q)

### Reinicia container inativo

> docker restart `<nome do container>`

### Reinicia todos os containers inativos

> docker restart $(docker ps -a -q)

### Para container inativo

> docker stop `<nome do container>`

### Para todos os containers inativos

> docker stop $(docker ps -a -q)

### Remove container inativo

> docker rm `<nome do container>`

### Remove container inativo

> docker container prune

### Remove todos os containers inativos

> docker rm $(docker ps -a -q)

# Docker composer

## Instala imagens e containers

> docker compose up

## Deleta containers

> docker compose down
