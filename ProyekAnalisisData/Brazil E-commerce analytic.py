# %% [markdown]
# # Proyek Analisis Data: E-commerce Public Dataset
# - **Nama:** Hanif Herofa
# - **Email:** herovva@gmail.com
# - **ID Dicoding:** mc200d5y2221

# %% [markdown]
# ## Menentukan Pertanyaan Bisnis

# %% [markdown]
# - Bagaimana pola penjualan produk berdasarkan kategori selama periode 2016-2018, dan kategori produk apa yang memberikan kontribusi pendapatan tertinggi?
# - Bagaimana perbandingan nilai rata-rata transaksi (average order value) antar wilayah geografis di Brazil?

# %% [markdown]
# ## Import Semua Packages/Library yang Digunakan

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import urllib
%pip install unidecode
import unidecode
import matplotlib.image as mpimg

# %% [markdown]
# ## Data Wrangling

# %% [markdown]
# ### Gathering Data

# %%
# Data customers

# Import data customers
customers_df = pd.read_csv('data/customers_dataset.csv')

# Copy dataframe untuk digunakan nanti
customers_df_original = customers_df.copy()

# Print 5 baris pertama dari dataframe
print('5 baris pertama dari dataframe:')
print(customers_df.head())

# Jumlah keseluruhan baris dan kolom
print('\nJumlah keseluruhan baris dan kolom:')
print(customers_df.shape)

# %%
# Data geolocations

# Import data geolocations
geolocations_df = pd.read_csv('data/geolocation_dataset.csv')

# Copy dataframe untuk digunakan nanti
geolocations_df_original = geolocations_df.copy()

# Print 5 baris pertama dari dataframe
print('5 baris pertama dari dataframe:')
print(geolocations_df.head())

# Jumlah keseluruhan baris dan kolom
print('\nJumlah keseluruhan baris dan kolom:')
print(geolocations_df.shape)

# %%
# Data order items

# Import data order items
orders_items_df = pd.read_csv('data/order_items_dataset.csv')

# Copy dataframe untuk digunakan nanti
orders_items_df_original = orders_items_df.copy()

# Print 5 baris pertama dari dataframe
print('5 baris pertama dari dataframe:')
print(orders_items_df.head())

# Jumlah keseluruhan baris dan kolom
print('\nJumlah keseluruhan baris dan kolom:')
print(orders_items_df.shape)

# %%
# Data order payments

# Import data order payments
orders_payments_df = pd.read_csv('data/order_payments_dataset.csv')

# Copy dataframe untuk digunakan nanti
orders_payments_df_original = orders_payments_df.copy()

# Print 5 baris pertama dari dataframe
print('5 baris pertama dari dataframe:')
print(orders_payments_df.head())

# Jumlah keseluruhan baris dan kolom
print('\nJumlah keseluruhan baris dan kolom:')
print(orders_payments_df.shape)

# %%
# Data order reviews

# Import data order reviews
orders_reviews_df = pd.read_csv('data/order_reviews_dataset.csv')

# Copy dataframe untuk digunakan nanti
orders_reviews_df_original = orders_reviews_df.copy()

# Print 5 baris pertama dari dataframe
print('5 baris pertama dari dataframe:')
print(orders_reviews_df.head())

# Jumlah keseluruhan baris dan kolom
print('\nJumlah keseluruhan baris dan kolom:')
print(orders_reviews_df.shape)

# %%
# Data orders

# Import data orders
orders_df = pd.read_csv('data/orders_dataset.csv')

# Copy dataframe untuk digunakan nanti
orders_df_original = orders_df.copy()

# Print 5 baris pertama dari dataframe
print('5 baris pertama dari dataframe:')
print(orders_df.head())

# Jumlah keseluruhan baris dan kolom
print('\nJumlah keseluruhan baris dan kolom:')
print(orders_df.shape)

# %%
# Data product category name translation

# Import data product category name translation
product_category_name_translation_df = pd.read_csv('data/product_category_name_translation.csv')

# Copy dataframe untuk digunakan nanti
product_category_name_translation_df_original = product_category_name_translation_df.copy()

