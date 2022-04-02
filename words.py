# def print_upper_words(words):
#     """Given a list of words, print each word in uppercase"""
    
#     for word in words:
#         if word.startswith('e') or word.startswith('E'):
#             print(word.upper())

def print_upper_words(words, must_start_with):
    """Print uppercased word on sep line, if starts with one of given letters"""
    
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break