import spacy
import pandas as pd

# Load the CSV file
df = pd.read_csv('customer_feedback.csv')

# Check the first few rows of the data
print("First few rows of the data:\n")
print(df.head())

# Check for missing values
print("\nChecking for missing values:\n")
print(df.isnull().sum())

# Get a summary of the data
print("\nSummary of the data:\n")
print(df.info())

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to preprocess text
def preprocess_text(text):
    doc = nlp(text)
    
    # Remove stopwords and punctuation, and lemmatize the tokens
    clean_tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    
    # Join the tokens back into a clean string
    cleaned_text = " ".join(clean_tokens)
    
    return cleaned_text

# Apply the preprocessing function to the feedback column
df['Cleaned_Feedback'] = df['Feedback'].apply(preprocess_text)

# Display the cleaned data
print("Cleaned data:\n")
print(df[['Feedback', 'Cleaned_Feedback']].head())

# Save cleaned data
df.to_csv('cleaned_feedback.csv', index = False)
