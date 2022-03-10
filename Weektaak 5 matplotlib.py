import matplotlib as plt


def file_reader(file1, file2, file3, file4):
    """
    This function reads each of the 4 NCBI files and splits them in a list.

    :param file1: file 054372.1_5 from NCBI
    :param file2: file 758892.1_7 from NCBI
    :param file3: file 056844.1_8 from NCBI
    :param file4: file 057856.1_8 from NCBI
    """

    with open(file1) as data1:
        Data_List1 = []
        for line in data1:
            List1 = line.strip().split("   ")
            Data_List1.append(List1)
        for row in Data_List1:
            print(row)


def graph_prepare(x, y):
    """
    This function prepares a graph.

    :param x: protein sequences on the x-axis
    :param y: match hits on the y-axis (in percentages)
    """

    plt.plot(x, y, 'g-')  # Plots out the axes and makes the line green
    plt.title("Total counts of exons per chromosome")  # Title for the graph
    plt.xlabel("Chromosome")  # Title for the x-axis
    plt.ylabel("Exon count")  # Title for the y-axis
    plt.show()  # Makes the graph show up when running the program


def graph_plotter(gc_list, file_name, reading_distance):
    # calculation = seq_len / reading_distance
    # print(f"the result of {seq_len} / {reading_distance} =\n {calculation}")
    y = gc_list
    x = range(len(gc_list))
    plt.scatter(x, y, 5, c=gc_list, cmap="Reds")
    plt.ylim([0, 100])
    plt.title(f"GC% of {file_name}\n"
              f"per {reading_distance} base pairs", loc="left")
    plt.ylabel("GC content in %")
    plt.xlabel(f"Amount of observations")
    plt.grid(color="green", linestyle="--", linewidth=0.75)
    # plt.savefig(f"{file_name}")
    plt.show()


def main():
    # Files
    file1 = "lcl_NC_001549.1_prot_NP_054372.1_5.pim"
    file2 = "lcl_NC_004455.1_prot_NP_758892.1_7.pim"
    file3 = "lcl_NC_001722.1_prot_NP_056844.1_8.pim"
    file4 = "lcl_NC_001802.1_prot_NP_057856.1_8.pim"

    # Functions
    file_list = [file1, file2, file3, file4]
    file_reader(file1, file2, file3, file4)
    # graph_prepare(1, 1)
    # graph_plotter(..., file_list, 10000, 150000)

    return file_list


main()
