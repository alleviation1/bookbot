def get_number_words(text):
    print(f"Found {len(text.split())} total words")

def get_number_characters(text):
    letter_count = {}

    for letter in text.lower():
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1

    return letter_count

def sort_letter_count(letter_dict):
    return dict(sorted(letter_dict.items(), key=lambda item: item[1], reverse=True))