# Print 5 baris pertama dari dataframe
print('5 baris pertama dari dataframe:')
print(product_category_name_translation_df.head())

# Jumlah keseluruhan baris dan kolom
print('\nJumlah keseluruhan baris dan kolom:')
print(product_category_name_translation_df.shape)

# %%
# Data products

# Import data products
products_df = pd.read_csv('data/products_dataset.csv')

# Copy dataframe untuk digunakan nanti
products_df_original = products_df.copy()

# Print 5 baris pertama dari dataframe
print('5 baris pertama dari dataframe:')
print(products_df.head())

# Jumlah keseluruhan baris dan kolom
print('\nJumlah keseluruhan baris dan kolom:')
print(products_df.shape)

# %%
# Data sellers

# Import data sellers
sellers_df = pd.read_csv('data/sellers_dataset.csv')

# Copy dataframe untuk digunakan nanti
sellers_df_original = sellers_df.copy()

# Print 5 baris pertama dari dataframe
print('5 baris pertama dari dataframe:')
print(sellers_df.head())

# Jumlah keseluruhan baris dan kolom
print('\nJumlah keseluruhan baris dan kolom:')
print(sellers_df.shape)

# %% [markdown]
# **Insight:**
# - Melalui import csv di atas, telah berhasil dilakukan -----

# %% [markdown]
# ### Assessing Data

# %%
# Data customers

print('\nInfo data customers:')
print(customers_df.info()) # Menampilkan informasi data customers

# Jumlah data yang hilang pada dataset customers
print('\nJumlah data yang hilang pada dataset customers:')
print(customers_df.isnull().sum()) # Mengecek data yang hilang

# Jumlah data yang duplikat pada dataset customers
print('\nJumlah data yang duplikat pada dataset customers:')
print(customers_df.duplicated().sum()) # Mengecek data yang duplikat

# Statistik deskriptif dari dataset customers
print('\nStatistik deskriptif dari dataset customers:')
print(customers_df.describe()) # Menampilkan statistik deskriptif

# %% [markdown]
# **Insight:**
# - xxx
# - xxx

# %%
# Data geolocations

print('\nInfo data geolocations:')
print(geolocations_df.info()) # Menampilkan informasi data geolocations

# Jumlah data yang hilang pada dataset geolocations
print('\nJumlah data yang hilang pada dataset geolocations:')
print(geolocations_df.isnull().sum()) # Mengecek data yang hilang

# Jumlah data yang duplikat pada dataset geolocations
print('\nJumlah data yang duplikat pada dataset geolocations:')
print(geolocations_df.duplicated().sum()) # Mengecek data yang duplikat

# Statistik deskriptif dari dataset geolocations
print('\nStatistik deskriptif dari dataset geolocations:')
print(geolocations_df.describe()) # Menampilkan statistik deskriptif

# %%
# Data order items

print('\nInfo data order items:')
print(orders_df.info()) # Menampilkan informasi data order items

# Jumlah data yang hilang pada dataset order items
print('\nJumlah data yang hilang pada dataset order items:')
print(orders_df.isnull().sum()) # Mengecek data yang hilang

# Jumlah data yang duplikat pada dataset order items
print('\nJumlah data yang duplikat pada dataset order items:')
print(orders_df.duplicated().sum()) # Mengecek data yang duplikat

# Statistik deskriptif dari dataset order items
print('\nStatistik deskriptif dari dataset order items:')
print(orders_df.describe()) # Menampilkan statistik deskriptif

# %%
# Data order payments

print('\nInfo data order payments:')
print(orders_payments_df.info()) # Menampilkan informasi data order payments

# Jumlah data yang hilang pada dataset order payments
print('\nJumlah data yang hilang pada dataset order payments:')
print(orders_payments_df.isnull().sum()) # Mengecek data yang hilang

# Jumlah data yang duplikat pada dataset order payments
print('\nJumlah data yang duplikat pada dataset order payments:')
print(orders_payments_df.duplicated().sum()) # Mengecek data yang duplikat

