# Azure AI Sales Data Assistant

A cloud-hosted Python application that combines data analysis with Azure AI to answer natural-language questions about sales data.

LIVE DEMO: https://sarah-ai-cloud-assistant-cugkfpc0cxgbgyab.westus3-01.azurewebsites.net/ 

## Project Overview

This project was created as a portfolio project to explore how AI and cloud services can be integrated into a practical Python application.

The current application works with a small sales dataset stored as a CSV file.

Users can ask questions such as:

- Which product made the most money?
- Which product sold the most?
- What is the total revenue?

The application interprets the question using an Azure-hosted GPT model and then uses Python/pandas to calculate the correct result.

## Architecture

The application follows a simple flow:

1. User interface — Streamlit: Users view sales metrics, explore a revenue chart, and enter questions.
2. AI interpretation — Azure AI: GPT-4.1-mini classifies natural-language questions into supported categories.
3. Data processing — Python and pandas: The application loads the CSV dataset, calculates revenue, and retrieves the requested results.
4. Cloud hosting — Azure App Service: The application is hosted as a web application and can be accessed through its public URL.
5. Deployment automation — GitHub Actions: A workflow installs project dependencies and deploys changes to Azure when code is pushed to the main branch.

User
  │
  ▼
Streamlit Web Dashboard
  │
  ▼
Azure AI - GPT-4.1-mini
  │
  ▼
Question classification
  │
  ├── highest_revenue
  ├── most_units
  └── total_revenue
  │
  ▼
Python + pandas
  │
  ▼
Sales data (CSV)
  │
  ▼
Calculated result

## Current Features

The application can:

- Load sales data from a CSV file
- Calculate product revenue
- Identify the product with the highest revenue
- Identify the product with the most units sold
- Calculate total revenue
- Understand natural-language questions
- Classify questions using an Azure-hosted GPT model
- Perform the actual calculations locally with Python and pandas

## Technologies

- Python — application logic and data processing
- pandas — data manipulation and calculations
- Microsoft Azure AI — natural-language question classification
- GPT-4.1-mini — AI model used to interpret questions
- Streamlit — interactive web dashboard
- Azure App Service — cloud hosting
- Azure Identity — authentication to Azure AI services
- Git and GitHub — version control and source code management
- CSV — sample data storage

## Example Questions

Which product made the most money? 

Result:

Product with the highest revenue:
Laptop
Revenue: €30,000

The AI is used to understand the user's intent. The numerical result is calculated by Python and pandas based on the underlying dataset.

## Project Structure

Sarah-s-ai-cloud-journey/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── data/
    └── sales.csv

##Getting Started

1. Clone the repository

git clone https://github.com/sarahasg19/Sarah-s-Coding-Journey.git
cd Sarah-s-Coding-Journey

2. Create a virtual environment

python3 -m venv .venv

3. Activate the virtual environment

source .venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

5. Authenticate with Azure

The application uses Azure Identity for authentication.

For local development, authenticate with the Azure CLI:

az login

6. Run the dashboard

python -m streamlit run streamlit_app.py

## Project Status

Status: Deployed portfolio prototype — ongoing development.

The current version supports a defined set of sales-related questions. Expanding the range of supported questions and improving error handling are potential next steps.

## Learning Objectives

This project explores:

- Integrating generative AI into a Python application
- Combining AI-based intent classification with deterministic data analysis
- Building interactive data applications with Streamlit
- Hosting Python applications on Microsoft Azure
- Using managed identities for cloud authentication
- Automating deployment with GitHub Actions
- Documenting and maintaining a cloud-based software project
