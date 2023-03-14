def calculate_hexamer_score(seq):
    from collections import Counter
    hexamers = [seq[i:i+6] for i in range(len(seq)-5)]
    counts = Counter(hexamers)
    score = sum(counts.values())
    return score
