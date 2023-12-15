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
    len_of_schem = len(engine)
    ast_locations = []# list of (x,y) coords

    while row < len_of_schem:
        
        for col,char in enumerate(engine[row]):
            if char == '*':
                ast_locations.append((col,row))
        row += 1

    for coords in ast_locations:
        x,y = coords
        pass
        
    print("total: " + str(ast_locations))

doc.closed
                                  
"""
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
              """
