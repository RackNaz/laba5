def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:
                shifted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            result += shifted_char
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

input_text = input("Введите строку для шифрования: ")
shift_amount = int(input("Введите сдвиг: "))

encrypted_text = caesar_cipher_encrypt(input_text, shift_amount)
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift_amount)

print("Зашифрованный текст:", encrypted_text)
print("Расшифрованный текст:", decrypted_text)