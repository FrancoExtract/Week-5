import matplotlib as plt


def file_reader(file):
    """
    This function reads the matrices in all files and returns the values in
    separate lists.

    :param file: percentages of matches between the sequences
    """

    with open(file) as data1:
        data_list1 = []  # List for the matrix data
        for line in data1:
            if "#" not in line and not line.isspace():  # isspace() returns
                # true if the string is a whitespace string. FALSE otherwise.
                line = line.rstrip().split()
                i = (line.index('100.00') + 1)
                for unit in line[i:]:
                    data_list1.append(float(unit))
        print(data_list1)
        return data_list1


def data_list_processor(data_list1):
    """This function processes the appended data list from the matrix
    and makes it able to be passed to the histogram function.

    :param data_list1: list with the matrix data per file
    """


def histogram_prepare(x, y):
    """
    This function prepares a histogram for the data to be passed through.

    :param x: protein sequences on the x-axis
    :param y: match hits on the y-axis (in percentages)
    """

    plt.plot(x, y, 'g-')  # Plots out the axes and makes the line green
    plt.title("Total counts of exons per chromosome")  # Title for the graph
    plt.xlabel("Chromosome")  # Title for the x-axis
    plt.ylabel("Exon count")  # Title for the y-axis


def histogram_data(data_list_processor):
    """
    This function passes the data from the matrices to the histogram_prepare
    function and shows the data accordingly.

    :param data_list_processor: data from the matrices
    """

    plt.show()  # Makes the graph show up when running the program
    # yuh = 1
    # print(yuh)


# def graph_plotter(gc_list, file_name, reading_distance):
# calculation = seq_len / reading_distance
# print(f"the result of {seq_len} / {reading_distance} =\n {calculation}")
# y = gc_list
# x = range(len(gc_list))
# plt.scatter(x, y, 5, c=gc_list, cmap="Reds")
# plt.ylim([0, 100])
# plt.title(f"GC% of {file_name}\n"
# f"per {reading_distance} base pairs", loc="left")
# plt.ylabel("GC content in %")
# plt.xlabel(f"Amount of observations")
# plt.grid(color="green", linestyle="--", linewidth=0.75)
# plt.savefig(f"{file_name}")
# plt.show()


def main():
    # Files
    file1 = "lcl_NC_001549.1_prot_NP_054372.1_5.pim"
    file2 = "lcl_NC_004455.1_prot_NP_758892.1_7.pim"
    file3 = "lcl_NC_001722.1_prot_NP_056844.1_8.pim"
    file4 = "lcl_NC_001802.1_prot_NP_057856.1_8.pim"

    # Functions
    file_list = [file1, file2, file3, file4]
    file_reader(file1)
    file_reader(file2)
    file_reader(file3)
    file_reader(file4)
    # data_list_processor(data_list1)
    # histogram_prepare(1, 1)
    # histogram_data(data_list_processor)
    # graph_plotter(..., file_list, 10000)


main()
