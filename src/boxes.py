import cv2
import imutils
import numpy as np


def get_bounding_boxes(mask):
    """
    Compute bounding box position for each sprite.
    """
    cnts = cv2.findContours(
        mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    cnts = imutils.grab_contours(cnts)

    boxes = []
    for c in cnts:
        if cv2.contourArea(c) > 100:
            x, y, w, h = cv2.boundingRect(c)
            boxes.append([x, y, w, h])
    return boxes


def sort_boxes(boxes, rows):
    """
    Sort boxes according to position, and order them into rows.
    """
    # Global reverse sort on y
    boxes = sorted(boxes, key=lambda x: x[1], reverse=False)

    # Order in rows
    sorted_boxes = []
    count = 0
    for nb_sprites in rows:
        row = []
        for _ in range(nb_sprites):
            row.append(boxes[count])
            count += 1
        # Row sort on x
        row = sorted(row, key=lambda x: x[0])
        sorted_boxes.append(row)
    return sorted_boxes


def draw_boxes(boxes, image):
    """
    Draw bounding boxes on image, for debugging purposes.
    """
    new_img = image.copy()
    for box in boxes:
        x, y, w, h = box
        new_img = cv2.rectangle(
            new_img, (x, y), (x + w, y + h), (0, 255, 0), 2
        )
    cv2.imwrite("media/boxes.png", new_img)


def get_sprites(boxes, image):
    """
    Get each sprite accord to box position
    """
    sprites = []
    for row in boxes:
        new_row = []
        for b in row:
            x, y, w, h = b
            sprite = image[y : y + h, x : x + w]
            sprite = cv2.cvtColor(sprite, cv2.COLOR_BGR2RGB)
            new_row.append(sprite)
        sprites.append(new_row)
    return sprites
