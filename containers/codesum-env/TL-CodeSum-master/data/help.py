def replace_lines_code(dirname, file_name, idx):
    lines = open(str(dirname + "/" + file_name), 'r', encoding='utf-8').readlines()
    for i in range(len(lines)):
        line = lines[i][1:-2]
        line += "\n"
        line = f"{idx}" + "\t" + line
        if i == 0:
            print(line)
        
        lines[i] = line
        idx += 1
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(lines)
    return idx
    
def replace_lines_nl(dirname, file_name, idx):
    lines = open(str(dirname + "/" + file_name), 'r', encoding='utf-8').readlines()
    for i in range(len(lines)):
        line = lines[i][:-1]
        line += "\n"
        line = f"{idx}" + "\t" + line
        if i == 0:
            print(line)
        lines[i] = line
        idx += 1
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(lines)
    return idx
    


idx = replace_lines_code("test", "test.token.code", 0)
idx = replace_lines_code("valid", "valid.token.code", idx)
idx = replace_lines_code("train", "train.token.code", idx)

idx = replace_lines_nl("test", "test.token.nl", 0)
idx = replace_lines_nl("valid", "valid.token.nl", idx)
idx = replace_lines_nl("train", "train.token.nl", idx)

    
  