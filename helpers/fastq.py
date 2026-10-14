
def calculate_gc(sequence: str) -> float:
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    gc_count = g_count + c_count
    length = len(sequence)

    return gc_count / length * 100

def check_gc(gc_percent: float, gc_bounds) -> bool:
    if isinstance(gc_bounds, (int, float)):
        lower_bound = 0
        upper_bound = gc_bounds
    else:
        lower_bound = gc_bounds[0]
        upper_bound = gc_bounds[1]

    return lower_bound <= gc_percent <= upper_bound

def check_length(sequence: str, length_bounds) -> bool:
    length = len(sequence)
    if isinstance(length_bounds, (int, float)):
        lower_bound = 0
        upper_bound = length_bounds
    else:
        lower_bound = length_bounds[0]
        upper_bound = length_bounds[1]

    return lower_bound <= length <= upper_bound

def check_quality(quality: str, quality_threshold: float) -> bool:
    total_quality = 0

    for char in quality:
        phred_score = ord(char) - 33
        total_quality = total_quality + phred_score

    average_quality = total_quality / len(quality)

    return average_quality >= quality_threshold

def read_fastq_record(file):
    header = file.readline()
    if not header:
        return None
    sequence = file.readline().strip()
    separator = file.readline()
    quality = file.readline().strip()

    return header, sequence, separator, quality