# :calendar: Day 76+77: 6/14/2022-6/17/2022

---

## Topics

:clipboard: Getting Started with Python Flask

---

## Resources

:star: [Flask on PyPI](https://pypi.org/project/Flask)

:star: [Flask documentation](https://flask.palletsprojects.com/en/2.1.x)

:star: [Jinja2 documentation](https://jinja.palletsprojects.com/en/3.1.x)

---

## Tasks

:white_check_mark: Watch videos 1-4

:white_large_square: Watch videos 5-6

---

## Notes

### :notebook: 6/14/22

- Cleaned-up and organized files from previous lesson.
- Staged files for new lesson.

---

### :notebook: 6/15/22

- Watched videos 1-4
- Setup test application environment files:
    - \[days/_76/flask_app/app.py](https://github.com/timothyhull/100daysofcode/blob/main/days/_76/flask_app/app.py): Main Flask application.
    - \[days/_76/flask_app/data.py](https://github.com/timothyhull/100daysofcode/blob/main/days/_76/flask_app/data.py): Mock database for Flask application.
    - \[days/_76/flask_app/templates/index.html](https://github.com/timothyhull/100daysofcode/blob/main/days/_76/flask_app/templates/index.html): Jinja2 templated Flask application HTML file.

- Installed Flask from PyPI with `pip install flask`.
    - Requires and automatically installs `Jinja2`.

- Started Flask application setup in \[days/_76/flask_app/app.py](https://github.com/timothyhull/100daysofcode/blob/main/days/_76/flask_app/app.py):

    ```python
    # Import the Flask class to create the web application
    from flask import Flask

    # Import render_template to create HTML files using Jinja2
    from flask import render_template

    # Create a Flask application object for this file
    app = Flask(__name__)

    # Create a function for a default/root web application route
    @app.route
    def index():

        # Return HTML text to render as a web page
        return render_template('index.html')

    if __name__ == '__main__':
        # Run the Flask app
        app.run(
            host='localhost',
            port=5000,
            debug=True
        )
    ```

    - Successfully tested the Flask app by navigating to [http://127.0.0.1:5000](http://127.0.0.1:5000).
        - Added port forwarding for TCP 5000 to [.devcontainer/devcontainer.json](https://github.com/timothyhull/100daysofcode/blob/main/.devcontainer/devcontainer.json).

---

### :notebook: 6/16/22

- Watched part of video 5.
- Added a simple data structure (dictionary) to \[days/_76/flask_app/data.py](https://github.com/timothyhull/100daysofcode/blob/main/days/_76/flask_app/data.py).
- Imported the data structure (`favorite_pizzas`) into \[days/_76/flask_app/app.py](https://github.com/timothyhull/100daysofcode/blob/main/days/_76/flask_app/app.py):

    ```python
    from _76.flask_app.data import favorite_pizzas
    ```

- Added the `favorite_pizzas` dictionary to the `render_template` function, to pass it to the Jinja2 template:

    ```python
    app.render_template(
        # Template name
        'index.html',
        # Python variable name assigned to the Jinja2 template reference name
        # It is common for kwarg name and value to be the same things
        favorite_pizzas=favorite_pizzas
    )
    ```

---

### :notebook: 6/17/22

- Watched remainder of video 5.
- Added Jinja2 syntax to the \[days/_76/flask_app/templates/index.html](https://github.com/timothyhull/100daysofcode/blob/main/days/_76/flask_app/templates/index.html) template that displays the values in the `favorite_pizzas` dictionary.

- Watched video 6.
