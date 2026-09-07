import os
import shutil

def organize_jpg_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created folder: {destination_folder}")

    files = os.listdir(source_folder)
    moved_count = 0

    for file in files:
        if file.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)

            shutil.move(source_path, destination_path)
            print(f"Moved: {file}")
            moved_count += 1

    if moved_count == 0:
        print("No .jpg files found in the source folder.")
    else:
        print(f"\nDone! Moved {moved_count} .jpg file(s).")

source = input("Enter the source folder path: ")
destination = input("Enter the destination folder path: ")

organize_jpg_files(source, destination)