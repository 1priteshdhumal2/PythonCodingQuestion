def count_vowels(string):
    vowels = 'aeiouAEIOU'
    cnt = 0

    for char in string:
        if char in vowels:
            cnt += 1

    return cnt

string = input("Enter a string: ")

print(count_vowels(string))