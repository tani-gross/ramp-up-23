def reverse_string(str):
    vowels = "aeiouAEIOU"
    new_str = ""
    vowel_count = 0

    for letter in str:
        if letter in vowels:
            vowel_count += 1
        new_str = letter + new_str 
    
    print(f"Reversed: {new_str}, Vowel Count: {vowel_count}")



        