import streamlit as st

st.title('Rangkuman data yang tercantum pada findings')

old = """
Data needed:
- total n: 4542
- jumlah artikel netral 2022-2025: 1970
- persentase berita netral dari total: 43.4%
- selisih netral sama negatif (persentase dan jumlah): 3.5% & 160

  Berita positif
- jumlah dan persentase berita positif: 762 & 16.8%
- jumlah berita positif label 2: 293
- jumlah berita positif label 3: 242
- jumlah berita positif label 1 & 4: 164
- jumlah berita positif label 0: 63

  Berita negatif
- jumlah berita negatif label 0: 699
- jumlah berita negatif label 2: 501
- jumlah berita negatif label 4: 199
"""

# new =

st.markdown("""
Data needed:
- total n: 4542
- jumlah artikel netral 2022-2025: 1970
- persentase berita netral dari total: 43.4%
- selisih netral sama negatif (persentase dan jumlah): 3.5% & 160

  Berita positif
- jumlah dan persentase berita positif: 762 & 16.8%
- jumlah berita positif label 2: 293
- jumlah berita positif label 3: 242
- jumlah berita positif label 1 & 4: 164
- jumlah berita positif label 0: 63
total positif = (293 + 242 + 164 + 63) = 762

  Berita negatif
- jumlah berita negatif label 0: 699
- jumlah berita negatif label 1: 8
- jumlah berita negatif label 2: 501 
- jumlah berita negatif label 3: 403
- jumlah berita negatif label 4: 199
total negatif = (699 + 8 + 501 + 403 + 199) = 1810


  Berita netral
- jumlah berita netral label 0: 235
- jumlah berita netral label 1: 384
- jumlah berita netral label 2: 593 + 235 = 828 
- jumlah berita netral label 3: 519
- jumlah berita netral label 4: 239
total netral = (235 + 384 + 593 + 519 + 239) = 1970



""")
