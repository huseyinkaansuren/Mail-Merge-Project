with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    name_file.close()

with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_content = letter_file.read()


for name in names:
    name = name.strip("\n")
    letter_content = letter_content.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(letter_content)
