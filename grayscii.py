# Grayscii by Will Cunningham
# A tool to convert images into ascii text using custom ascii palettes

from grid import BrightnessGrid
import argparse
from pathlib import Path
from PIL import Image


def convert_image(image: Image, size: tuple, palette: str) -> BrightnessGrid:
    """
    Converts an image into a BrightnessGrid object and returns that
    """

    # get the image in grayscale
    im = image.convert(mode="L")

    # if a size was given, resize
    if size is not None:
        im = im.resize(size)

    w, h = im.size
    grid = BrightnessGrid(w, h, '@', pal=palette)
    
    for x in range(w):
        for y in range(h):
            val = im.getpixel((x, y)) / 256
            grid.draw_point(x, y, val)

    return grid


if __name__ == "__main__":
    # set up command line argument parsing
    parser = argparse.ArgumentParser()

    parser.add_argument("image", type=Path, 
        help="""The path of the image file that you want to convert.""")

    parser.add_argument("-o", "--output", type=Path, default=None,
        help="""The .txt file you wish to create and write the output to. If not specified, the program will simply print the output to stdout.""")

    parser.add_argument("-x", "--width", type=int, default=None,
        help="""The width in characters the output ascii image should be. If specified, -y is also required.""")

    parser.add_argument("-y", "--height", type=int, default=None,
        help="""The height in characters the output ascii image should be. If specified, -x is also required.""")

    parser.add_argument("-p", "--palette", type=str, default=".oO0",
        help="""The ascii palette to render the converted image in. The first character corresponds to the lowest brightness value and the last character corresponds to the highest brightness value. For example, a palette string could be .oO0 or +=#@. Palettes cannot start with a minus sign, but can be any length over 0.""")

    args = parser.parse_args()

    # ensure file path was valid
    filepath = args.image
    assert filepath.exists(), f"Filepath {filepath} of the input file does not exist"

    # handle the image resizing argument parsing
    size = None
    if args.width is not None or args.height is not None:
        assert args.width is not None and args.height is not None, f"When specifying the size of the output, both -x and -y must be specified."
        size = (args.width, args.height)

    # ensure the palette was valid
    assert len(args.palette) > 0, f"The palette must be at least one character"

    # convert the image
    im = Image.open(filepath.as_posix())
    grid = convert_image(im, size, args.palette)
    print(grid)