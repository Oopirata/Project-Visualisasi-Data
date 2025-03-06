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

# %% [markdown]
# Data customers

# %%
# Import data customers
customers_df = pd.read_csv('data/customers_dataset.csv')

# Copy dataframe untuk tetap menyimpan dataframe aslinya
customers_df_original = customers_df.copy()

# Print 5 baris pertama dari dataframe
print('5 baris pertama dari dataframe:')
print(customers_df.head())

# Jumlah keseluruhan baris dan kolom
print('\nJumlah keseluruhan baris dan kolom:')
print(customers_df.shape)

# %% [markdown]
# Data geolocations

# %%
# Import data geolocations
geolocations_df = pd.read_csv('data/geolocation_dataset.csv')

# Copy dataframe untuk tetap menyimpan dataframe aslinya
geolocations_df_original = geolocations_df.copy()

# Print 5 baris pertama dari dataframe
print('5 baris pertama dari dataframe:')
print(geolocations_df.head())

# Jumlah keseluruhan baris dan kolom
print('\nJumlah keseluruhan baris dan kolom:')
print(geolocations_df.shape)

# %% [markdown]
# Data order items

# %%
# Import data order items
orders_items_df = pd.read_csv('data/order_items_dataset.csv')

# Copy dataframe untuk tetap menyimpan dataframe aslinya
orders_items_df_original = orders_items_df.copy()

# Print 5 baris pertama dari dataframe
print('5 baris pertama dari dataframe:')
print(orders_items_df.head())

# Jumlah keseluruhan baris dan kolom
print('\nJumlah keseluruhan baris dan kolom:')
print(orders_items_df.shape)

# %% [markdown]
# Data order payments

# %%
# Import data order payments
orders_payments_df = pd.read_csv('data/order_payments_dataset.csv')

# Copy dataframe untuk tetap menyimpan dataframe aslinya
orders_payments_df_original = orders_payments_df.copy()

# Print 5 baris pertama dari dataframe
print('5 baris pertama dari dataframe:')
print(orders_payments_df.head())

# Jumlah keseluruhan baris dan kolom
print('\nJumlah keseluruhan baris dan kolom:')
print(orders_payments_df.shape)

# %% [markdown]
# Data order reviews

# %%
# Import data order reviews
orders_reviews_df = pd.read_csv('data/order_reviews_dataset.csv')

# Copy dataframe untuk tetap menyimpan dataframe aslinya
orders_reviews_df_original = orders_reviews_df.copy()

# Print 5 baris pertama dari dataframe
print('5 baris pertama dari dataframe:')
print(orders_reviews_df.head())

# Jumlah keseluruhan baris dan kolom
print('\nJumlah keseluruhan baris dan kolom:')
print(orders_reviews_df.shape)

# %% [markdown]
# Data orders

# %%
# Import data orders
orders_df = pd.read_csv('data/orders_dataset.csv')

# Copy dataframe untuk tetap menyimpan dataframe aslinya
orders_df_original = orders_df.copy()

# Print 5 baris pertama dari dataframe
print('5 baris pertama dari dataframe:')
print(orders_df.head())

# Jumlah keseluruhan baris dan kolom
print('\nJumlah keseluruhan baris dan kolom:')
print(orders_df.shape)

# %% [markdown]
# Data product category name translation

# %%
# Import data product category name translation
category_translation_df = pd.read_csv('data/product_category_name_translation.csv')

# Copy dataframe untuk tetap menyimpan dataframe aslinya
category_translation_df_original = category_translation_df.copy()

# Print 5 baris pertama dari dataframe
print('5 baris pertama dari dataframe:')
print(category_translation_df.head())

# Jumlah keseluruhan baris dan kolom
print('\nJumlah keseluruhan baris dan kolom:')
print(category_translation_df.shape)

# %% [markdown]
# Data products

# %%
# Import data products
products_df = pd.read_csv('data/products_dataset.csv')

# Copy dataframe untuk tetap menyimpan dataframe aslinya
products_df_original = products_df.copy()

# Print 5 baris pertama dari dataframe
print('5 baris pertama dari dataframe:')
print(products_df.head())

