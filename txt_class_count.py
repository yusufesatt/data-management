"""
    This project reads the txt files in the specified folder
    and calculates how many annotations there are for each class.
"""
import argparse
import os
from collections import defaultdict


def txt_folders_class_count(path):
    """
    This function reads the txt files in the specified folder
    and calculates how many annotations there are for each class.

    Args:
        path (str) : Path to the folder where the txt files are located.

    Returns:
        A dictionary of how many annotations there are for each class
    """

    class_annotation_numbers = defaultdict(int)

    for class_folder in os.listdir(path):
        class_folder_path = os.path.join(path, class_folder)

        if os.path.isdir(class_folder_path):
            for file in os.listdir(class_folder_path):
                if file.endswith('.txt'):
                    annotation_file_path = os.path.join(class_folder_path, file)
                    with open(annotation_file_path, 'r', encoding='utf-8') as read_file:
                        labels = read_file.readlines()
                        for annotation in labels:
                            class_id = annotation.strip().split()[0]
                            class_annotation_numbers[class_id] += 1

    for class_id, annotation_number in class_annotation_numbers.items():
        print(f"Category ID: {class_id} Number of Annotations: {annotation_number}")

    total_annotation = sum(class_annotation_numbers.values())
    print(f"Total number of annotations: {total_annotation}")


parser = argparse.ArgumentParser(description='Txt folders class count')
parser.add_argument('--input_path', type=str, help='Txt folders path', required=True)
args = parser.parse_args()

input_path = args.input_path
txt_folders_class_count(input_path)
