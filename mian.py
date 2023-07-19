import streamlit as st
st.write('# Menghitung luas :p')
st.write('by minum')

panjang= st.number_input('Masukan Panjangnya', 0)
lebar= st.number_input('Masukan Lebarnya', 0)
Hitung_persegi= st.button('Hasil luas persegi')
Hitung_keliling_persegi= st.button('Hasil keliling pesegi')
Hitung_luas_segitiga= st.button('Hasil luas segitiga')

if Hitung_persegi:
    luas_persegi = panjang * lebar
    st.success(f'Hasil luas persegi adalah:{luas_persegi}')
if Hitung_keliling_persegi:
    keliling_persegi = 2 * panjang + 2 * lebar
    st.success(f'Hasil keliling persegi adalah:{keliling_persegi}')
if Hitung_luas_segitiga:
    luas_segitiga= 1/2 * panjang * lebar
    st.success(f'Hasil luas segitiga adalah:{luas_segitiga}')

