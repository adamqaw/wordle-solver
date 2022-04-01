class Solver:
    def __init__(self, word: str, available_letters: str, indexes_empty: list):
        self.word_input = word
        self.available_letters = list(available_letters.upper())
        self.indexes_empty = indexes_empty
        
        # self.word_input = 's*o*t'.upper()
        # self.available_letters = list('qwtyuodfgjkzxcvbnm'.upper())
        # self.indexes_empty = [1, 3]

    def three_greens(self):
        nw = self.word_input
        idx_range = range(len(self.indexes_empty))
        with open('possible_words.txt', mode='w') as data:
            for i in range(len(self.available_letters)):
                nw.replace(nw[self.indexes_empty[idx_range[i]]], self.available_letters[i])
                data.write(f'{nw}\n')
                for j in range(len(self.available_letters)):
                    nw.replace(nw[self.indexes_empty[idx_range[j]]], self.available_letters[j])
                    data.write(f'{nw}\n')

    def two_greens(self):
        nw = self.word_input
        idx_range = range(len(self.indexes_empty))
        with open('possible_words.txt', mode='w') as data:
            for i in range(len(self.available_letters)):
                nw.replace(nw[self.indexes_empty[idx_range[i]]], self.available_letters[i])
                data.write(f'{nw}\n')
                for j in range(len(self.available_letters)):
                    nw.replace(nw[self.indexes_empty[idx_range[j]]], self.available_letters[j])
                    data.write(f'{nw}\n')
                for k in range(len(self.available_letters)):
                    nw.replace(nw[self.indexes_empty[idx_range[k]]], self.available_letters[k])
                    data.write(f'{nw}\n')

    def one_green(self):
        nw = self.word_input
        idx_range = range(len(self.indexes_empty))
        with open('possible_words.txt', mode='w') as data:
            for i in range(len(self.available_letters)):
                nw.replace(nw[self.indexes_empty[idx_range[i]]], self.available_letters[i])
                data.write(f'{nw}\n')
                for j in range(len(self.available_letters)):
                    nw.replace(nw[self.indexes_empty[idx_range[j]]], self.available_letters[j])
                    data.write(f'{nw}\n')
                for k in range(len(self.available_letters)):
                    nw.replace(nw[self.indexes_empty[idx_range[k]]], self.available_letters[k])
                    data.write(f'{nw}\n')
                    for l in range(len(self.available_letters)):
                        nw.replace(nw[self.indexes_empty[idx_range[l]]], self.available_letters[l])
                        data.write(f'{nw}\n')

    def preprocess(self):
        nw = '*****'
        idx_range = range(5)
        with open('possible_words.txt', mode='w') as data:
            for l1 in range(len(self.available_letters)):
                nw.replace(nw[idx_range[l1]], self.available_letters[l1])
                data.write(f'{nw}\n')
                for l2 in range(len(self.available_letters)):
                    nw.replace(nw[idx_range[l2]], self.available_letters[l2])
                    data.write(f'{nw}\n')
                    for l3 in range(len(self.available_letters)):
                        nw.replace(nw[idx_range[l3]], self.available_letters[l3])
                        data.write(f'{nw}\n')
                        for l4 in range(len(self.available_letters)):
                            nw.replace(nw[idx_range[l4]], self.available_letters[l4])
                            data.write(f'{nw}\n')
                            for l5 in range(len(self.available_letters)):
                                nw.replace(nw[idx_range[l5]], self.available_letters[l5])
                                data.write(f'{nw}\n')


test1 = Solver(word='s*o*t', available_letters='qwtyuodfgjkzxcvbnm', indexes_empty=[1, 3])
test1.three_greens()
