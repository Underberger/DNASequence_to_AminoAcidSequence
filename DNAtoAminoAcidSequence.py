import pyperclip # needed module to copy mRNA sequence to clipboard
# User input DNA sequence
try:
    DNA_sequence = input("Please enter the DNA sequence below: \n")
except:
    print("Invalid, please enter a valid DNA sequence.")
# DNA sequence to uppercases
DNA = DNA_sequence.upper()

# check nucleotides for thymine (-> uracil)
mRNA = ""
for nuc in DNA:
    if nuc == "T":
        mRNA = mRNA + "U" # replace T with U
    else:
        mRNA = mRNA + nuc # do nothing

#codons = [mRNA[start:start+3] for start in range(0,len(mRNA),3)] # save codons in a list

genetic_code = { # genetic code in a list
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R', 'AGA': 'R', 'AGG': 'R',
    'AAC': 'N', 'AAU': 'N',
    'GAC': 'D', 'GAU': 'D',
    'UGC': 'C', 'UGU': 'C',
    'CAA': 'Q', 'CAG': 'Q',
    'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
    'CAC': 'H', 'CAU': 'H',
    'AUA': 'I', 'AUC': 'I', 'AUU': 'I',
    'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L', 'UUA': 'L', 'UUG': 'L',
    'AAA': 'K', 'AAG': 'K',
    'AUG': 'M',
    'UUC': 'F', 'UUU': 'F',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
    'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S', 'AGC': 'S', 'AGU': 'S',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
    'UGG': 'W',
    'UAC': 'Y', 'UAU': 'Y',
    'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
    'UAA': "Stop", 'UAG': "Stop", 'UGA': "Stop"
}

amino_acid_sequence = ""
for i in range(0, len(mRNA) - 2, 3):
    codon = mRNA[i:i + 3] # create codons
    amino_acid_sequence = amino_acid_sequence + genetic_code[codon] # add amino acids together to the sequence
    
print("Success! Amino acid sequence copied on the clipboard and shown below:\n" + amino_acid_sequence) # give back the sequence
pyperclip.copy(amino_acid_sequence) # copy the sequence on clipboard