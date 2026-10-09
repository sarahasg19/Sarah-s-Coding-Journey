import pandas as pd
from pathlib import Path

from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

def load_data():
    project_folder = Path(__file__).parent
    csv_file = project_folder / "data" / "sales.csv"

    data = pd.read_csv(csv_file)
    data["Revenue"] = data["Units_Sold"] * data["Price"]

    return data

endpoint = "https://sarahshah--6807-resource.services.ai.azure.com/openai/v1"
deployment_name = "gpt-4.1-mini"

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://ai.azure.com/.default"
)

client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)


def analyze_sales(data):
    highest_revenue_product = data.loc[data["Revenue"].idxmax()]

    return highest_revenue_product

def ask_ai(question):
    response = client.responses.create(
        model=deployment_name,
        input=question
    )

    return response.output_text

def classify_question(question):
    prompt = f"""
Classify the user's question into exactly one of these categories:

- highest_revenue
- most_units
- total_revenue

Return only the category name.

User question:
{question}
"""

    response = client.responses.create(
        model=deployment_name,
        input=prompt
    )

    return response.output_text.strip()



def answer_question(data, question):

    category = classify_question(question)

    if category == "highest_revenue":
        result = analyze_sales(data)

        print("\nProduct with the highest revenue:")
        print(result["Product"])
        print(f"Revenue: €{result['Revenue']:,.0f}")

    elif category == "most_units":
        result = data.loc[data["Units_Sold"].idxmax()]

        print("\nProduct with the most units sold:")
        print(result["Product"])
        print(f"Units sold: {result['Units_Sold']}")

    elif category == "total_revenue":
        total_revenue = data["Revenue"].sum()

        print("\nTotal revenue:")
        print(f"€{total_revenue:,.0f}")

    else:
        print("\nSorry, I don't understand that question yet.")


if __name__ == "__main__":
    data = load_data()

    while True:
        question = input("\nWhat would you like to know about the sales data? ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        answer_question(data, question)