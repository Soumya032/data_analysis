import streamlit as st
import pandas as pd
import plotly.express as px
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("Flipkart Mobile - 2.csv")
    return df


df = load_data()
st.set_option('deprecation.showPyplotGlobalUse', False)
# Sidebar options
sidebar_options = ["Home","Highest Rated Phones", "Sales and Discount", "Sales and Price",
                        "Top 100 highest rated phones",
                        "Top 5 phones with highest number of ratings",
                        "Top 5 phones with highest sales",
                        "Top 5 phones with highest cost",
                        "RAM vs. Battery Capacity",
                        "Top 10 phones by brand",
                        "Top 10 phones under 10k",
                        "Price vs. Discount of Mobile Phones",
                        "Top 10 best selling Samsung phone models",
                        "Top 10 best selling Apple phone models",
                        "Sort by highest ratings",
                        "Plot number of ratings of brands",
                        "Plot percentage of number of models by brand",
                        "Plot sales by RAM",
                        "Sales by Camera Type",
                        "Market Percentage"]
sidebar_choice = st.sidebar.radio("Select a data analysis option", sidebar_options)

# Highest Rated Phones
if sidebar_choice == "Home":
    st.title("Mobile Phone Sales Analysis")
    st.write("Welcome to the Mobile Phone Sales Analysis Dashboard! Please select an option from the menu on the left to view the corresponding analysis.")
    # Add a horizontal line to separate the content from the group members section
    st.markdown("---")

    st.subheader("Group members")
    st.write("Aarushi Sharma    2006152")
    st.write("Deepak Motwani    2006171")
    st.write("Akankshya Barua   2006255")
    st.write("Soumya Ranjan Das 2006295")
elif sidebar_choice == "Highest Rated Phones":
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
    st.markdown("---")
    st.write("In this analysis we have compared 'The ratings of different phones' and found that x2 is the Highest Rated phone with more than 120k ratings in total")

# Sales and Discount
elif sidebar_choice == "Sales and Discount":
    st.header("Sales and Discount")
    figure = px.scatter(data_frame=df, x="sales", y="discount_percent",
                        trendline="ols",
                        title="Relationship between Sales and Discount Percent of Phones")
    st.plotly_chart(figure)
    st.markdown("---")
    st.write("In this analysis we have compared the relationship between 'Sales' and 'Discount percentage' and found that higher the discount percentage higher is the sales of the phone")

# Sales and Price
elif sidebar_choice == "Sales and Price":
    st.header("Sales and Price")
    figure = px.scatter(data_frame=df, x="sales_price", y="sales",
                        trendline="ols",
                        title="Relationship between Sales and Price of Phones")
    st.plotly_chart(figure)
    st.markdown("---")
    st.write("In this analysis we have compared the relationship between 'Sales' and 'Price' of a mobile phone  and found that higher the price lower the sales")

    # we can see that cheaper phones have higher sales
    st.write("We can see that cheaper phones have higher sales")
# Analysis
elif sidebar_choice == "Top 100 highest rated phones":
        st.title("Top 100 highest rated phones")
        highest_rated = df.sort_values(by=["ratings"], ascending=False).head(100)
        st.dataframe(highest_rated)
        st.markdown("---")
        st.write("In this analysis we found the 100 top rated mobile phones .")

elif sidebar_choice == "Top 5 phones with highest number of ratings":
        highest_rated = df.sort_values(by=["ratings"], ascending=False).head(100)
        company_counts = highest_rated["brand"].value_counts().head(5)
        fig = px.bar(x=company_counts.index, y=company_counts.values,
                     labels={"x": "Brand", "y": "Number of ratings"},
                     title="Top 5 phones with highest number of ratings")
        st.plotly_chart(fig)
        st.markdown("---")
        st.write("In this analysis we found the top 5 rated mobile phones")

elif sidebar_choice == "Top 5 phones with highest sales":
        highest_rated = df.sort_values(by=["ratings"], ascending=False).head(100)
        company_sales = highest_rated.groupby("brand")["sales"].sum().sort_values(ascending=False).head(5)
        fig = px.bar(x=company_sales.index, y=company_sales.values,
                     labels={"x": "Brand", "y": "Sales"},
                     title="Top 5 phones with highest sales")
        st.plotly_chart(fig)
        st.markdown("---")
        st.write("In this analysis we found the top 5 phones on the basis of sales numbers ")

elif sidebar_choice == "Top 5 phones with highest cost":
        highest_rated = df.sort_values(by=["ratings"], ascending=False).head(100)
        company_cost = highest_rated.groupby("brand")["sales_price"].sum().sort_values(ascending=False).head(5)
        fig = px.bar(x=company_cost.index, y=company_cost.values,
                     labels={"x": "Brand", "y": "Sales price"},
                     title="Top 5 phones with highest cost")
        st.plotly_chart(fig)
        st.markdown("---")
        st.write("In this analysis we have found the Top 5 costliest phones in the market")

