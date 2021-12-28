import csv
import os


def suffixduplicatestrings(liststrings):
    dicts = {}
    for i in range(len(liststrings)):
        if liststrings[i] in dicts:
            dicts[liststrings[i]] += 1
            liststrings[i] = liststrings[i] + "_" + str(dicts[liststrings[i]])
        else:
            dicts[liststrings[i]] = 0
    return liststrings

def merge(inputFilesPath,outputFilesPath):
    #inputFilesPath = args.ifp
    #outputFilesPath = args.ofp + "/out.csv"
    print(os.listdir(inputFilesPath))
    inputs = os.listdir(inputFilesPath)
    # inputs = [f for f in os.listdir(inputFilesPath) if os.path.isfile(f)]
    print("inputs: -----------------")
    print(inputs)
    # First determine the field names from the top line of each input file
    # Comment 1 below
    fieldnames = []
    for filename in inputs:
        with open(inputFilesPath + "/" + filename, "r", newline="", encoding='utf8') as f_in:
            reader = csv.reader(f_in)
            headers = next(reader)
            headers = suffixduplicatestrings(headers)
            # print("headers: -----------------")
            # print(headers)
            for h in headers:
                if h not in fieldnames and not h.startswith('Log Work'):
                    fieldnames.append(h)
    print("fieldnames: -----------------")
    print(fieldnames)
    # Then copy the data
    with open(outputFilesPath, "w", newline="", encoding='utf8') as f_out:  # Comment 2 below
        writer = csv.DictWriter(f_out, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        for filename in inputs:
            with open(inputFilesPath + "/" + filename, "r", newline="", encoding='utf8') as f_in:
                reader = csv.DictReader(f_in)  # Uses the field names in this file
                reader.fieldnames = suffixduplicatestrings(reader.fieldnames)

                for line in reader:
                    writer.writerow(line)



