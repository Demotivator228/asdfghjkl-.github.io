from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the command from the input field
        command = request.form['command']
        
        # Run the Jupyter Notebook file
        result = subprocess.check_output(['jupyter', 'nbconvert', '--to', 'html', 'my_neural_network.ipynb'])
        
        # Convert the result to a string and remove any unnecessary characters
        result = result.decode('utf-8').replace('\n', '').replace('\r', '')
        
        return render_template('index.html', result=result)
        
    # If a command has not been submitted, render the index template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
