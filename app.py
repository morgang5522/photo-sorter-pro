import os
import uuid
import re
from flask import Flask, render_template, request, send_from_directory

IMAGE_DIR = "images"
SETS_DIR = "sets"

os.makedirs(SETS_DIR, exist_ok=True)

app = Flask(__name__)

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]

@app.route("/")
def index():
    images = sorted([f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(("jpg","jpeg","png"))])
    if not images:
        return "<h1>All done!</h1><p>No more images to sort.</p>"

    image = images[0]
    upcoming_images = images[1:7] # Show next 6 images
    
    sets_data = []
    # Natural sort for alphabetical + numerical awareness
    raw_sets = [s for s in os.listdir(SETS_DIR) if os.path.isdir(os.path.join(SETS_DIR, s))]
    sorted_sets = sorted(raw_sets, key=natural_sort_key)

    for s in sorted_sets:
        set_path = os.path.join(SETS_DIR, s)
        files = sorted([f for f in os.listdir(set_path) if f.lower().endswith(("jpg","jpeg","png"))])
        sets_data.append({
            "name": s,
            "thumbnail": files[0] if files else None,
            "count": len(files)
        })

    return render_template("index.html", 
                                image=image, 
                                upcoming=upcoming_images,
                                sets=sets_data, 
                                remaining=len(images))

@app.route("/image/<path:name>")
def image(name):
    return send_from_directory(IMAGE_DIR, name)

@app.route("/set-image/<set_name>/<path:filename>")
def set_image(set_name, filename):
    return send_from_directory(os.path.join(SETS_DIR, set_name), filename)

@app.route("/assign", methods=["POST"])
def assign():
    data = request.json
    image_name = data["image"]
    set_name = data["set"]

    if not set_name:
        # Find existing "set_N" directories and find the next number
        existing_sets = [s for s in os.listdir(SETS_DIR) if os.path.isdir(os.path.join(SETS_DIR, s))]
        numbers = []
        for s in existing_sets:
            match = re.match(r'^set_(\d+)$', s)
            if match:
                numbers.append(int(match.group(1)))
        
        next_num = max(numbers) + 1 if numbers else 1
        set_name = f"set_{next_num}"

    set_path = os.path.join(SETS_DIR, set_name)
    os.makedirs(set_path, exist_ok=True)

    src = os.path.join(IMAGE_DIR, image_name)
    dst = os.path.join(set_path, image_name)
    
    if os.path.exists(src):
        os.rename(src, dst)

    return {"ok": True}

if __name__ == "__main__":
    app.run(debug=True, port=5050)


