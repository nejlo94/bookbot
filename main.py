import sys
from stats import get_num_words, get_char_count, sort_characters

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def main():
    # Check if book path is passed as a CLI argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with error code 1

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

    char_counts = get_char_count(book_text)
    sorted_chars = sort_characters(char_counts)

    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")

if __name__ == "__main__":
    main()

