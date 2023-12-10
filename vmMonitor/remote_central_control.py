from flask import Flask, render_template,jsonify
import os
from datetime import datetime,timedelta
app = Flask(__name__)

# Route to render the HTML page
@app.route('/')
def index():
    image_folder = 'static'
    
    # image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]
    # for f in image_files:
    #     creation_time = datetime.fromtimestamp(os.path.getctime(os.path.join(image_folder,f)))
    #     current_time = datetime.now()
    #     age = current_time - creation_time
    #     if age > timedelta(minutes=2):
    #         for i in range(10):
    #             try:
    #                 os.remove(os.path.join(image_folder,f))
    #             except:
    #                 pass
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]
    # image_files_final = []
    # for f in image_files:
    #     creation_time = datetime.fromtimestamp(os.path.getctime(os.path.join(image_folder,f)))
    #     current_time = datetime.now()
    #     age = current_time - creation_time
    #     print("pre")
    #     # if age < timedelta(minutes=2):
    #         print("appending")
    #         image_files_final.append(f)

    
    # Create a list of dictionaries containing image names and paths
    images = [{'name': f[:-4], 'path': os.path.join(image_folder, f)} for f in image_files]
    
    return render_template('index.html', images=images)




if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
