import pandas as pd
from pathlib import Path

def load_data():
    project_folder = Path(__file__).parent
    csv_file = project_folder / "data" / "sales.csv"

    data = pd.read_csv(csv_file)
    data["Revenue"] = data["Units_Sold"] * data["Price"]

    return data


def analyze_sales(data):
    highest_revenue_product = data.loc[data["Revenue"].idxmax()]

    return highest_revenue_product


def answer_question(data, question):

   if "highest revenue" in question.lower():
    result = analyze_sales(data)

    print("\nProduct with the highest revenue:")
    print(result["Product"])
    print(f"Revenue: €{result['Revenue']:,.0f}")

   elif "most units" in question.lower():
    result = data.loc[data["Units_Sold"].idxmax()]

    print("\nProduct with the most units sold:")
    print(result["Product"])
    print(f"Units sold: {result['Units_Sold']}")

   elif "total revenue" in question.lower():
    total_revenue = data["Revenue"].sum()

    print("\nTotal revenue:")
    print(f"€{total_revenue:,.0f}")

   else:
    print("\nSorry, I don't understand that question yet.")

data = load_data()

while True:
    question = input("\nWhat would you like to know about the sales data? ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    answer_question(data, question)