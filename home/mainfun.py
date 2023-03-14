from .ficketscore import calculate_fickett_score
from .cpgislands import calculate_cpg_islands
from .gccontent import calculate_gc_content
from .hexamer import calculate_hexamer_score
from .orflength import calculate_longest_orf
from .transcriptlength import calculate_transcript_length
from .mfescore import calculate_mfe_score


def create_feature(seq):
    fickett_score=calculate_fickett_score(seq)
    cpg_islands=calculate_cpg_islands(seq)
    gc_content = calculate_gc_content(seq)
    orf_length = calculate_longest_orf(seq)
    transcriptlength = calculate_transcript_length(seq)
    # hexamer_score = calculate_hexamer_score(seq)
    # mfescore = calculate_mfe_score(seq)
    
    feature = [
        orf_length,
        gc_content,
        transcriptlength,
        cpg_islands,
        fickett_score,
        # hexamer_score,
        # mfescore,
        ]
    
    return [feature]