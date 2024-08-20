import streamlit as st
import pandas as pd
from PIL import Image

def run():

    # membuat judul
    st.title('Bone Cancer Prediction')

    # membuat subheader
    st.subheader('Computer Vision pada dataset Bone Cancer')

    #image
    image = Image.open('bone.png')
    st.image(image, caption = 'Bone Cancer Prediction')

    # deskripsi
    st.write('Nama : Heru')
    st.write('Batch : HCK - 018')
    st.write('## Backgorund')
    st.write('Kanker tulang adalah kondisi yang sangat serius, di mana deteksi dini sangat penting untuk keberhasilan pengobatan. Project ini bertujuan untuk mengembangkan model Artificial Neural Network (ANN) yang dapat memprediksi keberadaan kanker tulang melalui hasil X-ray, dengan fokus pada peningkatan recall agar model tidak melakukan salah deteksi terhadap kasus-kasus kanker yang sebenarnya ada. ')
    st.write('## Problem Statement')
    st.write('Tujuan project kali ini adalah untuk mengembangkan model yang mampu memprediksi keberadaan kanker tulang dari hasil X-ray dengan akurat. Model ini dirancang dengan fokus khusus pada recall, sehingga dapat meminimalkan kemungkinan kesalahan ketika pasien yang sebenarnya menderita kanker justru teridentifikasi sebagai sehat. Dengan begitu, risiko diagnosa yang terlewat bisa dikurangi, sehingga hasil pengobatan pasien dapat lebih ditingkatkan.')

    # buat garis
    st.markdown('---')

     # # bold
    st.write('## Exploratory Data Analysis (EDA)')

    # buat garis
    st.markdown('---')

    # EDA 1
    st.write('#### Bagaimana Distribusi Klasifikasi Data?')
    st.image("Distribution.jpg", caption="Distribusi Klasifikasi Data")

    # Deskripsi
    st.write('- Jumlah distribusi yang tidak jauh berbeda pada cancer dan normal.')
    st.write('- 56.3% Merupakan klasifikasi Normal')
    st.write('- 43.7% Merupakan klasifikasi Cancer')
    st.write('- Data Slightly imbalanced')

    # EDA 2
    st.write('#### Bagaimana gambar X-ray dari tulang yang normal dan yang terkena kanker dalam Data?')
    st.image("randovis.jpg", caption="Gambar X-ray dari tulang terkena kanker")
    st.image("randovis2.png", caption="Gambar X-ray dari tulang yang normal")

    # Deskripsi
    st.write('- 5 gambar tulang yang masuk pada klasifikasi normal')
    st.write('- 5 gambar tulang yang masuk pada klasifikasi kanker')
    st.write('- Ukuran gambar sebesar 640x640 pixel')
    st.write('- Gambar memiliki 3 channel')

if __name__ == '__main__':
    run()
