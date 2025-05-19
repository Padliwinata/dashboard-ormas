from collections import Counter

import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_csv('processed.csv')
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
        df['ormas_mentioned'].unique().tolist(),
        default=['Ormas Saja']
    )


headlines_df = df[(df['date'].dt.year.isin(years)) & (df['sentiment'].isin(sentiments))]

if specific:
    headlines_df = headlines_df[headlines_df['ormas_mentioned'].isin(ormas)]


st.header('Tabel')
st.dataframe(headlines_df.reset_index(drop=True))

st.header('Wordcount')
wordcount_total = ' '.join(headlines_df['headline']).split()

wordcount_total_counter = Counter(wordcount_total)

wordcount_df = pd.DataFrame(wordcount_total_counter.items(), columns=['keyword', 'jumlah']).sort_values(by='jumlah', ascending=False).reset_index(drop=True)
st.dataframe(wordcount_df)

st.header('Wordcloud')

wordcloud_title = st.text_input("Wordcloud Title", "Wordcloud Ormas")
headlines = ' '.join(headlines_df['headline'])
if len(headlines.split()) == 0:
    headlines = ' '.join(df['headline'])
    st.toast('Data tidak ditemukan :)')
wc = WordCloud(width=800, height=400, background_color='white').generate(headlines)
_, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wc)
plt.axis('off')
plt.title(wordcloud_title)
st.pyplot(plt)


st.header('Pie Chart')

sentiment_counts = headlines_df['sentiment'].value_counts()


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return f'{val} ({pct:.1f}%)'
    return my_autopct


# Create a Matplotlib figure
fig, ax = plt.subplots()
sentiment_counts.plot(
    kind='pie',
    autopct=make_autopct(sentiment_counts),
    startangle=90,
    ylabel='',  # Hide y-label
    ax=ax
)
existing_sentiments = [s for s in sentiments if s in sentiment_counts]
total = sentiment_counts[existing_sentiments].sum() if existing_sentiments else 0

ax.set_title(
    f'Sentimen semua ormas pada tahun {", ".join(str(year) for year in years)}, {total} berita'
)

# ax.set_title(f'Sentimen semua ormas pada tahun {", ".join(str(year) for year in years)}, {sentiment_counts[sentiments].sum()} berita')

if specific:
    existing_sentiments = [s for s in sentiments if s in sentiment_counts]
    total = sentiment_counts[existing_sentiments].sum() if existing_sentiments else 0

    ax.set_title(
        f'Sentimen semua ormas pada tahun {", ".join(str(year) for year in years)}, {total} berita'
    )
    # try:
    #     ax.set_title(f'Sentimen ormas: {", ".join(ormas)} pada tahun {", ".join(str(year) for year in years)}, {sentiment_counts[sentiments].sum()} berita')
    # except KeyError:
    #     st.toast('Data tidak ditemukan :)')
    #     ax.set_title(f'Sentimen semua ormas pada tahun {", ".join(str(year) for year in years)} sejumlah {sentiment_counts[sentiments].sum()} berita')

ax.axis('equal')  # Make pie circular
plt.tight_layout()

# Display the pie chart in Streamlit
st.pyplot(fig)

missing_sentiments = [s for s in sentiments if s not in sentiment_counts]
if len(missing_sentiments) != 0:
    st.text(f"Sentimen {', '.join(missing_sentiments)} tidak ditemukan")

