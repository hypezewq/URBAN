first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = [len(words[0]) - len(words[1]) for words in zip(first, second) if len(words[0]) != len(words[1])]
second_result = [len(word) == len(second[ind]) for ind, word in enumerate(first)]
print(first_result)
print(second_result)
