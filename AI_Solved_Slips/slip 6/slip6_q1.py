import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK stop words
nltk.download('stopwords')

def remove_stopwords(input_text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(input_text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

def main():
    # Read the passage from a text file
    with open('your_text_file.txt', 'r') as file:
        passage = file.read()

    # Remove stop words
    result = remove_stopwords(passage)

    # Display the result
    print("Original Passage:")
    print(passage)
    print("\nPassage after removing stop words:")
    print(result)

# Call the main function directly
main()
