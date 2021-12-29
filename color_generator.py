# Web Dev with Flask, Image processing via Pillow, Numpy and Matplotlib

# Import Modules
# Flask - Generates the Website
from flask import Flask, render_template, request, flash
# Forms - Image forms + form validation
from forms import ImageForm
# Image handling and encoding
from color_finder import get_image, get_length, find_top_colors, reshape_colors
from base64 import b64encode
# Get Env variables
from dotenv import load_dotenv
from os import getenv

# Load Environment variables
load_dotenv()

# Configure App
app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')


# Configure routes
@app.route('/', methods=['GET', 'POST'])
def home():
    form = ImageForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Store in file for later use
            image_file = request.files.get('image')
            # Create URI for the image file
            encoded = b64encode(image_file.read()).decode('utf-8')
            mime = "image/jpeg"
            image_uri = f"data:{mime}; base64, {encoded}"
            # Get colors
            # Get ndarray from image file
            image_array = get_image(image_file)
            image_length = get_length(image_array)
            # Retrieve top 10 colors
            top_colors = find_top_colors(image_array)
            if top_colors is False:
                flash('Invalid Input!')
                return render_template('index.html', form=form)
            # Reshape the top 10 colors into dict of hexcodes
            top_colors = reshape_colors(top_colors, image_length)
            return render_template('result.html', image=image_uri, colors=top_colors)
        else:
            flash('Invalid input, please make sure that the image is jpg/png format')
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
