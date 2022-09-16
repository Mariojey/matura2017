file = open("przyklad.txt", "r").read().split('\n')
min_light = 255
max_light = 0

for lines in file:
    if len(lines.split(" ")) < 2 or len(lines.split(" ")[1]) < 1:
        continue
    line = lines.split(" ")
    for item in line:
         if int(item) > max_light:
             max_light = int(item)
         else: 
            if int(item) < min_light:
                min_light = int(item)
print(str(min_light), str(max_light))
