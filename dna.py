import sys
import csv
import itertools

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py FILENAME .txt")



    # Read data from csv file and add each team to the team list
    database = sys.argv[1]
    sequence = sys.argv[2]


    with open(database) as file:
        reader = csv.DictReader(file)
        # reads only the STRs from databases, 1st row without the name, we use method fieldnames and we select the fields from index 1 , not 0 to exclude the field name
        #STRs = reader.fieldnames[1:]
        people = list(reader)

    # Read from the sequence file and save it to memory
    with open(sequence, "r") as file:
        sequence = file.read()


    #compute the longest run of consequitive repeats for each of the STR in the sequence string
    max_counts =[]

    for i in range(1, len(reader.fieldnames)):
        STR = reader.fieldnames[i]
        max_counts.append(0)
    # Loop through the sequence to find STR
        for j in range(len(sequence)):
            STR_count = 0
            # If match found, start counting repetitions
            if sequence[ j: (j + len(STR))] == STR:
                k = 0
                while sequence[ (j + k) : (j + k + len(STR))] == STR:
                    STR_count += 1
                    k += len(STR)
                # If bigger maximum of repeats found, update max_counts
                if STR_count > max_counts[i - 1]:
                    max_counts[i - 1] = STR_count


    #Look for a match in the database
    for i in range(len(people)):
        matches = 0
        for j in range(1, len(reader.fieldnames)):
            if int(max_counts[j - 1]) == int(people[i]  [reader.fieldnames[j]]):
                matches += 1
            if matches == (len(reader.fieldnames) - 1):
                print(people[i]["name"])
                exit(0)
    print("No match")


if __name__ == "__main__":
    main()