# Jumlah keseluruhan baris dan kolom
print('\nJumlah keseluruhan baris dan kolom:')
print(products_df.shape)

# %% [markdown]
# Data sellers

# %%
# Import data sellers
sellers_df = pd.read_csv('data/sellers_dataset.csv')

# Copy dataframe untuk tetap menyimpan dataframe aslinya
sellers_df_original = sellers_df.copy()

# Print 5 baris pertama dari dataframe
print('5 baris pertama dari dataframe:')
print(sellers_df.head())

# Jumlah keseluruhan baris dan kolom
print('\nJumlah keseluruhan baris dan kolom:')
print(sellers_df.shape)

# %% [markdown]
# **Insight:**
# - Melalui import csv di atas, telah berhasil dilakukan penimporan 8 dataset yang terkait dengan e-commerce di Brazil.
# - Dataset-dataset ini mencakup informasi tentang pelanggan, geolokasi, pesanan, pembayaran, ulasan, produk, kategori produk, dan penjual.
# - Pada masing-masing dataframe telah dibuat `copy()` untuk menyimpan data asli.

# %% [markdown]
# ### Assessing Data

# %% [markdown]
# Data customers

# %%
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
# - Dataset customers terdiri dari 99.441 baris dan 5 kolom.
# - Tidak terdapat nilai yang hilang (missing values) pada dataset customers.
# - Tidak terdapat data duplikat pada dataset customers.
# - Semua pelanggan memiliki ID yang unik.

# %% [markdown]
# Data geolocations

# %%
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

# %% [markdown]
# **Insight:**
# - Dataset geolocations terdiri dari 1.000.163 baris dan 5 kolom.
# - Terdapat banyak data duplikat dalam dataset geolocation, yang mungkin menunjukkan beberapa kode pos yang sama.
# - Data latitude dan longitude tersedia untuk semua lokasi.

# %% [markdown]
# Data order items

# %%
print('\nInfo data order items:')
print(orders_items_df.info()) # Menampilkan informasi data order items

# Jumlah data yang hilang pada dataset order items
print('\nJumlah data yang hilang pada dataset order items:')
print(orders_items_df.isnull().sum()) # Mengecek data yang hilang

# Jumlah data yang duplikat pada dataset order items
print('\nJumlah data yang duplikat pada dataset order items:')
print(orders_items_df.duplicated().sum()) # Mengecek data yang duplikat

# Statistik deskriptif dari dataset order items
print('\nStatistik deskriptif dari dataset order items:')
print(orders_items_df.describe()) # Menampilkan statistik deskriptif

# %% [markdown]
# **Insight:**
# - Dataset order items terdiri dari 112.650 baris dan 7 kolom.
# - Tidak ada nilai yang hilang dalam dataset.
# - Data ini mencakup informasi tentang produk yang dibeli, harga, dan pengiriman.

# %% [markdown]
# Data order payments

# %%
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

# %% [markdown]
# **Insight:**
# - Dataset order payments terdiri dari 103.886 baris dan 5 kolom.
# - Tidak ada nilai yang hilang dalam dataset.
# - Data ini mencakup informasi tentang metode pembayaran dan nilai pembayaran.

# %% [markdown]
# Data orders

# %%
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

# %% [markdown]
# **Insight:**
# - Dataset orders terdiri dari 99.441 baris dan 8 kolom.
# - Terdapat beberapa nilai yang hilang pada kolom order_approved_at, order_delivered_carrier_date, dan order_delivered_customer_date, kemungkinan kosong karena ada order yang dibatalkan.
# - Tidak ada data duplikat dalam dataset.
# - Data ini mencakup informasi tentang status pesanan dan waktu pemrosesan.

# %% [markdown]
# Data product category name translation

# %%
print('\nInfo data product category name translation:')
print(category_translation_df.info()) # Menampilkan informasi data product category name translation

# Jumlah data yang hilang pada dataset product category name translation
print('\nJumlah data yang hilang pada dataset product category name translation:')
print(category_translation_df.isnull().sum()) # Mengecek data yang hilang

# Jumlah data yang duplikat pada dataset product category name translation
print('\nJumlah data yang duplikat pada dataset product category name translation:')
print(category_translation_df.duplicated().sum()) # Mengecek data yang duplikat

