message = input(">")

word_list = message.split(" ")

print(word_list)

emojis = {
    ":)" : "😀",
    ":(" : "😔"
}

for word in word_list:
    if word == ":)":
        print(emojis[":)"])
    elif  word == ":(":
        print(emojis[":("])
    else:
        print(word)

output = ""
for word in word_list:
    output += emojis.get(word,word) + " "

print(output)
