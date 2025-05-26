import os
import shutil
import logging

# Configure logging
logging.basicConfig(filename="file_organizer.log", level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def organize_files(source_dir):
    """Organizes files in a directory based on their extensions."""

    try:
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")

        files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

        if not files:
            print(f"No files to organize in '{source_dir}'.")  # More informative message
            return

        for filename in files:
            file_path = os.path.join(source_dir, filename)
            name, ext = os.path.splitext(filename)
            ext = ext.lstrip(".").lower()

            if not ext:
                print(f"Skipping file without extension: '{filename}'") # More informative message
                continue

            target_dir = os.path.join(source_dir, ext)
            os.makedirs(target_dir, exist_ok=True)

            target_path = os.path.join(target_dir, filename)

            if os.path.exists(target_path):
                counter = 1
                while os.path.exists(os.path.join(target_dir, f"{name} ({counter}){ext}")):
                    counter += 1
                target_filename = f"{name} ({counter}){ext}" # store the new file name
                target_path = os.path.join(target_dir, target_filename)
                shutil.move(file_path, target_path)
                print(f"Moved '{filename}' to '{target_dir}' (renamed to '{target_filename}' to avoid overwrite)")
            else:
                shutil.move(file_path, target_path)
                print(f"Moved '{filename}' to '{target_dir}'")

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        logging.exception("An unexpected error occurred:")  # Log the full traceback
        print("An unexpected error occurred. Check the log file for details.")


if __name__ == "__main__":
    source_directory = input("Enter the directory to organize (or drag and drop the folder): ").strip('"')
    organize_files(source_directory)
    print("File organization complete.")