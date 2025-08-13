def large_power(base,exponent):
    result = base ** exponent
    if result >5000:
        return True
    else:
        return False
    
print(f"larger power: {large_power(10,20)}")



def divisible_by_ten(num):
    remainder  = num%10
    if remainder==0:
        return True
    else:
        return False
print(f"Is divisible by 10: {divisible_by_ten(5)}")