def calculate_fickett_score(seq):
    """
    Calculates the Fickett score for a given DNA sequence.
    """
    num_a = seq.count('A')
    num_c = seq.count('C')
    num_g = seq.count('G')
    num_t = seq.count('T')
    
    if num_a + num_c + num_g + num_t == 0:
        return 0
    
    freq_a = num_a / (num_a + num_c + num_g + num_t)
    freq_c = num_c / (num_a + num_c + num_g + num_t)
    freq_g = num_g / (num_a + num_c + num_g + num_t)
    freq_t = num_t / (num_a + num_c + num_g + num_t)
    
    r_y_ratio = (freq_a + freq_g) / (freq_c + freq_t)
    a_t_ratio = freq_a / freq_t
    gc_content = freq_g + freq_c
    fickett_score = (r_y_ratio * a_t_ratio) + gc_content - 0.5
    
    return fickett_score