import os
for root, dirs, files in os.walk("/home/ubuntu"):
    for file in files:
        if file.lower().startswith("license"):
            file_path = os.path.join(root, file)
            with open(file_path, "r") as fin1:
                content=fin1.read()
            with open("final_license.txt", "a") as fin1:
                fin1.write(f"\n{content}")
