num_list = {"one":"o1e",
            "two":"t2o",
            "three":"3", 
            "four":"4", 
            "five":"5", 
            "six":"6", 
            "seven":"7", 
            "eight":"8", 
            "nine":"9"}





with open("doc.txt") as text:
    lines = text.readlines()
    total = 0
    
    for line in lines:

        print(line)
        first_num=''
        second_num=''
        first_check = True
        sub = ""
        
        for k,v in num_list.items():
            line = line.replace(k, str(v))

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
