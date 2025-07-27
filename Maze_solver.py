import numpy as np
import cv2 as cv


def in_v_set(val):  # User defined V set
    # Define which pixel values are considered part of the maze (bright pixels)
    v_set = [250, 251, 252, 253, 254, 255]
    return (val in v_set)


def CCA_4v(og_img):  # CCA algorithm using 4 connectivity
    # Add 1-pixel border around the image with value 0
    top, bottom, left, right = 1, 1, 1, 1
    img = cv.copyMakeBorder(og_img, top, bottom, left, right, cv.BORDER_CONSTANT, value=0)

    # Initialize output image (labels) with zeros
    out_img = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
    val = 0  # Starting label value
    row, col = img.shape  # Get dimensions of bordered image

    # Scan through each pixel (excluding borders)
    for i in range(1, row - 1):
        for j in range(1, col - 1):
            # Check if current pixel is part of the maze
            if in_v_set(img[i, j]):
                # Get neighboring pixel values and labels
                top = img[i - 1, j]
                left = img[i, j - 1]
                top_l = out_img[i - 1, j]
                left_l = out_img[i, j - 1]

                # Case 1: Neither top nor left neighbor is in V set
                if not in_v_set(top) and not in_v_set(left):
                    val = val + 1  # New component found
                    out_img[i, j] = val

                # Case 2: Both neighbors are in V set
                elif in_v_set(top) and in_v_set(left):
                    if (top_l == left_l):
                        out_img[i, j] = top_l  # Same label
                    else:
                        # Different labels - merge to the smaller one
                        out_img[i, j] = min(top_l, left_l)
                        # Update all pixels with the larger label
                        for x in range(row):
                            for y in range(col):
                                if out_img[x, y] == max(top_l, left_l):
                                    out_img[x, y] = min(top_l, left_l)

                # Case 3: Only left neighbor is in V set
                elif in_v_set(left) and not in_v_set(top):
                    out_img[i, j] = left_l  # Inherit left label

                # Case 4: Only top neighbor is in V set
                elif not in_v_set(left) and in_v_set(top):
                    out_img[i, j] = top_l  # Inherit top label
            else:
                # Pixel not in V set - background (label 0)
                out_img[i, j] = 0

    # Return unique labels, count of labels, and labeled image
    return np.unique(out_img), np.unique(out_img).size, out_img


def main():
    # Load input image as grayscale
    img_inp = cv.imread("maze.png", 0)
    if img_inp is None:
        print("Error: Could not load image 'maze.png'")
        return

    # Show original image
    cv.imshow('og_image', img_inp)
    cv.waitKey(0)

    # Perform connected component analysis
    unique_values, unique_count, out_img = CCA_4v(img_inp)
    row, col = out_img.shape

    # Create a color map for visualization
    label_color_map = {}
    np.random.seed(42)  # To ensure same colors every run (optional)

    # Assign colors to each label
    for label in unique_values:
        if label == 0:
            label_color_map[label] = np.array([255, 255, 255])  # White for background
        else:
            # Random color for each component
            color = np.random.randint(0, 256, size=3, dtype=np.uint8)
            label_color_map[label] = color

    # Create colored visualization image
    labeled_img = np.zeros((row, col, 3), dtype=np.uint8)
    for i in range(1, row - 1):
        for j in range(1, col - 1):
            label = out_img[i, j]
            labeled_img[i, j] = label_color_map[label]  # Assign color based on label

    # Show colored components image
    cv.imshow('labeled_colored_image', labeled_img)
    cv.waitKey(0)

    # Find entry and exit points
    start_col = -1
    end_col = -1

    # Find first bright pixel in first row (entry)
    for i in range(1, col - 1):
        if out_img[1, i] >= 1:
            start_col = i
            break

    # Find first bright pixel in last row (exit)
    for i in range(1, col - 1):
        if out_img[row - 2, i] >= 1:
            end_col = i
            break

    # Check if entry and exit were found
    if start_col == -1 or end_col == -1:
        print("Could not find entry or exit point.")
        return

    # Check if entry and exit have same label (connected)
    if out_img[1, start_col] == out_img[row - 2, end_col]:
        print("A path exists: Label", out_img[row - 2, end_col])
    else:
        print("No valid path found.")

    # Create final visualization showing only the path (if exists)
    final_img = np.zeros((row, col, 3), dtype=np.uint8)

    for i in range(1, row - 1):
        for j in range(1, col - 1):
            label = out_img[i, j]
            if label == 0:
                final_img[i, j] = np.array([255, 255, 255])  # white color
            elif label == out_img[row - 2, end_col]:
                final_img[i, j] = np.array([0, 255, 0])  # green color
            else:
                final_img[i, j] = np.array([0, 0, 0])  # black color

    # Show final path visualization
    cv.imshow('labeled_path_image', final_img)
    cv.waitKey(0)


if __name__ == '__main__':
    main()
    cv.destroyAllWindows()