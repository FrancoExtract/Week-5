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


def main():
    codon_plotter()
    clustal_file_compiler()


main()
