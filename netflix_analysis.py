import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import shutil

# Copy and rename the dataset to Netflix_shows_movies
shutil.copy("netflix_data.csv", "Netflix_shows_movies.csv")
print("Step 1 Done: File renamed to Netflix_shows_movies.csv")

# Load the dataset into a dataframe
df = pd.read_csv("Netflix_shows_movies.csv")
print(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns")

# Check for missing values before cleaning
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill missing values with appropriate replacements
df["director"].fillna("Unknown", inplace=True)
df["cast"].fillna("Unknown", inplace=True)
df["country"].fillna(df["country"].mode()[0], inplace=True)
df["date_added"].fillna("Unknown", inplace=True)
df["rating"].fillna(df["rating"].mode()[0], inplace=True)
df["duration"].fillna("Unknown", inplace=True)

# Drop rows where genre or type is missing since they are essential
df.dropna(subset=["listed_in", "type"], inplace=True)

# Confirm missing values have been handled
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Save the cleaned dataset
df.to_csv("Netflix_shows_movies.csv", index=False)
print("Step 2 Done: Data cleaned and saved")

# Display the shape and data types of the dataset
print("\nDataset Shape:", df.shape)
print("\nData Types:")
print(df.dtypes)

# Show statistical summary of the dataset
print("\nStatistical Summary:")
print(df.describe(include="all"))

# Count how many Movies vs TV Shows are in the dataset
print("\nContent Type Distribution:")
print(df["type"].value_counts())

# Show the top 10 countries producing Netflix content
print("\nTop 10 Countries:")
print(df["country"].value_counts().head(10))

# Show how many titles fall under each rating
print("\nRatings Count:")
print(df["rating"].value_counts())

# Extract the year from date_added and count titles added per year
df["year_added"] = pd.to_datetime(df["date_added"], errors="coerce").dt.year
print("\nContent Added Per Year:")
print(df["year_added"].value_counts().sort_index())
print("Step 3 Done: Data exploration complete")

# Split genres since each title can have multiple genres separated by commas
all_genres = []
for entry in df["listed_in"].dropna():
    all_genres.extend([g.strip() for g in entry.split(",")])

# Count each genre and keep the top 15
genre_df = pd.DataFrame(Counter(all_genres).items(), columns=["Genre", "Count"])
genre_df = genre_df.sort_values("Count", ascending=False).head(15)

# Plot a horizontal bar chart of the top 15 genres
plt.figure(figsize=(12, 6))
sns.barplot(data=genre_df, x="Count", y="Genre", hue="Genre", palette="Reds_r", legend=False)
plt.title("Top 15 Most Watched Genres on Netflix", fontsize=16)
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig("most_watched_genres.png")
print("Saved: most_watched_genres.png")

# Plot the distribution of content ratings using a count plot
plt.figure(figsize=(10, 5))
sns.countplot(
    data=df,
    x="rating",
    order=df["rating"].value_counts().index,
    hue="rating",
    palette="coolwarm",
    legend=False
)
plt.title("Netflix Ratings Distribution", fontsize=16)
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("ratings_distribution.png")
print("Saved: ratings_distribution.png")

# Plot a pie chart showing the split between Movies and TV Shows
type_counts = df["type"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(
    type_counts,
    labels=type_counts.index,
    autopct="%1.1f%%",
    colors=["#E50914", "#221F1F"],
    startangle=140
)
plt.title("Movies vs TV Shows on Netflix", fontsize=16)
plt.tight_layout()
plt.savefig("content_type_pie.png")
print("Saved: content_type_pie.png")

# Plot the number of titles added to Netflix each year
year_counts = df["year_added"].value_counts().sort_index().dropna()
plt.figure(figsize=(12, 5))
plt.fill_between(year_counts.index, year_counts.values, color="#E50914", alpha=0.4)
plt.plot(year_counts.index, year_counts.values, color="#E50914", linewidth=2.5, marker="o")
plt.title("Netflix Content Added Per Year", fontsize=16)
plt.xlabel("Year")
plt.ylabel("Number of Titles Added")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("content_added_per_year.png")
print("Saved: content_added_per_year.png")

print("All steps complete. Check your folder for the chart images.")