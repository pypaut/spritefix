import cv2
import matplotlib.pyplot as plt
import numpy as np

from boxes import get_bounding_boxes, draw_boxes, get_sprites, sort_boxes
from mask import get_mask
from parser import parse


def main():
    # Parse arguments
    args = parse()
    sheet = cv2.imread("media/sheet.png")
    rows = int(args.rows)
    cols = int(args.columns)

    # Load sheet configuration
    s = open("media/rows.txt", "r").read()[:-1]  # Remove newline
    rows = [int(n) for n in s.split(" ")]

    # Get sprite positions from mask
    mask = get_mask()
    boxes = get_bounding_boxes(mask)  # box is [x, y, w, h]

    # Draw boxes (debug)
    draw_boxes(boxes, sheet)

    # Sanity check
    assert len(boxes) == sum(rows)

    # Sort boxes
    boxes = sort_boxes(boxes, rows)

    # Get sprites from initial sheet, using sorted boxes positions
    sprites = get_sprites(boxes, sheet)

    # Get sprite max size
    sprite_size = max(
        [max(len(s), len(s[0])) for s in rows for rows in sprites]
    )

    # Create new sprite sheet
    new_sheet = np.array((rows * sprite_size, cols * sprite_size))
    i = 0
    j = 0
    for r in sprites:
        for s in r:
            pos_i = i * sprite_size
            pos_j = j * sprite_size
            new_sheet[
                pos_i : pos_i + s.shape[0], pos_j : pos_j + s.shape[1]
            ] = s.copy()
            i += 1
        j += 1
        i = 0

    plt.imshow(new_sheet)
    plt.show()


if __name__ == "__main__":
    main()
