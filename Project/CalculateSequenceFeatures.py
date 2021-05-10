from Bio.SeqUtils import MeltingTemp as mt
from Bio.SeqUtils import molecular_weight
from Bio.Seq import Seq
from Bio.SeqUtils import GC

# mystring = 'CGTTCCAAAGATGTGGGCATGAGCTTAC'
# mydna = Seq(mystring)
fhr = open("Ecoli_DatasetCDS.fasta", "r")
fh1 = open("CDS_features.txt", "w")

for mystring in fhr:
    mystring = mystring.rstrip()
    mydna = Seq(mystring)
    # print(mystring)
    # Sequence length
    len_str = len(mystring)
    # print(len)
    fh1.write("+1\t1:"+str(len_str)+"\t")

    # Count A
    # print(mydna.count("A"))
    fh1.write("2:"+str(mydna.count("A"))+"\t")

    # Count T
    fh1.write("3:"+str(mydna.count("T"))+"\t")

    # Count G
    fh1.write("4:"+str(mydna.count("G"))+"\t")

    # Count C
    fh1.write("5:"+str(mydna.count("C"))+"\t")

    # Count AA
    fh1.write("6:"+str(mydna.count("AA"))+"\t")

    # Count AT
    fh1.write("7:"+str(mydna.count("AT"))+"\t")

    # Count AG
    fh1.write("8:"+str(mydna.count("AG"))+"\t")

    # Count AC
    fh1.write("9:"+str(mydna.count("AC"))+"\t")

    # Count TA
    fh1.write("10:"+str(mydna.count("TA"))+"\t")

    # Count TT
    fh1.write("11:"+str(mydna.count("TT"))+"\t")

    # Count TC
    fh1.write("12:"+str(mydna.count("TC"))+"\t")

    # Count TG
    fh1.write("13:"+str(mydna.count("TG"))+"\t")

    # Count GA
    fh1.write("14:"+str(mydna.count("GA"))+"\t")

    # Count GT
    fh1.write("15:"+str(mydna.count("GT"))+"\t")

    # Count GC
    fh1.write("16:"+str(mydna.count("GC"))+"\t")

    # Count GG
    fh1.write("17:"+str(mydna.count("GG"))+"\t")

    # Count CA
    fh1.write("18:"+str(mydna.count("CA"))+"\t")

    # Count CT
    fh1.write("19:"+str(mydna.count("CT"))+"\t")

    # Count CG
    fh1.write("20:"+str(mydna.count("CG"))+"\t")

    # Count CC
    fh1.write("21:"+str(mydna.count("CC"))+"\t")

    # Melting temperature
    fh1.write("22:"+str('%0.2f' % mt.Tm_Wallace(mystring))+"\t")

    # GC content
    fh1.write("23:"+str(GC(mydna))+"\t")

    # Molecular weight
    fh1.write("24:"+str("%0.2f" % molecular_weight(mystring))+"\n")

fh1.close()
fhr.close()