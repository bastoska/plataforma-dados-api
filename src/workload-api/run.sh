#!/bin/bash

## variáveis
container_name=workload-api
image_name=$container_name:1.0
requirements_image_name=$container_name-requirements:1.0

# função para exibir ajuda
show_help() {
cat << EOF
Uso: ${0##*/} {build|build_reqs|build_run|build_test|run|test|help}

Este script gerencia containers e imagens Docker para a API workload.

Comandos:
    build           Constrói a imagem Docker para a aplicação.
    build_reqs      Constrói a imagem Docker para os requisitos.
    build_run       Constrói a imagem Docker e executa o container da aplicação.
    build_test      Constrói a imagem Docker e executa o container de testes.
    run             Executa o container da aplicação.
    test            Executa o container de testes.
    help            Exibe esta mensagem de ajuda e sai.

Exemplos:
    ./${0##*/} build          # Constrói a imagem Docker para a aplicação.
    ./${0##*/} build_run      # Constrói a imagem Docker e executa o container da aplicação.
    ./${0##*/} test           # Executa o container de testes.

EOF
}

build_requirements_image () {
  docker image build -f DockerfileRequirements -t $requirements_image_name .
}

build_image () {
  ## função para construir a imagem do APP

  ## verificando se a imagem de requirements está construída antes de prosseguir
  if docker image inspect $requirements_image_name > /dev/null 2>&1; then
    docker image build -t $image_name .
    
  else
    echo "Erro: A imagem $requirements_image_name não existe. Por favor, construa-a primeiro usando 'build_reqs'."
    exit 1
  fi
}

up_container () {
  ## função para executar o container do app

  ## verificando se a imagem do APP está construída antes de prosseguir
  if docker image inspect $image_name > /dev/null 2>&1; then
    docker rm -f $container_name
    docker run -d -p 8080:8080 -v ./volume/data:/app/app/data --name $container_name $image_name
    docker logs -f $container_name

  else
    echo "Erro: A imagem $image_name não existe. Por favor, construa-a primeiro usando 'build' ou use o comando 'build_run'."
    exit 1
  fi
}

up_container_test () {
  ## função para executar os testes

  ## verificando se a imagem do APP está construída antes de prosseguir
  if docker image inspect $image_name > /dev/null 2>&1; then
    container_name=workload-api-test
    docker run --rm --name $container_name $image_name pytest

  else
    echo "Erro: A imagem $image_name não existe. Por favor, construa-a primeiro usando 'build' ou use o comando 'build_test'."
    exit 1
  fi
}

build_run () {
  ## função para construir a imagem e executar o container da API
  build_image
  up_container
}

build_test () {
  ## função para construir a imagem e executar o container de testes da API
  build_image
  up_container_test
}

case $1 in
  build)
    build_image
    ;;
  build_reqs)
    build_requirements_image
    ;;
  build_run)
    build_run
    ;;
  build_test)
    build_test
    ;;
  run)
    up_container
    ;;
  test)
    up_container_test
    ;;
  help|-h|--help)
    show_help
    ;;
  *)
    echo "Erro: Comando inválido."
    show_help
    exit 1
    ;;
esac
