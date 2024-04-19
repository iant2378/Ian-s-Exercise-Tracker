from flask import Flask, render_template, request

app = Flask(__name__)

# Initial calorie count
calories = 0

@app.route('/')
def home():
    return render_template('index.html', calories=calories)

@app.route('/add_calories', methods=['POST'])
def add_calories():
    global calories
    # Get the number of calories from the form
    calories_to_add = int(request.form['calories'])
    # Add the calories to the total count
    calories += calories_to_add
    # Redirect back to the home page
    return home()

@app.route('/reset_calories', methods=['POST'])
def reset_calories():
    global calories
    # Reset the calorie count to zero
    calories = 0
    # Redirect back to the home page
    return home()

if __name__ == '__main__':
    app.run(debug=True)
