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

def character_count():
    text = main().lower()
    character_dict = {}
    for i in text:
        if i in character_dict:
            character_dict[i] +=1
        else:
            character_dict[i] = 1
    return character_dict

