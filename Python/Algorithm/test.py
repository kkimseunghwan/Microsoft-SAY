text = "shimpanzinni\nbana\nnini\n"


lines = text.splitlines()
print(lines)
# >> ['shimpanzinni', 'bana', 'nini']

lines = text.splitlines(keepends=True)
print(lines)
# >> ['shimpanzinni\n', 'bana\n', 'nini\n']

lines = text.split('\n')
print(lines)
# >> ['shimpanzinni', 'bana', 'nini', '']

print(text.replace('\n', ''))