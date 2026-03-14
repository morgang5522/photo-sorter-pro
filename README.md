# Photo Sorter Pro

A fast, keyboard-friendly web application for quickly sorting through a large number of images and organizing them into sets. This entire application is AI generated.

## Features

- **Fast & Responsive UI**: Built with a dark mode interface and smooth animations.
- **Keyboard Shortcuts**: Press `n` to quickly create a new set without using the mouse.
- **Upcoming Previews**: See what images are coming up next so you can plan your sets.
- **Visual Sets**: The sidebar automatically uses the first image assigned as a thumbnail for easy visual identification.
- **Natural Sorting**: Set names are sorted naturally (e.g., `set_1`, `set_2`, `set_10`).

## Getting Started

### Prerequisites

- Python 3.8+

### Installation & Setup

1. **Clone or download this repository**
   Make sure you are in the project folder containing `app.py`.

2. **Set up a Python Virtual Environment**
   It's highly recommended to run this within a virtual environment to avoid conflicts.

   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
   - On **Windows**:
     ```bash
     venv\\Scripts\\activate
     ```

4. **Install Dependencies**
   Install Flask inside the activated environment:

   ```bash
   pip install flask
   ```

5. **Prepare Your Images**
   Place the images you want to sort inside the `images` folder (create the folder if it doesn't exist).
   ```bash
   mkdir images
   # Copy your .jpg, .jpeg, or .png files into the images folder
   ```

### Running the App

1. Make sure your virtual environment is activated.
2. Run the Flask development server:
   ```bash
   python3 app.py
   ```
3. Open your web browser and go to: [http://127.0.0.1:5050](http://127.0.0.1:5050)

### How to Use

1. The main image to be sorted is displayed prominently.
2. Below it, you'll see a preview of the next 6 images in your queue.
3. Click **"+ Create New Set"** or press the **`n`** key to create a new folder.
4. Provide an optional name for the set (or leave blank to auto-generate one).
5. The image is instantly moved into that set's folder inside the `sets/` directory, and the next image loads automatically.
6. To assign subsequent images to an existing set, simply click that set's card in the right sidebar.
