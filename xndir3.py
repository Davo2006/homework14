files = ['input1.txt','input2.txt','input3.txt']
datas = []
for file in files:
    with open(file,) as f:
        datas.append(f.read())
with open("output.txt","w") as f:
    f.write('\n'.join(datas))