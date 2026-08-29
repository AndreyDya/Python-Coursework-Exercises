from P6_config import MAXIMUM_INPUT_LENGTH
from P6_config import MAXIMUM_WORD_LENGTH


def validate_input(sentence):
    """
    Validates input and returns (is_valid, error_message, cleaned_sentence)
    """
    # Check for empty input
    if not sentence or sentence.strip() == "":
        return False, "Error - Input cannot be empty", None

    # Trim and reduce multiple spaces, and remove standalone hyphens/dashes
    words_temp = sentence.split()
    words_temp = [word for word in words_temp if word not in ["-"]]
    sentence = " ".join(words_temp)

    # Check maximum input length
    if len(sentence) > MAXIMUM_INPUT_LENGTH:
        return (
            False,
            f"Error - Input too long (maximum {MAXIMUM_INPUT_LENGTH} characters)",
            None,
        )

    # Remove allowed punctuation (not including hyphens within words)
    punctuation = ".,!?;:–—"
    cleaned = ""
    for char in sentence:
        if char not in punctuation:
            cleaned += char

    # Remove asterisks from words
    words = cleaned.split()
    words = [word.rstrip("*") for word in words]

    # Filter out empty strings after cleaning
    words = [word for word in words if word]

    # Check if input becomes empty after cleaning
    if not words:
        return False, "Error - No valid words found after removing punctuation", None

    # Check for minimum 3 words
    if len(words) < 3:
        return False, "Error – please enter a full sentence", None

    for word in words:
        # Check for excessively long words
        if len(word) > MAXIMUM_WORD_LENGTH:
            return (
                False,
                f"Error - Word too long: '{word[:15]}...' (maximum {MAXIMUM_WORD_LENGTH} characters per word)",
                None,
            )

        # Check for mixed words (letters + numbers)
        if any(c.isalpha() for c in word) and any(c.isdigit() for c in word):
            return False, "Error – Enter valid words", None

        # Check for invalid characters (anything that's not letter, digit, apostrophe, asterisk, or hyphen)
        # Allow apostrophes for contractions, hyphens for compound words, and Unicode letters
        if not all(
            c.isalpha() or c.isdigit() or c == "'" or c == "’" or c == "*" or c == "-"
            for c in word
        ):
            return False, "Error – Enter valid words", None

    # Check if all words are only numbers
    if all(word.isdigit() for word in words):
        return False, "Error – numbers do not constitute a sentence", None

    # Check if sentence contains at least one valid word
    if not any(any(c.isalpha() for c in word) for word in words):
        return False, "Error – numbers do not constitute a sentence", None

    return True, None, " ".join(words)
