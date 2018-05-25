import glob
from os import path

base_path = "data/track-accel2"


def get_images():
    return glob.glob(path.join(base_path, '*.jpg'))


def print_images():
    images = get_images()
    print(len(images))
    print(images)


if __name__ == "__main__":
    print_images()