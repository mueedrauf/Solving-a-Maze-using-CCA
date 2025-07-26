# 🧩 Solving a Maze using Connected Component Analysis (CCA)

<img src="https://img.shields.io/badge/OpenCV-4.x-blue" alt="OpenCV Version">
<img src="https://img.shields.io/badge/Python-3.8%2B-yellow">
<img src="https://img.shields.io/badge/Algorithm-CCA-brightgreen">

🚀 This project demonstrates how to analyze and solve a binary maze image using **Connected Component Analysis (CCA)**. The maze is scanned, labeled, colored, and finally checked for a valid path between the entry and exit using a simple yet effective labeling logic!

---

## 🧠 What is Connected Component Analysis?

Connected Component Analysis (CCA) is a classic image processing technique to identify **connected regions (blobs)** in a binary image. This is achieved by scanning the image pixel by pixel and grouping pixels with similar values that are connected to each other.

In our context, CCA helps:
- 🔍 Label all the paths in a maze.
- 🎨 Visually distinguish each connected region.
- ✅ Check if a path exists from the start to the end.

---

## 📸 Input

You must provide a **binary maze image** named `maze.png` in the working directory.

Example:

White → path (value ≈ 255)
Black → wall (value ≈ 0)

yaml
Copy
Edit

---

## 🛠️ How It Works

1. **📥 Load and Preprocess**
   - Loads the grayscale maze image.
   - Adds a border to avoid index errors.

2. **🧩 Labeling Algorithm**
   - Applies a connected component labeling algorithm with 4-connectivity.
   - Labels pixels from 1 onwards using neighbors (top and left).
   - Resolves label conflicts by assigning the minimum label.

3. **🎨 Color Mapping**
   - Converts labels into RGB colors for visualization.

4. **🧭 Path Detection**
   - Finds the first bright pixel on the top and bottom rows as entry and exit.
   - Checks if both belong to the same connected component.

5. **✅ Final Result**
   - Shows a green path if a valid path exists, otherwise displays only labels.

---

## 🧾 Output Summary

- 🖼️ `labeled_image` – All detected connected components (grayscale).
- 🎨 `labeled_colored_image` – Colorful display of unique paths.
- 🟢 `labeled_path_image` – Shows the valid path (if exists) in **green**.

---

## 🔍 Visual Workflow

maze.png ──▶ [ Grayscale Conversion ]
└─▶ [ CCA Labeling ]
└─▶ [ Label Coloring ]
└─▶ [ Entry-Exit Detection ]
└─▶ [ Final Path Display ✅ ]

yaml
Copy
Edit

---

## 💻 Installation & Usage

### 🔧 Requirements

```bash
pip install opencv-python numpy
▶️ Run the Code
bash
Copy
Edit
python maze_cca_solver.py
