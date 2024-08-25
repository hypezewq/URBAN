def custom_write(file_name, string):
    string_positions = {}
    with open(file_name, 'w', encoding="utf-8") as f:
        for num, line in enumerate(string):
            string_positions[(num + 1, f.tell())] = line
            f.write(f"{line}\n")
    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)