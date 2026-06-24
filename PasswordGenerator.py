# Password Generator 
import random
import string

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    print("Lowercase letters: ", s1)
    s2 = string.ascii_uppercase
    print("Uppercase letters: ", s2)        
    s3 = string.digits
    print("Digits: ", s3)
    s4 = string.punctuation
    print("Punctuation: ", s4)
    plen = int(input("Enter the password length: "))
    s = []
    s.extend(list(s1))  
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    #print(s)
    random.shuffle(s)
    #print(s)
    print("Your password is being generated...")
    password = ''.join(random.sample(s, plen))
    print("Generated Password: ", password)