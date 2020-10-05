
fasta_dict = {}
seq = '' 

h_l = []
s_l = []
ref_seq=[]

first_list = []
middle_list = []
last_list = []

result_list = []

header = None
with open("rosalind_splc.txt", 'r') as handle:
    for line in handle:
        line = line.strip()
        if line.startswith(">"):
            if header:
                fasta_dict[header] = seq
            header = line[1:]
            fasta_dict[header] = ''
            seq = ''
        else:
            seq += line
    if header:
        fasta_dict[header] = seq


for k,v in fasta_dict.items():
    h_l.append(k)
    s_l.append(v)

#print(h_l)
#print(s_l)

#print(len(s_l))

T_l = []

for i in range(len(s_l)):
    T = s_l[0].index(s_l[i])
    T_l.append(T)

#print(T_l)    

#print(sorted(T_l))

# 순서대로 배열 못하나
T_sl = []
T_sl = T_l
#print(T_sl)

s_sl = []
s_sl = s_l
#print(s_sl)

d = dict(zip(T_sl,s_sl))
#print(d)

result_T = []

sort_T = sorted(T_sl)
#print(sort_T)
for i in sort_T:
    result_T.append(d[i])

#print(result_T)


for i in range(len(result_T)):
    if i == 0 :
        first_seq = result_T[0][0:s_l[0].index(result_T[1])]
        #print(first_seq)
        first_list.append(first_seq)


    elif i == len(result_T)-1:
        last_seq = result_T[0][s_l[0].index(result_T[i])+len(result_T[i]) : len(result_T[0])]
        #print(last_seq)
        last_list.append(last_seq)

    elif result_T[i] in result_T[0]:
        middle_seq = result_T[0][result_T[0].index(result_T[i])+len(result_T[i]) : result_T[0].index(result_T[i+1])]
        #print(middle_seq)
        middle_list.append(middle_seq)

result_list = first_list + middle_list + last_list

#Result = sorted(result_list, key=len(s_l[0].index()))

#print(Result)

#print(result_list)

result = ''.join(result_list)

Seq = result.replace('T','U')

#print(Seq.strip(' '))

RNA_codon = {
'UUU': 'F' ,'CUU' :'L' ,'AUU' :'I' ,'GUU' :'V',
'UUC': 'F', 'CUC':'L', 'AUC': 'I', 'GUC': 'V',
'UUA': 'L','CUA':'L','AUA':'I','GUA':'V',
'UUG': 'L','CUG': 'L','AUG': 'M','GUG': 'V',
'UCU': 'S'  ,    'CCU': 'P'  ,    'ACU': 'T',     'GCU': 'A',
'UCC': 'S'  ,    'CCC': 'P'  ,    'ACC': 'T',     'GCC': 'A',
'UCA': 'S'  ,    'CCA': 'P'  ,    'ACA': 'T',     'GCA': 'A',
'UCG': 'S'  ,    'CCG': 'P'  ,    'ACG': 'T',     'GCG': 'A',
'UAU': 'Y'  ,    'CAU': 'H'  ,    'AAU': 'N',     'GAU': 'D',
'UAC': 'Y'  ,    'CAC': 'H'  ,    'AAC': 'N',     'GAC': 'D',
'UAA': 'Stop',   'CAA': 'Q'  ,    'AAA': 'K',     'GAA': 'E',
'UAG': 'Stop',   'CAG': 'Q'  ,    'AAG': 'K',     'GAG': 'E',
'UGU': 'C'   ,   'CGU': 'R'  ,    'AGU': 'S',     'GGU': 'G',
'UGC': 'C'   ,   'CGC': 'R'  ,    'AGC': 'S',     'GGC': 'G',
'UGA': 'Stop',   'CGA': 'R'  ,    'AGA': 'R',     'GGA': 'G',
'UGG': 'W'   ,   'CGG': 'R'  ,    'AGG': 'R',     'GGG': 'G',
}
l = []

for i in range(0, len(Seq), 3):
    l.append(Seq[i:i+3])

for s in range(len(l)):
    codon = RNA_codon[l[s]]
    if codon == "Stop":
        continue

    print(codon, end='')


