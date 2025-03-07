import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="Brazil E-commerce Analysis",
    page_icon="🛒",
    layout="wide"
)

st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E88E5;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #4CAF50;
    }
    .insight-box {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
        color: #333333;  /* Dark text color for better contrast */
    }
    .insight-box p {
        color: #333333;  /* Ensuring paragraph text is dark */
        font-size: 1rem;
    }
    .insight-box strong {
        color: #1E88E5;  /* Blue color for emphasis */
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<p class='main-header'>Brazil E-commerce Public Dataset Analysis</p>", unsafe_allow_html=True)
st.markdown("**Author:** Hanif Herofa")

st.markdown("""
This dashboard provides insights into Brazil's e-commerce market from 2016 to 2018, 
focusing on sales patterns by product category and regional differences in average order value.
""")

@st.cache_data
def load_data():
    df = pd.read_csv('main_data.csv')

    date_columns = [col for col in df.columns if 'date' in col.lower() or 'timestamp' in col.lower()]
    for col in date_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col])

    if 'order_purchase_timestamp' in df.columns and 'orders_year' not in df.columns:
        df['orders_year'] = df['order_purchase_timestamp'].dt.year
        df['orders_month'] = df['order_purchase_timestamp'].dt.month
        df['orders_yearmonth'] = df['order_purchase_timestamp'].dt.strftime('%Y-%m')
    
    return df

with st.spinner('Loading data...'):
    try:
        df = load_data()
        st.success('Data loaded successfully!')

        with st.expander("Preview of the dataset"):
            st.dataframe(df.head())

        with st.expander("Dataset information"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Number of rows:** {df.shape[0]}")
                st.write(f"**Number of columns:** {df.shape[1]}")
            with col2:
                st.write(f"**Date range:** {df['order_purchase_timestamp'].min().date()} to {df['order_purchase_timestamp'].max().date()}")
    
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.info("Please make sure 'main_data.csv' is in the same directory as this app.")
        st.stop()

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select a page:",
    ["Overview", "Sales Patterns by Category", "Regional Analysis", "About"]
)

if 'orders_year' in df.columns:
    years = sorted(df['orders_year'].unique())
    selected_years = st.sidebar.multiselect(
        "Filter by year(s):",
        years,
        default=years
    )
    
    if selected_years:
        df_filtered = df[df['orders_year'].isin(selected_years)]
    else:
        df_filtered = df
        st.sidebar.warning("No year selected. Showing all data.")
else:
    df_filtered = df
    st.sidebar.warning("Year column not found. Showing all data.")

