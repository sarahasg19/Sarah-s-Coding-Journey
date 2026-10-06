# AI Cloud Data Assistant

A Python-based AI data assistant that combines local data analysis with Microsoft Azure AI.

The application allows users to ask natural-language questions about sales data. Azure OpenAI is used to understand and classify the user's question, while Python and pandas perform the actual data analysis.

## Project Overview

This project was created as a portfolio project to explore how AI and cloud services can be integrated into a practical Python application.

The current application works with a small sales dataset stored as a CSV file.

Users can ask questions such as:

- Which product made the most money?
- Which product sold the most?
- What is the total revenue?

The application interprets the question using an Azure-hosted GPT model and then uses Python/pandas to calculate the correct result.

## Architecture

```text
User
  │
  ▼
Natural-language question
  │
  ▼
Microsoft Azure AI
GPT-4.1-mini
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
CSV sales data
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

- Python
- pandas
- Microsoft Azure AI
- Azure-hosted GPT-4.1-mini
- Azure Identity
- Microsoft Foundry
- Git
- GitHub
- CSV

## Project Goal

The goal of this project is to build a small cloud-based AI data assistant step by step.

The current version performs the data analysis locally with Python.

Future versions will integrate AI and Microsoft Azure services.

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

6. Run the application

python app.py

## Project Status

In development

The current version is a functional prototype.

Future improvements could include:

- A web-based user interface
- More advanced data analysis
- Additional question types
- Data visualization
- Improved error handling
- Deployment as a cloud-based application

Learning Goals

This project is helping me build practical experience with:

- Python development
- Data analysis
- AI integration
- Microsoft Azure
-Cloud-based AI services
- Git and GitHub
- Building and documenting a small end-to-end application