# Statistik deskriptif dari dataset order payments
print('\nStatistik deskriptif dari dataset order payments:')
print(orders_payments_df.describe()) # Menampilkan statistik deskriptif

# %%


# %%
# Data orders

print('\nInfo data orders:')
print(orders_df.info()) # Menampilkan informasi data orders

# Jumlah data yang hilang pada dataset orders
print('\nJumlah data yang hilang pada dataset orders:')
print(orders_df.isnull().sum()) # Mengecek data yang hilang

# Jumlah data yang duplikat pada dataset orders
print('\nJumlah data yang duplikat pada dataset orders:')
print(orders_df.duplicated().sum()) # Mengecek data yang duplikat

# Statistik deskriptif dari dataset orders
print('\nStatistik deskriptif dari dataset orders:')
print(orders_df.describe()) # Menampilkan statistik deskriptif

# %%
# Data product category name translation

print('\nInfo data product category name translation:')
print(product_category_name_translation_df.info()) # Menampilkan informasi data product category name translation

# Jumlah data yang hilang pada dataset product category name translation
print('\nJumlah data yang hilang pada dataset product category name translation:')
print(product_category_name_translation_df.isnull().sum()) # Mengecek data yang hilang

# Jumlah data yang duplikat pada dataset product category name translation
print('\nJumlah data yang duplikat pada dataset product category name translation:')
print(product_category_name_translation_df.duplicated().sum()) # Mengecek data yang duplikat

# Statistik deskriptif dari dataset product category name translation
print('\nStatistik deskriptif dari dataset product category name translation:')
print(product_category_name_translation_df.describe()) # Menampilkan statistik deskriptif

# %%
# Data products

print('\nInfo data products:')
print(products_df.info()) # Menampilkan informasi data products

# Jumlah data yang hilang pada dataset products
print('\nJumlah data yang hilang pada dataset products:')
print(products_df.isnull().sum()) # Mengecek data yang hilang

# Jumlah data yang duplikat pada dataset products
print('\nJumlah data yang duplikat pada dataset products:')
print(products_df.duplicated().sum()) # Mengecek data yang duplikat

# Statistik deskriptif dari dataset products
print('\nStatistik deskriptif dari dataset products:')
print(products_df.describe()) # Menampilkan statistik deskriptif

# %%
# Data sellers

print('\nInfo data sellers:')
print(sellers_df.info()) # Menampilkan informasi data sellers

# Jumlah data yang hilang pada dataset sellers
print('\nJumlah data yang hilang pada dataset sellers:')
print(sellers_df.isnull().sum()) # Mengecek data yang hilang

# Jumlah data yang duplikat pada dataset sellers
print('\nJumlah data yang duplikat pada dataset sellers:')
print(sellers_df.duplicated().sum()) # Mengecek data yang duplikat

# Statistik deskriptif dari dataset sellers
print('\nStatistik deskriptif dari dataset sellers:')
print(sellers_df.describe()) # Menampilkan statistik deskriptif

# %% [markdown]
# ### Cleaning Data

# %%
# Mengubah kolom waktu menjadi datetime pada dataset orders
orders_df['order_purchase_timestamp'] = pd.to_datetime(orders_df['order_purchase_timestamp'])
orders_df['order_approved_at'] = pd.to_datetime(orders_df['order_approved_at'])
orders_df['order_delivered_carrier_date'] = pd.to_datetime(orders_df['order_delivered_carrier_date'])
orders_df['order_delivered_customer_date'] = pd.to_datetime(orders_df['order_delivered_customer_date'])
orders_df['order_estimated_delivery_date'] = pd.to_datetime(orders_df['order_estimated_delivery_date'])

# Mengubah kolom waktu menjadi datetime pada dataset order_items
orders_items_df['shipping_limit_date'] = pd.to_datetime(orders_items_df['shipping_limit_date'])


# %%
# Cleaning 1

# Menggabungkan dataset product dengan dataset category name
products_dengan_category = products_df.merge(
    product_category_name_translation_df,
    on='product_category_name',
    how='left'
)

# print(products_dengan_category.head())

