SCHEM_CHARS= ['@','#','$','%','&','*','-','=','+','/']
sec_tot = 0
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
    len_of_schem = len(engine)

    while row < len_of_schem:
        row_numbers = []
        numbers = ''
        start = 0
        end = 0
        for col,char in enumerate(engine[row]):
            if engine[row][col].isnumeric():
                if numbers == '':
                    start = col
                numbers += char                   
            elif not(bool(engine[row][col].isnumeric())) and numbers != '' :
                end = col - 1
                #print((numbers,start,end))
                row_numbers.append((numbers,start,end))
                numbers = ''
            if numbers != '' and col == len(engine[row])-1:
                end = col
                
                row_numbers.append((numbers,start,end))
                numbers = ''

        for number in row_numbers:
            test_num, start, end = number
            space_around_num = []
            engine_part = False
            if start == 0:
                start = 1
            if end == len(engine[row]):
                end = len(engine[row])-1
            if row == 0:
                space_around_num.append(engine[row][start-1:end+2])
                space_around_num.append(engine[row+1][start-1:end+2])   
            elif row == (len_of_schem-1):
                space_around_num.append(engine[row-1][start-1:end+2])
                space_around_num.append(engine[row][start-1:end+2])   
            else:
                space_around_num.append(engine[row-1][start-1:end+2])
                space_around_num.append(engine[row][start-1:end+2])
                space_around_num.append(engine[row+1][start-1:end+2])
                
            if confirm_part(space_around_num):
                #print(test_num)
                total = total + int(test_num)

        row += 1
    print("total: " + str(total))
    pass

doc.closed