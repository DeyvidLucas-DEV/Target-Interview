def reverse_string(s):
    chars = list(s)
    start = 0
    end = len(chars) - 1
    
    while start < end:
        chars[start], chars[end] = chars[end], chars[start]
        start += 1
        end -= 1
    
    return ''.join(chars)

input_string = input("Digite uma palavra: ")
reversed_string = reverse_string(input_string)
print(f"Invertida: {reversed_string}")
