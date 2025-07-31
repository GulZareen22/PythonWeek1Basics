#------User name Generation------
Name=input("Enter your full name: ")
Parts=Name.strip().split()
import random
random_no=random.randint(0,100)
if len(Parts)>=2:
    print(f"Your username generated is:{Parts[0].lower()}{Parts[-1].lower()}{random_no}")
else:
    print(f"your usename generated is: {Parts[0].lower()}{random_no}")


 #-----Vowels\Consonants Counter----
A=input("Enter a word or a sentence: ")
vowels=0
consonants=0
for char in A:
    if char.isalpha():
        if char.lower() in 'aeiou':
            vowels+=1
        else:
            consonants+=1
    

print(f"Total vowels={vowels}")
print(f"Total consonants={consonants}")

        


