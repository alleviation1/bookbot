import sys
from stats import get_number_words, get_number_characters, sort_letter_count

def get_book_text(file):
    with open(file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    words = get_book_text(sys.argv[1])
    get_number_words(words)

    print("--------- Character Count -------")
    letter_count = get_number_characters(words)
    letter_count = sort_letter_count(letter_count)

    for letter, count in letter_count.items():
        print(f"{letter}: {count}")

    print("============= END ===============")

main()