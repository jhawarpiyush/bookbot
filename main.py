def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        book_report(book_name=book_path, book_wordcount=book_word_counter(
            file_contents), book_charactercount=book_character_counter(file_contents))


def book_word_counter(booktext: str):
    words = booktext.split()
    return len(words)


def book_character_counter(booktext: str):
    charactercount = {}

    booktext_lowered = booktext.lower()
    for character in booktext_lowered:
        if character.isalpha():
            if character in charactercount:
                charactercount[character] = charactercount[character] + 1
            else:
                charactercount[character] = 1
    return charactercount


def book_report(book_name: str, book_wordcount: int, book_charactercount: dict[str, int]):
    print(f"--- Begin report of {book_name} ---")
    print(f"{book_wordcount} words found in the document\n\n")
    book_charactercount = sorted(
        book_charactercount.items(), key=lambda item: item[1], reverse=True)
    for item in book_charactercount:
        print(f"The '{item[0]}' character was found {item[1]} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
