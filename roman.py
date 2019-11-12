class Roman:
    """Class for Roman numeral object"""

    charMap = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    def __init__(self, romanString):
        self.roman = romanString

    def decimal(self):
        pass

    def decompose(self):
        decomposed = []
        letter = self.roman[0]
        count = 1
        for i in range(1, len(self.roman)):
            if letter == self.roman[i]:
                count += 1
            else:
                decomposed.append((letter,count))
                letter = self.roman[i]
                count = 1
        decomposed.append((letter,count))

        return decomposed
