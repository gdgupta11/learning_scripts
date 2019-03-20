#!/usr/bin/python

'''
Small script to convert the Decimal to HexaDecimal.

How does Decimal to HexaDecimal convert happens:

Hexa decimal has base of 16. So take the decimal and divide by 16 and put reminder to identify corresponding HexDecimal. The excercise continues with quotient till we get 0 quotient.

Taking the reminder value from left to right and convert using hexaDecimal scale.

'''


def dec2hex(decimalNum):
    hexaChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hexString = ''
    dec = decimalNum

    while dec > 0:
        hexNumber = dec % 16   # The reminder is used to get corresponding value from above hexaChars
        hexString = hexaChars[hexNumber] + hexString
        dec = dec // 16  # divide untill you get 0 as quotient value.

    return hexString


def main():
    decimalNum = int(input("Enter the decimal: "))
    value = dec2hex(decimalNum)
    print("The decimal {} conversation to hexaDecimal is {} ".format(decimalNum, value))


if __name__ == '__main__':
    main()