# Statistik deskriptif dari dataset product category name translation
print('\nStatistik deskriptif dari dataset product category name translation:')
print(category_translation_df.describe()) # Menampilkan statistik deskriptif

# %% [markdown]
# **Insight:**
# - Dataset product category translation terdiri dari 71 baris dan 2 kolom.
# - Tidak ada nilai yang hilang dalam dataset.
# - Dataset ini berisi terjemahan nama kategori produk dari Portugis ke Inggris.

# %% [markdown]
# Data products

# %%
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

# %% [markdown]
# **Insight:**
# - Dataset products terdiri dari 32.951 baris dan 9 kolom.
# - Terdapat beberapa nilai yang hilang pada kolom product_category_name dan kolom-kolom deskripsi produk.
# - Tidak ada data duplikat dalam dataset.
# - Dataset ini mencakup informasi tentang dimensi dan berat produk.

# %% [markdown]
# Data sellers

# %%
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
# **Insight:**
# - Dataset sellers terdiri dari 3.095 baris dan 4 kolom.
# - Tidak ada nilai yang hilang dalam dataset.
# - Tidak ada data duplikat dalam dataset.
# - Dataset ini mencakup informasi tentang lokasi penjual.

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


# %% [markdown]
# Cleaning 1: Integrasi Kategori Produk dan Ekstraksi Fitur Waktu

# %%
# Menggabungkan dataset product dengan dataset category name
products_with_categories = products_df.merge(
    category_translation_df,
    on='product_category_name',
    how='left'
)

# Mencari product dengan category name yang tidak ditemukan translasinya
missing_translation = products_with_categories[products_with_categories['product_category_name_english'].isnull()]
print(f"Product dengan category name yang tidak ditemukan translasinya: {len(missing_translation)}")

# Mengisi missing value dengan 'uncategorized'
products_with_categories['product_category_name_english'] = products_with_categories['product_category_name_english'].fillna('uncategorized')

# Membuat kolom baru untuk Year dan Month pada dataset orders
orders_df['orders_year'] = orders_df['order_purchase_timestamp'].dt.year
orders_df['orders_month'] = orders_df['order_purchase_timestamp'].dt.month
orders_df['orders_yearmonth'] = orders_df['order_purchase_timestamp'].dt.to_period('M')

# Mengecek apakah rentang waktu benar dari 2016 hingga 2018
year_counts = orders_df['orders_year'].value_counts().sort_index()


# Persentase order yang sudah selesai
completed_orders = orders_df[orders_df['order_status'] == 'delivered']
print(f"Persentase order yang sudah selesai: {len(completed_orders) / len(orders_df) * 100:.2f}%")

# %% [markdown]
# Cleaning 2: Persiapan Data untuk Analisis Order Value dan Lokasi

# %%
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

# %% [markdown]
# Menyiapkan Dataset untuk Analisis Pola Penjualan Produk

# %%
pattern = completed_orders.merge(
    orders_items_df,
    on='order_id',
    how='inner'
).merge(
    products_with_categories,
    on='product_id',
    how='inner'
)

print(pattern[['orders_year', 'orders_month']].sort_values(by=['orders_year', 'orders_month'], ascending=False).drop_duplicates())

# Menambahkan total price (product price + shipping)
pattern['total_price'] = pattern['price'] + pattern['freight_value']

# %% [markdown]
# Menyiapkan Dataset untuk Analisis Average Order Value berdasarkan Lokasi

# %%
order_values_by_location = orders_df.merge(
    order_values, on='order_id', how='inner'
).merge(
    customers_df[['customer_id', 'customer_city', 'customer_state']],
    on='customer_id',
    how='inner'
)

completed_orders_by_location = order_values_by_location[order_values_by_location['order_status'] == 'delivered']
print("Contoh data hasil integrasi untuk analisis lokasi (5 baris pertama):")
print(completed_orders_by_location[['order_id', 'customer_state', 'customer_city', 'order_value']].head())

