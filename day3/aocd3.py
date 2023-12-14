with open("doc.txt", encoding='utf-8') as doc:

    
    schematic = doc.readlines()

    engine = [x.strip() for x in schematic]

    print(engine)
    print(engine[0][2])



doc.closed