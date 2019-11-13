class Roman:
    """Class for Roman numeral object"""

    charMap = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    valMap = {n:c for c,n in charMap.items()}

    def __init__(self, inputValue):
        if type(inputValue) == str:
            self.roman = inputValue
            self.decimal = self.fromString()
            if self.fromInt() != self.roman:
                msg = "Input string is not a legal roman numeral, do you mean \"{}\"?".format(self.fromInt())
                raise InputError(msg)
        elif type(inputValue) == int:
            if inputValue < 4000:
                self.decimal = inputValue
                self.roman = self.fromInt()
            else:
                msg = "Cannot create a roman numeral higher than 3999"
                raise InputError(msg)
        else:
            msg = "A roman numeral can only be created from an integer or a string"
            raise InputError(msg)

    def __repr__(self):
        return self.roman

    def fromString(self):
        decomposed = self.decompose()
        val = sum(Roman.charMap[c[0]]*c[1]*c[2] for c in decomposed)
        return val

    def decompose(self):
        decomposed = []
        letter = self.roman[0]
        count = 1
        for i in range(1, len(self.roman)):
            if letter == self.roman[i]:
                count += 1
            else:
                if Roman.charMap[letter] < Roman.charMap[self.roman[i]]:
                    sign = -1
                else:
                    sign = 1
                decomposed.append((letter,count,sign))
                letter = self.roman[i]
                count = 1
        decomposed.append((letter,count,1))
        return decomposed

    def fromInt(self):
        romanList = list()
        current = self.decimal
        singleChars = sorted(Roman.valMap.keys(), reverse = True)
        for i in range(len(singleChars)):
            val = singleChars[i]
            count = current // val
            if 0 < count < 4:
                romanList.append(count * Roman.valMap[val])
            elif count == 4:
                if romanList[-1] == Roman.valMap[singleChars[i-1]]:
                    romanList[-1] = Roman.valMap[val] + Roman.valMap[singleChars[i-2]]
                else:
                    romanList.append(Roman.valMap[val] + Roman.valMap[singleChars[i-1]])
            current -= count * val
        return "".join(romanList)

class InputError(Exception):
    """Exception raised for errors in the input
    """
    def __init__(self, message):
        self.message = message