
def intRoman(num: int):

    nums = [1, 4, 5, 9, 10, 40, 50, 90,100, 400, 500, 900, 1000]
    
    roman = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]
    
    i = 12
    arr = []
    while num > 0:
        div = num // nums[i]
        num = num % nums[i]
        while div > 0:
            arr.append(roman[i])
            div -= 1
        i -= 1
    
    return ("".join(arr))

print(intRoman(58))


