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
        totalVal = 0
        for i in range(0, len(self.roman)):
            currentChar = self.roman[i]
            currentVal = Roman.charMap[currentChar]
            if i <= len(self.roman)-2:
                nextVal = Roman.charMap[self.roman[i+1]]
                if currentVal >= nextVal:
                    totalVal += currentVal
                else:
                    totalVal -= currentVal
            else:
                totalVal += currentVal
        return totalVal

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