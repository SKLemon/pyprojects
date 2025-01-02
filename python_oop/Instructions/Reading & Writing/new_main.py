# with open("logs.txt") as file:
#     contents = file.read()
#     print(contents)

# In Python, file paths can be absolute or relative. An absolute path specifies the location from the root directory,
# while a relative path specifies the location relative to the current directory. For example:
# Absolute path: "/home/user/project/logs.txt"
# Relative path: "./logs.txt"

with open("./logs.txt", mode="a") as file:
    file.write("\nnew text3.0")
