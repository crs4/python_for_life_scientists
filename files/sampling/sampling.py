import argparse
import random
import sys


def make_parser():
    parser = argparse.ArgumentParser(description='Randomly sampling a FASTQ file')
    parser.add_argument("input", help="input FASTQ filename")
    parser.add_argument("output", help="output FASTQ filename")
    parser.add_argument("-n", "--number", type=int, help="number of reads to sample")
    parser.add_argument("-p", "--percentage", type=int, help="percentage of reads to sample")
    parser.add_argument("-r", "--replicates", type=int, help="number of output files to write", default=1)

    return parser


def count_records(filename, record_length=4):
    print("counting records....")
    with open(filename) as input:
        num_lines = sum([1 for line in input])
    total_records = int(num_lines / record_length)
    return total_records
    
    
def main():
    parser = make_parser()
    args = parser.parse_args()
    
    if args.percentage and args.number:
       sys.exit("give either a percentage or a number of reads to sample, not both")

    if not args.percentage and not args.number:
       sys.exit("you must give either a percentage or a number of reads to sample")

    total_records = count_records(args.input)
    records_to_sample = args.number if args.number else (total_records * args.percentage) // 100
    number_of_replicates = args.replicates

    input_filename = args.input
    output_filename = args.output
       
    print("sampling {} out of {} records, replicated {} times".format(records_to_sample, total_records, number_of_replicates))

    outputs = []

    for i in range(number_of_replicates):
        outputs.append([open("{}_{}".format(i, output_filename), "w"), 
                        random.sample(range(total_records), records_to_sample)]
                       )
   
    record_number = 0
    with open(input_filename) as input:
        for line1 in input:
            line2 = input.readline()
            line3 = input.readline()
            line4 = input.readline()
            for output, keep in outputs:
                if record_number in keep:
                    output.writelines([line1, line2, line3, line4])    
            record_number += 1
            if record_number % ((total_records * 10) / 100) == 0:
                print("{} % done".format((record_number / total_records) * 100))

    for output, keep in outputs:
        output.close()

    print("All done!")


if __name__ == '__main__':
    # execute only if run as a script
    main()
