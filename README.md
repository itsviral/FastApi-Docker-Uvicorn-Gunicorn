# FastApi-Docker-Conda-Uvicorn-Gunicorn

This repository provides an example of how to build, containerize, and deploy a FastAPI application using Docker, Conda for environment management, Uvicorn as the ASGI server, and Gunicorn for handling production-level deployments.

## Project Overview

This project is designed to demonstrate how to efficiently set up a FastAPI application, containerize it using Docker, and deploy it with Uvicorn and Gunicorn. Additionally, it includes instructions for setting up Oracle as the database using a Docker container.

## Project Structure

- **app/**: Contains the main application code and configurations.
  - **config/**: Configuration files for the FastAPI application.
    - `config.py`: Configuration settings for the application.
  - **logger/**: Logging setup for the application.
    - `logger.py`: Configuration for logging, including custom formats and log levels.
  - **logs/**: Directory where log files are stored.
    - `app.log`: Application logs.
    - `gunicorn_error_access.log`: Logs for Gunicorn errors and access logs.
  - **test/**: Test files for the FastAPI application.
    - `test_main.py`: Python test script for the main application.
    - `test_main.http`: HTTP test script for testing the API endpoints.
  - `main.py`: The main FastAPI application file.
  - `__init__.py`: Marks the app directory as a package.

- **Dockerfile**: Defines the Docker image build process for containerizing the application.
- **docker-compose.yml**: Docker Compose file for managing multi-container Docker applications, useful for running the app in development or production.
- **gunicorn_server_config.py**: Gunicorn configuration file, setting up the number of workers, threads, and other server settings.
- **requirements.txt**: A list of Python dependencies needed for the project (if using pip for dependency management).
- **conda/environment.yml**: Conda environment file listing dependencies, allowing you to replicate the environment in a Conda environment.
- **LICENSE**: The project's license (MIT License).
- **.dockerignore**: Specifies files and directories that should be ignored by Docker when building the image.
- **.gitignore**: Specifies files and directories that should be ignored by Git.
- **README.md**: This file, providing an overview of the project and setup instructions.

## Docker Setup

### Creating Docker Networking

If you need to create a Docker network, use the following command:

```bash
docker network create my-network
```

### Build Docker Image

To build the Docker image from the root directory of this repository, use:

```bash
docker build -t fastapi:v1 .
```

You can check the images with:

```bash
docker images
```

### Run Docker Container

Run the container using the image built:

```bash
docker run -p 8000:8000 --name fastapi fastapi:v1
```

If you want to run the container on a specific network:

```bash
docker run -d --name container1 --network=my-network fastapi:v1
```

### Oracle Database Setup

You can set up an Oracle database using the following commands:

```bash
docker pull gvenzl/oracle-free
docker run -d -p 1521:1521 -e ORACLE_PASSWORD=oracle gvenzl/oracle-free
docker ps -a
docker exec <container_name|id> resetPassword oracle
```

## Docker Management Commands

Here are some useful Docker commands for managing containers and images:

- Stop all running containers:

  ```bash
  docker stop $(docker ps -q)
  ```

- Remove all stopped containers:

  ```bash
  docker rm $(docker ps -a -q)
  ```

- Remove all Docker images:

  ```bash
  docker rmi $(docker images -q)
  ```

- Prune the system to remove unused data:

  ```bash
  docker system prune
  ```

- Stop and remove all containers using Docker Compose:

  ```bash
  docker-compose down
  ```

- Start containers with Docker Compose:

  ```bash
  docker-compose up
  ```

## Logging

Logging is configured to output both application logs and Gunicorn error/access logs to files located in the `app/logs/` directory. This setup ensures that you can monitor and debug your application effectively.

## Testing

You can run tests using the test scripts located in the `app/test/` directory. These include both Python-based tests and HTTP requests to test your API endpoints.

To run the Python tests:

```bash
pytest app/test/test_main.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request if you have any improvements or suggestions.

## Contact

If you have any questions or need further assistance, feel free to reach out via GitHub or connect with me on LinkedIn.
