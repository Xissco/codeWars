def is_interesting(number, awesome_phrases):
    if number < 98: return 0
    elif number == 98 or number == 99: return 1
    for x in range(3):
        num = number + x
        if num in awesome_phrases: return 2 if not x else 1        
        else:            
            num_str = str(num)
            if num_str[1:] == '0' * (len(num_str) - 1): return 2 if not x else 1
            if num_str == num_str[::-1]: return 2 if not x else 1
            if num_str in "1234567890": return 2 if not x else 1
            if num_str in "9876543210": return 2 if not x else 1
    return 0

tests = [
    {'n': 3, 'interesting': [1337, 256], 'expected': 0},
    {'n': 1336, 'interesting': [1337, 256], 'expected': 1},
    {'n': 1337, 'interesting': [1337, 256], 'expected': 2},
    {'n': 11208, 'interesting': [1337, 256], 'expected': 0},
    {'n': 11209, 'interesting': [1337, 256], 'expected': 1},
    {'n': 11211, 'interesting': [1337, 256], 'expected': 2},
        ]
for t in tests:
    print(is_interesting(t['n'], t['interesting']), t['expected'])