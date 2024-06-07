with open("input.txt",) as f:
    data = f.read()
x = []
for i in data:
    x.append(f"{i}:{data.count(i)}")
with open("output.txt","w") as f:
    f.write("\n".join(x))