import random
import sys


def main():
    file_name = file_acceptor()
    file_opener(file_name)


def file_acceptor():
    file_name = sys.argv[1:1]
    file_name = str(file_name)
    file_name = "immunidefficiencyvirus.FASTA"
    return file_name


def file_opener(file_name):
    with open(file_name, "r") as open_file:
        sequences = fasta_reader(open_file)
        randomized_sequences = sequence_randomizer(sequences)
        file_writer(randomized_sequences)
        # for key, value in randomized_sequences.items():
        #     print(key)
        #     for key2, value2 in value.items():
        #         print(key2, value2)


def fasta_reader(open_file):
    header = ""
    sequence_dict = {}
    for line in open_file:
        if line.startswith(">"):
            header = line
            sequence_dict[header] = ""
        else:
            sequence_dict[header] += line.rstrip()
    return sequence_dict


def sequence_randomizer(sequence_dict):
    tmp_randomized_dict = {}
    randomized_dict = {}
    x = range(100)
    for key, value in sequence_dict.items():
        for n in x:
            tmp_randomized_dict[n] = ''.join(random.sample(value, len(value)))
        randomized_dict[key] = tmp_randomized_dict
    return randomized_dict


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
