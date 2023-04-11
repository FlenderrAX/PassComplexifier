import random
from Levenshtein import distance
from colorama import Fore, Back, Style

a = input("Entrez votre mot de passe à complexer : ")
b = int(input("Entrez la distance entre votre mot de passe initial est votre alternative : "))


shuffled_char = ''.join(random.sample(a, len(a)))

while True:
    if distance(a, shuffled_char) >= b:
        print(Style.RESET_ALL)
        while b > len(a):
            b = int(input("La distance doit être inférieure à la longueur du mot de passe : "))
        if len(shuffled_char) < 8 or len(shuffled_char) > 16:
            print(Fore.YELLOW + shuffled_char)
            print(Style.RESET_ALL)
            lenght = len(shuffled_char) - 16 or len(shuffled_char) + 8
            shuffled_char = shuffled_char[:lenght]
        else :
            print(Fore.GREEN + shuffled_char)   
            print(Style.RESET_ALL)
            break
    elif distance(a, shuffled_char) <= b:
        print(Style.RESET_ALL)
        print(Fore.RED + (shuffled_char))
        print(Style.RESET_ALL)
        a = ''.join(random.sample(a, len(a)))
        shuffled_char = ''.join(random.sample(a, len(a))) + ''.join(random.sample(shuffled_char, len(shuffled_char)))