from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Network share paths
image_folders = [
    '\\\\DESKTOP-CCBHJE3\\static',
    '\\\\DESKTOP-A804AU5\\static',
    "\\\\USER-PC\\static"

]

# Route to serve the images
@app.route('/<desktop>/static/<filename>')
def serve_image(desktop, filename):
    valid_folders = [f for f in image_folders if desktop.lower() in f.lower()]
    if valid_folders:
        folder_path = os.path.join(valid_folders[0], filename)
        return send_from_directory(os.path.dirname(folder_path), os.path.basename(folder_path))
    else:
        return "Image not found", 404

# Route to render the HTML page
@app.route('/')
def index():
    images = []
    for image_folder in image_folders:
        folder_name = os.path.dirname(image_folder).split("\\")[2]
        
        print("FOLDERNAME",folder_name)
        image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]
        images.extend([{'name': f[:-4], 'path': f'http://localhost:5001/{folder_name}/static/{f}'} for f in image_files])

    # Debug: Print the constructed image paths
    for image in images:
        print(f"Constructed Image Path: {image['path']}")

    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
