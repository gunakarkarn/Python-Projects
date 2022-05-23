def DecimalToBinary(num):
    
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')

dec_val= int(input("Enter a number in decimal: "))
DecimalToBinary(dec_val) 