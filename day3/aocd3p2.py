SCHEM_CHARS= ['@','#','$','%','&','*','-','=','+','/']

def confirm_part(space_around_num):
    test_string = ''
    for row in space_around_num:
        test_string = test_string + row
    #print(test_string)
    if any(char in SCHEM_CHARS for char in test_string):
        #print(test_string)
        return True
    else:
        return False


with open("doc.txt", encoding='utf-8') as doc:
    schematic = doc.readlines()
    engine = [x.strip() for x in schematic]
    total = 0
    row = 0
    gear_ratio_total = 0
    len_of_schem = len(engine)
    ast_locations = []# list of (x,y) coords
    gear_groups = []


    def check_top(x,y):
        tot_num = []
        if engine[y-1][x-1].isnumeric() and engine[y-1][x].isnumeric() and engine[y-1][x+1].isnumeric():
            tot_num.append(engine[y-1][x-1:x+2])
        if engine[y-1][x-1].isnumeric() and engine[y-1][x].isnumeric() and not engine[y-1][x+1].isnumeric():
            tot_num.append(engine[y-1][x-2:x+1].replace('.',''))
        if engine[y-1][x-1].isnumeric() and not engine[y-1][x].isnumeric() and not engine[y-1][x+1].isnumeric():
            tot_num.append(engine[y-1][x-3:x].replace('.',''))
        if  not engine[y-1][x-1].isnumeric() and engine[y-1][x].isnumeric() and engine[y-1][x+1].isnumeric():
            tot_num.append(engine[y-1][x:x+3].replace('.',''))
        if  not engine[y-1][x-1].isnumeric() and not engine[y-1][x].isnumeric() and engine[y-1][x+1].isnumeric():
            tot_num.append(engine[y-1][x+1:x+4].replace('.',''))
        if  not engine[y-1][x-1].isnumeric() and engine[y-1][x].isnumeric() and not engine[y-1][x+1].isnumeric():
            tot_num.append(engine[y-1][x].replace('.',''))
        if  engine[y-1][x-1].isnumeric() and not engine[y-1][x].isnumeric() and engine[y-1][x+1].isnumeric():
            tot_num.append(engine[y-1][x+1:x+4].replace('.',''))
            tot_num.append(engine[y-1][x-3:x].replace('.',''))
        return tot_num

    def check_mid(x,y):
        tot_num = []
        if engine[y][x-1].isnumeric():
            tot_num.append(engine[y][x-3:x].replace('.',''))
        if engine[y][x+1].isnumeric():
            tot_num.append(engine[y][x+1:x+4].replace('.',''))
        print(tot_num)
        return tot_num

    def check_bot(x,y):
        tot_num = []
        if engine[y+1][x-1].isnumeric() and engine[y+1][x].isnumeric() and engine[y+1][x+1].isnumeric():
            tot_num.append(engine[y+1][x-1:x+2])
        if engine[y+1][x-1].isnumeric() and engine[y+1][x].isnumeric() and not engine[y+1][x+1].isnumeric():
            tot_num.append(engine[y+1][x-2:x+1].replace('.',''))
        if engine[y+1][x-1].isnumeric() and not engine[y+1][x].isnumeric() and not engine[y+1][x+1].isnumeric():
            tot_num.append(engine[y+1][x-3:x].replace('.',''))
        if  not engine[y+1][x-1].isnumeric() and engine[y+1][x].isnumeric() and engine[y+1][x+1].isnumeric():
            tot_num.append(engine[y+1][x:x+3].replace('.',''))
        if  not engine[y+1][x-1].isnumeric() and not engine[y+1][x].isnumeric() and engine[y+1][x+1].isnumeric():
            tot_num.append(engine[y+1][x+1:x+4].replace('.',''))
        if  not engine[y+1][x-1].isnumeric() and engine[y+1][x].isnumeric() and not engine[y+1][x+1].isnumeric():
            tot_num.append(engine[y+1][x].replace('.',''))
        if  engine[y+1][x-1].isnumeric() and not engine[y+1][x].isnumeric() and engine[y+1][x+1].isnumeric():
            tot_num.append(engine[y+1][x+1:x+4].replace('.',''))
            tot_num.append(engine[y+1][x-3:x].replace('.',''))
        return tot_num

    def check_gear(x,y):
        gears =[]
        gears += check_top(x,y)
        gears += check_mid(x,y)
        gears += check_bot(x,y)
        print(gears)
        return gears

    while row < len_of_schem:
        for col,char in enumerate(engine[row]):
            if char == '*':
                ast_locations.append((col,row))
        row += 1

    for coords in ast_locations:
        x,y= coords
        gear_groups.append(check_gear(x,y))

    

    for gears in gear_groups:
        temp_tot = 0
        if len(gears) == 1:
            print(gears)
        if len(gears) != 1:
            temp_tot = int(gears[0]) * int(gears[1])
        gear_ratio_total = gear_ratio_total + temp_tot

    print(len(gear_groups))
    print(gear_ratio_total)
    #print("total: " + str(ast_locations))


doc.closed