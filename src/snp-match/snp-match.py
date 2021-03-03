import pandas as pd
import sys
import os
import glob

if __name__ == '__main__':

    input_folder = os.environ.get('CA_INPUT_FOLDER', '/mnt/input')
    output_folder = os.environ.get('CA_OUTPUT_FOLDER', '/mnt/output')
    config_folder = os.environ.get('CA_CONFIG_FOLDER', '/app')

    if not os.path.isdir(input_folder):
        print(f'Input folder missing or invalid: {input_folder}')
        exit(1) 
    if not os.path.isdir(output_folder):
        print(f'Output folder missing or invalid: {output_folder}')
        exit(1)
    if not os.access(output_folder, os.W_OK):
        print(f'Output folder is not writeable: {output_folder}')
        exit(1)

    print(f'Input:  {input_folder}')
    print(f'Output: {output_folder}')
    print(f'Config: {config_folder}')

    snps = pd.read_csv(f"{input_folder}/snp_clean.csv")
    # TODO - check snps table has the required fields

    # Read the mutations of interest
    top_mutations = pd.read_csv(f"{config_folder}/top_mutations.csv")

    # Make sure chromosome is treated as string in both tables so we can match
    top_mutations.chromosome = top_mutations.chromosome.astype(str)
    snps.chromosome = snps.chromosome.astype(str)

    with open(f'{output_folder}/result.csv', 'w') as rf:

        # Print the header row
        rf.write('"hgnc_symbol","ensembl_gene_id","chromosome","chromosome_start","chromosome_end", "mutated_from_allele","mutated_to_allele","matches"\n')

        # Loop through each of the genes of interest and filter the snps table, calculate unique donors
        for i, r in top_mutations.iterrows():
            # Matching clauses
            match_chr = snps['chromosome'] == r['chromosome']
            match_chr_start = snps['chromosome_start'] == r['chromosome_start']
            match_chr_end= snps['chromosome_end'] == r['chromosome_end']
            match_mutated_from_allele = snps['mutated_from_allele'] == r['mutated_from_allele']
            match_mutated_to_allele = snps['mutated_to_allele'] == r['mutated_to_allele']
            
            matches = snps.loc[match_chr & match_chr_start & match_chr_end & match_mutated_from_allele & match_mutated_to_allele]
            unique_donors = matches['donor_id'].unique()
            
            print(matches.shape, unique_donors.size, unique_donors)
            
            result = [
                        r['hgnc_symbol'],
                        r['ensembl_gene_id'],
                        r['chromosome'],
                        r['chromosome_start'],
                        r['chromosome_end'],
                        r['mutated_from_allele'],
                        r['mutated_to_allele'],
                        unique_donors.size,
                ]
            rf.write(','.join([str(x) for x in result]))
            rf.write('\n')