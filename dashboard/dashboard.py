import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='dark')

@st.cache_data
def load_data():
    df = pd.read_csv('dashboard/main_data.csv')
    
    if 'shipping_limit_date_x' in df.columns:
        df['shipping_limit_date_x'] = pd.to_datetime(df['shipping_limit_date_x'])
    return df

all_df = load_data()

# Mengambil data tahun 2017
if 'shipping_limit_date_x' in all_df.columns:
    all_df = all_df[all_df['shipping_limit_date_x'].dt.year == 2017]
    all_df['month'] = all_df['shipping_limit_date_x'].dt.month_name()
else:
    all_df['month'] = 'Unknown'

with st.sidebar:        
    st.header("Filter Data (2017)")
    
    # List urutan bulan dari Januari - Desember
    urutan_kalender = [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    
    # Ambil bulan unik dari data
    bulan_dari_data = all_df['month'].dropna().unique().tolist()    
    bulan_list = sorted(bulan_dari_data, key=lambda x: urutan_kalender.index(x))
    
    # Fitur filter 1: Bulan
    selected_month = st.multiselect(
        label='Pilih Bulan',
        options=bulan_list,
        default=bulan_list
    )
    
    # Fitur filter 2: Tipe Pembayaran
    payment_list = all_df['payment_type'].dropna().unique().tolist()
    payment_list = sorted(payment_list)
    selected_payment = st.multiselect(
        label='Pilih Tipe Pembayaran',
        options=payment_list,
        default=payment_list
    )
    
main_df = all_df[
    (all_df['month'].isin(selected_month)) & 
    (all_df['payment_type'].isin(selected_payment))
]

def create_product_df(df):
    groupby_product = df.groupby('product_category_name_english_x')['order_item_id_x'].count().reset_index()
    groupby_product = groupby_product.sort_values(by='order_item_id_x', ascending=False)
    return groupby_product

def create_payment_type_df(df):
    groupby_payment = df.groupby('payment_type').size().reset_index(name='payment_count')
    groupby_payment = groupby_payment.sort_values(by='payment_count', ascending=False)
    return groupby_payment

groupby_product = create_product_df(main_df)
groupby_payment_type = create_payment_type_df(main_df)


st.header('E-Commerce Performance Dashboard :sparkles:')

st.subheader('Best & Worst Performing Products (2017)')

# Cek apakah data kosong setelah difilter
if groupby_product.empty:
    st.warning("Data produk tidak tersedia untuk kombinasi filter ini.")
else:
    # VISUALISASI 1: TOP 3 BEST
    st.markdown("#### Top 3 Best Product by Number of Sales")
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    colors_best = ["#72BCD4", "#D3D3D3", "#D3D3D3"]
    
    sns.barplot(
        x='product_category_name_english_x', 
        y='order_item_id_x', 
        data=groupby_product.head(3), 
        palette=colors_best,
        hue='product_category_name_english_x',
        legend=False,
        ax=ax1
    )
    ax1.set_xlabel('Product Name', fontsize=12)
    ax1.set_ylabel('Purchase Amount', fontsize=12)
    ax1.tick_params(axis='x', rotation=15) 
    
    st.pyplot(fig1) 
    
    st.write("---") 
    
    # VISUALISASI 2: TOP 3 WORST
    st.markdown("#### Top 3 Worst Product by Number of Sales")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    colors_worst = ["#72BCD4", "#D3D3D3", "#D3D3D3"]
    worst_data = groupby_product.tail(3).sort_values(by='order_item_id_x', ascending=True)
    
    sns.barplot(
        x='product_category_name_english_x', 
        y='order_item_id_x', 
        data=worst_data, 
        palette=colors_worst,
        hue='product_category_name_english_x',
        legend=False,
        ax=ax2
    )
    ax2.set_xlabel('Product Name', fontsize=12)
    ax2.set_ylabel('Purchase Amount', fontsize=12)
    ax2.tick_params(axis='x', rotation=15)
    
    st.pyplot(fig2)


st.subheader("Payment Type Usage (2017)")

if groupby_payment_type.empty:
    st.warning("Data metode pembayaran tidak tersedia untuk kombinasi filter ini.")
else:
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        fig3, ax3 = plt.subplots(figsize=(6, 6))
        top_payments = groupby_payment_type.head(4)
        
        explode_len = len(top_payments)
        explode = tuple([0.1] + [0] * (explode_len - 1)) if explode_len > 0 else ()
        
        if explode_len > 0:
            ax3.pie(
                top_payments['payment_count'],
                explode=explode,
                labels=top_payments['payment_type'],
                autopct='%1.1f%%',
                shadow=True,
            )
            ax3.set_title('Persentase Payment Type yang Digunakan', fontsize=15)
            st.pyplot(fig3)