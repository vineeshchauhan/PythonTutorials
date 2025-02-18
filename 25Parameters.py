def greet_user(first_name,last_name):
    print(f'Welcome Abroad')
    message = f'Hi {first_name} {last_name}'
    return message

print(greet_user(last_name="Vineesh",first_name="Chauhan"))


def print_with_emoji(message):
    emojis = {
        ":)": "😀",
        ":(": "😔"
    }
    word_list = message.split(" ")

    output = ""
    for word in word_list:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
output = print_with_emoji(message)
print(output)