import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Judul Aplikasi
st.title("Aplikasi Visualisasi Data")

# Upload file
uploaded_file = st.file_uploader("Unggah file CSV atau Excel", type=['csv', 'xlsx'])

if uploaded_file is not None:
    # Membaca file yang diunggah
    try:
        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(uploaded_file)
        else:
            data = pd.read_excel(uploaded_file)
        
        # Menampilkan data
        st.write("Berikut adalah data yang diunggah:")
        st.dataframe(data)

        # Menampilkan statistik deskriptif
        st.write("Statistik Deskriptif:")
        st.write(data.describe())

        # Visualisasi Data
        st.write("Visualisasi Kolom Numerik")
        numeric_columns = data.select_dtypes(['float', 'int']).columns
        selected_column = st.selectbox("Pilih kolom untuk visualisasi", numeric_columns)

        if selected_column:
            st.write(f"Histogram untuk kolom {selected_column}")
            fig, ax = plt.subplots()
            sns.histplot(data[selected_column], kde=True, ax=ax)
            st.pyplot(fig)

    except Exception as e:
        st.error(f"Terjadi kesalahan dalam memproses file: {e}")

