
def calculate_gc(sequence: str) -> float:
    """
    Calculates GC content of a nucleotide sequence.
    Arguments:
    sequence: nucleotide sequence
    Returns GC content as a percentage.
    """
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    gc_count = g_count + c_count
    length = len(sequence)

    return gc_count / length * 100

def check_gc(gc_percent: float, gc_bounds) -> bool:
    """
    Checks whether GC content is within the specified bounds.

    Arguments:
    gc_percent: GC content as a percentage
    gc_bounds: allowed GC content range or upper bound

    Returns True if GC content is within the bounds, otherwise False.
    """
    if isinstance(gc_bounds, (int, float)):
        lower_bound = 0
        upper_bound = gc_bounds
    else:
        lower_bound = gc_bounds[0]
        upper_bound = gc_bounds[1]

    return lower_bound <= gc_percent <= upper_bound

def check_length(sequence: str, length_bounds) -> bool:
    """
    Checks whether sequence length is within the specified bounds.

    Arguments:
    sequence: nucleotide sequence
    length_bounds: allowed sequence length range or upper bound

    Returns True if sequence length is within the bounds, otherwise False.
    """
    length = len(sequence)
    if isinstance(length_bounds, (int, float)):
        lower_bound = 0
        upper_bound = length_bounds
    else:
        lower_bound = length_bounds[0]
        upper_bound = length_bounds[1]

    return lower_bound <= length <= upper_bound

def check_quality(quality: str, quality_threshold: float) -> bool:
    """
    Checks whether average read quality meets the specified threshold.

    Arguments:
    quality: FASTQ quality string
    quality_threshold: minimum average Phred quality

    Returns True if average quality is at least the threshold, otherwise False.
    """
    total_quality = 0

    for char in quality:
        phred_score = ord(char) - 33
        total_quality = total_quality + phred_score

    average_quality = total_quality / len(quality)

    return average_quality >= quality_threshold
