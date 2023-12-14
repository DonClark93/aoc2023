text = open("doc.txt")

total = 0

for line in text:
    first_check = True
    first_num = ''
    second_num = ''
    for char in line:
        if char.isnumeric() and first_check:
            first_num = char
            second_num = char
            first_check = False
        elif char.isnumeric():
            second_num = char
        sub = first_num + second_num
    total = total + int(sub)

print(total)