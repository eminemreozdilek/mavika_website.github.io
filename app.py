from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for the About page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the Gallery page
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# Route for the Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
