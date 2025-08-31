import collections

Neuclotides = ["A", "C", "G", "T"]
DNA_reverse_complement_map = {"A": "T", "C": "G", "G": "C", "T": "A"}


def validate_seq(sequence: str):

    upper_case_seq = sequence.upper()

    for neuclotide in upper_case_seq:
        if neuclotide not in Neuclotides:
            return False

    return upper_case_seq


def count_nueclotide_frequency(sequence):

    return dict(collections.Counter(sequence))


def transcribe(sequence: str):

    return sequence.replace("T", "U")


def reverse_complement(sequence: str):

    return "".join([DNA_reverse_complement_map[neu] for neu in sequence])[::-1]
