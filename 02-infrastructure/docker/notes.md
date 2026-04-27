# Docker

## Core Concepts
*What Docker is and why*

**Container** – Isolated process with its own filesystem, network, and resources  
**Image** – Read-only template used to create containers  
**Dockerfile** – Script with instructions to build an image  
**Registry** – Storage for images (Docker Hub, ECR, GCR)  
**Docker Engine** – Runtime that builds and runs containers

**VM vs Container**:

| | VM | Container |
|---|---|---|
| Isolation | Full OS | Process-level |
| Size | GBs | MBs |
| Startup | Minutes | Seconds |
| Overhead | High | Low |

---

## Images
*Templates for containers*

```bash
docker pull nginx               # download from registry
docker images                   # list local images
docker rmi nginx                # remove image
docker build -t myapp:1.0 .     # build from Dockerfile
docker tag myapp:1.0 myapp:latest
```

### Image Layers
*Each instruction adds a layer*

```dockerfile
FROM python:3.11-slim    # base layer
COPY . /app              # new layer
RUN pip install flask    # new layer
```

Layers are cached — if a layer hasn't changed, Docker reuses it. Put rarely-changing instructions first.

---

## Dockerfile
*Instructions to build an image*

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
```

### Key Instructions

**FROM** – Base image  
**WORKDIR** – Set working directory inside container  
**COPY** – Copy files from host to image  
**RUN** – Execute command during build (creates layer)  
**EXPOSE** – Document which port the app uses  
**ENV** – Set environment variable  
**CMD** – Default command when container starts  
**ENTRYPOINT** – Fixed command, CMD becomes its arguments

**CMD vs ENTRYPOINT**:

```dockerfile
# CMD — overridable
CMD ["python", "main.py"]
# docker run myapp python other.py  ← overrides CMD

# ENTRYPOINT — fixed command
ENTRYPOINT ["python"]
CMD ["main.py"]
# docker run myapp other.py  ← runs: python other.py
```

---

## Containers
*Running instances of images*

```bash
docker run nginx                          # run container
docker run -d nginx                       # detached (background)
docker run -p 8080:80 nginx               # map host:container port
docker run -e DB_URL=postgres nginx       # env variable
docker run -v /host/path:/app/data nginx  # bind mount

docker ps                    # list running containers
docker ps -a                 # all containers (including stopped)
docker stop <id>             # stop gracefully
docker rm <id>               # remove stopped container
docker logs <id>             # view logs
docker exec -it <id> bash    # open shell inside container
```

---

## Volumes
*Persistent data outside containers*

**Bind Mount** – Host directory mapped into container  
**Named Volume** – Docker-managed storage, survives container removal

```bash
# Named volume
docker volume create mydata
docker run -v mydata:/app/data myapp

# Bind mount
docker run -v $(pwd)/data:/app/data myapp

docker volume ls
docker volume rm mydata
```

Use named volumes for databases and persistent state. Use bind mounts for development (live code reload).

---

## Networking
*How containers communicate*

**bridge** – Default. Containers on same network can talk by name  
**host** – Container shares host network (Linux only)  
**none** – No networking

```bash
docker network create mynet
docker run --network mynet --name db postgres
docker run --network mynet --name api myapp
# api can reach db at hostname "db"

docker network ls
docker network inspect mynet
```

---

## Docker Compose
*Multi-container apps defined in one file*

```yaml
# docker-compose.yml
services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

```bash
docker compose up -d       # start all services
docker compose down        # stop and remove containers
docker compose down -v     # also remove volumes
docker compose logs api    # logs for one service
docker compose ps          # status of services
docker compose build       # rebuild images
```

---

## .dockerignore
*Exclude files from build context*

```
__pycache__/
*.pyc
.env
.git
node_modules/
*.log
```

Reduces image size and avoids sending secrets to the build context.

---

## Best Practices

- Use official slim base images (`python:3.11-slim`, `node:20-alpine`)
- Copy `requirements.txt` before code to maximize layer caching
- One process per container
- Never store secrets in images — use env vars or secrets managers
- Use `.dockerignore` to keep images small
- Tag images with versions (`myapp:1.2.0`), not just `latest` in production
- Use `COPY` instead of `ADD` unless you need tar extraction
