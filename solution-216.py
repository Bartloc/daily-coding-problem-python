def roman_to_arab(roman=''):
    
    roman_dict={
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
    }
     
    if not roman:
        return 0
    num=0
    num_p=0
    for r in roman:
        if num_p<roman_dict[r]:
            num -=2*num_p
        num +=roman_dict[r]
        num_p=roman_dict[r]
    return num
assert roman_to_arab('XIV')==14
