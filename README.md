Documentation:

Project Overview:

Project Name: SMS Management and Monitoring System

Description: A full-stack web application to manage SMS sending sessions across different country-operator pairs, monitor SMS metrics, and alert on critical issues. The system is built with a Flask backend, React frontend, MongoDB and MySQL databases, and uses Prometheus and Grafana for monitoring.

Functional Requirements:

User Authentication: Secure API endpoints using JWT.
Process Management: Start, stop, and restart SMS sessions programmatically.

Country-Operator Management: CRUD operations to add, remove, or update country-operator pairs.

Real-Time Metrics: Retrieve SMS sent, success rates, and errors.

Alerts and Notifications: Send alerts on critical issues using Telegram.

Frontend Dashboard: Display metrics, manage sessions, and visualize data.

API Documentation

Authentication Endpoints

Login

Endpoint: /login
Method: POST
Request Body:

json
{
  "username": "string",
  "password": "string"
}

Response:
access_token: JWT token to be used in Authorization headers.
Protected Endpoints (Use JWT in Authorization header):

Add, retrieve, update, delete country-operator pairs.
Control SMS program sessions.
Country-Operator Endpoints
Add Country-Operator

Endpoint: /country-operator
Method: POST
Request Body:

json
{
  "country": "string",
  "operator": "string",
  "is_high_priority": boolean
}

Response:
Success message with status code 201.
Get All Country-Operators

Endpoint: /country-operator
Method: GET

Response:
JSON array of country-operator pairs.
Delete Country-Operator

Endpoint: /country-operator/<country>/<operator>
Method: DELETE

Response:
Success message with status code 200.
Alert Endpoints
Trigger Alert

Endpoint: /alert
Method: POST
Request Body:

Copy code
{
  "message": "string"
}

Response:
Success message confirming alert sent.
Database Schema
MongoDB:

Database: sms_config
Collection: country_operator
Fields:
country: String
operator: String
is_high_priority: Boolean
MySQL:

Database: sms_metrics
Table: sms_metrics
Fields:
id: INT (Primary Key)
country: VARCHAR(10)
operator: VARCHAR(50)
sms_sent: INT
success_rate: FLOAT
failures: INT
timestamp: TIMESTAMP (Defaults to current timestamp)

Frontend Functionality
Dashboard: Displays real-time SMS metrics, with options to start, stop, and restart programs.

Program Control: Interface to manage SMS programs.
Country-Operator Management: Interface to add, update, and remove country-operator pairs.
Authentication: Login page secured with JWT.

Running the Project:

Start MongoDB and MySQL: Ensure both databases are running locally.

Run Flask:

Update the values of the following in app.py:
JWT_SECRET_KEY="SECRET_KEY"
MONGO_URL="mongodb://localhost:27017/"
MYSQL-host="localhost"
MYSQL_USER="your_mysql_user"
MYSQL_PASSWORD="your_mysql_password"
MYSQL_DB="sms_metrics"

Start the Flask app with flask run.

Run React:
Start the frontend with npm start.

Trigger Alerts:
Configure and test Telegram notifications.
This documentation should provide a comprehensive guide for setting up, running, and maintaining the SMS Management System. Let me know if you'd like more details on any specific part!