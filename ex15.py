from simplecrypt import decrypt
with open('dataset\\encrypted(ex15).bin', 'rb') as enc:
    encrypted = enc.read()
with open('dataset\\passwords(ex15).txt') as passwords:
    for password in passwords:
        try:
            print(decrypt(password.strip(), encrypted).decode('utf-8'))#decode -декодикровка из бит в строку
            break
        except:
            pass
