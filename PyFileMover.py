import shutil
from pathlib import Path

# Obtain the user's downloads folder in any operating system
download_folder = Path.home() / "Downloads"

# Specify the list of category folders
category_folders = {
    "Images": ["jpg", "jpeg", "png", "gif", "bmp", "tif", "tiff"],
    "Documents": ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt"],
    "Videos": ["mp4", "mkv", "avi", "mov"],
    "Music": ["mp3", "wav", "aac", "m4a"],
    "Others": ["exe", "zip", "rar", "7z", "tar", "gz", "sh", "deb"],
}

# Create the category folders in the downloads folder
for category in category_folders:
    (download_folder / category).mkdir(parents=True, exist_ok=True)


# Move files to the category folders
def move_files():
    for file_path in download_folder.iterdir():
        if file_path.is_file():
            file_ext = file_path.suffix.lower()[1:]
            # Determine the category of the file based on its extension
            category = next(
                (key for key, value in category_folders.items() if file_ext in value),
                "Others",
            )
            category_folder = download_folder / category
            try:
                # Move the file to its corresponding category folder
                shutil.move(str(file_path), str(category_folder))
            except Exception as e:
                # Handle any errors that occur during file movement
                print(f"Error moving '{file_path.name}' to '{category_folder}': {e}")


# Call the function to move files
move_files()
