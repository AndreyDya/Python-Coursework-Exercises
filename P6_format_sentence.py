def format_sentence(cleaned_sentence):
    """
    Reverses words while preserving capitalization, except:
    1. First word of original sentence is lowercased (unless it's an acronym/proper noun)
    2. First word of reversed sentence is capitalized
    """
    words = cleaned_sentence.split()

    # Lowercase the first word unless it's all caps (acronym) or has mixed case (proper noun like iPad)
    if words:
        first_word = words[0]
        # Only lowercase if it's standard sentence case (first letter capital, rest lowercase)
        if first_word[0].isupper() and (
            len(first_word) == 1 or first_word[1:].islower()
        ):
            words[0] = first_word.lower()

    # Reverse the words
    reversed_words = words[::-1]

    # Capitalize the first letter of the first word after reversal
    if reversed_words:
        reversed_words[0] = (
            reversed_words[0][0].upper() + reversed_words[0][1:]
            if len(reversed_words[0]) > 1
            else reversed_words[0].upper()
        )

    reversed_sentence = " ".join(reversed_words)

    return reversed_sentence