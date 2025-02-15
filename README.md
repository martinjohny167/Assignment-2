
Database Automation and CI/CD Pipeline 🚀
Overview 📝
This project automates database schema changes and implements a CI/CD pipeline for deploying changes to an AWS RDS MySQL database. It consists of:

SQL Automation: Python script to create and modify a projects table in the database.
CI/CD Pipeline: GitHub Actions to automatically deploy database changes on push to the main branch.
Files 📂
automate_sql.py: Python script to create a projects table and add a budget column.
.github/workflows/ci_cd_pipeline.yml: GitHub Actions workflow to execute the Python script.
add_departments.sql: SQL script to add a departments table (for testing).
Setup 🛠️
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/your-username/your-repository.git
cd your-repository
Install Python dependencies:

bash
Copy
Edit
pip install mysql-connector-python
Add Repository Secrets 🔐:

Go to Settings > Secrets in GitHub.
Add the following secrets:
DB_HOST: RDS endpoint
DB_USER: Database username
DB_PASSWORD: Database password
DB_NAME: Database name
Workflow ⚙️
The workflow runs on every push to the main branch.
It sets up the environment, installs dependencies, and runs automate_sql.py to apply database changes.
Testing ✅
Push a change to the main branch. The GitHub Actions workflow will run and update your RDS database.

Documentation 📚
The full setup and testing details are documented in the attached PDF.

