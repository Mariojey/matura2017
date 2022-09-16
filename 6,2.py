file = open("przyklad.txt", "r").read().split('\n')
min_letters = 0
for lines in file:
    if len(lines.split(" ")) < 2 or len(lines.split(" ")[1]) < 1:
        continue
    line = lines.split(" ")
    for i in range(320):
        if line[i] != line[319-i]:
            min_letters += 1
            break
print(str(min_letters))