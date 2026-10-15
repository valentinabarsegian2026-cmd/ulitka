import os

from helpers.fastq import calculate_gc, check_gc, check_length, check_quality

def filter_fastq(
    input_fastq: str,
    output_fastq: str,
    gc_bounds=(0, 100),
    length_bounds=(0, 2**32),
    quality_threshold: float = 0
):
    os.makedirs("filtered", exist_ok=True)
    output_path = os.path.join("filtered", output_fastq)

    with open(input_fastq, "r") as input_file:
        with open(output_path, "w") as output_file:
            for header in input_file:
                sequence = next(input_file).strip()
                separator = next(input_file)
                quality = next(input_file).strip()
                gc_percent = calculate_gc(sequence)
                gc_ok = check_gc(gc_percent, gc_bounds)
                length_ok = check_length(sequence, length_bounds)
                quality_ok = check_quality(quality, quality_threshold)

                if gc_ok and length_ok and quality_ok:
                    output_file.write(header)
                    output_file.write(sequence + "\n")
                    output_file.write(separator)
                    output_file.write(quality + "\n")
