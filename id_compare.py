import sys, getopt, os, pandas as pd, csv

def main(argv):
    file1 = './' + argv[0]
    file2 = './' + argv[1]

    print ('File 1:' + file1)
    print ('File 2:' + file2)

    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    df1_ids = set(df1.values.flatten())
    df2_ids = set(df2.values.flatten())

    missing_in_file2 = []
    for i in df1_ids:
        print('Checking' + ' ' + str(i))
        if i not in df2_ids:
            print('Missing' + ' ' + str(i))
            missing_in_file2.append(str(i))

    textfile = open("in_file1_not_in_file2.csv", "w")
    
    for element in missing_in_file2:
        textfile.write(element + '\n')
    textfile.close()

if __name__ == '__main__':
    main(sys.argv[1:])