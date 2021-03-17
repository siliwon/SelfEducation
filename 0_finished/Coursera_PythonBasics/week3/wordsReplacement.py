string = input()
first_substring = string[:string.find(' ')]
second_substring = string[string.find(' ') + 1:]
print(second_substring, first_substring, sep=' ')
