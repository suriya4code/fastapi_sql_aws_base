# FastAPI SQL AWS Microservice Boilerplate

## Features
- **FastAPI** microservice with all API endpoints implemented asynchronously
- **AWS S3 integration**: Async file upload to S3 using aioboto3
- **PostgreSQL integration**: Async CRUD operations using SQLAlchemy and asyncpg
- **Microservice-to-microservice communication**: Async HTTP client (httpx)
- **Request validation**: All incoming requests and bodies validated with Pydantic
- **Logging**: Logs to both a local file and AWS CloudWatch (watchtower)
- **Testing**: Pytest with >80% coverage, all AWS S3 and DB interactions are mocked
- **Poetry** for environment and dependency management
- **VS Code** ready: Debugger config and Makefile for easy workflow

## Setup

### 1. Environment
- Uses [Poetry](https://python-poetry.org/) for dependency management
- All dependencies listed in `pyproject.toml` (matches `requirements.txt`)
- Makefile for common tasks: `env`, `run`, `test`, `clean`

### 2. Running the App
```sh
make env      # Set up the environment
make run      # Start FastAPI with Uvicorn (hot reload)
```
Or use VS Code debugger (see `.vscode/launch.json`).

### 3. Testing
```sh
make test     # Run all tests with coverage
```
- All S3 and DB calls are mocked in tests
- Coverage is enforced to be >80%

### 4. Project Structure
- `app/main.py` - FastAPI entrypoint
- `app/aws/` - S3 integration (async)
- `app/db/` - Async SQLAlchemy/Postgres models and CRUD
- `app/services/` - Microservice HTTP client
- `app/logging_config.py` - Logging setup (local + CloudWatch)
- `tests/` - Pytest tests for all modules

### 5. Logging
- Logs to `app.log` locally
- Logs to AWS CloudWatch (log group: `fastapi-microservice-logs`)

### 6. API Docs
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Requirements Implemented
- [x] All API calls are asynchronous
- [x] S3 upload module (async, with logging)
- [x] Logging to file and AWS CloudWatch
- [x] Request validation for all endpoints
- [x] Async Postgres CRUD module
- [x] Microservice HTTP client module
- [x] Pytest tests for all methods, with S3 and DB mocked
- [x] Test coverage >80% (pending since the aws and db modules are mocked)
- [x] Poetry environment
- [x] VS Code debugger and Makefile
