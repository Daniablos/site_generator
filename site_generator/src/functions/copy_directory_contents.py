import os
import shutil

def copy_directory_contents(source_path: str, destination_path: str) -> None:
    """
    Копирует все содержимое (файлы и поддиректории) из исходной директории
    в целевую директорию.

    Перед копированием, если целевая директория существует, она и все ее
    содержимое полностью удаляются. Затем целевая директория создается заново,
    и в нее рекурсивно копируются все файлы и поддиректории из исходной
    директории.    
    """
    print(f"Cleaning destination directory: {destination_path}")
    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)
        print(f"Deleted existing contents of {destination_path}")

    os.makedirs(destination_path, exist_ok=True)
    print(f"Created destination directory: {destination_path}")
    
    print(f"Starting copy from '{source_path}' to '{destination_path}'")
    for dirpath, dirnames, filenames in os.walk(source_path):
        relative_path = os.path.relpath(dirpath, source_path)
        current_destination_dir = os.path.join(destination_path, relative_path)
        os.makedirs(current_destination_dir, exist_ok=True)
        for filename in filenames:
            source_file_path = os.path.join(dirpath, filename)
            destination_file_path = os.path.join(current_destination_dir, filename)
            print(f"  Copying file: {source_file_path} to {destination_file_path}")
            shutil.copy2(source_file_path, destination_file_path)
    print(f"Finished copying contents from '{source_path}' to '{destination_path}'")