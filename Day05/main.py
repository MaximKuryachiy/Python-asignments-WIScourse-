import sys

def get_input():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} FILENAME")

    filename = sys.argv[1]

    try:
        with open(filename, "r") as fh:
            text = fh.read()
        print(text)
        print(type(text))

        A_count = 0
        #G_count = 0
        #C_count = 0
        #T_count = 0
        #X_count = 0

        for letter in text:
            if letter == 'A':
                A_count += 1
        print('A:','        ', A_count, str((A_count/len(text))*100), '%')
            #if letter == 'G':
                #G_count += 1
            #if letter == 'C':
                #C_count += 1
            #if letter == 'T':
                #T_count += 1
            #if letter == 'X':
                #X_count += 1
            
        return text
        
    except FileNotFoundError:
        exit(f"Error: File {filename} not found.")
    except IOError:
        exit(f"Error: An error occurred while reading the file {filename}.")

if __name__ == "__main__":
    get_input()
