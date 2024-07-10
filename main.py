def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(text, book_path)
    

def get_value(d):
    return list(d.values())[0]

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    characters = text.lower()
    character_count = {}
    for c in characters:
        if c in character_count:
            if  c.isalpha():
                character_count[c] += 1
        else:
            if  c.isalpha():
                character_count[c] = 1
    return character_count

def print_report(text, book_path):  
    num_words = get_num_words(text)
    character_count = get_num_char(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    list_of_characters = [{key: value} for key, value in character_count.items()]
    list_of_characters.sort(key=get_value, reverse=True)
    for d in list_of_characters:
        for key, value in d.items():    
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()