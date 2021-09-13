with open('trump.txt', 'r') as ff:
    with open('donald.txt','w') as fd:
        for line in ff:
            if not line.isspace():
                fd.write(line)
