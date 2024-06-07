with open("input.txt",) as f:
    data = f.read()
find = input("Enter the word to find... ")
replace = input("Enter the word to replace with... ")
with open("output.txt","w") as f:
    f.write(data.replace(find,replace))