def calculate_cpg_islands(seq):
    cpg_islands = []
    num_islands = 0
    cpg_count = 0
    in_island = False
    
    for i in range(len(seq)-1):
        if seq[i:i+2].upper() == 'CG':
            cpg_count += 1
            if not in_island:
                in_island = True
        else:
            if cpg_count > 0:
                cpg_islands.append(cpg_count)
                cpg_count = 0
                in_island = False
    
    if cpg_count > 0:
        cpg_islands.append(cpg_count)
    
    num_islands = len(cpg_islands)
    
    return num_islands