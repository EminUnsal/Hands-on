
def Convert_Roman( num):
        symbol = [ "M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        value = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        roman_num = ''
        i = 0
        while  num > 0:
            for x in range(num // value[i]):
                roman_num += symbol[i]
            num %= value[i]
            i += 1
        return roman_num
print(Convert_Roman(49))
print(Convert_Roman(4))
print(Convert_Roman(1249))
print(Convert_Roman(67))