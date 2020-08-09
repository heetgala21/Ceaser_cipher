def encrypt(text,step):
        crypted=[]
        UpCase=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        LoCase=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        for letter in text:#to iterate over each letter in entered sentence.
                if letter in UpCase:# if letter is upper case
                        num=UpCase.index(letter)# assign letter's index to num
                        if((num-step)<0):#if letter's index is less than shift number
                                n = step - num
                                crypted.append(UpCase[len(UpCase)-n])
                        else:
                                crypted.append(UpCase[num-step])
                elif letter in LoCase:#same as above, except if letter is lower case
                        num=LoCase.index(letter)
                        if((num-step)<0):
                                n = step - num
                                crypted.append(LoCase[len(LoCase)-n])
                        else:
                                crypted.append(LoCase[num-step])
                else:
                        crypted.append(letter)
        final= ''.join(str(e) for e in crypted)#if iterated letter is " "(blank space)
        return final

text = str(input("Enter a string to encrypt it:"))
step = int(input("Enter shift amount:"))
print(encrypt(text,step))