if page == "Overview":
    st.markdown("<p class='sub-header'>Overview of E-commerce Data</p>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Orders", f"{df_filtered['order_id'].nunique():,}")
    
    with col2:
        if 'total_price' in df_filtered.columns:
            total_revenue = df_filtered['total_price'].sum()
            st.metric("Total Revenue", f"R$ {total_revenue:,.2f}")
        else:
            if 'price' in df_filtered.columns and 'freight_value' in df_filtered.columns:
                total_revenue = (df_filtered['price'] + df_filtered['freight_value']).sum()
                st.metric("Total Revenue", f"R$ {total_revenue:,.2f}")
            else:
                st.metric("Total Revenue", "Not available")
    
    with col3:
        if 'total_price' in df_filtered.columns:
            avg_order_value = df_filtered.groupby('order_id')['total_price'].sum().mean()
            st.metric("Avg. Order Value", f"R$ {avg_order_value:.2f}")
        else:
            st.metric("Avg. Order Value", "Not available")
    
    with col4:
        if 'product_category_name_english' in df_filtered.columns:
            st.metric("Total Categories", f"{df_filtered['product_category_name_english'].nunique()}")
        else:
            st.metric("Total Categories", "Not available")

    st.markdown("### Monthly Sales Trend")
    
    if 'orders_yearmonth' in df_filtered.columns and ('total_price' in df_filtered.columns or ('price' in df_filtered.columns and 'freight_value' in df_filtered.columns)):
        if 'total_price' in df_filtered.columns:
            monthly_sales = df_filtered.groupby('orders_yearmonth')['total_price'].sum().reset_index()
            price_col = 'total_price'
        else:
            monthly_sales = df_filtered.groupby('orders_yearmonth')[['price', 'freight_value']].sum().reset_index()
            monthly_sales['total_price'] = monthly_sales['price'] + monthly_sales['freight_value']
            price_col = 'total_price'

        monthly_sales['date'] = pd.to_datetime(monthly_sales['orders_yearmonth'])
        monthly_sales = monthly_sales.sort_values('date')

        fig = px.line(
            monthly_sales, 
            x='orders_yearmonth', 
            y=price_col,
            labels={'orders_yearmonth': 'Month', price_col: 'Sales (BRL)'},
            title='Monthly Sales Trend'
        )
        
        fig.update_layout(
            xaxis_title="Month",
            yaxis_title="Sales (BRL)",
            hovermode="x unified"
        )
        
        st.plotly_chart(fig, use_container_width=True)

        monthly_orders = df_filtered.groupby('orders_yearmonth')['order_id'].nunique().reset_index()
        monthly_orders['date'] = pd.to_datetime(monthly_orders['orders_yearmonth'])
        monthly_orders = monthly_orders.sort_values('date')
        
        fig = px.bar(
            monthly_orders,
            x='orders_yearmonth',
            y='order_id',
            labels={'orders_yearmonth': 'Month', 'order_id': 'Number of Orders'},
            title='Monthly Order Count'
        )
        
        fig.update_layout(
            xaxis_title="Month",
            yaxis_title="Number of Orders",
            hovermode="x unified"
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Required columns for monthly trend analysis are not available.")

    st.markdown("### Key Insights")
    
    st.markdown("""
    <div class="insight-box">
        <p>📈 <strong>Growth Trend:</strong> The Brazilian e-commerce market shows significant growth from 2016 to 2018.</p>
    </div>
    
    <div class="insight-box">
        <p>🗓️ <strong>Seasonal Patterns:</strong> November (likely Black Friday) shows peak sales across most categories.</p>
    </div>
    
    <div class="insight-box">
        <p>🏠 <strong>Category Leaders:</strong> Home goods (bed_bath_table) and health & beauty products lead in revenue.</p>
    </div>
    
    <div class="insight-box">
        <p>🗺️ <strong>Regional Variations:</strong> Smaller states often have higher average order values but fewer total orders.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Sales Patterns by Category":
    st.markdown("<p class='sub-header'>Sales Patterns by Product Category (2016-2018)</p>", unsafe_allow_html=True)
    
    if 'product_category_name_english' not in df_filtered.columns:
        st.error("Product category column not found in the dataset.")
        st.stop()

    if 'total_price' in df_filtered.columns:
        category_sales = df_filtered.groupby('product_category_name_english')['total_price'].sum().reset_index()
        price_col = 'total_price'
    else:
        if 'price' in df_filtered.columns and 'freight_value' in df_filtered.columns:
            category_sales = df_filtered.groupby('product_category_name_english')[['price', 'freight_value']].sum().reset_index()
            category_sales['total_price'] = category_sales['price'] + category_sales['freight_value']
            price_col = 'total_price'
        else:
            st.error("Price information not found in the dataset.")
            st.stop()

    category_sales = category_sales.sort_values(price_col, ascending=False)

    st.markdown("### Top Product Categories by Revenue")
    top_n = st.slider("Select number of top categories to display:", 5, 20, 10)
    top_categories = category_sales.head(top_n)
    
    fig = px.bar(
        top_categories,
        x='product_category_name_english',
        y=price_col,
        labels={'product_category_name_english': 'Product Category', price_col: 'Revenue (BRL)'},
        title=f'Top {top_n} Product Categories by Revenue',
        color=price_col,
        color_continuous_scale=px.colors.sequential.Blues
    )
    
    fig.update_layout(
        xaxis_title="Product Category",
        yaxis_title="Revenue (BRL)",
        xaxis={'categoryorder':'total descending'}
    )
    
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Monthly Sales Trend by Category")

    selected_categories = st.multiselect(
        "Select categories to compare:",
        category_sales['product_category_name_english'].tolist(),
        default=category_sales['product_category_name_english'].head(5).tolist()
    )
    
    if selected_categories:
        if 'orders_yearmonth' in df_filtered.columns:
            filtered_data = df_filtered[df_filtered['product_category_name_english'].isin(selected_categories)]

            if 'total_price' in filtered_data.columns:
                monthly_category_sales = filtered_data.groupby(['orders_yearmonth', 'product_category_name_english'])[price_col].sum().reset_index()
            else:
                monthly_category_sales = filtered_data.groupby(['orders_yearmonth', 'product_category_name_english'])[['price', 'freight_value']].sum().reset_index()
                monthly_category_sales['total_price'] = monthly_category_sales['price'] + monthly_category_sales['freight_value']
                price_col = 'total_price'

            monthly_category_sales['date'] = pd.to_datetime(monthly_category_sales['orders_yearmonth'])
            monthly_category_sales = monthly_category_sales.sort_values('date')

            fig = px.line(
                monthly_category_sales,
                x='orders_yearmonth',
                y=price_col,
                color='product_category_name_english',
                labels={'orders_yearmonth': 'Month', price_col: 'Sales (BRL)', 'product_category_name_english': 'Category'},
                title='Monthly Sales Trend by Category'
            )
            
            fig.update_layout(
                xaxis_title="Month",
                yaxis_title="Sales (BRL)",
                legend_title="Category",
                hovermode="x unified"
            )
            
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Required columns for monthly trend analysis are not available.")
    else:
        st.warning("Please select at least one category to display the trend.")

    st.markdown("### Monthly Heatmap for Top Categories")
    
    if 'orders_month' in df_filtered.columns:
        top_n_heatmap = st.slider("Select number of top categories for heatmap:", 3, 15, 8)
        top_heatmap_categories = category_sales['product_category_name_english'].head(top_n_heatmap).tolist()

        heatmap_data = df_filtered[df_filtered['product_category_name_english'].isin(top_heatmap_categories)]

        if 'total_price' in heatmap_data.columns:
            monthly_heatmap = heatmap_data.groupby(['orders_month', 'product_category_name_english'])[price_col].sum().reset_index()
        else:
            monthly_heatmap = heatmap_data.groupby(['orders_month', 'product_category_name_english'])[['price', 'freight_value']].sum().reset_index()
            monthly_heatmap['total_price'] = monthly_heatmap['price'] + monthly_heatmap['freight_value']
            price_col = 'total_price'

        heatmap_pivot = monthly_heatmap.pivot(index='product_category_name_english', columns='orders_month', values=price_col)

        fig, ax = plt.subplots(figsize=(12, 8))
        sns.heatmap(heatmap_pivot, annot=True, fmt=".0f", cmap="YlGnBu", ax=ax)
        plt.title('Monthly Sales by Category')
        plt.ylabel('Product Category')
        plt.xlabel('Month')
        
        st.pyplot(fig)
    else:
        st.warning("Month column not available for heatmap visualization.")

    st.markdown("### Key Insights on Product Categories")
    
    st.markdown("""
    <div class="insight-box">
        <p>🏠 <strong>Home Products Dominance:</strong> "bed_bath_table" category has the highest revenue, showing Brazilian customers' preference for home products in online shopping.</p>
    </div>
    
    <div class="insight-box">
        <p>🌡️ <strong>Health & Beauty Growth:</strong> Personal care products are consistently among top performers, indicating a strong market for these items.</p>
    </div>
    
    <div class="insight-box">
        <p>🗓️ <strong>Seasonal Variations:</strong> Most categories show similar seasonal patterns with November peaks, but some categories like toys and electronics have more pronounced holiday season effects.</p>
    </div>
    
    <div class="insight-box">
        <p>📱 <strong>Tech Products Performance:</strong> Electronics categories (like computers_accessories) make the top 10, but don't dominate as they might in other global markets.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Regional Analysis":
    st.markdown("<p class='sub-header'>Regional Analysis of Average Order Value</p>", unsafe_allow_html=True)

    required_columns = ['customer_state', 'order_id']
    price_columns = ['total_price', 'price', 'freight_value']
    
    if not all(col in df_filtered.columns for col in required_columns) or not any(col in df_filtered.columns for col in price_columns):
        st.error("Required columns for regional analysis are not available in the dataset.")
        st.stop()

    if 'total_price' in df_filtered.columns:
        price_col = 'total_price'
    else:
        df_filtered['total_price'] = df_filtered['price'] + df_filtered['freight_value']
        price_col = 'total_price'

    order_values = df_filtered.groupby(['order_id', 'customer_state'])[price_col].sum().reset_index()
    aov_per_state = order_values.groupby('customer_state')[price_col].mean().reset_index()
    aov_per_state = aov_per_state.rename(columns={price_col: 'average_order_value'})

    order_count_per_state = order_values.groupby('customer_state')['order_id'].count().reset_index()
    order_count_per_state = order_count_per_state.rename(columns={'order_id': 'order_count'})

    state_metrics = aov_per_state.merge(order_count_per_state, on='customer_state')

    state_metrics['total_revenue'] = state_metrics['average_order_value'] * state_metrics['order_count']

    state_metrics_by_aov = state_metrics.sort_values('average_order_value', ascending=False)

    st.markdown("### Average Order Value by State")
    
    fig = px.bar(
        state_metrics_by_aov,
        x='customer_state',
        y='average_order_value',
        labels={'customer_state': 'State', 'average_order_value': 'Average Order Value (BRL)'},
        title='Average Order Value by State',
        color='average_order_value',
        color_continuous_scale=px.colors.sequential.Viridis
    )

    national_avg = state_metrics_by_aov['average_order_value'].mean()
    fig.add_hline(
        y=national_avg,
        line_dash="dash",
        line_color="red",
        annotation_text=f"National Avg: R${national_avg:.2f}",
        annotation_position="bottom right"
    )
    
    fig.update_layout(
        xaxis_title="State",
        yaxis_title="Average Order Value (BRL)",
        xaxis={'categoryorder':'total descending'}
    )
    
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Relationship between Order Count and Average Order Value")
    
    fig = px.scatter(
        state_metrics,
        x='order_count',
        y='average_order_value',
        size='total_revenue',
        color='total_revenue',
        hover_name='customer_state',
        text='customer_state',
        labels={
            'order_count': 'Number of Orders',
            'average_order_value': 'Average Order Value (BRL)',
            'total_revenue': 'Total Revenue (BRL)'
        },
        title='Relationship between Order Count, AOV, and Total Revenue by State',
        color_continuous_scale=px.colors.sequential.Viridis
    )
    
    fig.update_traces(textposition='top center')
    
    fig.update_layout(
        xaxis_title="Number of Orders",
        yaxis_title="Average Order Value (BRL)",
        legend_title="Total Revenue",
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Distribution of Order Values")
    
    fig = px.histogram(
        order_values,
        x=price_col,
        nbins=50,
        labels={price_col: 'Order Value (BRL)'},
        title='Distribution of Order Values',
        color_discrete_sequence=['skyblue']
    )
    
    mean_value = order_values[price_col].mean()
    median_value = order_values[price_col].median()
    
    fig.add_vline(x=mean_value, line_dash="dash", line_color="red", 
                  annotation_text=f"Mean: R${mean_value:.2f}", annotation_position="top right")
    fig.add_vline(x=median_value, line_dash="dash", line_color="green", 
                  annotation_text=f"Median: R${median_value:.2f}", annotation_position="top left")
    
    fig.update_layout(
        xaxis_title="Order Value (BRL)",
        yaxis_title="Count",
        xaxis_range=[0, 500]
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("### Top Cities by Average Order Value")
    
    if 'customer_city' in df_filtered.columns:
        city_order_values = df_filtered.groupby(['order_id', 'customer_state', 'customer_city'])[price_col].sum().reset_index()
        aov_per_city = city_order_values.groupby(['customer_state', 'customer_city'])[price_col].mean().reset_index()
        aov_per_city = aov_per_city.rename(columns={price_col: 'average_order_value'})
        
        order_count_per_city = city_order_values.groupby(['customer_state', 'customer_city'])['order_id'].count().reset_index()
        order_count_per_city = order_count_per_city.rename(columns={'order_id': 'order_count'})
        
        city_metrics = aov_per_city.merge(order_count_per_city, on=['customer_state', 'customer_city'])
        
        min_orders = st.slider("Minimum orders per city:", 1, 50, 10)
        filtered_cities = city_metrics[city_metrics['order_count'] >= min_orders]
        
        top_n_cities = st.slider("Number of top cities to display:", 5, 50, 15)
        top_cities = filtered_cities.sort_values('average_order_value', ascending=False).head(top_n_cities)
        
        fig = px.bar(
            top_cities,
            x='customer_city',
            y='average_order_value',
            color='customer_state',
            labels={
                'customer_city': 'City',
                'average_order_value': 'Average Order Value (BRL)',
                'customer_state': 'State'
            },
            title=f'Top {top_n_cities} Cities by Average Order Value (min. {min_orders} orders)',
            hover_data=['order_count']
        )
        
        fig.update_layout(
            xaxis_title="City",
            yaxis_title="Average Order Value (BRL)",
            xaxis={'categoryorder':'total descending'},
            height=600
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("City column not available for city-level analysis.")

    st.markdown("### Key Insights on Regional Patterns")
    
    st.markdown("""
    <div class="insight-box">
        <p>🗺️ <strong>Regional Disparities:</strong> States like PB, AL, AC, and RR show significantly higher average order values than the national average.</p>
    </div>
    
    <div class="insight-box">
        <p>📉 <strong>Inverse Relationship:</strong> States with higher order volumes tend to have lower average order values, suggesting different shopping behaviors between high-volume and low-volume regions.</p>
    </div>
    
    <div class="insight-box">
        <p>🏙️ <strong>Urban vs. Rural Patterns:</strong> Major urban centers like São Paulo (SP) show higher order frequencies but lower average values, while more remote areas make fewer but larger purchases.</p>
    </div>
    
    <div class="insight-box">
        <p>📊 <strong>Distribution Skewness:</strong> The significant difference between mean and median order values indicates a positively skewed distribution with a small number of very high-value orders influencing the average.</p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("<p class='sub-header'>About This Project</p>", unsafe_allow_html=True)
    
    st.markdown("""
    ## Brazil E-commerce Public Dataset Analysis
    
    This project analyzes Brazilian e-commerce public dataset from Olist Store, the largest department store in Brazilian marketplaces.
    The dataset contains information on 100,000 orders from 2016 to 2018 made at multiple marketplaces in Brazil.
    
    ### Key Business Questions
    
    1. **Sales Patterns by Product Category:**
       - How do product sales patterns vary by category during 2016-2018?
       - Which product categories contribute the highest revenue?
    
    2. **Regional Analysis:**
       - How does the average order value (AOV) compare across different geographical regions in Brazil?
       - What factors might explain the regional variations in customer spending?
    
    ### Methodology
    
    The analysis involved:
    - Data cleaning and integration of multiple datasets
    - Time series analysis of sales patterns
    - Categorization and ranking of product performance
    - Regional comparison of customer spending patterns
    - Visualization of key insights through charts and maps
    
    ### Tools Used
    
    - Python (Pandas, NumPy, Matplotlib, Seaborn)
    - Streamlit for interactive dashboard
    - Plotly for enhanced visualizations
    
    ### Author
    
    **Hanif Herofa**  
    Email: herovva@gmail.com  
    ID Dicoding: mc200d5y2221
    """)

st.markdown("---")
st.markdown("Brazil E-commerce Analysis Dashboard | Created with Streamlit")