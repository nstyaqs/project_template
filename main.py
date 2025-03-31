from app.io.input import input_text, read_file_builtin #, read_file_pandas
from app.io.output import output_text, write_file_builtin #, write_file_pandas
#due to a failure to load the pandas folder, all functions related to it are commented out

def main():
    text_from_console = input_text()

    text_from_file_builtin = read_file_builtin("data/input_builtin.txt")
    #text_from_file_pandas = read_file_pandas("data/input_pandas.txt")

    output_text(text_from_console)
    output_text(text_from_file_builtin)
    #output_text(text_from_file_pandas)

    write_file_builtin(text_from_console, "data/output_builtin.txt")
    write_file_builtin(text_from_file_builtin, "data/output_builtin.txt")
    #write_file_builtin(text_from_file_pandas, "data/output_builtin.txt")

    #write_file_pandas(text_from_console, "data/output_pandas.txt")
    #write_file_pandas(text_from_file_builtin, "data/output_pandas.txt")
    #write_file_pandas(text_from_file_pandas, "data/output_pandas.txt")


if __name__ == "__main__":
    main()

