import os


def main():
    files = file_acceptor()
    file_opener(files)


def file_acceptor():
    """Accepts files from directory with correct file
     extensions as "file" in a list.

    :return file_list"""
    file_extension = (".FASTA", ".fasta", ".txt")
    file_list = []
    for file in os.listdir():
        if file.endswith(file_extension):
            file_list.append(file)
    return file_list


def file_opener(file_list):
    """Opens file in current scope using with to automatically close
    when processing on file is done."""
    for file in file_list:
        # Opens file in current scope.
        with open(file, 'r') as open_file:
            sequence_dict = fasta_reader(open_file)
            envelop_dict = dict_sorter(sequence_dict)
            file_writer(envelop_dict)


def fasta_reader(open_file):
    """Reads all the lines in a file and makes a structured dictionary
    out of them that uses the header of the file as key and the sequence
    of that protein as the value.
    data_output(file, envelop_dict, internal_dict)
    :param open_file
    :return sequence_dict"""
    # Make empty header and dictionary that can be used to store all
    # sequences in an organized manner.
    header = ""
    sequence_dict = {}
    for line in open_file:
        if line.startswith(">"):
            # Makes a list of all elements of the header line split by
            # spaces. Then gets the 1st / 0th element from that list.
            header = line.split(" ")
            header = "".join(header)
            header = ''.join(map(str, header))
            # Makes a key out of the header with an empty value.
            sequence_dict[header] = ""
        else:
            # Removes newline character at end of sentence and adds the
            # correct sequence as value to the dictionary.
            sequence_dict[header] += line.rstrip()
    return sequence_dict


def dict_sorter(sequence_dict):
    """Imports a protein sequence dictionary and determines if the
    protein is an envelope protein by the code that is appended to the
    string. Returns two dictionaries with all envelope proteins and
    all internal proteins.

    :param sequence_dict
    :return env_dict"""
    env_dict = {}
    for key, value in sequence_dict.items():
        if "=env" in key:
            env_dict[key] = value
    return env_dict


def file_writer(env_dict):
    file = open("immunidefficiencyvirus.FASTA", "a")
    for key, value in env_dict.items():
        file.write(key)
        file.write(value)
        file.write("\n"*2)
    file.close()


if __name__ == '__main__':
    main()
