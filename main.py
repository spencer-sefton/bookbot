import sys
from stats import count_words, count_characters, sort_characters

def main():
    try:
        path = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(path)
    word_count = len(count_words(text))
    char_dict = count_characters(text)
    char_sorted = sort_characters(char_dict)
    print_results(path, word_count, char_sorted)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()    

def print_results(path, word_count, char_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()