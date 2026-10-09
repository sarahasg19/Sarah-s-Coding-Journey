import streamlit as st

from app import load_data, classify_question, analyze_sales


st.title("🤖 AI Cloud Data Assistant")

st.subheader("Ask questions about your sales data")

st.write(
    "Use natural language to explore sales data with "
    "Azure AI and Python."
)

data = load_data()

st.subheader("Sales Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Revenue", f"€{data['Revenue'].sum():,.0f}")

with col2:
    st.metric("Units Sold", f"{data['Units_Sold'].sum():,}")

with col3:
    st.metric("Products", f"{data['Product'].nunique()}")

question = st.text_input(
    "What would you like to know about the sales data?"
)

st.subheader("Revenue by Product")

chart_data = data[["Product", "Revenue"]].set_index("Product")

st.bar_chart(chart_data)

if st.button("Ask AI"):
    if question:
        category = classify_question(question)

        if category == "highest_revenue":
            result = analyze_sales(data)

            st.success(
                f"Product with the highest revenue: "
                f"{result['Product']} — €{result['Revenue']:,.0f}"
            )

        elif category == "most_units":
            result = data.loc[data["Units_Sold"].idxmax()]

            st.success(
                f"Product with the most units sold: "
                f"{result['Product']} — {result['Units_Sold']} units"
            )

        elif category == "total_revenue":
            total_revenue = data["Revenue"].sum()

            st.success(
                f"Total revenue: €{total_revenue:,.0f}"
            )

        else:
            st.warning(
                "Sorry, I don't understand that question yet."
            )

    else:
        st.warning("Please enter a question.")