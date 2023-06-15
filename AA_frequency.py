import sys
import glob

ext = "faa"

dir = sys.argv[1] if len(sys.argv) > 1 else input("Name of the folder that contains the faa files of the MAGs with the extension .{}: ".format(ext))

mat = "{}_AAfreq.matrix".format(dir)
try:
    with open(mat, "w") as mat_file:
        mat_data = {}
        bugs = {}
        aa_names = {
            "G": "Glycine",
            "P": "Proline",
            "A": "Alanine",
            "V": "Valine",
            "L": "Leucine",
            "I": "Isoleucine",
            "M": "Methionine",
            "C": "Cysteine",
            "F": "Phenylalanine",
            "Y": "Tyrosine",
            "W": "Tryptophan",
            "H": "Histidine",
            "K": "Lysine",
            "R": "Arginine",
            "Q": "Glutamine",
            "N": "Asparagine",
            "E": "GlutamicAcid",
            "D": "AsparticAcid",
            "S": "Serine",
            "T": "Threonine"
        }

        for faa in glob.glob("{}/*.{}".format(dir, ext)):
            fn = faa.split(".faa")[0]
            bug = fn.split("/")[-1]
            bugs[bug] = 1
            AAs = []
            AAs_count = {}

            with open(faa) as faa_file:
                for line in faa_file:
                    line = line.strip()
                    if line.startswith(">"):
                        continue
                    line = line.replace("*", "")
                    line = line.upper()
                    aas = list(line)
                    for aa in aas:
                        if aa in aa_names:
                            AAs.append(aa)
                            if aa in AAs_count:
                                AAs_count[aa] += 1
                            else:
                                AAs_count[aa] = 1

            out = "{}_AAfreq.tab".format(bug)
            with open(out, "w") as out_file:
                total = len(AAs)
                print("{}\t{}".format(bug, total))
                for aa in AAs_count:
                    freq = AAs_count[aa] / total
                    round_freq = round(freq, 4)
                    print("*{}\t{}\t{}\t{}".format(aa, AAs_count[aa], total, round_freq))
                    print("{}\t{}".format(aa, round_freq), file=out_file)
                    if bug not in mat_data:
                        mat_data[bug] = {}
                    mat_data[bug][aa] = round_freq

        header = "Genome\t"
        for aa in sorted(aa_names.keys()):
            header += "{}\t".format(aa)
        header = header[:-1]
        print(header, file=mat_file)

        for bug in bugs:
            line = "{}\t".format(bug)
            for aa in sorted(aa_names.keys()):
                if bug in mat_data and aa in mat_data[bug]:
                    line += "{}\t".format(mat_data[bug][aa])
                else:
                    print("WARNING: {} doesn't have {}".format(bug, aa))
            line = line[:-1]
            print(line, file=mat_file)
            print(line)

except IOError as e:
    print("Can't create {}: {}".format(mat, str(e)))
