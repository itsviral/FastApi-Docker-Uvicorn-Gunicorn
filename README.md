# FastApi-Docker-Uvicorn-Gunicorn


# If Need to create Docker Networking 
# docker network create my-network


# Build Docker Image from the docker Root File of Repo
docker build -t fastapi:v1 .
Docker images
docker run -d --name container1 --network=mynetwork d72d12a88ed4


# Setup Oracle Image 
docker pull gvenzl/oracle-free
docker run -d -p 1521:1521 -e ORACLE_PASSWORD=oracle gvenzl/oracle-free
docker ps -a
docker exec <container name|id> resetPassword oracle
