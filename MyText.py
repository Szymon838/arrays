def count_words(text):
    words = text.split()
    return len(words)

def words_by_length(text):
    words = text.split()
    words.sort(key=len, reverse=True)
    return words

def words_alphabetically(text):
    words = text.split()
    words.sort()
    return words