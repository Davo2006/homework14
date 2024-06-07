with open('input.txt',) as f:
    data = f.read()
lines_count = 25
lines = data.splitlines()
i = 1
while lines:
    lines_ = lines[:lines_count]
    lines = lines[lines_count:]
    with open(f"output{i}.txt","w") as f:
        f.write('\n'.join(lines_))