string = input()
d = len(string) // 2
print(string[:d] == string[:len(string) - d - 1 :-1])
