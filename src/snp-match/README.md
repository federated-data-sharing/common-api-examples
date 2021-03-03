# README - snp-match

## Introduction

This example illustrates a simple matching rule for single neucleotide polymorphisms (SNPs). A research may have a number of SNPs of interest and would like to check whether a data source has matching donors of genomic data. In a federated context, it is not possible to work directly with SNP data. However, an anonymous summary of matches

## Configuration

The example uses a file [`top_mutations.csv`](./top_mutations.csv) to list SNPs of interest. This should be a CSV file with at least the following columns:

- `hgnc_symbol` - the [HUGO nomenclature](https://www.genenames.org/) symbol for the gene of interest
- `ensembl_gene_id` - the [Ensembl](https://www.ensembl.org/index.html) ID for the gene
- `chromosome` - the chromosome the SNP is on
- `chromosome_start` - the start position of the SNP
- `chromosome_end` - the end position of the SNP
- `mutated_from_allele` - the 'reference' sequence
- `mutated_to_allele` - the 'mutated' sequence

The matching algorithm will sift through a remote table of genese that have the core fields above plus a field `donor_id` - it will match on the specification of the SNP of interest and count unique donors that have a match. All other fields are ignored. Note that `hgnc_symbol` and `ensembl_gene_id` are not used in the matching process.

The results of the script are written to a CSV file `results.csv` which contains the SNP records plus an additional field `matches` which is the count of unique donors.

## Running the example

- When running locally via `run-local.sh` - the `top_mutations.csv` file is read and used. The script expects a file called `snp_clean.csv` in its input folder.
- When running via Docker, the `top_mutations.csv` is built into the container - future iterations will take configuration in some other way. Test the Docker version via `run-docker.sh` 
- When run from this folder, both approaches will read from the `./input` folder and write output to `./output/results.csv`
