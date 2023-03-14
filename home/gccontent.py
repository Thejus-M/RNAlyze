def calculate_gc_content(seq):
    gc_count = seq.count('G') + seq.count('C')
    total_count = len(seq)
    return (gc_count / total_count) * 100