import cv2
import numpy as np

from boxes import get_bounding_boxes, get_sprites, sort_boxes
from mask import get_mask


def main():
    print("Loading sheet and configuration...")
    sheet = cv2.imread("media/sheet.png")
    s = open("media/rows.txt", "r").read()[:-1]  # Remove newline
    rows = [int(n) for n in s.split(" ")]

    nb_rows = len(rows)
    nb_cols = max(rows)

    # Get sprite positions from mask
    print("Computing sprite positions...")
    mask = get_mask()
    boxes = get_bounding_boxes(mask)  # box is [x, y, w, h]

    # Sanity check
    print("Checking coherence of results...")
    assert len(boxes) == sum(rows)

    # Sort boxes
    print("Sorting and ordering sprite positions...")
    boxes = sort_boxes(boxes, rows)

    # Get sprites from initial sheet, using sorted boxes positions
    print("Extracting sprites...")
    sprites = get_sprites(boxes, sheet)

    # Save each sprite
    # for i in range(nb_rows):
    #     for j in range(rows[i]):
    #         cv2.imwrite(f"media/sprite_{i}{j}.png", sprites[i][j])

    # Get sprite max size
    print("Computing new sprite spacing...")
    sizes = []
    for r in sprites:
        for s in r:
            sizes.append(len(s))
            sizes.append(len(s[0]))
    sprite_size = int(max(sizes) * 1.5)

    # Create new sprite sheet
    print("Creating new sprite sheet...")
    new_sheet = np.zeros((nb_rows * sprite_size, nb_cols * sprite_size, 3))

    print("Copying sprites to new sheet...")
    # From bottom
    for i in range(nb_rows):
        for j in range(rows[i]):
            pos_i = i * sprite_size + sprite_size
            pos_j = j * sprite_size + sprite_size//2
            new_sheet[
                pos_i - sprites[i][j].shape[0]: pos_i,
                pos_j: pos_j + sprites[i][j].shape[1],
            ] = sprites[i][j].copy()

    print("Saving new sprite sheet...")
    cv2.imwrite("media/fixed_sheet.png", new_sheet)

    print("Making transparent background...")

    print("Done!")


if __name__ == "__main__":
    main()
