#!/usr/bin/env python
# Tui Popenoe
# challenge207E.py - DNA Replication

import sys

def get_dna_pairs():
    return {
        'A' : 'T',
        'T' : 'A',
        'G' : 'C',
        'C' : 'G'
    }

def get_codons():
    return {
        'TTT' : 'Phe',
        'TTC' : 'Phe',
        'TTA' : 'Leu',
        'TTG' : 'Leu',
        'CTT' : 'Leu',
        'CTC' : 'Leu',
        'CTA' : 'Leu',
        'CTG' : 'Leu',
        'ATT' : 'Ile',
        'ATC' : 'Ile',
        'ATA' : 'Ile',
        'ATG' : 'Met',
        'GTT' : 'Val',
        'GTC' : 'Val',
        'GTA' : 'Val',
        'GTG' : 'Val',
        'TCT' : 'Ser',
        'TCC' : 'Ser',
        'TCA' : 'Ser',
        'TCG' : 'Ser',
        'AGT' : 'Ser',
        'AGC' : 'Ser',
        'CCT' : 'Pro',
        'CCC' : 'Pro',
        'CCA' : 'Pro', 
        'CCG' : 'Pro',
        'ACT' : 'Thr',
        'ACC' : 'Thr',
        'ACA' : 'Thr',
        'ACG' : 'Thr',
        'GCT' : 'Ala',
        'GCC' : 'Ala',
        'GCA' : 'Ala',
        'GCG' : 'Ala',
        'TAT' : 'Tyr',
        'TAC' : 'Tyr',
        'TAA' : 'STOP',
        'TAG' : 'STOP',
        'CAT' : 'His',
        'CAC' : 'His',
        'CAA' : 'Gin',
        'CAG' : 'Gin',
        'AAT' : 'Asn',
        'AAC' : 'Asn',
        'AAA' : 'Lys',
        'AAG' : 'Lys',
        'GAT' : 'Asp',
        'GAC' : 'Asp',
        'GAA' : 'Glu',
        'GAG' : 'Glu',
        'TGT' : 'Cys',
        'TGC' : 'Cys',
        'TGA' : 'STOP',
        'TGG' : 'Trp',
        'CGT' : 'Arg',
        'CGC' : 'Arg',
        'CGA' : 'Arg',
        'CGG' : 'Arg',
        'AGA' : 'Arg',
        'AGG' : 'Arg',
        'GGT' : 'Gly',
        'GGC' : 'Gly',
        'GGA' : 'Gly',
        'GGG' : 'Gly'
    }

def dna_replication(dna):
    print(' '.join(dna))
    dna_pairs = get_dna_pairs()
    return [dna_pairs[x] for x in dna]

def codon_replication(dna):
    codons = get_codons()
    output = []
    for i, val in enumerate(dna):
        if i % 3 == 0:
            codon = ''.join(dna[i:i+3])
            if codon in codons and codons[codon] is not 'STOP':
                output.append(codons[codon])
            else:
                output.append(codons[codon])
                break
    return output

def main():
    if len(sys.argv) > 1:
        print(' '.join(dna_replication(sys.argv[1:])))
        print(' '.join(codon_replication(sys.argv[1:])))
    else:
        dna_input = sys.stdin.readline().strip().split()
        print(' '.join(dna_replication(dna_input)))
        print(' '.join(codon_replication(dna_input)))

if __name__ == '__main__':
    main()

