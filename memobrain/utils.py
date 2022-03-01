from pathlib import Path
import glob

def find_files(file_ext, cpath='.'):
    all_paths = []
    for file_path in Path(cpath).rglob(file_ext):
        all_paths.append(file_path)

    return all_paths
