def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_amount = get_word_amount(text)
    letter_quantities = get_letter_amount(text)
    sorted_dict = sort_dict(letter_quantities)

    print(text)
    print(f"\n ^-----Report of {book_path}-----^")
    print(f"\n{word_amount} words were found in this book!\n")
    for letter, count in sorted_dict:
        print(f"The '{letter}' character was found {count} times")
    print("-------------End of report-------------")
    

def sort_dict(dict):
    return sorted(dict.items(), key=lambda item: item[1], reverse=True)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_amount(text):
    global lowered_text
    lowered_text = text.lower()
    words = lowered_text.split()
    return len(words)

def get_letter_amount(text):
    letter_quantities = {}
    for word in text.lower():
        for letter in word:
            if letter.isalpha():
                if letter not in letter_quantities:
                    letter_quantities[letter] = 1
                else:
                    letter_quantities[letter] += 1
    return letter_quantities

main()