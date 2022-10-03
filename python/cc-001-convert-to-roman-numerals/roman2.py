num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
def num2roman(num):
    if num == "Exit":
        print("Exiting the program... Good Bye")
    elif type(num) == str or num < 0 or num >= 4000:
        print("Not Valid Input !!!")
    else:
        roman = ''
        while num > 0 :
            for i, r in num_map:
                while num >= i:
                    roman += r
                    num -= i
        return roman
print(num2roman(49))
print(num2roman(4))
print(num2roman(1249))
print(num2roman(67))
















