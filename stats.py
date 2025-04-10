def get_num_words(text):
    words = text.split()
    return len(words)
def get_char_count(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1

        else:
            char_counts[char] = 1

    return char_counts
def sort_characters(char_counts):
    # Build a list of dictionaries for alphabetic characters only
    sorted_list = []

    for char, count in char_counts.items():
        if char.isalpha():  # skip spaces, punctuation, numbers, etc.
            sorted_list.append({'char': char, 'count': count})

    # Sort the list descending by count
    sorted_list.sort(key=lambda item: item['count'], reverse=True)

    return sorted_list
