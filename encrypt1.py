from cryptography.fernet import Fernet

#message = "pythonchallenge"
message=input("Enter message to be encrypted: ")
key = Fernet.generate_key()
fernet = Fernet(key)
encMessage = fernet.encrypt(message.encode())
print("encrypted string: ", encMessage)
decMessage = fernet.decrypt(encMessage).decode()
print("decrypted string: ", decMessage)