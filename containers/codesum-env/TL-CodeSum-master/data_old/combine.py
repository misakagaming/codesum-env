filenames = ["test/test.token.code", "train/train.token.code", "valid/valid.token.code"]
with open('data_ps.declbodies', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(' '.join(line.split()[1:]))
                outfile.write("\n")
                
                
filenames = ["test/test.token.nl", "train/train.token.nl", "valid/valid.token.nl"]
with open('data_ps.descriptions', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write("'")
                outfile.write(' '.join(line.split()[1:]))
                outfile.write("'\n")