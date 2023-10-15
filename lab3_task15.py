#шифр цезаря . Попросите пользователя ввести строку и сдвинуть все буквы в строке на N позиций вперед по алфавиту (циклически), где N — целое число, введенное пользователем. Распечатать зашифрованную строку

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

try:
    user_input = input("Enter a string: ")
    shift = int(input("Enter the shift value (an integer): "))
    encrypted_string = caesar_cipher(user_input, shift)
    print("Encrypted string:", encrypted_string)
except ValueError:
    print("Please enter a valid integer for the shift value.")