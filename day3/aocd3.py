with open("doc.txt", encoding='utf-8') as doc:

    
    schematic = doc.readlines()
    engine = [x.strip() for x in schematic]
    print(engine)

    row = 0
    len_of_schem = len(engine)

    while row < len_of_schem:
        row_numbers = []
        numbers = ''
        start = 0
        end = 0
    
        for col,char in enumerate(engine[row]):
            print(bool(engine[row][col].isnumeric()))
            print(f"row{row}col{col}")
            if engine[row][col].isnumeric():
                if numbers == '':
                    start = col
                numbers += char
                                
            elif not(bool(engine[row][col].isnumeric())) and numbers != '' :
                end = col
                row_numbers.append((numbers,start,end))
                numbers = ''
                
                


        
        print(row_numbers)
        row += 1
    
    pass



doc.closed