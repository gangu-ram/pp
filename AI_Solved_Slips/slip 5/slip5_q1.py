import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download the WordNet resource if not already downloaded
nltk.download('punkt')
nltk.download('wordnet')

def lemmatize_text(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Initialize the WordNet lemmatizer
    lemmatizer = WordNetLemmatizer()
    
    # Lemmatize each word in the list
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    
    # Join the lemmatized words to form the lemmatized text
    lemmatized_text = ' '.join(lemmatized_words)
    
    return lemmatized_text

# Example usage
input_text = "The dogs are barking loudly outside."
output_text = lemmatize_text(input_text)

print("Original Text:", input_text)
print("Lemmatized Text:", output_text)
