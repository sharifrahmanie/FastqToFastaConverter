import re
at_sym_list = []
at_list = []
plus_sym_list = []
plus_list = []
with open("file.fastq") as fq:
    for row,line in enumerate(fq, start = 1):
        at_sym = re.findall("^@", line)
        at_sym_list.append(at_sym)
        plus_sym = re.findall("^\+", line)
        plus_sym_list.append(plus_sym)
    for i in range(0, row,4):
        if '@' in at_sym_list[i]:
            at_list.append(at_sym_list[i])        
    for i in range(2, row,4):
          if '+' in plus_sym_list[i]:
            plus_list.append(plus_sym_list[i])            
    if row/len(at_list) != 4 or row/len(plus_list) != 4:
        raise Exception("Incorrect FastQ file (length or @ symbol)")       
    fq.seek(0)
    fq_len = len(fq.readlines())
    fq.seek(0)
    with open("file.fasta", "w") as fa:
        fa.write(">file\n")
        for row,line in enumerate(fq, start = 1):
            if row in range(-2, fq_len, 4):
                line = line.strip()
                print(line, file = fa)
                print(line)
# @sharifrahmanie
