def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    path = "./books/frankenstein.txt"
    print(get_book_text(path))

main()

