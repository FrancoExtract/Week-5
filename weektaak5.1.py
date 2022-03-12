# Weektaak 5.1.py
# Sequence-to-ClustalO Converter
# By Sam Sokolov

import random
import sys


def main():
    file_name = file_acceptor()
    file_opener(file_name)


def file_acceptor():
    """This function retrieves the specified FASTA file,
    and lets the code run through."""
    file_name = sys.argv[1:1]  # Asks for the code to be run
    file_name = str(file_name)
    file_name = "immunidefficiencyvirus.FASTA"
    return file_name


def file_opener(file_name):
    """This function opens the file as a variable with a "while" loop,
    and declares further used functions as variables to be used in the code.

    :param file_name: name of the specified FASTA file"""
    with open(file_name, "r") as open_file:
        sequences = fasta_reader(open_file)  # Reader function is 'sequences' variable
        randomized_sequences = sequence_randomizer(sequences)  # Randomizer variable
        file_writer(randomized_sequences)  # Randomized sequences passed to file writer


def fasta_reader(open_file):
    header = ""
    sequence_dict = {}  # Dictionary used for the sequences within the file
    for line in open_file:
        if line.startswith(">"):  # If '>' is present in the line
            header = line
            sequence_dict[header] = ""
        else:
            sequence_dict[header] += line.rstrip()
    return sequence_dict


def sequence_randomizer(sequence_dict):
    tmp_randomized_dict = {}
    randomized_dict = {}
    x = range(100)  # 100 sequences
    for key, value in sequence_dict.items():  # Key = index; Value = sequence itself
        for n in x:
            # Join = random part of the sequence adds to the sequence
            tmp_randomized_dict[n] = ''.join(random.sample(value, len(value)))
        randomized_dict[key] = tmp_randomized_dict
    return randomized_dict  # 100 new


def file_writer(randomized_dict):
    for sequence_name, nested_keys in randomized_dict.items():
        header_buffer = sequence_name.split('[')
        file = open(header_buffer[0], "a")
        for key, sequence in nested_keys.items():
            header = f"{header_buffer[0]}_{key+1}"
            file.write(header)
            file.write("\n")
            file.write(sequence)
            file.write('\n'*2)
        file.close()


if __name__ == '__main__':
    main()
