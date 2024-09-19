string = "The shining, and the sun is bright. The sun is powerful."

string = ''.join(item for item in string if item not in [",", "."])

words = string.split()

print(words)

count_word = {}

for word in words:
    word = word.lower()
    if word in count_word:
        count_word[word] += 1
    else:
        count_word[word] = 1

print(count_word)

largest = 0
for i, j in count_word.items():
    if largest < j:
        largest = j
        frequent = i
        
print(largest, frequent)


