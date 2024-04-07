import re


def main() -> None:
    book_file_path = "books/frankenstein.txt"
    print_report(book_file_path)


def print_report(book_file_path) -> None:
    # Read book contents
    book_contents = get_book_contents(book_file_path)

    print(f"--- Begin report of {book_file_path} ---")

    # Get and display word count
    book_word_count = get_word_count(book_contents)
    print(f"Word count: {book_word_count}\n")

    # Get letter counts and print them
    letter_counts = get_letter_count(book_contents)
    for letter in letter_counts:
        print(f"The '{letter.get('letter')}' character was found {letter.get('count')} times.")

    print("\n--- End report ---")


def get_book_contents(file_path) -> str:
    with open(file_path, "r") as book:
        book_contents = book.read()
        return book_contents


def get_word_count(book_contents) -> int:
    words = book_contents.split()
    return len(words)


def get_letter_count(book_contents) -> dict:
    book_lower_letters_only = re.sub(r"[^a-z]+", "", book_contents.lower())

    letter_count_dict = dict()
    for letter in book_lower_letters_only:
        letter_count_dict.update(
            {letter.upper(): letter_count_dict.get(letter.upper(), 0) + 1}
        )

    return sort_letter_count(letter_count_dict)


def sort_letter_count(letter_count_dict) -> list:
    def sort_on(dict):
        return dict["count"]

    letter_counts = [
        {"letter": letter, "count": count}
        for letter, count in letter_count_dict.items()
    ]
    letter_counts.sort(reverse=True, key=sort_on)
    return letter_counts


main()
