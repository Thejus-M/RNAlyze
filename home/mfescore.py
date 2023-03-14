def calculate_mfe_score(seq):
    from Bio.Seq import Seq
    from Bio.SeqUtils import MeltingTemp
    rna_seq = Seq(str(seq))
    mfe = MeltingTemp.Tm_Wallace(rna_seq.transcribe().reverse_complement())
    return mfe