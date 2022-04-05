from Program3 import SearchCommonElements

class EqualSumPairs(SearchCommonElements):
    def __init__(self):
        super().__init__()
        self.sumList = []

    def count_sum(self):
        sum_map = {}
        self.possible_pairs()
        print(self.print_pair())
        self.possible_pairs()
        for ele in self.pair_obtained:
            sum = int(ele[0]) + int(ele[1])
            if sum in sum_map:
                sum_map[sum] += 1
            else:
                sum_map[sum] = 1

        for ele in sum_map:
            if sum_map[ele] != 1:
                self.sumList.append(ele)

        return len(self.sumList)


if __name__ == '__main__':
    equalSum = EqualSumPairs()
    print(equalSum.count_sum())

