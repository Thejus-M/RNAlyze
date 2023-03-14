def calculate_longest_orf(sequence):
    longest_orf_length = 0
    for frame in range(3):
        for pos in range(frame, len(sequence)-2, 3):
            codon = sequence[pos:pos+3]
            if codon == 'ATG':
                orf_length = 0
                for pos2 in range(pos, len(sequence)-2, 3):
                    codon2 = sequence[pos2:pos2+3]
                    if codon2 in ('TAA', 'TAG', 'TGA'):
                        break
                    else:
                        orf_length += 3
                if orf_length > longest_orf_length:
                    longest_orf_length = orf_length
    return longest_orf_length
