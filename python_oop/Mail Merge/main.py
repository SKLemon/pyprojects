# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names_list_path = "./Input/Names/invited_names.txt"
template_message_path = "./Input/Letters/starting_letter.txt"
output_path = "./Output/ReadyToSend"

# Getting list of names
with open(names_list_path, mode="r") as names_file:
    names_list = names_file.readlines()

# Getting template message
with open(template_message_path, mode="r") as template_file:
    template = template_file.read()

# Writing the message and saving the file in its specific folder
for each_name in names_list:
    stripped_name = each_name.strip()
    new_message = template.replace("[name]", stripped_name)
    with open(f"{output_path}/{stripped_name}.txt", mode="w") as new_file:
        new_file.write(new_message)

print("Mail Merge Complete! Check the output folder")
