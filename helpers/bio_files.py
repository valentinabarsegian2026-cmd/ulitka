def convert_multiline_fasta_to_oneline(
    input_fasta: str,
    output_fasta = None
) -> None:
    """
    Converts multiline FASTA sequences to one-line sequences.
    Arguments:
    input_fasta: path to the input FASTA file
    output_fasta: path to the output FASTA file
    Returns None.
    """
    if output_fasta is None:
        output_fasta = "oneline.fasta"
    with open(input_fasta, "r") as input_file:
        with open(output_fasta, "w") as output_file:
            sequence = ""
            for line in input_file:
                if line.startswith(">"):
                    if sequence:
                        output_file.write(sequence + "\n")

                    output_file.write(line)
                    sequence = ""

                else:
                    sequence += line.strip()

            if sequence:
                output_file.write(sequence + "\n")

