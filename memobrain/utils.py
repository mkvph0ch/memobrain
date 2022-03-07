from pathlib import Path
from PIL import Image
import glob

def find_files(file_ext, cpath='.'):
    '''find all files with {file_ext} in {cpath}
    file_ext: str
    cpath: str or path object
    return <list>
    '''
    all_paths = []
    for file_path in Path(cpath).rglob(f"*.{file_ext}"):
        all_paths.append(file_path)

    return all_paths

def convert_images(image_paths, file_ext='gif'):
    '''convert all images with suffix {file_ext} in {image_paths}
    image_paths: list (str or path objects)
    '''
    for image_path in image_paths:
        if image_path.suffix == f".{file_ext}":
            im = Image.open(image_path)
            im_jpg = image_path.parent.joinpath(f"{image_path.stem}.jpg")
            im.save(im_jpg)

    return None
