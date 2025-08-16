def count_words(text):
    return text.split()

def count_characters(text):
    char_counts = {}
    for char in text:
        letter = char.lower()
        if letter in char_counts:
            char_counts[letter] += 1
        else:
            char_counts[letter] = 1
    return char_counts

def sort_on(item):
    return item["num"]

def sort_characters(dict):
    sorted_characters = []
    for char in dict:
        sorted_characters.append({"char": char, "num": dict[char]})
    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters