import random
import sys
import pandas as pd
import matplotlib as plt


def clustal_file_compiler():
    file1 = "lcl_NC_001549.1_prot_NP_054372.1_5.pim"
    file2 = "lcl_NC_004455.1_prot_NP_758892.1_7.pim"
    file3 = "lcl_NC_001722.1_prot_NP_056844.1_8.pim"
    file4 = "lcl_NC_001802.1_prot_NP_057856.1_8.pim"


def codon_plotter():
    for element in codon_bias_list:
        df = pd.DataFrame(element)
        df.plot.bar()
        plt.title(file_name)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left',
                   borderaxespad=-3)
        f = plt.figure()
        f.set_figwidth(20)
        f.set_figheight(10)
        plt.show()


def graph_prepare(x, y):
    """
    This function prepares a graph.

    :param x: chromosome data on the x-axis
    :param y: exon data on the y-axis
    """

    plt.plot(x, y, 'g-')  # Plots out the axes and makes the line green
    plt.title("Total counts of exons per chromosome")  # Title for the graph
    plt.xlabel("Chromosome")  # Title for the x-axis
    plt.ylabel("Exon count")  # Title for the y-axis
    plt.show()  # Makes the graph show up when running the program


def main():
    clustal_file_compiler()
    codon_plotter()
    graph_prepare(1, 1)


main()
