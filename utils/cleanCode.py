import re
 
with open("framework.txt", "r+") as f:
    p = re.compile("//|///")
    lines = [line for line in f.readlines() if p.search(line) is None]
    f.seek(0)
    f.truncate(0)
    f.writelines(lines)

