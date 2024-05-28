def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Welcome to the Caesar Cipher Tool")
    choice = input("Would you like to encrypt or decrypt a text? (1 for encrypt, 2 for decrypt): ").strip()

    if choice not in ['1', '2']:
        print("Invalid choice. Please enter '1' for encrypt or '2' for decrypt.")
        return
    if choice == '1':
        print("Encrypting...")
    else: 
        print("Decrypting...")

    text = input("Enter the text: ").strip()
    try:
        shift = int(input("Enter the shift value: ").strip())
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    if choice == '1':
        result = encrypt(text, shift)
        print("Encrypted text:", result)
    
    else:
        result = decrypt(text, shift)
        print("Decrypted text:", result)

if __name__ == "__main__":
    main()
