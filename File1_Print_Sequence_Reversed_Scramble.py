import random

def process_protein_sequence(protein_sequence: str):
    # Reverse the sequence
    reversed_sequence = protein_sequence[::-1]
    
    # Scramble the sequence
    scrambled_sequence = list(protein_sequence)
    random.shuffle(scrambled_sequence)
    scrambled_sequence = ''.join(scrambled_sequence)
    
    return reversed_sequence, scrambled_sequence

# Example input
Protein_Sequence = "PROTEINSEQUENCE"
reversed_seq, scrambled_seq = process_protein_sequence(Protein_Sequence)

print("Original Sequence:", Protein_Sequence)
print("Reversed Sequence:", reversed_seq)
print("Scrambled Sequence:", scrambled_seq)
