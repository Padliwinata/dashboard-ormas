import streamlit as st

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
  Berita positif
- jumlah berita positif label 2: 293
- jumlah berita positif label 3: 242
- jumlah berita positif label 1 & 4: 164
- jumlah berita positif label 0: 62 -> (+1) 63

  Berita negatif
- jumlah berita negatif label 0: 709 -> (-9) 700 -> (-1) 699
- jumlah berita negatif label 1: 8
- jumlah berita negatif label 2: 511 -> (-11) 500 -> (+2) 501
- jumlah berita negatif label 3: 415 -> (-12) 403
- jumlah berita negatif label 4: 200 -> (-2) 198 -> (+1) 199


  Berita netral
- jumlah berita netral label 0: 226 -> (+9) 235
- jumlah berita netral label 1: 384
- jumlah berita netral label 2: 583 -> (+11) 594 -> (-1) 593
- jumlah berita netral label 3: 507 -> (+12) 519
- jumlah berita netral label 4: 238 -> (+2) 240 -> (-1) 239

""")

st.image('proof.png')