elif sidebar_choice == "RAM vs. Battery Capacity":
        fig = px.scatter(df, x="RAM", y="battery_capacity", trendline="ols",
                         labels={"RAM": "RAM (GB)", "battery_capacity": "Battery Capacity (mAh)"},
                         title="RAM vs. Battery Capacity (scatter plot)")
        st.plotly_chart(fig)
        st.markdown("---")
        st.write("In this analysis we have compared RAM of a mobile phone and the battery capacity we could see Higher the RAM higher the battery capacity needed")

elif sidebar_choice == "Top 10 phones by brand":
    highest_rated=df.sort_values(by=["ratings"], ascending=False)
    highest_rated=highest_rated.head(100)

    Company=highest_rated["brand"].value_counts()
    label=Company.index
    counts=highest_rated["num_of_ratings"]
    counts=counts.head(5)
    figure= px.bar(highest_rated, x=label, y=counts, title="Top 10 phones by brand")
    st.plotly_chart(figure)
    st.markdown("---")
    st.write("In this analysis we have the found the top 10 mobile phones by brand")

elif sidebar_choice == "Top 10 phones under 10k":
    st.title("Top 10 phones under 10k")
    top_10_phones=df.sort_values("sales_price").head(10)
    phone_names=top_10_phones["brand"]
    phone_prices=top_10_phones["sales_price"]
    plt.pie(phone_prices, labels=phone_names, autopct='%1.1f%%', startangle=90)
    plt.title("Top 10 Phones Under 10k")
    plt.axis('equal')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    st.markdown("---")
    st.write("In this analysis we have compared found top 10 phones in the lower category that is 10k ")

elif sidebar_choice == "Price vs. Discount of Mobile Phones":
    st.title("Price vs. Discount of Mobile Phones")
    phone_prices=df['sales_price']
    phone_discounts=df['discount_percent']
    plt.scatter(phone_prices, phone_discounts)
    plt.title("Price vs. Discount of Mobile Phones")
    plt.xlabel("Price")
    plt.ylabel("Discount")
    st.pyplot()
    st.markdown("---")
    st.write("In this analysis we have found the relationship between price and discount percentage  of phones.")

elif sidebar_choice == "Top 10 best selling Samsung phone models":
    st.title("Top 10 best selling Samsung phone models")
    samsung_df = df[df['brand'] == 'Samsung']
    top_10_samsung_phones = samsung_df.sort_values('sales', ascending=False).head(10)
    labels = top_10_samsung_phones['model']
    values = top_10_samsung_phones['sales']
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title("Top 10 Best Selling Samsung Phone Models")
    st.pyplot()
    st.markdown("---")
    st.write("In this analysis we have made a pie chart showing the top 10 best selling phone models and found that galaxy f-41 it has a market share of 76%")

elif sidebar_choice == "Top 10 best selling Apple phone models":
    st.title("Top 10 best selling Apple phone models")
    apple_df = df[df['brand'] == 'Apple']
    top_10_apple_phones = apple_df.sort_values('sales', ascending=False).head(10)
    labels = top_10_apple_phones['model']
    values = top_10_apple_phones['sales']
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title("Top 10 Best Selling Apple Phone Models")
    st.pyplot()
    st.markdown("---")
    st.write("In this analysis we have made a pie chart showing the top selling 10 iphone model  and found that iphone SE is top selling phone with 57% market share ")

elif sidebar_choice == "Sort by highest ratings":
    st.title("Sort by highest Star Ratings")
    highest_rated = df.sort_values(by=["ratings"], ascending=False)
    st.write(highest_rated.head(100))
    st.markdown("---")
    st.write("In this analysis we sorted the data on the basis of their average rating on a score of 5 multiple phones topped the list with an average of 4.6star rating")

elif sidebar_choice == "Plot number of ratings of brands":
    highest_rated = df.sort_values(by=["ratings"], ascending=False)
    highest_rated = highest_rated.head(100)
    phones = highest_rated["brand"].value_counts()
    label = phones.index
    counts = highest_rated["num_of_ratings"]
    counts = counts.head(5)
    figure = px.bar(highest_rated, x=label, y=counts, title="Number of ratings of brands")
    st.plotly_chart(figure)
    st.markdown("---")
    st.write("Precentage of number of models of different brand in the market Realme has the highest number of phones in the market")

