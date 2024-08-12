Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def encrypt(text, shift):
...     result = ""
...     
...     # Loop through each character in the text
...     for i in range(len(text)):
...         char = text[i]
...         
...         # Encrypt uppercase characters
...         if char.isupper():
...             result += chr((ord(char) + shift - 65) % 26 + 65)
...         # Encrypt lowercase characters
...         elif char.islower():
...             result += chr((ord(char) + shift - 97) % 26 + 97)
...         # Keep non-alphabetic characters unchanged
...         else:
...             result += char
... 
...     return result
... 
... def decrypt(text, shift):
...     return encrypt(text, -shift)
... 
... # Example usage
... text = "Hello, World!"
... shift = 3
... 
... encrypted_text = encrypt(text, shift)
... print(f"Encrypted: {encrypted_text}")
... 
... decrypted_text = decrypt(encrypted_text, shift)
