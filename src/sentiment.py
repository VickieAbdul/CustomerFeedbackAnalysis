import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Add the SpacyTextBlob component (provides polarity scores)
nlp.add_pipe("spacytextblob")

# Function to analyze sentiment
def get_sentiment(text):
    doc = nlp(text)
    polarity = doc._.blob.polarity  # Sentiment score: -1 (negative) to +1 (positive)
    
    if polarity > 0.05:
        return "Positive"
    elif polarity < -0.05:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis to the cleaned feedback column
df['Sentiment'] = df['Cleaned_Feedback'].apply(get_sentiment)

# Display the first few rows
print(df[['Feedback', 'Cleaned_Feedback', 'Sentiment']].head())

# Save to CSV
df.to_csv('customer_feedback_with_sentiment.csv', index=False)
