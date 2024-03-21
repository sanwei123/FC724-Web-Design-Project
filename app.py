from flask import Flask, render_template, redirect, flash, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SubmitField

# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secrete-key'

# Define the form class using WTForms
class DataCollectionForm(FlaskForm):
    name = StringField('Name')
    student_number = StringField('Student Number')
    email = StringField('Email')
    grades = StringField('Average Grade')
    satisfaction = RadioField('Overall Satisfaction', choices=[('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5')])
    suggestions = TextAreaField('Improvement Suggestions')
    submit = SubmitField('Submit')

# Route for the home/welcome page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the information page
@app.route('/information')
def information():
    return render_template('info.html')

# Route for the data collection page
@app.route('/data-collection', methods=['GET', 'POST'])
def data_collection():
    form = DataCollectionForm()
    if form.validate_on_submit():
        # Process the valid form data and save to a file
        with open('data/responses.txt', 'a') as file:
            file.write(f'Name: {form.name.data}\n')
            file.write(f'Student Number: {form.student_number.data}\n')
            file.write(f'Email: {form.email.data}\n')
            file.write(f'Average Grade: {form.grades.data}\n')
            file.write(f'Satisfaction: {form.satisfaction.data}\n')
            file.write(f'Suggestions: {form.suggestions.data}\n')
            file.write('-----\n')

        flash('Data submitted successfully!', 'success')
        return redirect(url_for('data_collection'))  # Redirect to clear the form
    return render_template('form.html', form=form)

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)  # Turn off debug mode in production
