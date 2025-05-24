# 🐳 FastAPI + MySQL Docker Setup

This project uses Docker Compose to orchestrate a FastAPI application and a MySQL database.

## 📦 Requirements

- [Docker CE](https://docs.docker.com/get-docker/)
- [Docker Compose CLI](https://docs.docker.com/compose/)

---

## 🚀 Running the Project

1. **Build the containers:**

   ```bash
   docker compose build
   ```

2. **Start the MySQL service in detached mode:**

   ```bash
   docker compose up -d mysql
   ```

3. **Start the FastAPI application:**

   ```bash
   docker compose up api
   ```

---

## 🌐 API URL

Once running, the FastAPI application will be available at:

```
http://0.0.0.0:8000
```

You can access the interactive documentation at:

```
http://0.0.0.0:8000/docs
```

---

## 🛑 Stopping the services

To stop all running containers:

```bash
docker compose down
```