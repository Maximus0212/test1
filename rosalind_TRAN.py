with open('rosalind_tran.txt','r') as f_input, open('rosalind_tran_out.txt', 'w') as f_output:
    block = []
    for line in f_input:
        if line.startswith('>'):
            if block:
                f_output.write(''.join(block) + '\n')
                block = []
            f_output.write(line)
        else:
            block.append(line.strip())
    if block:
        f_output.write(''.join(block)+'\n')

header = []
seq = []
with open('rosalind_tran_out.txt', 'r') as handle:
    for line in handle:
        if line.startswith('>'):
            header += line.strip().split()
        else:
            seq += line.strip().split()

fasta_dic = dict(zip(header, seq))
print(fasta_dic)

ts = 0
tv = 0

for i in range(len(seq[0])):
    if seq[0][i] == 'G':
        if seq[1][i] == 'A':
            ts += 1
        elif seq[1][i] == 'C':
            tv += 1
        elif seq[1][i] == 'T':
            tv += 1
    elif seq[0][i] == 'A':
        if seq[1][i] == 'C':
            tv += 1
        elif seq[1][i] == 'T':
            tv += 1
        elif seq[1][i] == 'G':
            ts += 1
    
    elif seq[0][i] == 'C':
        if seq[1][i] == 'A':
            tv += 1
        elif seq[1][i] == 'T':
            ts += 1
        elif seq[1][i] == 'G':
            tv += 1
    
    elif seq[0][i] == 'T':
        if seq[1][i] == 'C':
            ts += 1
        elif seq[1][i] == 'A':
            tv += 1
        elif seq[1][i] == 'G':
            tv += 1
    

print(ts)
print(tv)   

print(round(ts/tv, 10))
 
