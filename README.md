# 🐍 Python CI Demo

A simple Python project demonstrating **CI/CD with Jenkins and Docker** on Windows.  
This repository shows how to build, test, and report results for a Python project using **Jenkins pipelines** and **Docker containers**.

---

## 📌 Features

- **Python functionality:**
  - Simple math functions: `add(a, b)`, `multiply(a, b)`
  - Utility function: `is_even(n)`  
- **Testing:**
  - Unit tests written with **pytest**
  - Automatic test report generation (`results.xml`)  
- **CI/CD Pipeline:**
  - Automated Docker image build
  - Running tests inside a Docker container
  - Publishing test results to Jenkins
  - Container kept for inspection after the run
- **GitHub integration:**
  - Trigger Jenkins builds on push or PR
  - Example of CI workflow for Python projects

## 🐳 Docker Integration

The Jenkins pipeline builds a Docker image `python-ci-demo` from this project, mounts the workspace inside the container, and executes tests:

📂 Project Structure
├── app.py             # Main Python application
├── test_app.py        # Pytest unit tests
├── requirements.txt   # Python dependencies
├── Jenkinsfile        # Jenkins pipeline definition
└── README.md          # Project documentation
