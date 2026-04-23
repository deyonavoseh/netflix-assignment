# Load the required libraries
library(ggplot2)
library(dplyr)

# Load the cleaned Netflix dataset
df <- read.csv("Netflix_shows_movies.csv", stringsAsFactors = FALSE)
print("Dataset loaded successfully")
print(dim(df))

# Count the number of titles per rating and sort from highest to lowest
rating_counts <- df %>%
  filter(!is.na(rating), rating != "") %>%
  group_by(rating) %>%
  summarise(Count = n(), .groups = "drop") %>%
  arrange(desc(Count))

print(rating_counts)

# Create a bar chart showing the ratings distribution
ggplot(rating_counts, aes(x = reorder(rating, -Count), y = Count, fill = rating)) +
  geom_bar(stat = "identity", show.legend = FALSE) +
  geom_text(aes(label = Count), vjust = -0.5, fontface = "bold", size = 3.5) +
  labs(
    title    = "Netflix Ratings Distribution",
    subtitle = "Number of titles per rating category",
    x        = "Rating",
    y        = "Count"
  ) +
  theme_minimal(base_size = 13) +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),
    plot.title  = element_text(face = "bold", size = 15)
  )

# Save the chart as a PNG file
ggsave("ratings_distribution_R.png", width = 10, height = 6)
print("Saved: ratings_distribution_R.png")