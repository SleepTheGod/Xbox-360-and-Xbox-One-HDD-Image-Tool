import os
import sys
import argparse
import shutil

def extract_files(source_directory, destination_directory):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    for root, dirs, files in os.walk(source_directory):
        for file in files:
            source_file = os.path.join(root, file)
            relative_path = os.path.relpath(source_file, source_directory)
            destination_file = os.path.join(destination_directory, relative_path)
            destination_folder = os.path.dirname(destination_file)

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            shutil.copy2(source_file, destination_file)

    print("Extraction completed.")

def main():
    parser = argparse.ArgumentParser(description="Xbox Hard Drive File Extractor")
    parser.add_argument("source_directory", help="Source directory containing Xbox hard drive files")
    parser.add_argument("destination_directory", help="Destination directory to copy extracted files")
    args = parser.parse_args()

    extract_files(args.source_directory, args.destination_directory)

if __name__ == "__main__":
    main()
