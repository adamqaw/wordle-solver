# QUICK SOLVER FOR TESTING
# In this example, word[0] and word[2] are uncertain, word[1], word[3], word[4] are green.


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
