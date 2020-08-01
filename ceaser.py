def encrypt(text,step):
        crypted=[]
        UpCase=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        LoCase=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        for letter in text:
                if letter in UpCase:
                        num=UpCase.index(letter)
                        if((num-step)<0):
                                n = step - num
                                crypted.append(UpCase[len(UpCase)-n])
                        else:
                                crypted.append(UpCase[num-step])
                elif letter in LoCase:
                        num=LoCase.index(letter)
                        if((num-step)<0):
                                n = step - num
                                crypted.append(LoCase[len(LoCase)-n])
                        else:
                                crypted.append(LoCase[num-step])
                else:
                        crypted.append(letter)
        final= ''.join(str(e) for e in crypted)
        return final

text = str(input("Enter a string to encrypt it:"))
step = int(input("Enter shift amount:"))
print(encrypt(text,step))
