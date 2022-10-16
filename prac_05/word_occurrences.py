"""
Word Occurrences
Estimate: 30mins
Actual: 24mins
"""
word_to_count = {}
text = input("Text: ")
words = text.split(" ")
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
    max_length = max(len(words) for word in list(word_to_count.keys()))
words = list(word_to_count.keys())
words.sort()
for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]} ")