elif sidebar_choice == "Plot percentage of number of models by brand":
    st.title("Plot percentage of number of models by brand")
    df['brand'].value_counts().plot.pie(autopct='%1.1f%%')
    title = ("Market share of each brand")
    st.pyplot()
    st.markdown("---")
    st.write(" In this analysis we plotted a pie chart of the Market share of each brand and found that Realme phones have the maximum sales with 33.6% and also found that Sales of Apple iphones were the lowest with only 8.5% sales.")

elif sidebar_choice == "Plot sales by RAM":
    st.title("Plot sales by RAM")
    contribution = df.groupby(['brand'])['sales'].sum().sort_values(ascending=False)
    contribution.plot(kind='pie', title='Sales of different brands', figsize=[7, 7],
                      autopct=lambda p: '{:.1f}%'.format(p))
    ax = sns.catplot(x="RAM", y="sales", data=df, height=4, aspect=2, kind='bar')
    st.pyplot(ax)
    st.markdown("---")
    st.write("In this analysis we found the Relation between sales of mobile phone and RAM(GB),It can be clearly seen that the sales of 2GB RAM mobile phone is the highest")

elif sidebar_choice == "Sales by Camera Type":
    st.title("Sales by Camera Type")

    # Merge the three columns into one column
    df_bar = df.copy()
    df_bar['camera_type'] = ''
    for col in [col for col in df.columns if 'num_rear_camera' in col]:  # creating new columns with high low and medium
        df['single_cam'] = df[col].apply(lambda x: x == 1)
        df['dual_cam'] = df[col].apply(lambda x: x == 2)
        df['triple_cam'] = df[col].apply(lambda x: x == 3)
        df['quad_cam'] = df[col].apply(lambda x: x == 4)

    df_bar = df[['single_cam', 'dual_cam', 'triple_cam', 'quad_cam', 'sales']].copy()

    # Merge the four columns into one column
    df_bar['camera_type'] = ''
    df_bar.loc[df_bar['single_cam'] == True, 'camera_type'] = 'Single Camera'
    df_bar.loc[df_bar['dual_cam'] == True, 'camera_type'] = 'Dual Camera'
    df_bar.loc[df_bar['triple_cam'] == True, 'camera_type'] = 'Triple Camera'
    df_bar.loc[df_bar['quad_cam'] == True, 'camera_type'] = 'Quad Camera'

    # Drop the individual camera type columns
    df_bar.drop(['single_cam', 'dual_cam', 'triple_cam', 'quad_cam'], axis=1, inplace=True)

    # Group the dataframe by the camera type and calculate the sum of sales
    sales_by_cam = df_bar.groupby('camera_type')['sales'].sum()

    # Create a bar chart of the sales by camera type
    fig, ax = plt.subplots()
    ax.bar(sales_by_cam.index, sales_by_cam.values, color='blue')

    # Set the chart title and axis labels
    ax.set_title('Sales by Camera Type')
    ax.set_xlabel('Camera Type')
    ax.set_ylabel('Sales')

    # Show the chart
    st.pyplot(fig)
    st.markdown("---")
    st.write("We found the relationship between camera type and the sales of the phone and found that Dual cam mobiles are the highest selling phones in the market")
else:
    for col in [col for col in df.columns if 'sales_price' in col]:  # creating new columns with high low and medium
        df['models_under_1lakh'] = df[col].apply(lambda x: 50000 <= x <= 100000)
        df['models_under_50k'] = df[col].apply(lambda x: 25000 <= x <= 50000)
        df[('models_uder_25k')] = df[col].apply(lambda x: x <= 25000)

    # Plot market percentage by brand for phones above 50k, 25k-50k, and under 25k
    st.subheader("Market Percentage")
    market_percentage_1lakh = df.groupby(['brand'])['models_under_1lakh'].sum().sort_values(ascending=False)
    market_percentage_50k = df.groupby(['brand'])['models_under_50k'].sum().sort_values(ascending=False)
    market_percentage_25k = df.groupby(['brand'])['models_uder_25k'].sum().sort_values(ascending=False)

    st.write("Market Percentage of phones having value more than 1 lakh")
    st.plotly_chart(px.pie(market_percentage_1lakh, values='models_under_1lakh',
                           names=market_percentage_1lakh.index,
                           title="Market Percentage of Phones Above 1 Lakh"))

    st.write("Market Percentage of phones having value between 25k and 50k")
    st.plotly_chart(px.pie(market_percentage_50k, values='models_under_50k',
                           names=market_percentage_50k.index,
                           title="Market Percentage of Phones having values between 25k and 50k"))

    st.write("Market Percentage of phones having value less than 25k")
    st.plotly_chart(px.pie(market_percentage_25k, values='models_uder_25k',
                           names=market_percentage_25k.index,
                           title="Market Percentage of Phones having values between 25k and 50k"))
    
    #top 10 best selling applephone model,plot percentage by no of model
