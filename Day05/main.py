import sys

def get_input():

    Total_A_counts = 0
    Total_G_counts = 0
    Total_C_counts = 0
    Total_T_counts = 0
    Total_X_counts = 0
    filenames = sys.argv[1:]
    for filename in filenames:

        try:
            print(filename)
            with open(filename, "r") as fh:
                text = fh.read()
            print(text)

            A_count = 0
            G_count = 0
            C_count = 0
            T_count = 0
            X_count = 0

            for letter in text:
                if letter == 'A':
                    A_count += 1
                if letter == 'G':
                    G_count += 1
                if letter == 'C':
                    C_count += 1
                if letter == 'T':
                    T_count += 1
                if letter == 'X':
                    X_count += 1
            print('A:','                   ', A_count, '    ' , (A_count/len(text))*100, '%')
            print('G:','                   ', G_count, '    ' , (G_count/len(text))*100, '%')
            print('C:','                   ', C_count, '    ' , (C_count/len(text))*100, '%')
            print('T:','                   ', T_count, '    ' , (T_count/len(text))*100, '%')
            print('Unknown nucleotide:   ', X_count,'    ' ,(X_count/len(text))*100, '%')
            print('Total: ', A_count+G_count+C_count+T_count+X_count)

            Total_A_counts += A_count
            Total_G_counts += G_count
            Total_C_counts += C_count
            Total_T_counts += T_count
            Total_X_counts += X_count

        except FileNotFoundError:
            exit(f"Error: File {filename} not found.")
        except IOError:
            exit(f"Error: An error occurred while reading the file {filename}.")
    Mega_Total_counts = Total_A_counts+Total_G_counts+Total_C_counts+Total_T_counts+Total_X_counts
    print('Total stats:')
    print('A','                    ', Total_A_counts,'      ', (Total_A_counts/Mega_Total_counts)*100, '%')
    print('G','                    ', Total_G_counts,'      ', (Total_G_counts/Mega_Total_counts)*100, '%')
    print('C','                    ', Total_C_counts,'      ', (Total_C_counts/Mega_Total_counts)*100, '%')
    print('T','                    ', Total_T_counts,'      ', (Total_T_counts/Mega_Total_counts)*100, '%')
    print('Unknown','              ', Total_X_counts,'      ', (Total_X_counts/Mega_Total_counts)*100)
    print('Total','                ', Mega_Total_counts)
    return [Total_A_counts, Total_G_counts, Total_C_counts, Total_T_counts, Total_X_counts]

if __name__ == "__main__":
    get_input()
