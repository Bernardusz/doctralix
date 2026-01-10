# Doctralix
> A robust Django & PostgreSQL based LMS for schools and organizations.
## Prerequisites
- Git
- Python
- Postgres
- Docker
- Docker Compose
- Redis (Future)

## Instalation & Setup
- Clone the repo:  
```bash
git clone https://github.com/Bernardusz/doctralix.git
```
- Copy the ```.env.example``` then create both ```.env``` and ```.env.prod```: 
```bash
cp .env.example .env
cp .env.example .env.prod
```
- Build and start the container: 
```bash
docker compose -f docker-compose.dev.yml up -d --build
```
or
```bash
docker compose -f docker-compose.prod.yml up -d --build
```
- Access the site at: [http://localhost:8000](http://localhost:8000)

## 🛠️ Common Commands

**Run Migrations:**
```bash
docker exec -it doctralix_backend python manage.py migrate
```
**Create a Superuser:**
```bash
docker exec -it doctralix_backend python manage.py createsuperuser
```

## Tech stacks used
- Backend: Django 
- Databse: PostgreSQL
- In-Memory Store: Redis (Planned)



## Environtment Variable

| .env key       | Usage  |
|----------------|--------|
| POSTGRES_USER  | A username for your Postgres user |
| POSTGRES_PASSWORD | A password for your Postgres user  |
| POSTGRES_DB  |  A name for your DB instance  |
| DB_HOST  |  The name to access DB container  |
| DB_PORT  |  The port in which the DB will be running  |
| DEBUG  |  The key to either turn on/turn off DEBUG mode in Django |
| SECRET_KEY  |  Django secret key |
| ALLOWED_HOSTS  |  The hosts in which your Django can interact with |

## License
> Licensed under the [MIT License](LICENSE)

## Note
> Made with caffeine and jokes ☕ 🐧💀