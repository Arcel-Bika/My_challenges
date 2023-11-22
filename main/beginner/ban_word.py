"""
Enoncé:
    - Ecrire un algorithme qui bannie les mots interdits

Fonction:
    - ban(): Pour censurer les mots interdits exemple, con retourne c**

Liste principal des mots à bannir
    - [con, pute]

"""

message = input(str("Ecrivez votre message : ")).lower()

ban_word = ["con", "pute"]

message_list = message.split()
compter_message = len(message_list)
compter_interdict = len(ban_word)

i, j = int(0), int(0)

for i in range(compter_message):
    for j in range(compter_interdict):
        if message_list[i] == ban_word[j]:
            convert = int(len(message_list[i]))
            message_list[i] = message_list[i][0] + "*" * (convert - 1)
            j = j + 1
    i = i + 1

print(" ".join(message_list))