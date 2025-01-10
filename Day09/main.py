import argparse
import re

def file_opener(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read().strip()
        return file_content

def longest_duplicate(file_content):
    pattern_length = 1
    longest_subseq = ''
    
    while True:
        duplicate_pattern = f'(?=([ATCG]{{{pattern_length}}}).*?\\1)'
        match_list = list(re.finditer(duplicate_pattern, file_content))
        
        if not match_list:
            break
        
        longest_subseq = match_list[0].group(1)
        pattern_length += 1
    
    return longest_subseq

def count_methionine(file_content):
    # Methionine codon in DNA is "ATG"
    methionine_count = file_content.upper().count('ATG')
    return methionine_count

def main():
    parser = argparse.ArgumentParser(description="Analyze DNA sequence")
    parser.add_argument('path', type=str, help='The path to the file containing the DNA sequence')
    parser.add_argument('analysis', type=str, choices=['duplicates', 'methionine'], help='The type of analysis to perform')
    args = parser.parse_args()
    file_path = args.path
    analysis_type = args.analysis
    
    file_content = file_opener(file_path)
    
    if analysis_type == 'duplicates':
        longest_subseq = longest_duplicate(file_content)
        if longest_subseq:
            print("The longest repeating subsequence is:", longest_subseq)
        else:
            print("No repeating subsequence found.")
    elif analysis_type == 'methionine':
        methionine_count = count_methionine(file_content)
        print(f"The number of methionine (ATG) codons is: {methionine_count}")

if __name__ == '__main__':
    main()
