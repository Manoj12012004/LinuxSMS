Here's a comprehensive, step-by-step guide to setting up and running your Flask-based SMS Management System, focusing on MongoDB, MySQL, Flask, and React. 

---

# SMS Management System Documentation

### Project Overview
A web-based SMS management system that allows users to control and monitor SMS sessions across different country-operator pairs, using a Flask backend, React frontend, MongoDB, MySQL, and Telegram notifications.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Project Setup](#project-setup)
   - Backend Setup (Flask)
   - Database Setup (MongoDB and MySQL)
   - Frontend Setup (React)
3. [Running the Project](#running-the-project)
4. [API Endpoints](#api-endpoints)
5. [Testing the System](#testing-the-system)
6. [Configuration](#configuration)
7. [Alerts](#alerts)
8. [Troubleshooting](#troubleshooting)

---

### 1. Prerequisites

Ensure the following software is installed:
- **Python 3.8+**
- **Node.js & npm**
- **MongoDB** (running locally or accessible on a server)
- **MySQL** (running locally or accessible on a server)
- **Telegram Bot** for alerts (optional but recommended)

---

### 2. Project Setup

#### A. Backend Setup (Flask)

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Linux/macOS
   venv\Scripts\activate      # On Windows
   ```

3. **Install backend dependencies**:
   ```bash
   pip install Flask pymongo mysql-connector-python Flask-JWT-Extended requests
   ```

4. **Create `.env` file**:
   In the project root, create a `.env` file to store configuration variables:
   ```env
   JWT_SECRET_KEY="your_jwt_secret"
   MONGO_URI="mongodb://localhost:27017/"
   MYSQL_HOST="localhost"
   MYSQL_USER="your_mysql_user"
   MYSQL_PASSWORD="your_mysql_password"
   MYSQL_DB="sms_metrics"
   TELEGRAM_BOT_TOKEN="your_telegram_bot_token"
   TELEGRAM_CHAT_ID="your_telegram_chat_id"
   ```

#### B. Database Setup (MongoDB and MySQL)

1. **MongoDB**:
   - Start MongoDB if it isn’t running:
     ```bash
     mongod
     ```
   - MongoDB will automatically create the `sms_config` database and `country_operator` collection when accessed by the app.

2. **MySQL**:
   - Log into MySQL:
     ```bash
     mysql -u root -p
     ```
   - Create the `sms_metrics` database and table:
     ```sql
     CREATE DATABASE sms_metrics;
     USE sms_metrics;
     
     CREATE TABLE sms_metrics (
         id INT AUTO_INCREMENT PRIMARY KEY,
         country VARCHAR(10),
         operator VARCHAR(50),
         sms_sent INT,
         success_rate FLOAT,
         failures INT,
         timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
     );
     ```

#### C. Frontend Setup (React)

1. **Navigate to the frontend directory**:
   ```bash
   cd sms-dashboard
   ```

2. **Install frontend dependencies**:
   ```bash
   npm install
   ```

3. **Set up environment variables**:
   - Create a `.env` file in the frontend directory and add the backend URL:
     ```env
     REACT_APP_API_URL=http://localhost:5000
     ```

---

### 3. Running the Project

#### A. Start the Backend (Flask)

1. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

2. **Run the Flask app**:
   ```bash
   flask run
   ```
   - By default, the app will be accessible at `http://localhost:5000`.

#### B. Start the Frontend (React)

1. **Navigate to the frontend directory** (if not already there):
   ```bash
   cd sms-dashboard
   ```

2. **Run the React app**:
   ```bash
   npm start
   ```
   - The frontend will be accessible at `http://localhost:3000`.

---

### 4. API Endpoints

| Endpoint                  | Method | Description                         | Requires JWT |
|---------------------------|--------|-------------------------------------|--------------|
| `/login`                  | POST   | Authenticates user, returns token. | No           |
| `/country-operator`       | POST   | Adds a country-operator pair.      | Yes          |
| `/country-operator`       | GET    | Retrieves all pairs.               | Yes          |
| `/country-operator/<id>`  | DELETE | Deletes a specific pair.           | Yes          |
| `/alert`                  | POST   | Sends a Telegram alert.            | Yes          |

#### Example API Request
- **Login**:
  ```http
  POST /login
  {
    "username": "admin",
    "password": "password"
  }
  ```
- **Add Country-Operator**:
  ```http
  POST /country-operator
  {
    "country": "UZ",
    "operator": "uzmobile",
    "is_high_priority": true
  }
  ```

---

### 5. Testing the System

#### Authentication Test
1. Go to `http://localhost:3000/login`.
2. Enter your credentials. If successful, you’ll be redirected to the dashboard.

#### CRUD Operations
- Add, update, or delete country-operator pairs via the frontend or using API requests.

#### Alert Test
- Trigger an alert by calling the `/alert` endpoint or testing with a critical failure.

---

### 6. Configuration

To adjust settings, modify the `.env` file for each component:
- **Backend**: Update JWT secret, database credentials, and Telegram bot details.
- **Frontend**: Update the backend API URL in the `.env` file.

### 7. Alerts

Configure Telegram for real-time alerts:
1. Create a Telegram bot via BotFather and retrieve the bot token.
2. Get your chat ID by messaging the bot and using an API to retrieve your ID.
3. Update `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` in the backend `.env` file.

---

### 8. Troubleshooting

- **MongoDB/ MySQL Connection Errors**: Verify credentials and connection strings.
- **CORS Errors**: Add CORS headers in Flask using `flask-cors` if necessary.
- **JWT Issues**: Ensure the `JWT_SECRET_KEY` is properly configured.

---

This setup should provide a solid foundation for running and testing the SMS Management System. Let me know if you have any questions or run into issues along the way!