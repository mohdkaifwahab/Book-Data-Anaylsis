# 📚 Book Sales Data Analysis Dashboard

## 🌐 Live Application

Access the deployed dashboard here:

https://book-data-analysis.streamlit.app/

---

# 📖 Project Overview

The **Book Sales Data Analysis Dashboard** is an interactive data analytics application built using **Python and Streamlit**.

The purpose of this project is to analyze book-related data and extract insights about:

* Publishing trends
* Genre distribution
* Author performance
* Sales performance
* Price vs demand relationships
* Language distribution

This dashboard allows users to explore the dataset visually using multiple charts and statistical summaries.

The application demonstrates **data analysis, visualization, and dashboard development skills**, which are essential for **Data Analyst and Data Science roles**.

---

# 🎯 Objectives of the Project

The main goals of this project are:

* Perform **exploratory data analysis (EDA)** on book sales data
* Visualize important trends in the dataset
* Identify relationships between different variables
* Create an **interactive dashboard**
* Present insights in a clear and visual way

---

# 📊 Dataset Description

The dataset contains information about books including:

| Column             | Description                     |
| ------------------ | ------------------------------- |
| Book Name          | Name of the book                |
| Author             | Author of the book              |
| genre              | Genre category of the book      |
| Publishing Year    | Year the book was published     |
| language_code      | Language of the book            |
| sale price         | Price at which the book is sold |
| units sold         | Number of copies sold           |
| gross sales        | Total sales revenue             |
| Book_ratings_count | Number of ratings received      |

This dataset helps analyze **sales performance and popularity of books**.

---

# 🔧 Data Cleaning

Before analysis, the dataset was cleaned using the following steps:

1. Removed books published before **1970**
2. Removed rows with missing **Book Name**
3. Standardized column names
4. Ensured numerical columns were usable for analysis

These steps help improve **data quality and reliability of insights**.

---

# 📈 Key Performance Indicators (KPIs)

The dashboard displays important metrics:

### Total Books

Shows the total number of books in the dataset.

### Total Authors

Indicates how many unique authors are present.

### Total Genres

Shows the diversity of genres in the dataset.

### Total Units Sold

Represents the total number of book copies sold.

These KPIs provide a **quick overview of the dataset**.

---

# 📊 Data Visualizations and Their Purpose

Multiple charts are used to analyze the dataset from different perspectives.

---

## 1️⃣ Publishing Year Distribution (Histogram)

Purpose:

This chart shows how many books were published in different years.

Why this chart was used:

* Helps identify **publishing trends**
* Shows which years had more book publications
* Useful for understanding **industry growth over time**

---

## 2️⃣ Books per Genre (Bar Chart)

Purpose:

Shows the number of books available in each genre.

Why this chart was used:

* Helps understand **genre popularity**
* Shows which genres dominate the dataset
* Useful for identifying **market trends**

---

## 3️⃣ Sale Price vs Units Sold (Scatter Plot)

Purpose:

Shows the relationship between book price and units sold.

Why this chart was used:

* Helps determine whether **higher price affects sales**
* Identifies trends such as:

  * cheaper books selling more
  * premium books performing differently

This chart is commonly used for **relationship analysis**.

---

## 4️⃣ Units Sold by Publishing Year (Line Chart)

Purpose:

Shows how book sales change over time.

Why this chart was used:

* Line charts are ideal for **time-series analysis**
* Helps identify trends such as:

  * sales growth
  * declining periods

---

## 5️⃣ Language Distribution (Pie Chart)

Purpose:

Shows the proportion of books written in different languages.

Why this chart was used:

* Pie charts are useful for **showing percentage distribution**
* Helps identify which languages dominate the dataset

---

## 6️⃣ Rating Distribution by Genre (Box Plot)

Purpose:

Shows how ratings vary across genres.

Why this chart was used:

* Box plots help analyze:

  * distribution
  * outliers
  * spread of data
* Useful for comparing **ratings between genres**

---

## 7️⃣ Top Authors by Gross Sales (Bar Chart)

Purpose:

Shows which authors generated the highest sales revenue.

Why this chart was used:

* Helps identify **top-performing authors**
* Useful for understanding **market influence of authors**

---

## 8️⃣ Correlation Heatmap

Purpose:

Shows relationships between numerical variables.

Why this chart was used:

* Heatmaps help identify **correlations between variables**
* Useful for discovering relationships such as:

  * price vs sales
  * ratings vs popularity

---

# ⚡ Performance Optimization

The dataset loading is optimized using:

`st.cache_data`

This ensures the dataset is **loaded once and reused**, improving performance and reducing loading time.

---

# 🛠️ Technologies Used

The following technologies were used to build this project:

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Programming language      |
| Streamlit  | Dashboard framework       |
| Pandas     | Data manipulation         |
| Matplotlib | Data visualization        |
| Seaborn    | Statistical visualization |

---

# 📂 Project Structure

```
book-data-analysis
│
├── app.py
├── Books_Data_Clean.csv
├── requirements.txt
└── README.md
```

---

# ▶️ Running the Project Locally

Clone the repository:

```
git clone https://github.com/your-username/book-data-analysis.git
```

Move into the project folder:

```
cd book-data-analysis
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the Streamlit app:

```
streamlit run app.py
```

The dashboard will open in your browser.

---

# 👨‍💻 Author

Mohd Kaif

GitHub
https://github.com/kaifwahab001

LinkedIn
https://www.linkedin.com/in/kaif-wahab-571799245

---

⭐ If you found this project useful, consider giving it a star.
