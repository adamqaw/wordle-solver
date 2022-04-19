word = list('*O*ER')
letters = list('qeryuiopfhjkzxb'.upper())

with open('words.txt', mode='w') as data:
    for i in range(len(letters)):
        nw = word.copy()
        nw[0] = letters[i]
        data.write(f'{"".join(nw)}\n')

        for k in range(len(letters)):
            nw[2] = letters[k]
            data.write(f'{"".join(nw)}\n')
