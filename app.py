import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Book Sales Dashboard", layout="wide")

# ---------------- CACHE DATA ----------------
@st.cache_data
def load_data():
    df = pd.read_csv("Books_Data_Clean.csv")
    df = df[df['Publishing Year'] > 1970]
    df.dropna(subset=['Book Name'], inplace=True)
    df.columns = df.columns.str.strip()
    return df

df = load_data()

# ---------------- TITLE ----------------
st.title("📚 Book Sales Analytics Dashboard")

st.markdown("### Explore book performance, genres, sales trends and author insights")

# ---------------- KPIs ----------------
st.markdown("## Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Books", len(df))

with col2:
    st.metric("Total Authors", df['Author'].nunique())

with col3:
    st.metric("Total Genres", df['genre'].nunique())

with col4:
    st.metric("Total Units Sold", int(df['units sold'].sum()))

# ---------------- STATISTICS ----------------
st.markdown("## Dataset Statistics")
st.dataframe(df.describe().T)

# ---------------- CHARTS ----------------
st.markdown("## Data Visualization")

# -------- Row 1 --------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Publishing Year Distribution")

    fig, ax = plt.subplots()
    ax.hist(df['Publishing Year'], bins=20)

    st.pyplot(fig)

with col2:
    st.subheader("Books per Genre")

    genre_count = df['genre'].value_counts()

    fig, ax = plt.subplots()
    genre_count.plot(kind='bar', ax=ax)

    st.pyplot(fig)

# -------- Row 2 --------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sale Price vs Units Sold")

    fig, ax = plt.subplots()
    ax.scatter(df['sale price'], df['units sold'])

    ax.set_xlabel("Sale Price")
    ax.set_ylabel("Units Sold")

    st.pyplot(fig)

with col2:
    st.subheader("Units Sold by Publishing Year")

    year_sales = df.groupby('Publishing Year')['units sold'].sum()

    fig, ax = plt.subplots()
    year_sales.plot(ax=ax)

    st.pyplot(fig)

# -------- Row 3 --------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Language Distribution")

    language_count = df['language_code'].value_counts()

    fig, ax = plt.subplots()

    wedges, texts, autotexts = ax.pie(
        language_count,
        autopct='%1.1f%%',
        startangle=90
    )

    ax.axis('equal')

    ax.legend(
        wedges,
        language_count.index,
        title="Languages",
        loc="center left",
        bbox_to_anchor=(1, 0.5)
    )

    st.pyplot(fig)

with col2:
    st.subheader("Rating Distribution by Genre")

    fig, ax = plt.subplots()
    sns.boxplot(x='genre', y='Book_ratings_count', data=df, ax=ax)

    plt.xticks(rotation=45)

    st.pyplot(fig)

# -------- Row 4 --------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Authors by Gross Sales")

    author_sales = df.groupby('Author')['gross sales'].sum().sort_values(ascending=False).head(10)

    fig, ax = plt.subplots()
    author_sales.plot(kind='bar', ax=ax)

    st.pyplot(fig)

with col2:
    st.subheader("Correlation Heatmap")

    numeric_df = df.select_dtypes(include='number')

    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax)

    st.pyplot(fig)

# ---------------- RAW DATA ----------------
st.markdown("## Dataset")

if st.checkbox("Show Raw Data"):
    st.dataframe(df)