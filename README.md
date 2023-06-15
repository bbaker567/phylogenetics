# phylogenetics
## AA_frequency.py
Calulates the frequency of each of the 20 amino acids (AA) for each proteome in a directory. The input for the script is a direcotry of proteome files with the extension '.faa'. The output is a tabular formatted file of the AA frequencies for each proteomes and a tabular formatted file with all the proteomes together in a single table.

## removing_biased_aln_sites.py
Progressively removes the most biased sites from an alignment. This script specifically removes biases based on the ratio of [DE/IK] for halophiles compared to the same ratio for non halophiles. The input for this script is two alignment files: (1) only halophiles, and (2) non halophiles. The output is a dataframe of the alignment. The dataframe then needs to be run through df2faa.py to convert it to an alignment.

## df2faa.py
Converts an amino acid dataframe into an alignment file. Input is the dataframe from removing_biased_aln_sites.py
