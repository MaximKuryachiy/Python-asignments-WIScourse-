import argparse
import csv
import os
import pandas as pd
from Bio import Entrez

def search_and_download(term, max_items, email):
    Entrez.email = 'maximkuryachiy1998@gmail.com'

    search_handle = Entrez.esearch(db="nucleotide", term=term, retmax=max_items)
    search_results = Entrez.read(search_handle)
    search_handle.close()

    ids = search_results["IdList"]
    total_found = search_results["Count"]

    directory = f"{term}_files"
    os.makedirs(directory, exist_ok=True)

    file_names = []

    for idx in ids:
        fetch_handle = Entrez.efetch(db="nucleotide", id=idx, rettype="gb", retmode="text")
        data = fetch_handle.read()
        fetch_handle.close()

        file_name = os.path.join(directory, f"{idx}.gb")
        with open(file_name, "w") as file:
            file.write(data)
        
        file_names.append(file_name)

    print("Files downloaded:")
    for name in file_names:
        print(name)

    csv_file = "search_metadata.csv"
    fieldnames = ["Date", "Database", "Search Term", "Number Asked For", "Total Items Found"]

    file_exists = os.path.isfile(csv_file)

    with open(csv_file, "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "Date": pd.Timestamp.now(),
            "Database": "nucleotide",
            "Search Term": term,
            "Number Asked For": max_items,
            "Total Items Found": total_found
        })

    print(f"Metadata saved to {csv_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search and download items from GenBank.")
    parser.add_argument("term", type=str, help="Search term for GenBank.")
    parser.add_argument("max_items", type=int, help="Maximum number of items to download.")
    parser.add_argument("email", type=str, help="Email address for NCBI Entrez.")

    args = parser.parse_args()

    search_and_download(args.term, args.max_items, args.email)