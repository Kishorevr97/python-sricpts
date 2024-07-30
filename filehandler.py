with open("1.txt", "r") as fh:
    content=fh.read()
    print(content)

with open("1.txt", "w") as fh:
    fh.write("kishore devops engineer")

with open("1.txt", "a") as fh:
    fh.write("\nIn Bengaluru")
