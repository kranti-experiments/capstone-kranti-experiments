#Imports
from flask import Flask, render_template
from forms import CreateUserForm

def create_app():
    #Create a flask instance
    app = Flask('__name__')
    # Create Secret Key
    app.config['SECRET_KEY'] = "tsai"
    return app

# Create Flask Object
app = create_app()

#Rendering Home Page
@app.route('/', methods=['GET', 'POST'])
def homepage():
    '''
    This is the landing page
    local test: http://127.0.0.1:5000/
    permanent link: https://epai3-capstone-kranti.herokuapp.com/

    The page shows a placeholder to enter the user name.
    Upon clicking Test, it displays the entered name
    '''
    name = None
    form = CreateUserForm()

    #Validate Form
    if form.validate_on_submit():
        name = form.name.data
        if(not name.isupper()):
            name = name.capitalize()
        form.name.data = ''

    return render_template("user.html",
                           name = name,
                           form = form)

#Running the app
if __name__ == '__main__':
    # This will be useful for running the app locally
    app.run(debug=True)