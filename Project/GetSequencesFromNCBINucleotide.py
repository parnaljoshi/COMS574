from Bio import Entrez, SeqIO

Entrez.email = "parnal@iastate.edu"

fh1 = open("EcoliFT.txt", "r")
fhw1 = open("Ecoli_AllCDS.txt", "w")
fhw2 = open("Ecoli_AllNCS.txt", "w")
header = fh1.readline()
ncs_start = 0
ncs_end = 0
i = 1
for line in fh1:
    if "CDS" in line and i <= 1200:
        cds_start = line.split("\t")[0]
        cds_end = line.split("\t")[1]
        handle = Entrez.efetch(db="nucleotide",
                               id="NC_002695.2",
                               rettype="fasta",
                               strand=1,
                               seq_start=cds_start,
                               seq_stop=cds_end)
        coding_sequence = SeqIO.read(handle, "fasta")
        handle.close()
        fhw1.write(str(coding_sequence.seq)+"\n")
        #print("CDS: ", coding_sequence.seq)
        ncs_end = int(cds_start) - 1
        handle = Entrez.efetch(db="nucleotide",
                               id="NC_002695.2",
                               rettype="fasta",
                               strand=1,
                               seq_start=ncs_start,
                               seq_stop=ncs_end)
        noncoding_sequence = SeqIO.read(handle, "fasta")
        handle.close()
        fhw2.write(str(noncoding_sequence.seq)+"\n")
        #print("NCS: ", noncoding_sequence.seq)
        ncs_start = int(cds_end) + 1
        print(i)
        i += 1
fh1.close()
fhw1.close()
fhw2.close()
