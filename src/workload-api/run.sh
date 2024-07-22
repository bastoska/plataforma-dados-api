

up_container () {

  ## variáveis para conter o nome do container e da imagem
  container_name=workload_api
  image_name=$container_name:1.0

  ## removendo o container (caso não exista, ele seguirá para o próximo comando)
  docker rm -f $container_name

  ## construção da imagem
  docker image build -t $image_name .

  ## execução do container em modo deamon
  docker run -d -p 8080:8080 -v ./volume/data:/app/app/data --name $container_name $image_name

  ## visualizar continuamente os logs do container
  docker logs -f $container_name
}

up_container_test () {
  ## variáveis para conter o nome do container e da imagem
  container_name=workload_api-test
  image_name=$container_name:1.0

  ## removendo o container (caso não exista, ele seguirá para o próximo comando)
  docker rm -f $container_name

  ## construção da imagem
  docker image build -f DockerfileTest -t $image_name .

  ## execução do container em modo deamon
  docker run -d --name $container_name $image_name
  
  ## visualizar continuamente os logs do container
  docker logs -f $container_name
}

case $1 in
  up)
    up_container
    ;;
  test)
    up_container_test
    ;;
  *)
    echo "Usage: $0 {up|test|down}"
    ;;
esac