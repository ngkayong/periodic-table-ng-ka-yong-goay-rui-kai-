import random

def main():
    print("welcome to our game")
    print("Guess the answer")
    print("this element is released into the atmosphere through respiration")
    answer = input("name the element:")
    list =['carbon','nitrogen','oxygen','flourine','helium','neon']
    x = random.choice(list)
    
    if x == 'carbon':
        print("correct")
    elif x != 'carbon':
        print("wrong,the answer is carbon")
        
    
    print("this element is a common element in the universe,we breathe anout 79.02% in the air")
    answer = input("name the element:")
    list =['carbon','nitrogen','oxygen','flourine','helium','neon']
    y = random.choice(list)
    
    if y == 'nitrogen':
        print("correct")
    elif x != 'nitrogen':
        print("wrong,the answer is nitrogen")
    
       
    print("i type the hint after im done")
    answer = input("name the element:")
    list =['carbon','nitrogen','oxygen','flourine','helium','neon']
    z = random.choice(list)
       
    if z == 'oxygen':
        print("correct")
    elif z != 'oxygen':
        print("wrong,the answer is oxygen")

    print("i type the hint after im done")
    answer = input("name the element:")
    list =['carbon','nitrogen','oxygen','flourine','helium','neon']
    a = random.choice(list)
       
    if a == 'flourine':
        print("correct")
    elif a != 'flourine':
        print("wrong,the answer is flourine")
        
    print("i type the hint after im done")
    answer = input("name the element:")
    list =['carbon','nitrogen','oxygen','flourine','helium','neon']
    b = random.choice(list)
       
    if b == 'helium':
        print("correct")
    elif x != 'helium':
        print("wrong,the answer is helium")
    
        
    print("i type the hint after im done")
    answer = input("name the element:")
    list =['carbon','nitrogen','oxygen','flourine','helium','neon']
    c = random.choice(list)
       
    if c == 'neon':
        print("correct")
    elif c != 'neon':
        print("wrong,the answer is neon")

main()
