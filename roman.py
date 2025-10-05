def int_to_roman(num):  
    # Map of Roman numerals  
    val = [  
        1000, 900, 500, 400,  
        100, 90, 50, 40,  
        10, 9, 5, 4,  
        1  
    ]  
    syms = [  
        "M", "CM", "D", "CD",  
        "C", "XC", "L", "XL",  
        "X", "IX", "V", "IV",  
        "I"  
    ]  
      
    roman_num = ""  
    i = 0  
    while num > 0:  
        count = num // val[i]  
        roman_num += syms[i] * count  
        num -= val[i] * count  
        i += 1  
    return roman_num  
  
# Example usage  
number = int(input("Enter a number (1-3999): "))  
if 1 <= number <= 3999:  
    print(f"Roman numeral: {int_to_roman(number)}")  
else:  
    print("Number out of range!")  