# Mencari product dengan category name yang tidak ditemukan translasinya
missing_translation = products_dengan_category[products_dengan_category['product_category_name_english'].isnull()]
print(f"Product dengan category name yang tidak ditemukan translasinya: {len(missing_translation)}")

# Mengisi missing value dengan 'uncategorized'
products_dengan_category['product_category_name_english'] = products_dengan_category['product_category_name_english'].fillna('uncategorized')

# Membuat kolom baru untuk Year dan Month pada dataset orders
orders_df['orders_year'] = orders_df['order_purchase_timestamp'].dt.year
orders_df['orders_month'] = orders_df['order_purchase_timestamp'].dt.month
orders_df['orders_yearmonth'] = orders_df['order_purchase_timestamp'].dt.to_period('M')

# Mengecek apakah rentang waktu benar dari 2016 hingga 2018
year_counts = orders_df['orders_year'].value_counts().sort_index()


# Persentase order yang sudah selesai
completed_orders = orders_df[orders_df['order_status'] == 'delivered']
print(f"Persentase order yang sudah selesai: {len(completed_orders) / len(orders_df) * 100:.2f}%")

# %%
# Cleaning 2

# Menghitung total value per order
order_values = orders_payments_df.groupby('order_id')['payment_value'].sum().reset_index()
order_values = order_values.rename(columns={'payment_value': 'order_value'})

# Mencari order yang memiliki payment lebih dari 1
payment_count_per_order = orders_payments_df.groupby('order_id').size().reset_index(name='payment_count')
multiple_payment = payment_count_per_order[payment_count_per_order['payment_count'] > 1]
print(f"Jumlah order dengan multiple payment: {len(multiple_payment)}")

# Menyamakan data lokasi pelanggan
customers_df['customer_city'] = customers_df['customer_city'].str.upper().str.strip()
customers_df['customer_state'] = customers_df['customer_state'].str.upper().str.strip()

# Menghitung jumlah pelanggan di setiap city
customer_city_counts = customers_df.groupby(['customer_city', 'customer_state']).size().reset_index(name='customer_count')
print(f"Jumlah pelanggan di setiap city:\n{customer_city_counts}")

# Menghitung jumlah pelanggan di setiap state
customer_state_counts = customers_df['customer_state'].value_counts()
print(f"Jumlah pelanggan di setiap state:\n{customer_state_counts}")

# %%
# Integration 1
pattern = completed_orders.merge(
    orders_items_df,
    on='order_id',
    how='inner'
).merge(
    products_dengan_category,
    on='product_id',
    how='inner'
)

print(pattern[['orders_year', 'orders_month']].sort_values(by=['orders_year', 'orders_month'], ascending=False).drop_duplicates())

# Menambahkan total price (product price + shipping)
pattern['total_price'] = pattern['price'] + pattern['freight_value']

# Integration 2

order_values_by_location = orders_df.merge(
    order_values, on='order_id', how='inner'
).merge(
    customers_df[['customer_id', 'customer_city', 'customer_state']],
    on='customer_id',
    how='inner'
)

completed_orders_by_location = order_values_by_location[order_values_by_location['order_status'] == 'delivered']

# %% [markdown]
# **Insight:**
# - xxx
# - xxx

# %% [markdown]
# ## Exploratory Data Analysis (EDA)

# %% [markdown]
# ### Explore ...

# %%
# EDA untuk pertanyaan pertama

# Menampilkan tahun dan bulan
print("Distribusi order berdasarkan tahun:")
print(pattern['orders_year'].value_counts().sort_index())
print("\nDistribusi order berdasarkan bulan:")
print(pattern['orders_month'].value_counts().sort_index())

# Menampilkan top 10 kategori berdasarkan jumlah order
top_10_category = pattern['product_category_name_english'].value_counts().head(10)
print("\nTop 10 kategori berdasarkan jumlah order:")
print(top_10_category)

# Menampilkan top 10 total pendapatan per kategori
total_sales_per_category = pattern.groupby('product_category_name_english')['total_price'].sum()
total_sales_per_category = total_sales_per_category.sort_values(ascending=False)
print("\nTop 10 total pendapatan per kategori:")
print(total_sales_per_category.head(10))

