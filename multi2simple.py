import os
import sys
import getopt

from Bio import SeqIO


def main(argv):
    input_path = ''
    # path of execution
    output_path = os.path.dirname(os.path.abspath(__file__))
    file = ''

    # Get all arguments given
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["inputfile=", "outputfolder="])
    except getopt.GetoptError:
        print('multi2simple.py -i <inputfile> -o <outputfolder>')
        sys.exit(2)

    # Iteration over all arguments:
    for eachArg in sys.argv:
        print(eachArg)

    for opt, arg in opts:
        if opt == '-h':
            print('multi2simple.py -i <inputfile> -o <outputfolder>')
            sys.exit()
        elif opt in ("-i", "--inputfile"):
            if os.path.isabs(arg):
                file = os.path.basename(arg)
                input_path = os.path.dirname(arg)
            else:
                path = os.path.join(os.getcwd(), arg)
                file = os.path.basename(path)
                input_path = os.path.dirname(path)
        elif opt in ("-o", "--outputfolder"):
            if os.path.isabs(arg):
                output_path = arg
            else:
                output_path = os.path.join(os.getcwd(), arg)

    print('Fasta file: ' + file)
    for record in SeqIO.parse(os.path.join(input_path, file), "fasta"):
        SeqIO.write(record, os.path.join(output_path, record.description.replace(' ', '_') + '.fasta'), 'fasta')


if __name__ == "__main__":
    main(sys.argv[1:])
