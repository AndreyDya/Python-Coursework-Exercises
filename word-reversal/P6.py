# Andrey Dya
# Portfolio exercise 6
# Word Reversal
# A program that reverses the words in a sentence.

from P6_user_input import get_sentence
from P6_input_validation import validate_input
from P6_format_sentence import format_sentence


def main():
    while True:
        sentence = get_sentence()

        is_valid, error_message, cleaned_sentence = validate_input(sentence)

        if is_valid:
            print(f"{format_sentence(cleaned_sentence)}")
            break
        else:
            print(error_message)
            print()


if __name__ == "__main__":
    main()
