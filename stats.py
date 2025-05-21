def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    path = "./books/frankenstein.txt"
    return(get_book_text(path))

def wordcount():
    text = main()
    words = text.split()
    count = len(words)
    return count