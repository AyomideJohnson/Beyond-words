from nltk.stem import SnowballStemmer
# import library for stemming from na
# ltk
from nltk.stem import WordNetLemmatizer
# import library for lemmatizing from nltk
from wordcloud import WordCloud
# import library for creating a word cloud
import matplotlib.pyplot as plt
# Importing for plotting in the word cloud
import nltk

# Importing the natural langauge toolkit

nltk.download('stopwords')
# Downloads stopwords from nltk
stopwords = nltk.corpus.stopwords.words("english")
# Creating a list of English stopwords
nltk.download('wordnet')
# use for the lematizer and stemming

symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~,\'"


# symbols equals everything as a string


def remove_symbols(text):
    for symbol in symbols:
        text = text.replace(symbol, '')
    return text


# removes symbols from text and returns it


def word_counter(filename):
    # The function wordCounter takes a file as a parameter
    word_count = {}
    # Initializes an empty dictionary which is used to store word occurrences
    with open(filename, 'r', errors='ignore') as file:
        # this opens the file specified by the user and is in (reader mode 'r')
        contents = file.read()
        # the contents of the text is being read and stored in the variable contents
        contents = remove_symbols(contents)
        # contents goes through another method called remove_symbols
        words = contents.split()
        # Here we are using the split() method to split the contents into individual words

        # Lowercase conversion
        words = [word.lower() for word in words]

        # Remove single-character words
        words = [word for word in words if len(word) > 1]

        # Lemmatization
        lemmatizer = WordNetLemmatizer()
        # create a wordnetlemmatizer object
        words = [lemmatizer.lemmatize(word) for word in words]
        # Goes through all the words in the loop and performs lemmatization

        # Stemming
       # stemmer = SnowballStemmer('english')
        # create a snowballstemmer object for english
       # words = [stemmer.stem(word) for word in words]
        # stemming words

        for word in words:
            # Word becomes the first word in words and then the second and so as it iterates over till the end
            if word not in stopwords:
                # checking if the word is not a stopword
                if word in word_count:
                    # check if the word has occurred previously
                    word_count[word] += 1
                    # if the word has occurred it add 1 to the amount of time its occurred previously in the dictionary
                else:
                    word_count[word] = 1
                    # if the word has not occurred it add it to the dictionary

    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    # creates a new variable that has all the keys from the dictionary word_count but sorted using the sorted
    # function. The key=lambda x: x[1] argument specifies that the sorting should be based on the second element (the
    # count) of each tuple in the list lastly we reverse it, so we can print it in descending order instead of
    # ascending order

    # Create word cloud dictionary
    word_cloud_dict = {}
    for word, count in sorted_word_count:
        word_cloud_dict[word] = count

    # Generate and display word cloud
    wordcloud = WordCloud().generate_from_frequencies(word_cloud_dict)

    plt.imshow(wordcloud, interpolation='bilinear')
    # Displaying the word cloud image
    plt.axis("off")
    # Turning the axis labels off

    plt.show()
    # Showing the plot
    a = 0
    for word, count in sorted_word_count:
        a = a + 1
        # Now we are going into the variable to see the word and how many times it has been counted
        print(f"{word}: {count}")
        # this prints it in the format of the word then the number of times it was counted

    print(a)
word_counter(input("Enter your file name: "))

# This is where the user can input the file of their choosing
