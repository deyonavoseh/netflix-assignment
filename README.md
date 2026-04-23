# Netflix Shows and Movies - Visual Analytics Assignment

## Project Overview
This project analyzes the Netflix Shows and Movies dataset to gain insights
through data preparation, cleaning, exploration, and visualization.
The analysis was completed using Python and R as part of a data analytics assignment.

---

## Project Structure

netflix_assignment/
│
├── netflix_data.csv                  - Original raw dataset
├── Netflix_shows_movies.csv          - Cleaned and renamed dataset
├── netflix_analysis.py               - Main Python script
├── netflix_analysis.R                - R visualization script
├── most_watched_genres.png           - Bar chart of top 15 genres
├── ratings_distribution.png         - Ratings distribution chart (Python)
├── ratings_distribution_R.png       - Ratings distribution chart (R)
├── content_type_pie.png              - Pie chart of Movies vs TV Shows
├── content_added_per_year.png        - Line chart of content added per year
└── README.md                         - Project instructions and documentation

---

## Dataset
- File: netflix_data.csv
- Source: Netflix Shows and Movies dataset
- Size: 6,234 rows and 12 columns
- Columns: show_id, type, title, director, cast, country, date_added,
           release_year, rating, duration, listed_in, description

---

## Requirements

### Python
Make sure you have Python installed on your computer.
Then install the required libraries by running this in your terminal:

    pip install pandas matplotlib seaborn

### R
Make sure you have R and RStudio installed on your computer.
Then install the required packages by running this in RStudio:

    install.packages("ggplot2")
    install.packages("dplyr")

---

## How to Run

### Step 1 - Open your terminal
Navigate to your project folder by typing:

    cd path/to/netflix_assignment

### Step 2 - Run the Python script
This will perform all data preparation, cleaning, exploration and create all charts:

    python netflix_analysis.py

You will see the following printed in the terminal when successful:

    Step 1 Done: File renamed to Netflix_shows_movies.csv
    Step 2 Done: Data cleaned and saved
    Step 3 Done: Data exploration complete
    Saved: most_watched_genres.png
    Saved: ratings_distribution.png
    Saved: content_type_pie.png
    Saved: content_added_per_year.png
    All steps complete. Check your folder for the chart images.

### Step 3 - Run the R script
Open RStudio and set your working directory to the project folder:

    setwd("path/to/netflix_assignment")

Then open netflix_analysis.R and press Ctrl + Shift + Enter to run it.

You will see this in the RStudio console when successful:

    Dataset loaded successfully
    Saved: ratings_distribution_R.png

---

## What Each Script Does

### netflix_analysis.py

Step 1 - Data Preparation:
    Copies and renames the original dataset to Netflix_shows_movies.csv

Step 2 - Data Cleaning:
    Fills missing values in the director, cast, country,
    date_added, rating and duration columns.
    Drops rows where genre or type is missing.

Step 3 - Data Exploration:
    Prints the shape and data types of the dataset.
    Prints a full statistical summary using describe().
    Shows the distribution of Movies vs TV Shows.
    Shows the top 10 countries producing Netflix content.
    Shows how many titles fall under each rating.
    Shows how many titles were added to Netflix each year.

Step 4 - Data Visualization:
    Creates a horizontal bar chart of the top 15 most watched genres.
    Creates a count plot showing the distribution of content ratings.
    Creates a pie chart showing the split between Movies and TV Shows.
    Creates a line chart showing how many titles were added per year.
    All charts are saved as PNG files in the project folder.

### netflix_analysis.R

    Loads the cleaned Netflix_shows_movies.csv dataset.
    Counts the number of titles per rating category.
    Creates a bar chart of the ratings distribution using ggplot2.
    Saves the chart as ratings_distribution_R.png.

---

## Key Findings

- The dataset contains 6,234 titles in total.
- 68.4% are Movies and 31.6% are TV Shows.
- The most common genre is International Movies.
- The most common rating is TV-MA with 2,027 titles.
- The United States produces the most Netflix content with 2,032 titles.
- Netflix added the most content in 2019 with 2,057 titles.

---

## Libraries Used

Python:
- pandas        - for loading, cleaning and exploring the dataset
- matplotlib    - for creating charts and saving them as PNG files
- seaborn       - for styled statistical visualizations
- collections   - for counting genre occurrences
- shutil        - for copying and renaming the dataset file

R:
- ggplot2       - for creating the ratings distribution bar chart
- dplyr         - for filtering and summarising the ratings data

---

## Author
Avoseh Elizabeth