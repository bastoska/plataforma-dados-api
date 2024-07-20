

up_container () {
  container_name=workload_api
  image_name=$container_name:1.0

  docker rm -f $container_name

  docker image build -t $image_name .

  docker run -d -p 8080:8080 -v ./volume/data:/app/app/data --name $container_name $image_name

  docker logs -f $container_name
}


up_container