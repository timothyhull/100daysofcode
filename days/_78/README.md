,# :calendar: Day 78: 6/19/2022

---

## Topics

:clipboard: Getting Started with Python Flask

---

## Resources

:star: [How to Create a Basic Form in Python Flask](https://python.plainenglish.io/how-to-create-a-basic-form-in-python-flask-af966ee493fa)

:star: [Flask `Request` object](https://flask.palletsprojects.com/en/2.1.x/api/#flask.Request)

---

## Tasks

:white_check_mark: Choose application to create in Flask - building a basic Flask form

:white_check_mark: Write a simple, static Flask app

:white_check_mark: Write application

---

## Notes

### :notebook: 6/19/22

- Decided to build a basic Flask application that includes a form.

- Created a simple, static Flask application with two files:
    - Main application: [_76/flask_app/app.py](https://github.com/timothyhull/100daysofcode/blob/main/days/_76/flask_app/app.py)
    - Default template: [_78/flask_app/templates/index.html](https://github.com/timothyhull/100daysofcode/blob/main/days/_78/flask_app/templates/index.html).

- Created a simple Flask form input application that displays user form input for their first name.

### :notebook: 6/20/22

- Explored the Flask `Request` object, which contains data from the HTTP client request:
    - `request.form` contains a `dict` object of form data.
        - Each key in `request.form` represents a named field from the HTML form.
        - In this example, `request.form.name` provides the value of the **first_name** form field:

            ```html
            <form method="post">
                First Name: <input name="first_name" />
                <button type="submit">Submit</button>
            </form>
            ```

    - `str(request.headers)` displays all headers.
    - `request.query_string` displays everything in the URL string after the `?` character.

- Completed simple web app.
