import cryptography 
from cryptography.fernet import Fernet
import sys
import os
def this():
    def notthis():
        the_answer = input('Enter some bytes: ').encode('utf-8')
        enans = the_answer.decode('utf-8')
        print(the_answer)
        key = Fernet.generate_key()
        k = key.decode('utf-8')
        print(k)
        with open("symmetric.key", "wb") as fo:
            fo.write(key)
        f = Fernet(key)



        with open("pastkeys.txt", "r") as h:
            lines = h.readlines()
            if f in lines:
                print("invalid key")
            else:
                with open("pastkeys.txt", "a") as g:
                    j = key.decode('utf-8')
                    g.write(j + '\n')
                enanswer = f.encrypt(the_answer).decode('utf-8')
                print(enanswer)
                file = open('symmetric.key', 'rb')
                key = file.read()
                file.close()
                ans = f.decrypt(enanswer).decode('utf-8')
                with open("words.txt", "a") as g:
                    g.write(enanswer + "\n")
                heh = input("Do you want to change keys?")
                if heh == "Yes":
                     
                    this()
                else:
                    print("Program End")
    notthis()
this()    

       
