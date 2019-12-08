with open('referat.txt', 'r', encoding='cp1251') as f:
    read_referat=f.read()
    print(len((read_referat)))

    words_referat=read_referat.split()
    print(len(words_referat))

    punctuation=read_referat.replace(".","!")

with open('referat2.txt', 'w', encoding='cp1251') as d:
    d.write(punctuation)