import os
from tqdm import tqdm

# Can be converted to class structure in the future

def remove_empty_data (labels_folder, images_folder):
    initial_label_count = len([f for f in os.listdir(labels_folder) if f.endswith('.txt')])
    initial_image_count = len([f for f in os.listdir(images_folder) if
                               any(f.endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".bmp", ".gif", '.JPG', '.PNG', '.JPEG'])])

    label_files = [f for f in os.listdir(labels_folder) if f.endswith('.txt')]

    for label_file in label_files:
        label_file_path = os.path.join(labels_folder, label_file)
        base_filename, _ = os.path.splitext(label_file)
        possible_image_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif", '.JPG', '.PNG', '.JPEG']

        image_file_path = None
        for ext in possible_image_extensions:
            possible_image_path = os.path.join(images_folder, f"{base_filename}{ext}")
            if os.path.exists(possible_image_path):
                image_file_path = possible_image_path
                break

        if image_file_path and os.path.exists(label_file_path) and os.path.getsize(label_file_path) == 0:
            print(f"Deleting {label_file_path} and {image_file_path}")
            os.remove(label_file_path)
            os.remove(image_file_path)

    final_label_count = len([f for f in os.listdir(labels_folder) if f.endswith('.txt')])
    final_image_count = len([f for f in os.listdir(images_folder) if
                             any(f.endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".bmp", ".gif"])])

    print(f"Initial Label Count: {initial_label_count}")
    print(f"Final Label Count: {final_label_count}")
    print(f"Initial Image Count: {initial_image_count}")
    print(f"Final Image Count: {final_image_count}")


def process_folders(root_folder):
    for folder in os.listdir(root_folder):
        if (not folder.endswith('.yaml')) and (not folder.endswith('.txt')):
            folder_path = os.path.join(root_folder, folder)
            labels_folder = os.path.join(folder_path, 'labels')
            images_folder = os.path.join(folder_path, 'images')

            if os.path.exists(labels_folder) and os.path.exists(images_folder):
                print(f"Processing folder: {folder_path}")
                remove_empty_data(labels_folder, images_folder)
                print("")


def main():
    root_folder = r"your/folder/path" # your root folder path
    process_folders(root_folder)


if __name__ == "__main__":
    main()
