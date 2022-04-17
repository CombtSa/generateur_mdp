import random

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345679890"
choix = input('Voulez vous des caractere spéciaux, Oui ou Non')
if choix == 'Oui':
    caracterespeciaux = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345679890@#€_&-+()/*:;!?~`|•√π÷×¶∆£¥$¢^°={}\%©®™✓[]<>"
    for i in range(9):
        print(random.choice(caracterespeciaux))
elif choix == 'Non':
    for i in range(9):
        print(random.choice(alphabet))
else:
    print("Je n'ai pas compris la demande")





