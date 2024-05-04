"""
This script removes empty data from a folder structure.
"""

import argparse
import os


class DataRemover:
    """
    This class removes empty data from a folder structure.
    """

    def __init__(self, root_folder):
        self.root_folder = root_folder

    def remove_empty_data(self, labels_folder, images_folder):
        """
        Removes empty data from a folder structure.
        """
        initial_label_count = len([f for f in os.listdir(labels_folder) if f.endswith('.txt')])
        initial_image_count = len(
            [f for f in os.listdir(images_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])

        label_files = [f for f in os.listdir(labels_folder) if f.endswith('.txt')]

        for label_file in label_files:
            label_file_path = os.path.join(labels_folder, label_file)
            base_filename, _ = os.path.splitext(label_file)
            possible_image_extensions = [".jpg", ".jpeg", ".png"]

            image_file_path = None
            for ext in possible_image_extensions:
                possible_image_path = os.path.join(images_folder, f"{base_filename}{ext}")
                if os.path.exists(possible_image_path):
                    image_file_path = possible_image_path
                    break

            if (image_file_path and os.path.exists(label_file_path)
                    and os.path.getsize(label_file_path) == 0):
                print(f"Deleting {label_file_path} and {image_file_path}")
                os.remove(label_file_path)
                os.remove(image_file_path)

        final_label_count = len([f for f in os.listdir(labels_folder) if f.endswith('.txt')])
        final_image_count = len([f for f in os.listdir(images_folder)
                                 if f.lower().endswith(('.jpg', '.jpeg', '.png'))])

        print(f"Initial Label Count: {initial_label_count}")
        print(f"Final Label Count: {final_label_count}")
        print(f"Initial Image Count: {initial_image_count}")
        print(f"Final Image Count: {final_image_count}")

    def process_folders(self):
        """
        Processes all folders in the root folder.
        """
        for folder in os.listdir(self.root_folder):
            if (not folder.endswith('.yaml')) and (not folder.endswith('.txt')):
                folder_path = os.path.join(self.root_folder, folder)
                labels_folder = os.path.join(folder_path, 'labels')
                images_folder = os.path.join(folder_path, 'images')

                if os.path.exists(labels_folder) and os.path.exists(images_folder):
                    print(f"Processing folder: {folder_path}")
                    self.remove_empty_data(labels_folder, images_folder)
                    print("")


argparse = argparse.ArgumentParser()
argparse.add_argument("--input_path", type=str, required=True)
args = argparse.parse_args()

print(f"Root Folder Path: {args.input_path}")
input_path = args.input_path
data_remover = DataRemover(input_path)
data_remover.process_folders()
print("doe")