# ulitka

A small bioinformatics utility for working with FASTQ and FASTA files.

## Functions

### filter_fastq

Filters FASTQ reads by:
- GC content
- sequence length
- average Phred quality

Filtered reads are saved to the `filtered` directory.

### convert_multiline_fasta_to_oneline

Converts multiline FASTA sequences into one-line sequences.

## Project structure

- `ulitka.py` — FASTQ filtering
- `helpers/fastq.py` — helper functions for FASTQ processing
- `helpers/bio_files.py` — functions for working with bioinformatics files

## Requirements

Python 3.9 or newer.
Only the Python standard library is used.