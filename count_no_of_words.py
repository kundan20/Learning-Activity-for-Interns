fname = "Test_TextFile.txt"
count = 0
with open(fname, 'r') as file:
    for lines in file:
        words = lines.split()
        count += len(words)

print(count)