# Menampilkan pola penjualan bulanan
monthly_sales = pattern.groupby(['orders_year', 'orders_month'])['total_price'].sum().reset_index()
print("\nTren penjualan bulanan:")
print(monthly_sales.head(10))

# Total penjualan bulanan
monthly_sales_total = monthly_sales.groupby('orders_month')['total_price'].sum()
print("\nTotal penjualan bulanan:")
print(monthly_sales_total.head(10))

# Penjualan per kategori per bulan
monthly_sales_per_category = pattern.groupby(['orders_year', 'orders_month', 'product_category_name_english'])['total_price'].sum().reset_index()
print("\nPenjualan per kategori per bulan:")
print(monthly_sales_per_category.head(10))

# Statistik deskriptif
print("\nStatistik ddasar harga item:")
print(pattern['price'].describe())
print("\nStatistik biaya pengiriman:")
print(pattern['freight_value'].describe())

# EDA untuk pertanyaan kedua

# Menghitung order value per states
print("\nOrder value per state:")
order_value_per_state = completed_orders_by_location['customer_state'].value_counts()
print(order_value_per_state)

# Menghitung rata-rata order value per state
print("\nRata-rata order value per state:")
average_order_value_per_state = completed_orders_by_location.groupby('customer_state')['order_value'].mean().reset_index()
average_order_value_per_state = average_order_value_per_state.sort_values(by='order_value', ascending=False)
print(average_order_value_per_state)

# Mengitung median order value per state untuk mengetahui skewness
print("\nMedian order value per state:")
median_order_value_per_state = completed_orders_by_location.groupby('customer_state')['order_value'].median().reset_index()
median_order_value_per_state = median_order_value_per_state.sort_values(by='order_value', ascending=False)
print(median_order_value_per_state)

# Menghitung jumlah order per state
orders_by_state = completed_orders_by_location.groupby('customer_state').size().reset_index(name='order_count')
orders_by_state = orders_by_state.sort_values(by='order_count', ascending=False)
print("\nJumlah order per state:")
print(orders_by_state)

# Statistik nilai order
print("\nStatistik nilai order:")
print(completed_orders_by_location['order_value'].describe())

# Top 5 state dengan rata-rata order value tertinggi dan terendah
print("\nTop 5 state dengan rata-rata order value tertinggi:")
print(average_order_value_per_state.head())
print("\nTop 5 state dengan rata-rata order value terendah:")
print(average_order_value_per_state.tail())

# Top 10 kota berdasarkan rata-rata order value per state
print("\nTop kota berdasarkan rata-rata order value per state:")
top_cities_by_aov = completed_orders_by_location.groupby(['customer_state', 'customer_city'])['order_value'].mean().reset_index()
top_cities_by_aov = top_cities_by_aov.sort_values(by='order_value', ascending=False)
print(top_cities_by_aov.head(10))

# Mengecek outliers pada order value
q1 = completed_orders_by_location['order_value'].quantile(0.25)
q3 = completed_orders_by_location['order_value'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = completed_orders_by_location[(completed_orders_by_location['order_value'] < lower_bound) | (completed_orders_by_location['order_value'] > upper_bound)]
print(f"\nJumlah outliers: {len(outliers)} dari total {len(completed_orders_by_location)} order ({len(outliers) / len(completed_orders_by_location) * 100:.2f}%)")

# %% [markdown]
# **Insight:**
# - xxx
# - xxx

# %% [markdown]
# ## Visualization & Explanatory Analysis

# %% [markdown]
# ### Pertanyaan 1:

# %%


# %% [markdown]
# ### Pertanyaan 2:

# %%


# %% [markdown]
# **Insight:**
# - xxx
# - xxx

# %% [markdown]
# ## Analisis Lanjutan (Opsional)

# %%


# %% [markdown]
# ## Conclusion

# %% [markdown]
# - Conclution pertanyaan 1
# - Conclution pertanyaan 2


