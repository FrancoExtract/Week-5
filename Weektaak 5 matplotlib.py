import math
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np


def file_reader(file):
    """
    This function reads the matrices in all files and returns the values in
    separate lists.

    :param file: percentages of matches between the sequences
    """

    with open(file) as data1:
        data_list1 = []  # List for the matrix data
        for line in data1:
            # isspace() returns TRUE if string is whitespace; FALSE if not
            if "#" not in line and not line.isspace():
                line = line.rstrip().split()  # Strips space, splits in indices
                i = (line.index('100.00') + 1)  # Sees '100.00' as 1st index
                for unit in line[i:]:  # Loops through 1st 'til last index
                    # Append values to the data list as floats
                    data_list1.append(float(unit))
        print(data_list1)

        return data_list1


# def read_result(file):
# file_list = []

# with open(file, "r") as f:
# lines = f.readlines()[6:]
# for line in lines:
# try:
# x = line.split("100.00   ")
# y = x[1].split("   ")
# y[-1] = y[-1].strip()
# for i in y:
# file_list.append(float(i))
# except IndexError:
# pass
# return file_list


def histogram_prepare(data_list1):
    """
    This function prepares a histogram for the curated data list to be
    passed through, and shows the data in separate bars.

    :param data_list1: data from the matrix with matches
    """

    x = range(len(data_list1))  # Data list passes through "x" variable
    # bin_ranges = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    bin_ranges = int(math.sqrt(len(data_list1)))  # Ranges for histogram bars

    plt.hist(x, bins=bin_ranges)  # Plots the x-axis gives range for the bars
    plt.title("Histogram of percentage matrix")  # Title for the graph
    plt.xlabel("Percentage identity")  # Title for the x-axis
    plt.ylabel("Alignment hits")  # Title for the y-axis
    plt.ylim([0, 20])  # Viewing range 'til 20% for slightly easier reading
    plt.show()  # Makes the graph show up when running the code

    # sb.distplot(data_list1, hist=False, kde=True,
    # kde_kws={'shade': True, 'linewidth': 1}, )
    # plt.title("Histogram of percentage matrix")
    # plt.xlabel("Percentage identity")
    # plt.ylabel("Alignment hits")
    # plt.ylim([0, 20])
    # plt.show()


def prototype_hist():
    x = np.random.normal(170, 10, 250)

    plt.hist(x)
    plt.show()


def main():
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
    histogram_prepare(file1)
    # prototype_hist()
    # read_result(file1)


main()
