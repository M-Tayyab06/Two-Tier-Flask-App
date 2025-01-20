# Dockerized Flask App with MySQL Database

This project demonstrates the deployment of a simple Flask application with a MySQL database using Docker. The application accepts user input via a web interface, stores the input in a MySQL database, and displays stored entries. The entire setup leverages Docker networks for seamless communication between the Flask app and the MySQL database without using Docker Compose.

---

## Project Structure

```plaintext
project-folder/
├── flask-app/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── templates/
│       └── index.html
└── sql-scripts/
    └── init.sql
```

### Directory Descriptions

- **flask-app/**: Contains the Flask application and its dependencies.
  - `app.py`: Main application file.
  - `Dockerfile`: Instructions for building the Docker image for the Flask app.
  - `requirements.txt`: Python dependencies.
  - `templates/index.html`: Frontend HTML file for user input.

- **sql-scripts/**: Contains SQL initialization scripts for the database.
  - `init.sql`: Script to initialize the MySQL database.

---

## Prerequisites

- Docker installed on your machine.

---

## Setup Guide

### Step 1: Create a Docker Network

Create a custom Docker network to allow communication between containers:
```bash
docker network create flask-mysql-network
```

### Step 2: Set Up the MySQL Database

1. Navigate to the `sql-scripts/` directory:
   ```bash
   cd project-folder/sql-scripts
   ```

2. Start a MySQL container:
   ```bash
docker run --name mysql-db \
    --network flask-mysql-network \
    -e MYSQL_ROOT_PASSWORD=root \
    -e MYSQL_DATABASE=custom_db \
    -v "$(pwd):/docker-entrypoint-initdb.d" \
    -d mysql:latest
   ```
   This command:
   - Sets the root password to `root`.
   - Creates a database named `custom_db`.
   - Mounts the `init.sql` script to initialize the database.

### Step 3: Build and Run the Flask Application

1. Navigate to the `flask-app/` directory:
   ```bash
   cd ../flask-app
   ```

2. Build the Flask app Docker image:
   ```bash
   docker build -t flask-app .
   ```

3. Run the Flask app container:
   ```bash
   docker run --name flask-app \
       --network flask-mysql-network \
       -p 5000:5000 \
       -e FLASK_ENV=development \
       -d flask-app
   ```
   This command exposes the application on `http://localhost:5000`.

---

## Application Usage

1. Open your browser and navigate to `http://localhost:5000`.
2. Input data into the form on the homepage and submit.
3. Submitted data is stored in the MySQL database and displayed on the page.

---

## Key Files and Configurations

### `app.py`
This file contains the Flask app logic, handling routes, database connections, and user interactions.

### `Dockerfile`
Defines how the Flask app container is built:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

### `requirements.txt`
Specifies Python dependencies:
```plaintext
Flask
mysql-connector-python
```

### `init.sql`
Initializes the MySQL database with custom tables and configurations.

---

## Notes and Troubleshooting

- **Common Errors and Fixes**:
  - **MySQL container connection issues**: Ensure both containers are on the same Docker network.
  - **Port conflicts**: Ensure ports `5000` (Flask) and `3306` (MySQL) are available.

- Use the following command to inspect the Docker network:
  ```bash
  docker network inspect flask-mysql-network
  ```

---
