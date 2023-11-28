"""
Enoncé:
    - Ecrire un algorithme qui bannie les mots interdits

Fonction:
    - ban(): Pour censurer les mots interdits exemple, con retourne c**

Liste principal des mots à bannir
    - [con, pute]

"""

def ban(message, ban_list):
    message_list = message.lower().split()

    for i in range(len(message_list)):
        for banned_word in ban_list:
            if message_list[i] == banned_word:
                convert = len(message_list[i])
                message_list[i] = message_list[i][0] + "*" * (convert - 1)

    return " ".join(message_list)

# Liste principal des mots à bannir
ban_word = ["con", "pute"]

user_message = input("Ecrivez votre message : ")
censored_message = ban(user_message, ban_word)

print(censored_message)
