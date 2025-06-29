import os
import shutil
from pathlib import Path

EXTENSION_MAP = {
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma'],
    'Compressed': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp'],
    'Video': ['.mp4', '.mkv', '.mov', '.avi', '.wmv', '.flv', '.webm'],
    'Programs': ['.exe', '.msi', '.bat', '.cmd'],
    'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.rtf']
}

OTHERS_FOLDER = 'Others'

def organize_downloads(download_path: Path):
    if not download_path.exists() or not download_path.is_dir():
        print(f"Error: {download_path!r} is not a valid directory.")
        return

    script_name = Path(__file__).name

    for folder in list(EXTENSION_MAP.keys()) + [OTHERS_FOLDER]:
        target = download_path / folder
        target.mkdir(exist_ok=True)

    for item in download_path.iterdir():
        if item.is_dir():
            continue
        if item.name == script_name:
            continue

        ext = item.suffix.lower()
        moved = False

        for folder, extensions in EXTENSION_MAP.items():
            if ext in extensions:
                dest = download_path / folder / item.name
                shutil.move(str(item), str(dest))
                print(f"Moved {item.name} to {folder}/")
                moved = True
                break

        if not moved:
            dest = download_path / OTHERS_FOLDER / item.name
            shutil.move(str(item), str(dest))
            print(f"Moved {item.name} to {OTHERS_FOLDER}/")

def main():
    user_profile = os.environ.get('USERPROFILE')
    if not user_profile:
        print("Error: Cannot determine USERPROFILE environment variable.")
        return

    downloads = Path(user_profile) / 'Downloads'
    print(f"Organizing files in: {downloads}")
    organize_downloads(downloads)

if __name__ == '__main__':
    main()
