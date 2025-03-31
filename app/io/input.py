#import pandas as pd
#due to a failure to load the pandas folder, all functions related to it are commented out

def input_text():
    """Prompts the user to input text from the console.

    Returns:
        str: The text entered by the user.

    """
    return input("Enter text: ")

def read_file_builtin(filename):
    """Reads text from a file using Python's built-in capabilities.

    Returns:
        str: The content read from the file.

    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

#def read_file_pandas(filename):
    """Reads text from a file using the pandas library.

    Returns:
        str: The content read from the file.

    """
    #df = pd.read_fwf(filename, header=None)
    #return df.to_string(index=False, header=False)