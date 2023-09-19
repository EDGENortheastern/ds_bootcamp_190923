def fun_function(input_string):
    # Reverse the string
    reversed_str = input_string[::-1]
    
    # Count the vowels
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for char in input_string if char in vowels)
    
    return reversed_str, vowel_count

result = fun_function("Hello, World!")
print(result)