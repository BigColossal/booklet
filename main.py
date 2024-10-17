def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_amount = get_word_amount(text)
    letter_quantities = get_letter_amount()
    print(text)
    print(f"\n{word_amount} words were found in this book!")
    print(f"\n{letter_quantities}")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_amount(text):
    global lowered_text
    lowered_text = text.lower()
    words = lowered_text.split()
    return len(words)

def get_letter_amount():
    letter_quantities = {}
    word_list = transport_words_to_list()
    for word in word_list:
        for letter in word:
            if letter not in letter_quantities:
                letter_quantities[letter] = 1
            else:
                letter_quantities[letter] += 1
    return letter_quantities


def transport_words_to_list():
    word_list = []
    for word in lowered_text.split():
        word_list.append(word)
    return word_list

main()