# %% [markdown]
# **Insight:**
# - Dalam proses cleaning, kita telah berhasil mengintegrasikan beberapa dataset untuk mempersiapkan analisis.
# - Dari total pesanan, 96.48% sudah selesai (status delivered).
# - Terdapat produk yang kategorinya tidak ditemukan terjemahannya; ini telah ditangani dengan label 'uncategorized'.
# - Sekitar 2.65% pesanan menggunakan lebih dari satu metode pembayaran.
# - Data pesanan mencakup rentang waktu dari 2016 hingga 2018, dengan distribusi yang cenderung meningkat setiap tahun.

# %% [markdown]
# ## Exploratory Data Analysis (EDA)

# %% [markdown]
# ### Explore ...

# %% [markdown]
# EDA untuk pertanyaan pertama

# %%
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

# %% [markdown]
# **Insight:**
# - xxx
# - xxx

# %% [markdown]
# EDA untuk pertanyaan kedua

# %%
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
# ## Visualization & Explanatory Analysis

# %% [markdown]
# ### Pertanyaan 1:

# %%
# Menyiapkan plotting menggunakan seaborn untuk visualisasi
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

# Trend penjualan bulanan selama tahun 2016-2018
monthly_sales_trend = pattern.groupby(['orders_year', 'orders_month'])['total_price'].sum().reset_index()
monthly_sales_trend['yearmonth'] = monthly_sales_trend ['orders_year'].astype(str) + '-' + monthly_sales_trend['orders_month'].astype(str).str.zfill(2)
monthly_sales_trend = monthly_sales_trend.sort_values(by=['orders_year', 'orders_month'])

