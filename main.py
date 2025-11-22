import sys

from stats import get_char_stat, get_num_words, sort_dict


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

        file_contents = f.read()
        return file_contents

        return file_contents

def get_book_path_or_quit():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return sys.argv[1]


def main():
    book_path = get_book_path_or_quit()

    print("============ BOOKBOT ============")
    print("Analyzing book found at", book_path)
    text = get_book_text(book_path)

    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_dict = get_char_stat(text)
    sorted = sort_dict(char_dict)
    for i in sorted:
        print(i["name"] + ": " + str(i["num"]))

    print("============= END ===============")


main()
