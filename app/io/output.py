#import pandas as pd
#due to a failure to load the pandas folder, all functions related to it are commented out

def output_text(text):
    """Prints text to the console.

    Args:
        text (str): The text to be printed to the console.

    """
    print(text)

def write_file_builtin(text, filename):
    """Writes text to a file using Python's built-in capabilities.

    Args:
        text (str): The text to be written to the file.
        filename (str): The name of the file where the text will be written.

    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

#def write_file_pandas(text, filename):
    """"Writes text to a file using the pandas library.

    Args:
        text (str): The text to be written to the file.
        filename (str): The name of the file where the text will be written.

    """

    #df = pd.DataFrame([[text]])
    #df.to_csv(filename, index=False, header=False, encoding='utf-8')
