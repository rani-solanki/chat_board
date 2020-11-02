import json
with open("board.json","r") as my_file:
    data=json.load(my_file)
    for i in range(len(data)):
        massage=input("type the massage")
        print(data[massage])