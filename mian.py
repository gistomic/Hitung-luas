import streamlit as st
st.write('# Menghitung luas hehe')
st.write('by minum')

panjang= st.number_input('Masukan Panjangnya', 0)
lebar= st.number_input('Masukan Lebarnya', 0)
Hitung_persegi= st.button('Hasil luas persegi')
Hitung_keliling_persegi= st.button('Hasil keliling pesegi')
Hitung_luas_segitiga= st.button('Hasil luas segitiga')

if Hitung_persegi:
    luas_persegi = panjang * lebar
    st.success(f'Hasil luas persegi adalah:{luas_persegi}cm²')
if Hitung_keliling_persegi:
    keliling_persegi = 2 * panjang + 2 * lebar
    st.success(f'Hasil keliling persegi adalah:{keliling_persegi}cm²')
if Hitung_luas_segitiga:
    luas_segitiga= 1/2 * panjang * lebar
    st.success(f'Hasil luas segitiga adalah:{luas_segitiga}cm²')

st.write('# i like sego goreng and mango')
st.write('what 9+10')
one= st.button('21')
nine= st.button('19')

if one:
    st.success(':0 its false but ur cool!')
if nine:
    st.success(":3 its True!")
