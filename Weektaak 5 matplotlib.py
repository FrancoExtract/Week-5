import matplotlib.pyplot as plt


def file_reader(file):
    """
    This function reads the matrices in all files and returns the values in
    separate lists.

    :param file: percentages of matches between the sequences
    """

    with open(file) as data1:
        data_list1 = []  # List for the matrix data
        for line in data1:
            # isspace() returns TRUE if string is whitespace; FALSE if not.
            if "#" not in line and not line.isspace():
                line = line.rstrip().split()  # Strips space, splits in indices
                i = (line.index('100.00') + 1)  # Sees '100.00' as 1st index
                for unit in line[i:]:  # Loops through 1st 'til last index
                    # Appends values to the data list as floats
                    data_list1.append(float(unit))
        print(data_list1)

        return data_list1


def histogram_prepare(data_list1):
    """
    This function prepares a histogram for the curated data list to be
    passed through, and shows the data in separate bars.

    :param data_list1: sequence matches in the histogram
    """

    x = range(len(data_list1))  # Data list passes through "x" variable
    bin_ranges = [1, 50, 100, 150, 200, 250, 300, 350, 400, 404]

    plt.hist(x, bins=bin_ranges)  # Plots the x-axis gives range for the bars
    plt.title("Percentage matches per sequence")  # Title for the graph
    plt.xlabel("Sequence match")  # Title for the x-axis
    plt.ylabel("Percentage (%)")  # Title for the y-axis
    plt.ylim([0, 125])  # Viewing range 'til 125% for slightly easier reading
    plt.show()  # Makes the graph show up when running the code


# -----------------------------------------------------------------------------


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


def main(data_list1=None):
    # Files
    file1 = "lcl_NC_001549.1_prot_NP_054372.1_5.pim"
    file2 = "lcl_NC_004455.1_prot_NP_758892.1_7.pim"
    file3 = "lcl_NC_001722.1_prot_NP_056844.1_8.pim"
    file4 = "lcl_NC_001802.1_prot_NP_057856.1_8.pim"

    # Functions
    file_reader(file1)
    file_reader(file2)
    file_reader(file3)
    file_reader(file4)
    histogram_prepare(file_reader(data_list1))
    # graph_plotter(..., file_list, 10000)

    return data_list1


main()
