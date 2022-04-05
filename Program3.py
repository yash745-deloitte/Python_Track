from Program2 import PairsPossible

class SearchCommonElements(PairsPossible):
    def __init__(self):
        super().__init__()
        self.commonList = []

    def common(self):
        commonEle = {}
        for i in range(len(self.str1)):
            if self.str1[i] in commonEle:
                commonEle[self.str1[i]] += 1
            else:
                commonEle[self.str1[i]] = 1

        for i in range(len(self.string2)):
            if self.string2[i] in commonEle:
                commonEle[self.string2[i]] += 1
            else:
                commonEle[self.string2[i]] = 1

        for ele in commonEle:
            if commonEle[ele] != 1:
                self.commonList.append(ele)

        return self.commonList


if __name__ == '__main__':
    commonEle = SearchCommonElements()
    print(commonEle.common())

