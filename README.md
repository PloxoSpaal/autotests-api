# API Course Automation Tests

This project implements automated tests for
the [API Course Test Server](https://github.com/Nikita-Filonov/qa-automation-engineer-api-course). The
tests are written using **Python**, **Pytest**, **Allure**, **Pydantic**, **Faker** and **HTTPX**. The test
application’s source code is available on [GitHub](https://github.com/Nikita-Filonov/qa-automation-engineer-api-course).

## Project Overview

The goal of this project is to automate the testing of the API Course server, focusing on REST API testing. The
automated tests verify various functionalities of the application to ensure its stability and correctness.

This project is specifically designed for API autotests, incorporating best practices such as:

- API Clients for structured interaction with endpoints,
- Pytest fixtures for reusable and maintainable test setups,
- Pydantic models for strict data validation,
- Schema validation to ensure API contract correctness,
- Fake data generation to simulate real-world scenarios,
- And more advanced techniques to improve test efficiency and reliability.
- The project structure follows industry standards to ensure clarity, maintainability, and scalability of the test code.

## Getting Started

### Clone the Repository

To get started, clone the project repository using Git:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Create a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies. Follow the instructions for your operating
system:

#### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

Once the virtual environment is activated, install the project dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Running the Tests with Allure Report Generation

To run the tests and generate an Allure report, use the following command:

```bash
pytest -m "regression" --alluredir=./allure-results
```

This will execute all tests in the project and display the results in the terminal.

### Viewing the Allure Report

After the tests have been executed, you can generate and view the Allure report with:

```bash
allure serve allure-results
```

This command will open the Allure report in your default web browser.