# Visualisasi trend penjualan bulanan
plt.figure(figsize=(14, 6))
plt.plot(monthly_sales_trend['yearmonth'], monthly_sales_trend['total_price'], marker='o', linewidth=2, color='#3498db')
plt.title('Tren Penjualan Bulanan E-commerce Brazil (2016-2018)', fontsize=16, pad=20)
plt.xlabel('Tahun-Bulan', fontsize=14)
plt.ylabel('Total Penjualan (BRL)', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# %%
# Top 10 kategori produk berdasarkan pendapatan
top_10_revenue_categories = pattern.groupby('product_category_name_english')['total_price'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(14, 7))
ax = sns.barplot(x=top_10_revenue_categories.index, y=top_10_revenue_categories.values, hue=top_10_revenue_categories.index, palette='viridis', legend=False)
plt.title('10 Kategori Produk dengan Pendapatan Tertinggi', fontsize=16, pad=20)
plt.xlabel('Kategori Produk', fontsize=14)
plt.ylabel('Total Pendapatan (BRL)', fontsize=14)
plt.xticks(rotation=45, ha='right')

# Menambahkan nilai di atas bar
for i, v in enumerate(top_10_revenue_categories.values):
    ax.text(i, v + 5000, f'R${v:,.0f}', ha='center', fontsize=10)

plt.tight_layout()
plt.show()

# %%
# Visualisasi distribusi penjualan berdasarkan tahun
sales_by_year = pattern.groupby('orders_year')['total_price'].sum()

plt.figure(figsize=(10, 6))
ax = sns.barplot(x=sales_by_year.index, y=sales_by_year.values, hue=sales_by_year.index, palette='Blues_d', legend=False)
plt.title('Total Penjualan per Tahun', fontsize=16, pad=20)
plt.xlabel('Tahun', fontsize=14)
plt.ylabel('Total Penjualan (BRL)', fontsize=14)

# Menambahkan nilai di atas bar
for i, v in enumerate(sales_by_year.values):
    ax.text(i, v + 10000, f'R${v:,.0f}', ha='center', fontsize=12)

plt.tight_layout()
plt.show()

# %%
# Visualisasi pola penjualan bulanan
monthly_pattern = pattern.groupby('orders_month')['total_price'].sum().reset_index()

plt.figure(figsize=(12, 6))
ax = sns.barplot(x='orders_month', y='total_price', data=monthly_pattern, hue='orders_month', palette='YlGnBu', legend=False)
plt.title('Pola Penjualan Bulanan (Semua Tahun)', fontsize=16, pad=20)
plt.xlabel('Bulan', fontsize=14)
plt.ylabel('Total Penjualan (BRL)', fontsize=14)

# Menambahkan nilai di atas bar
for i, v in enumerate(monthly_pattern['total_price']):
    ax.text(i, v + 5000, f'R${v:,.0f}', ha='center', fontsize=10)

plt.tight_layout()
plt.show()

# %%
# Visualisasi heat map kategori produk teratas per bulan

# Memilih top 8 kategori untuk visualisasi
top_8_categories = pattern.groupby('product_category_name_english')['total_price'].sum().sort_values(ascending=False).head(8).index

# Filter data untuk top 8 kategori
top_categories_monthly = pattern[pattern['product_category_name_english'].isin(top_8_categories)]
heatmap_data = top_categories_monthly.groupby(['orders_month', 'product_category_name_english'])['total_price'].sum().reset_index()
heatmap_pivot = heatmap_data.pivot(index='product_category_name_english', columns='orders_month', values='total_price')

plt.figure(figsize=(16, 8))
sns.heatmap(heatmap_pivot, cmap="YlGnBu", annot=True, fmt='.0f', linewidths=.5, cbar_kws={'label': 'Total Penjualan (BRL)'})
plt.title('Penjualan Bulanan untuk 8 Kategori Produk Teratas', fontsize=16, pad=20)
plt.ylabel('Kategori Produk', fontsize=14)
plt.xlabel('Bulan', fontsize=14)
plt.tight_layout()
plt.show()

# %% [markdown]
# ### Pertanyaan 2:

# %%
# Visualisasi Average Order Value (AOV) per State di Brazil
average_order_value_per_state = completed_orders_by_location.groupby('customer_state')['order_value'].mean().reset_index()
average_order_value_per_state = average_order_value_per_state.sort_values(by='order_value', ascending=False)

plt.figure(figsize=(16, 8))
ax = sns.barplot(x='customer_state', y='order_value', data=average_order_value_per_state, hue='customer_state', palette='viridis', legend=False)
plt.title('Rata-rata Nilai Pesanan (AOV) per State di Brazil', fontsize=16, pad=20)
plt.xlabel('State', fontsize=14)
plt.ylabel('Average Order Value (BRL)', fontsize=14)
plt.axhline(y=average_order_value_per_state['order_value'].mean(), color='r', linestyle='--', alpha=0.7, 
            label=f'Rata-rata Nasional: R${average_order_value_per_state["order_value"].mean():,.2f}')
plt.legend()

# Menambahkan nilai di atas bar
for i, v in enumerate(average_order_value_per_state['order_value']):
    ax.text(i, v + 1, f'R${v:,.0f}', ha='center', fontsize=9, rotation=0)

plt.tight_layout()
plt.show()

# %%
# Visualisasi perbandingan jumlah order dengan AOV per state

# Menggabungkan data AOV dengan jumlah order
state_comparison = average_order_value_per_state.merge(
    completed_orders_by_location.groupby('customer_state').size().reset_index(name='order_count'),
    on='customer_state'
)

# Menambahkan kolom total revenue
state_comparison['total_revenue'] = state_comparison['order_value'] * state_comparison['order_count']

# Membuat scatter plot
plt.figure(figsize=(14, 8))
scatter = plt.scatter(state_comparison['order_count'], 
                     state_comparison['order_value'], 
                     s=state_comparison['total_revenue']/50000, 
                     c=state_comparison['total_revenue'], 
                     cmap='viridis', 
                     alpha=0.7)

# Menambahkan label pada setiap titik
for i, row in state_comparison.iterrows():
    plt.annotate(row['customer_state'], 
                (row['order_count'] + 50, row['order_value']), 
                fontsize=10)

plt.colorbar(scatter, label='Total Revenue (BRL)')
plt.title('Hubungan antara Jumlah Order, Average Order Value, dan Total Revenue per State', fontsize=16, pad=20)
plt.xlabel('Jumlah Order', fontsize=14)
plt.ylabel('Average Order Value (BRL)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# %%
# Visualisasi ox plot distribusi order value per state (top 10 states berdasarkan jumlah order)
top_10_states_by_orders = completed_orders_by_location['customer_state'].value_counts().head(10).index

plt.figure(figsize=(16, 8))
sns.boxplot(x='customer_state', y='order_value', data=completed_orders_by_location[completed_orders_by_location['customer_state'].isin(top_10_states_by_orders)], hue='customer_state', palette='Set3', legend=False)
plt.title('Distribusi Nilai Pesanan di 10 State dengan Jumlah Order Tertinggi', fontsize=16, pad=20)
plt.xlabel('State', fontsize=14)
plt.ylabel('Order Value (BRL)', fontsize=14)
plt.ylim(0, 500)  # Membatasi y-axis untuk melihat distribusi dengan lebih jelas
plt.tight_layout()
plt.show()

# %%
# Visualisasi heatmap untuk AOV 10 kota teratas di 5 state dengan AOV tertinggi

# Mendapatkan 5 state dengan AOV tertinggi
top_5_states_by_aov = average_order_value_per_state.head(5)['customer_state'].tolist()

# Filter kota di 5 state dengan AOV tertinggi
top_cities_in_top_states = completed_orders_by_location[completed_orders_by_location['customer_state'].isin(top_5_states_by_aov)]
top_cities_aov = top_cities_in_top_states.groupby(['customer_state', 'customer_city'])['order_value'].mean().reset_index()

# Untuk setiap state, ambil 10 kota dengan AOV tertinggi
top_cities_per_state = []
for state in top_5_states_by_aov:
    state_cities = top_cities_aov[top_cities_aov['customer_state'] == state].nlargest(10, 'order_value')
    top_cities_per_state.append(state_cities)

top_cities_final = pd.concat(top_cities_per_state)

# Membuat pivot table untuk visualisasi heatmap
heatmap_cities = top_cities_final.pivot(index='customer_city', columns='customer_state', values='order_value')

plt.figure(figsize=(14, 12))
sns.heatmap(heatmap_cities, cmap="YlOrRd", annot=True, fmt='.1f', linewidths=.5, cbar_kws={'label': 'Average Order Value (BRL)'})
plt.title('Average Order Value di Kota-kota Teratas dari 5 State dengan AOV Tertinggi', fontsize=16, pad=20)
plt.ylabel('Kota', fontsize=14)
plt.xlabel('State', fontsize=14)
plt.tight_layout()
plt.show()

# %%
# Visualisasi histogram distribusi Order Value dan perbandingan Mean vs Median
plt.figure(figsize=(12, 6))

# Histogram dengan KDE
sns.histplot(completed_orders_by_location['order_value'], kde=True, bins=50, color='skyblue')

# Menambahkan garis untuk mean dan median
plt.axvline(x=completed_orders_by_location['order_value'].mean(), color='red', linestyle='--', 
            label=f'Mean: R${completed_orders_by_location["order_value"].mean():,.2f}')
plt.axvline(x=completed_orders_by_location['order_value'].median(), color='green', linestyle='-.', 
            label=f'Median: R${completed_orders_by_location["order_value"].median():,.2f}')

plt.title('Distribusi Nilai Pesanan (Order Value)', fontsize=16, pad=20)
plt.xlabel('Order Value (BRL)', fontsize=14)
plt.ylabel('Frekuensi', fontsize=14)
plt.xlim(0, 500)  # Membatasi x-axis untuk melihat distribusi dengan lebih jelas
plt.legend()
plt.tight_layout()
plt.show()

# %% [markdown]
# **Insight:**
#  1. **Tren Penjualan Bulanan (2016-2018):**
#     - Terjadi peningkatan penjualan yang signifikan dari 2016 ke 2018, menunjukkan pertumbuhan bisnis e-commerce di Brazil.
#     - Terlihat adanya lonjakan penjualan pada bulan November, kemungkinan karena adanya event belanja besar seperti Black Friday.
#     - Awal tahun (Januari-Februari) cenderung menunjukkan penurunan penjualan dibandingkan akhir tahun sebelumnya.
#  
#  2. **Kategori Produk dengan Pendapatan Tertinggi:**
#     - Kategori "bed_bath_table" (peralatan tempat tidur, kamar mandi, dan meja) menjadi kontributor pendapatan tertinggi, diikuti oleh "health_beauty" dan "sports_leisure".
#     - Produk-produk rumah tangga dan perawatan pribadi mendominasi top 10 kategori pendapatan tertinggi, menunjukkan kebutuhan konsumen Brazil akan produk-produk tersebut melalui e-commerce.
#     - Meskipun kategori elektronik seperti "computers_accessories" dan "telephony" masuk dalam top 10, namun tidak mendominasi, yang mungkin berbeda dengan tren global e-commerce.
#  
#  3. **Pola Penjualan Musiman:**
#     - Penjualan cenderung meningkat di paruh kedua tahun (bulan 7-12) dengan puncaknya di bulan 11 (November).
#     - Bulan 5 (Mei) juga menunjukkan angka penjualan yang cukup tinggi, mungkin terkait dengan hari perayaan atau event promosi tertentu di Brazil.
#     - Pola penjualan bulanan ini konsisten di semua kategori produk teratas, yang menunjukkan bahwa faktor musiman mempengaruhi seluruh pasar e-commerce, bukan hanya kategori tertentu.
# 
#  4. **Variasi Average Order Value (AOV) antar State:**
#     - Terdapat variasi yang signifikan dalam AOV antar state di Brazil, dengan beberapa state menunjukkan AOV hingga 20-30% di atas rata-rata nasional.
#     - State seperti PB, AL, AC, RR, dan AP memiliki AOV tertinggi, meskipun jumlah total pesanan mereka relatif rendah dibandingkan state lain.
#     - State dengan jumlah pesanan terbanyak seperti SP (São Paulo) memiliki AOV yang lebih mendekati rata-rata nasional.
#  
#  5. **Hubungan antara Jumlah Order dan AOV:**
#     - Terdapat korelasi negatif antara jumlah order dan AOV; state dengan jumlah order yang lebih tinggi cenderung memiliki AOV yang lebih rendah.
#     - State-state yang lebih kecil atau kurang urbanisasi seperti AP, RR, dan AC memiliki AOV yang lebih tinggi tetapi volume pesanan yang jauh lebih rendah.
#     - Fenomena ini mungkin disebabkan oleh perbedaan infrastruktur logistik, dimana konsumen di daerah terpencil cenderung membuat pesanan yang lebih besar untuk mengompensasi biaya pengiriman atau keterbatasan akses.
#  
#  6. **Distribusi Order Value:**
#     - Distribusi order value menunjukkan positive skewness (menceng ke kanan), dengan banyak pesanan bernilai rendah dan sedikit pesanan bernilai sangat tinggi.
#     - Perbedaan yang signifikan antara mean (rata-rata) dan median menunjukkan adanya outlier yang mempengaruhi rata-rata.
#     - Sebagian besar pesanan bernilai antara R$50 hingga R$150, yang menunjukkan kisaran harga produk yang paling umum dibeli oleh konsumen Brazil.
#  
#  7. **Variasi dalam Kota-kota di State yang Sama:**
#     - Bahkan dalam state yang sama, terdapat variasi AOV yang signifikan antar kota.
#     - Kota-kota yang lebih kecil dalam state dengan AOV tinggi cenderung memiliki nilai pesanan rata-rata yang lebih tinggi dibandingkan kota-kota besar.
#     - Hal ini mungkin mencerminkan perbedaan perilaku konsumen, daya beli, atau preferensi produk antara daerah perkotaan dan pedesaan.

# %% [markdown]
# ## Analisis Lanjutan (Opsional)

# %%


# %% [markdown]
# ## Conclusion

# %% [markdown]
# - Conclution pertanyaan 1: Bagaimana pola penjualan produk berdasarkan kategori selama periode 2016-2018, dan kategori produk apa yang memberikan kontribusi pendapatan tertinggi?
# 
# 1. **Tren Pertumbuhan yang Kuat:**
#    - E-commerce di Brazil menunjukkan pertumbuhan yang signifikan dari 2016 hingga 2018, dengan peningkatan penjualan yang konsisten, menunjukkan adopsi dan penetrasi e-commerce yang cepat di pasar Brazil.
#    - Pertumbuhan ini mencerminkan tren global dimana konsumen semakin beralih ke belanja online untuk berbagai kategori produk.
# 
# 2. **Seasonality yang Jelas:**
#    - Terdapat pola musiman yang jelas dalam penjualan e-commerce Brazil, dengan puncak di bulan November (kemungkinan karena Black Friday) dan penurunan di awal tahun.
#    - Pola musiman ini konsisten di semua kategori produk teratas, menunjukkan perilaku konsumen yang dipengaruhi oleh siklus belanja tahunan dan event promosi besar.
#    - Bisnis e-commerce di Brazil harus merencanakan strategi inventaris dan pemasaran yang mempertimbangkan fluktuasi musiman ini untuk mengoptimalkan penjualan.
# 
# 3. **Dominasi Kategori Produk:**
#    - Kategori "bed_bath_table" (peralatan tempat tidur, kamar mandi, dan meja) menjadi kontributor pendapatan tertinggi, diikuti oleh produk kesehatan & kecantikan dan olahraga & rekreasi.
#    - Preferensi ini menunjukkan bahwa konsumen Brazil cenderung membeli produk rumah tangga dan perawatan pribadi secara online, mungkin karena kemudahan perbandingan produk dan harga.
#    - Strategi pemasaran dan pengembangan platform e-commerce di Brazil sebaiknya memberikan perhatian khusus pada kategori-kategori unggulan ini, sambil tetap mengembangkan kategori lain dengan potensi pertumbuhan tinggi.
# 
# - Conclution pertanyaan 2: Bagaimana perbandingan nilai rata-rata transaksi (average order value) antar wilayah geografis di Brazil?
# 
# 1. **Disparitas Regional yang Signifikan:**
#    - Terdapat variasi AOV yang signifikan antar state di Brazil, menunjukkan adanya disparitas ekonomi regional dan perbedaan perilaku konsumen.
#    - State-state dengan infrastruktur dan urbanisasi yang lebih rendah cenderung memiliki AOV yang lebih tinggi tetapi volume pesanan yang lebih rendah.
#    - Fenomena ini menunjukkan perlunya strategi pemasaran dan pengiriman yang disesuaikan dengan karakteristik masing-masing wilayah.
# 
# 2. **Inverse Relationship antara Volume dan AOV:**
#    - State dengan volume pesanan tinggi seperti SP (São Paulo) cenderung memiliki AOV yang lebih rendah, sementara state dengan volume pesanan rendah memiliki AOV yang lebih tinggi.
#    - Hal ini menunjukkan bahwa konsumen di daerah dengan akses e-commerce yang lebih umum membuat pesanan lebih sering tetapi dengan nilai lebih kecil, sementara konsumen di daerah dengan akses lebih terbatas membuat pesanan lebih besar tetapi lebih jarang.
#    - Strategi bisnis sebaiknya mempertimbangkan karakteristik ini dengan menawarkan insentif untuk meningkatkan AOV di state dengan volume tinggi, dan fokus pada peningkatan frekuensi pesanan di state dengan AOV tinggi.
# 
# 3. **Implikasi untuk Logistik dan Pengiriman:**
#    - Variasi AOV dan perilaku pembelian antar wilayah memiliki implikasi penting untuk strategi logistik dan pengiriman.
#    - Daerah dengan AOV tinggi tetapi frekuensi rendah mungkin memerlukan solusi pengiriman yang berbeda dibandingkan daerah dengan AOV rendah tetapi frekuensi tinggi.
#    - Optimalisasi rantai pasokan berdasarkan karakteristik regional ini dapat meningkatkan efisiensi dan kepuasan pelanggan secara signifikan.
# 
# 4. **Distribusi Nilai Pesanan yang Skewed:**
#    - Distribusi nilai pesanan yang menceng ke kanan (positively skewed) dengan perbedaan signifikan antara mean dan median menunjukkan adanya segmen konsumen yang berbeda.
#    - Mayoritas pelanggan membuat pesanan nilai menengah, dengan sebagian kecil yang membuat pesanan bernilai sangat tinggi.
#    - Strategi pemasaran dan pengembangan produk sebaiknya mempertimbangkan kedua segmen ini, dengan fokus pada peningkatan volume untuk segmen menengah dan mempertahankan loyalitas pelanggan premium.


