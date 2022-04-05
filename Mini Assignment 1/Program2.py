from Program1 import StringClass


class PairsPossible(StringClass):
    def __init__(self):
        super().__init__()
        self.string2 = input("Enter String for Pair : ")
        self.pair_obtained = []

    def possible_pairs(self):
        for i in range(len(self.string2)):
            for j in range(len(self.string2)):
                pair = [self.string2[i], self.string2[j]]
                self.pair_obtained.append(pair)

    def print_pair(self):
        for i in self.pair_obtained:
            print(i, " ")


if __name__ == '__main__':
    pair = PairsPossible()
    pair.possible_pairs()
    pair.print_pair()
