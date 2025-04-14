import ast  # Importing the ast module to safely evaluate strings containing Python literals
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt_tab')  # it is not downloaded by default .


def convert(obj):
    """
    Convert a string representation of a list of dictionaries into a list of names.

    Parameters:
    obj (str): A string containing a list of dictionaries, where each dictionary 
                has a 'name' key.

    Returns:
    list: A list of names extracted from the dictionaries.
    """
    
    # Initialize an empty list to store the names
    obj_list = []
    
    # Safely evaluate the string to convert it into a Python list of dictionaries
    # ast.literal_eval is used here to safely parse the string. Unlike eval(), 
    # literal_eval only allows certain Python literals (strings, numbers, tuples, 
    # lists, dicts, booleans, and None) to be evaluated. This prevents the 
    # execution of arbitrary code, making it a safer alternative for parsing 
    # untrusted input.
    for item in ast.literal_eval(obj):
        # Append the 'name' value from each dictionary to the obj_list
        obj_list.append(item['name'])
    
    # Return the final list of names
    return obj_list


def convert_cast(obj):
    """
    Convert a string representation of a list of dictionaries into a list of names.

    Parameters:
    obj (str): A string containing a list of dictionaries, where each dictionary 
                has a 'name' key.

    Returns:
    list: A list of names extracted from the dictionaries.
    """
    
    # Initialize an empty list to store the names
    obj_list = []
    
    # Safely evaluate the string to convert it into a Python list of dictionaries
    # ast.literal_eval is used here to safely parse the string. Unlike eval(), 
    # literal_eval only allows certain Python literals (strings, numbers, tuples, 
    # lists, dicts, booleans, and None) to be evaluated. This prevents the 
    # execution of arbitrary code, making it a safer alternative for parsing 
    # untrusted input.
    for item in ast.literal_eval(obj):
        # Append the 'name' value from each dictionary to the obj_list
        obj_list.append(item['name'])
        if len(obj_list) == 3:
            break
    
    # Return the final list of names
    return obj_list


def fetch_director(obj):
    """
    Convert a string representation of a list of dictionaries into a list of names.

    Parameters:
    obj (str): A string containing a list of dictionaries, where each dictionary 
                has a 'name' key.

    Returns:
    list: A list of names extracted from the dictionaries.
    """
    
    # Initialize an empty list to store the names
    director_list = []
    
    # Safely evaluate the string to convert it into a Python list of dictionaries
    # ast.literal_eval is used here to safely parse the string. Unlike eval(), 
    # literal_eval only allows certain Python literals (strings, numbers, tuples, 
    # lists, dicts, booleans, and None) to be evaluated. This prevents the 
    # execution of arbitrary code, making it a safer alternative for parsing 
    # untrusted input.
    for item in ast.literal_eval(obj):
        # Append the 'name' value from each dictionary to the obj_list
        if item['job'].lower() == 'director':
            # Append the 'name' value from each dictionary to the obj_list
            director_list.append(item['name'])
            break
    
    # Return the final list of names
    return director_list


def stem_text(text):
    """Stem the input text using the Porter Stemmer.
    word_tokenize: This is a specific function from the tokenize module. 
    It takes a string of text as input and splits it into individual words (tokens). 
    For example, the sentence "Hello, world!" would be tokenized into the tokens ["Hello", ",", "world", "!"]. 
    This function handles punctuation and whitespace, making it useful for preparing text for further analysis
    """

    stemmer = PorterStemmer()
    tokens = word_tokenize(text)  # Tokenize the text by splitting on whitespace
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    stemmed_text = ' '.join(stemmed_tokens)  # Join the stemmed tokens back into a single string
    return stemmed_text


