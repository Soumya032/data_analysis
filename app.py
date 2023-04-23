import streamlit as st
import pandas as pd
import plotly.express as px
import statsmodels.api as sm
import matplotlib.pyplot as plt


# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("Flipkart Mobile - 2.csv")
    return df


df = load_data()

# Sidebar options
sidebar_options = ["Highest Rated Phones", "Sales and Discount", "Sales and Price", "Market Percentage"]
sidebar_choice = st.sidebar.radio("Select a data analysis option", sidebar_options)

# Highest Rated Phones
if sidebar_choice == "Highest Rated Phones":
    st.header("Highest Rated Phones")
    highest_rated = df.sort_values(by=["ratings"], ascending=False)
    highest_rated = highest_rated.head(50)
    phones = highest_rated["model"].value_counts()
    label = phones.index
    counts = highest_rated["num_of_ratings"]
    counts = counts.head(12)
    figure = px.bar(highest_rated, x=label, y=counts,
                    title="Number of Ratings of Highest Rated Phones")
    st.plotly_chart(figure)

# Sales and Discount
elif sidebar_choice == "Sales and Discount":
    st.header("Sales and Discount")
    figure = px.scatter(data_frame=df, x="sales", y="discount_percent",
                        trendline="ols",
                        title="Relationship between Sales and Discount Percent of Phones")
    st.plotly_chart(figure)

# Sales and Price
elif sidebar_choice == "Sales and Price":
    st.header("Sales and Price")
    figure = px.scatter(data_frame=df, x="sales_price", y="sales",
                        trendline="ols",
                        title="Relationship between Sales and Price of Phones")
    st.plotly_chart(figure)

    # we can see that cheaper phones have higher sales
    st.write("We can see that cheaper phones have higher sales")
else:
    for col in [col for col in df.columns if 'sales_price' in col]:  # creating new columns with high low and medium
        df['models_under_1lakh'] = df[col].apply(lambda x: 50000 <= x <= 100000)
        df['models_under_50k'] = df[col].apply(lambda x: 25000 <= x <= 50000)
        df[('models_under_25k')] = df[col].apply(lambda x: x <= 25000)

    # Plot market percentage by brand for phones above 50k, 25k-50k, and under 25k
    st.subheader("Market Percentage")
    market_percentage_1lakh = df.groupby(['brand'])['models_under_1lakh'].sum().sort_values(ascending=False)
    market_percentage_50k = df.groupby(['brand'])['models_under_50k'].sum().sort_values(ascending=False)
    market_percentage_25k = df.groupby(['brand'])['models_under_25k'].sum().sort_values(ascending=False)

    st.write("Market Percentage of phones having value more than 1 lakh")
    st.plotly_chart(px.pie(market_percentage_1lakh, values='models_under_1lakh',
                           names=market_percentage_1lakh.index,
                           title="Market Percentage of Phones Above 1 Lakh"))

    st.write("Market Percentage of phones having value between 25k and 50k")
    st.plotly_chart(px.pie(market_percentage_50k, values='models_under_50k',
                           names=market_percentage_50k.index,
                           title="Market Percentage of Phones having values between 25k and 50k"))

    st.write("Market Percentage of phones having value less than 25k")
    st.plotly_chart(px.pie(market_percentage_25k, values='models_under_25k',
                           names=market_percentage_25k.index,
                           title="Market Percentage of Phones having values between 25k and 50k"))
