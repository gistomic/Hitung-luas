import streamlit as st
st.write('# Menghitung luas')
st.write('caranya masukan nomer yang ingin di hitung luasnya lalu tekan pilihanya untuk memperlihatkan hasilnya')

panjang= st.number_input('Masukan Panjangnya', 0)
lebar= st.number_input('Masukan Lebarnya', 0)
Hitung_persegi= st.button('Hitung luas persegi')
Hitung_keliling_persegi= st.button('Hitung keliling pesegi')
Hitung_luas_segitiga= st.button('Hitung luas segitiga')

if Hitung_persegi:
    luas_persegi = panjang * lebar
    st.success(f'Hasil luas persegi adalah:{luas_persegi}cm²')
if Hitung_keliling_persegi:
    keliling_persegi = 2 * panjang + 2 * lebar
    st.success(f'Hasil keliling persegi adalah:{keliling_persegi}cm²')
if Hitung_luas_segitiga:
    luas_segitiga= 1/2 * panjang * lebar
    st.success(f'Hasil luas segitiga adalah:{luas_segitiga}cm²')

st.write('# i like noodles')
st.write('what 9+10')
one= st.button('21')
nine= st.button('19')

if one:
    st.success('yes :0')
if nine:
    st.success("no >:3")

st.write('>created by Gis')
