## 🐳 Basic Docker Commands

| Command            | Description                  |
| ------------------ | ---------------------------- |
| `docker --version` | Show Docker version          |
| `docker info`      | Show system-wide information |
| `docker help`      | List Docker commands         |

## 📦 Docker Image Commands

| Command                          | Description                    |
| -------------------------------- | ------------------------------ |
| `docker build -t <name>:<tag> .` | Build image from Dockerfile    |
| `docker images`                  | List all images                |
| `docker pull <image>`            | Download image from Docker Hub |
| `docker rmi <image_id or name>`  | Remove image                   |
| `docker tag <src> <target>`      | Tag an image with a new name   |

## 🚢 Docker Container Commands

| Command                                    | Description                    |
| ------------------------------------------ | ------------------------------ |
| `docker run <image>`                       | Run a container                |
| `docker run -it <image> /bin/bash`         | Run with interactive terminal  |
| `docker run -d -p 80:80 <image>`           | Run detached with port mapping |
| `docker ps`                                | List running containers        |
| `docker ps -a`                             | List all containers            |
| `docker stop <container_id>`               | Stop a running container       |
| `docker start <container_id>`              | Start a stopped container      |
| `docker restart <container_id>`            | Restart container              |
| `docker rm <container_id>`                 | Remove container               |
| `docker exec -it <container_id> /bin/bash` | Access running container shell |
| `docker logs <container_id>`               | View container logs            |

## 🗃️ Volume Commands

| Command                        | Description            |
| ------------------------------ | ---------------------- |
| `docker volume create <name>`  | Create volume          |
| `docker volume ls`             | List volumes           |
| `docker volume inspect <name>` | Inspect volume details |
| `docker volume rm <name>`      | Delete volume          |

## 🌐 Network Commands

| Command                         | Description           |
| ------------------------------- | --------------------- |
| `docker network ls`             | List networks         |
| `docker network create <name>`  | Create custom network |
| `docker network inspect <name>` | View network details  |
| `docker network rm <name>`      | Remove network        |

## 🛠️ Other Useful Commands

| Command                               | Description                                |
| ------------------------------------- | ------------------------------------------ |
| `docker-compose up`                   | Start app using `docker-compose.yml`       |
| `docker-compose down`                 | Stop and remove all services               |
| `docker system prune`                 | Clean up unused containers, networks, etc. |
| `docker inspect <container_or_image>` | Get detailed JSON info                     |
| `docker save -o <file.tar> <image>`   | Save image to tarball                      |
| `docker load -i <file.tar>`           | Load image from tarball                    |
