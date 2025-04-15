# Flask Docker Application with Redis Integration

A Flask application Dockerized and integrated with Redis for caching. The application provides endpoints to check status and count visits.

## Part 1: Flask Application in Docker

### Build the Docker Image
```bash
docker build -t flasker .
```

### Run the Container
```bash
docker run -it -p 5000:5000 flasker
```

### Test the `/ping` Endpoint
```bash
curl http://localhost:5000/ping
```

**Expected Output**:
```json
{
  "status": "ok"
}
```

### Stop the Container
```bash
docker stop flasker
```

---

## Part 2: Docker Compose with Redis Integration

### Run Services
⚠️ **Ensure previous containers are stopped to avoid port conflicts**.
```bash
docker compose up -d
```

### Test Endpoints
1. Check the `/ping` endpoint:
   ```bash
   curl http://localhost:5000/ping
   ```

2. Check the `/count` endpoint (uses Redis to track visits):
   ```bash
   curl http://localhost:5000/count
   ```

### Teardown Services
```bash
docker compose down
```

