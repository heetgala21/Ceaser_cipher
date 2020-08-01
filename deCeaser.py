def decrypt(text,step):
        decrypted=[]
        UpCase=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        LoCase=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        for letter in text:
                if letter in UpCase:
                        num=UpCase.index(letter)
                        if((num+step)>(len(UpCase)-1)):
                                n = num - step
                                decrypted.append(UpCase[len(UpCase) - 1 - n])
                        else:
                                decrypted.append(UpCase[num+step])
                elif letter in LoCase:
                        num=LoCase.index(letter)
                        if((num+step)>(len(LoCase)-1)):
                                n = num - step
                                decrypted.append(LoCase[len(LoCase) - 1 - n])
                        else:
                                decrypted.append(LoCase[num+step])
                else:
                        decrypted.append(letter)
        final= ''.join(str(e) for e in decrypted)
        return final

text = str(input("Enter a string to dencrypt it:"))
step = int(input("Enter shift amount:"))
print(decrypt(text,step))
