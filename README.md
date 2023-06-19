# FastApi-Docker-Uvicorn-Gunicorn


# If Need to create Docker Networking 
# docker network create my-network
docker build -t fastapi:v1 .
docker images
docker run -d --name container1 --network=mynetwork d72d12a88ed4


# Build Docker Image from the docker Root File of Repo
docker build -t fastapi:v1 .
docker run -p 8000:8000 fastapi:v1 --name fastapi

# Setup Oracle Image 
docker pull gvenzl/oracle-free
docker run -d -p 1521:1521 -e ORACLE_PASSWORD=oracle gvenzl/oracle-free
docker ps -a
docker exec <container name|id> resetPassword oracle

# Docker run and stop commands
docker stop $(docker ps -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)
docker system prune
docker-compose down
docker-compose up