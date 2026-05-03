import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='dark')

all_df = pd.read_csv('main_data.csv')

with st.sidebar:
    st.image('farhan.png', width=150)
    
    st.markdown("### Farhan Nawwafal Pramudia")
    st.caption("Data Science Enthusiast | 6th Semester Student")
    
    st.write("---")
    st.write("🚀 *Submission Tugas Kelas Belajar Fundamental Analisis Data*")
    

def create_product_df(df):
    # Mengelompokkan berdasarkan nama produk dan menghitung jumlah pembelian
    groupby_product = df.groupby('product_category_name_english_x')['order_item_id_x'].count().reset_index()
    groupby_product = groupby_product.sort_values(by='order_item_id_x', ascending=False)
    return groupby_product

def create_payment_type_df(df):
    # Mengelompokkan berdasarkan tipe pembayaran
    groupby_payment = df.groupby('payment_type').size().reset_index(name='payment_count')
    groupby_payment = groupby_payment.sort_values(by='payment_count', ascending=False)
    return groupby_payment

# Siapkan dataframe
groupby_product = create_product_df(all_df)
groupby_payment_type = create_payment_type_df(all_df)

st.header('E-Commerce Performance Dashboard :sparkles:')

st.subheader('Best & Worst Performing Products')

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))

# Top 3 Best Products
colors_best = ["#72BCD4", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x='product_category_name_english_x', 
    y='order_item_id_x', 
    data=groupby_product.head(3), 
    palette=colors_best,
    hue='product_category_name_english_x',
    legend=False,
    ax=ax[0]
)
ax[0].set_xlabel('Product Name', fontsize=12)
ax[0].set_ylabel('Purchase Amount', fontsize=12)
ax[0].set_title('Top 3 Best Product by Number of Sales', loc='center', fontsize=15)
ax[0].tick_params(axis='x', rotation=15) 

# Top 3 Worst Products
colors_worst = ["#72BCD4", "#D3D3D3", "#D3D3D3"]

worst_data = groupby_product.tail(3).sort_values(by='order_item_id_x', ascending=True)
sns.barplot(
    x='product_category_name_english_x', 
    y='order_item_id_x', 
    data=worst_data, 
    palette=colors_worst,
    hue='product_category_name_english_x',
    legend=False,
    ax=ax[1]
)
ax[1].set_xlabel('Product Name', fontsize=12)
ax[1].set_ylabel('Purchase Amount', fontsize=12)
ax[1].set_title('Top 3 Worst Product by Number of Sales', loc='center', fontsize=15)
ax[1].tick_params(axis='x', rotation=15)

st.pyplot(fig)


st.subheader("Payment Type Usage")

# Menampilkan pie chart di tengah layar
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    fig2, ax2 = plt.subplots(figsize=(6, 6))
    explode = (0.1, 0, 0, 0)
    
    # Ambil top 4 payment type
    top_payments = groupby_payment_type.head(4)
    
    ax2.pie(
        top_payments['payment_count'],
        explode=explode,
        labels=top_payments['payment_type'],
        autopct='%1.1f%%',
        shadow=True,
    )
    ax2.set_title('Persentase Payment Type yang Digunakan', fontsize=15)

    st.pyplot(fig2)