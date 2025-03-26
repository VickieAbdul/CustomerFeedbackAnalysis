import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import wordcloud
from wordcloud import WordCloud

# Load data
df = pd.read_csv('customer_feedback_with_sentiment.csv')

# Set the style for the plot
sns.set_style("whitegrid")

# Count the occurrences of each sentiment
sentiment_counts = df['Sentiment'].value_counts()

# Create a bar plot
plt.figure(figsize=(6, 4))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette=['red', 'blue', 'green'])

# Add labels and title
plt.xlabel("Sentiment")
plt.ylabel("Number of Feedbacks")
plt.title("Customer Feedback Sentiment Distribution");

# Generate word cloud
# Define a function to generate word cloud
def generate_wordcloud(text, title, color):
    wordcloud = WordCloud(width=500, height=300, background_color="white", colormap=color).generate(text)

    # Display the word cloud
    plt.figure(figsize=(6, 4))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(title, fontsize=14);

# Separate positive and negative feedback
positive_text = " ".join(df[df["Sentiment"] == "Positive"]["Cleaned_Feedback"])
negative_text = " ".join(df[df["Sentiment"] == "Negative"]["Cleaned_Feedback"])

# Generate positive word clouds
generate_wordcloud(positive_text, "Most Common Words in Positive Feedback", "Greens")

# Generate negative word cloud
generate_wordcloud(negative_text, "Most Common Words in Negative Feedback", "Reds")
