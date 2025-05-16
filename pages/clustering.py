from collections import Counter

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"


df = pd.read_csv('processed_clustered.csv')
df['date'] = pd.to_datetime(df['date'])
df = df[(df['date'].dt.year >= 2022) & (df['date'].dt.year <= 2025)]

st.logo('logo.jpeg')

years = st.sidebar.multiselect(
    "Years",
    [2022, 2023, 2024, 2025],
    default=[2024]
)

sentiments = st.sidebar.multiselect(
    "Sentiments",
    ['Negative', 'Neutral', 'Positive'],
    default=['Negative', 'Neutral', 'Positive']
)

specific = st.sidebar.toggle("Specific Ormas")

ormas = []

if specific:
    ormas = st.sidebar.multiselect(
        'Ormas',
        df['ormas'].unique().tolist(),
        default=['Ormas Saja']
    )

headlines_df = df[(df['date'].dt.year.isin(years)) & (df['sentiment'].isin(sentiments))]

if specific:
    headlines_df = headlines_df[headlines_df['ormas'].isin(ormas)]

label = st.sidebar.multiselect('Label berita', options=[0, 1, 2, 3, 4], default=[0])


labels = df['labels_5']
embedding_2d = df[['x', 'y']].values

fig, ax = plt.subplots(figsize=(12, 8))
scatter = ax.scatter(
    embedding_2d[:, 0],
    embedding_2d[:, 1],
    c=labels,
    cmap='tab10',
    s=10,
    alpha=0.7
)

ax.set_title("Visualisasi 5 cluster isu", fontsize=16)
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label("Cluster ID")
ax.set_xlabel("UMAP Dimension 1")
ax.set_ylabel("UMAP Dimension 2")
ax.grid(True)

# ✅ Show in Streamlit
st.pyplot(fig)

headlines_df['label'] = labels

st.dataframe(headlines_df[headlines_df['label'].isin(label)][['date', 'headline', 'ormas', 'sentiment']])


