import re

class FastqToFastaConverter:
    def __init__(self):
        pass

    def convert(self, fq_file):
        idsl = []
        idsl2 = []
        at_sym_list = []
        at_list = []
        plus_sym_list = []
        plus_list = []
        
        with open(fq_file) as fq, open("file.fasta", "w") as fa:
            for row, line in enumerate(fq, start=1):
                ids = str(re.findall("^@.+", line))
                idsl.append(ids)
                at_sym = re.findall("^@", line)
                at_sym_list.append(at_sym)
                plus_sym = re.findall("^\+", line)
                plus_sym_list.append(plus_sym)
                
            for i in range(0, row, 4):
                if '@' in idsl[i]:
                    idsl2.append(str(idsl[i]))   
            for i in range(0, row, 4):
                if '@' in at_sym_list[i]:
                    at_list.append(at_sym_list[i])        
            for i in range(2, row, 4):
                if '+' in plus_sym_list[i]:
                    plus_list.append(plus_sym_list[i])            
            if row / len(at_list) != 4 or row / len(plus_list) != 4:
                raise Exception("Incorrect FastQ file (length or @ symbol)")       
            
            fq.seek(0)
            fq_len = len(fq.readlines())
            fq.seek(0)
            
            for i in idsl2:
                i = i.strip("[]''")
                i = i.replace("@", "")
                for row, line in enumerate(fq, start=1):
                    if row in range(-2, fq_len, 4):
                        line = line.strip()
                        fa.write(f'>{i}\n')
                        print(line, file=fa)
                        print(f'>{i}')
                        print(line)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py input.fastq")
        sys.exit(1)
    fq_file = sys.argv[1]
    converter = FastqToFastaConverter()
    converter.convert(fq_file)

