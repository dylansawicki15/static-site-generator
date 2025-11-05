import os
import shutil

def delete_contents_of_directory(directory: str):
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory {directory} does not exist")
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
        else:
            os.remove(file_path)

def copy_directory_to_directory(source_directory: str, target_directory: str):
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"Directory {source_directory} does not exist")
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    delete_contents_of_directory(target_directory)
    for file in os.listdir(source_directory):
        if os.path.isdir(os.path.join(source_directory, file)):
            copy_directory_to_directory(os.path.join(source_directory, file), os.path.join(target_directory, file))
        else:
            shutil.copy(os.path.join(source_directory, file), os.path.join(target_directory, file))

if __name__ == "__main__":
    copy_directory_to_directory("static", "public")