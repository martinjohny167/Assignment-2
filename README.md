# Database Automation and CI/CD Pipeline 🚀

## Overview 📝

This project automates database schema changes and implements a CI/CD pipeline for deploying changes to an **AWS RDS MySQL** database. It leverages a Python script for automating SQL operations and GitHub Actions for continuous integration and deployment.

### Key Features:
1. **SQL Automation**: A Python script (`automate_sql.py`) that:
   - Creates a `projects` table in the MySQL database.
   - Adds a `budget` column to the existing `projects` table.
   
2. **CI/CD Pipeline**: A GitHub Actions workflow (`ci_cd_pipeline.yml`) that:
   - Runs automatically when changes are pushed to the `main` branch.
   - Executes SQL scripts on an AWS RDS MySQL instance.

## Files 📂

- **`automate_sql.py`**: Python script to automate database schema creation and modification.
- **`.github/workflows/ci_cd_pipeline.yml`**: GitHub Actions workflow configuration to trigger the automation process.
- **`add_departments.sql`**: SQL script to add a `departments` table (for testing CI/CD deployment).

## Workflow ⚙️

The GitHub Actions workflow runs on every push to the `main` branch. It performs the following steps:

1. **Set up the environment**:
   - Install the `mysql-connector-python` package.
   - Configure the MySQL environment.

2. **Run the Python Script**:
   - Executes the SQL commands in `automate_sql.py` to create and modify tables in your RDS database.

## Testing ✅

1. After setting up the repository and adding the secrets, **push a change to the `main` branch**.
2. The GitHub Actions workflow will be triggered automatically, and the SQL scripts will be executed on your AWS RDS instance.

You can check the progress and logs of the workflow under the **Actions** tab in GitHub.

## Full Setup Instructions 📚

### 1. Setting Up AWS RDS:
- Create an RDS instance in the AWS Console.
- Use **MySQL** as the database engine.
- Configure the security group to allow access from GitHub Actions (or your local machine if testing locally).
- Create a new database (`companydb`).

### 2. Setting Up GitHub Actions:
- In your GitHub repository, go to **Settings > Secrets** and add the following secrets:
  - `DB_HOST`: The RDS endpoint of your instance (e.g., `database-1.cyvg56cxbepj.us-east-1.rds.amazonaws.com`).
  - `DB_USER`: The database username (e.g., `admin`).
  - `DB_PASSWORD`: The password for the database.
  - `DB_NAME`: The database name (e.g., `companydb`).
  
- Add the workflow file `.github/workflows/ci_cd_pipeline.yml` that will automate the process of executing SQL scripts to your RDS MySQL instance.

### 3. Testing the Workflow:
- After setting up the repository and secrets, you can test the process by pushing a new change to the `main` branch.
- The workflow will trigger and automatically apply the SQL changes to the RDS MySQL database.
  
You can check the workflow logs by going to the **Actions** tab in your GitHub repository.

## Notes ⚠️

- Ensure that your RDS instance allows inbound traffic from GitHub Actions by configuring the security group settings properly.
- You can test SQL script execution by modifying the scripts in the repository and pushing the changes to the `main` branch.

---

