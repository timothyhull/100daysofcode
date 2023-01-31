# :calendar: Days 86-87: 1/8/2023-1/31/2023

---

## Topics

:clipboard: Full-stack Web Apps Made Easy

---

## Resources

:star: [Episode 138 of the TalkPython podcast](https://talkpython.fm/episodes/show/138/anvil-all-web-all-python).

---

## Tasks

:white_check_mark: Watch video 22

:white_large_square: Watch videos 23-24

:white_large_square: Create a new Anvil website

:white_large_square: Listen to TalkPython podcast episode

---

## Notes

### :notebook: 1/7/23

- Watched video 22.
- Created Anvil project for practice application.

---

### :notebook: 1/8/23

- Started development of the `HomePage` **Form** to use as a layout template for remaining pages.

---

### :notebook: 1/9/23

- Redeveloped the `HomePage` **Form** to contain a title, navigation bar, and a blank **Content Panel** that will host other **Forms**.
- Created frameworks for the `HomeDetailsForm`, `AllDocsForm`, `AddDocsForm`, and `DocDetailsForm`.
    - The frameworks are based on a blank page and only contain a page headings at this time.
    - The frameworks do not have navigation and ;
- Created methods in the `HomeForm` **Form** to load other pages/frameworks:

```python
# From the HomeForm form
from ._anvil_designer import HomeFormTemplate
from anvil import *
from ..AddDocsForm import AddDocsForm
from ..AllDocsForm import AllDocsForm
from ..DocDetailsForm import DocDetailsForm
from ..HomeDetailsForm import HomeDetailsForm

class HomeForm(HomeFormTemplate):
def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    self.load_home_form()

def _clear_content_panel(self):
    """ Clear the main content panel. """
    self.content_panel.clear()

def load_home_form(self):
    """ Load HomeForm in the main content panel"""
    self._clear_content_panel()
    self.content_panel.add_component(HomeDetailsForm())

def load_add_docs_form(self):
    """ Load AddDocsForm in the main content panel"""
    self._clear_content_panel()
    self.content_panel.add_component(AddDocsForm())

def load_all_docs_form(self):
    """ Load AddDocsForm in the main content panel"""
    self._clear_content_panel()
    self.content_panel.add_component(AllDocsForm())

def load_doc_details_form(self):
    """ Load AddDocsForm in the main content panel"""
    self._clear_content_panel()
    self.content_panel.add_component(DocDetailsForm())

# Button click methods
def button_home_click(self, **event_args):
    """This method is called when the Home is clicked"""
    self.load_home_form()
    
def button_all_docs_click(self, **event_args):
    """This method is called when the all_docs button is clicked"""
    self.load_all_docs_form()

def button_doc_details_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.load_doc_details_form()

def button_add_doc_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.load_add_docs_form()
```

---

### :notebook: 1/10/23

- Started setup and testing of code that will change the color of the buttons in the `HomeForm` **Form** when navigating between different pages.
    - One button will be "active" and the others will be inactive.
    - A simple test showed the viability of the option:

```python
# Button click methods
    def button_home_click(self, **event_args):
        """This method is called when the Home is clicked"""
        self.load_home_form()
        self.button_home.foreground = ACTIVE_BUTTON_FG
        self.button_home.background = ACTIVE_BUTTON_BG
        self.button_all_docs.foreground = INACTIVE_BUTTON_FG
        self.button_all_docs.background = INACTIVE_BUTTON_BG    
        
    def button_all_docs_click(self, **event_args):
        """This method is called when the all_docs button is clicked"""
        self.load_all_docs_form()
        self.button_all_docs.foreground = ACTIVE_BUTTON_FG
        self.button_all_docs.background = ACTIVE_BUTTON_BG
        self.button_home.foreground = INACTIVE_BUTTON_FG
        self.button_home.background = INACTIVE_BUTTON_BG
```

---

### :notebook: 1/11/23

- Continued development of code that will change the color of the buttons in the `HomeForm` **Form** when navigating between different pages.
    - Moved code to the `client_utilities` module.
    - Unsuccessfully implemented the functions, because the `self` prefix for variable names in `client_utilities` has no meaning.
        - The functions are not contained within a class and the button objects are objects in the `HomeForm` **Form**.

---

### :notebook: 1/12/23

- Continued development of code that will change the color of the buttons in the `HomeForm` **Form** when navigating between different pages.
    - Achieved limited success by creating an `update_buttons` function in `client_utilities` and hard-setting button color values.
- Created a `home_form` object in `client_utilities` that has an instance of `HomeForm.HomeForm` assigned to it.
    - This allows any form that imports `client_utilities` to interact with object properties of the `HomeForm` form.
        - Including button colors.

---

### :notebook: 1/17/23

- Continued development of code that will change the color of the buttons in the `HomeForm` **Form** when navigating between different pages.
    - Tested passing string values of button object names to `client_utilities.update_buttons` to replace object names, which was unsuccessful.
    - Next step is to test passing button objects or mapped references to button objects themselves.

---

### :notebook: 1/18/23

- Continued development of code that will change the color of the buttons in the `HomeForm` **Form** when navigating between different pages.
    - Tested passing button objects (`self.button_home`) to `client_utilities.update_buttons` which produced inconsistent results.
    - Further testing required.

---

### :notebook: 1/19/23

- Identified solution to changing button colors.
    - Passing button objects (`self.button_home`) to `client_utilities.update_buttons` works correctly.
    - The missing piece to producing consistent results was changing the methodology for changing the light colors.
        - Changed instance object color assignment to `button.background == ACTIVE_BUTTON_FG` (from  `active_button.background`).
        -`button` refers to the instance of the `HomeForm` found in the `self.button_status` set.

        ```python
        # `HomeForm` form
        from ._anvil_designer import HomeFormTemplate
        from anvil import *
        from ..AddDocsForm import AddDocsForm
        from ..AllDocsForm import AllDocsForm
        from ..DocDetailsForm import DocDetailsForm
        from ..HomeDetailsForm import HomeDetailsForm
        from .. import client_utilities as cu


        class HomeForm(HomeFormTemplate):
        def __init__(self, **properties):
            # Set Form properties and Data Bindings.
            self.init_components(**properties)

            # Any code you write here will run before the form opens

            # Assign a 'HomeForm' instance to 'client_utilities.home_form'
            # Enables access to 'HomeForm' methods by other forms
            cu.home_form = self

            # Create a set object to declare button states
            self.button_status = {
                self.button_add_doc,
                self.button_all_docs,
                self.button_doc_details,
                self.button_home
            }

            # Load the home form
            self.load_home_form()

        def _clear_content_panel(self):
            """ Clear the main content panel. """
            self.content_panel.clear()

        # Form load action methods
        def load_home_form(self):
            """ Load HomeForm in the main content panel"""
            self._clear_content_panel()
            cu.update_buttons(active_button=self.button_home)
            self.content_panel.add_component(HomeDetailsForm())

        def load_add_docs_form(self):
            """ Load AddDocsForm in the main content panel"""
            self._clear_content_panel()
            cu.update_buttons(active_button=self.button_add_doc)
            self.content_panel.add_component(AddDocsForm())

        def load_all_docs_form(self):
            """ Load AddDocsForm in the main content panel"""
            self._clear_content_panel()
            cu.update_buttons(active_button=self.button_all_docs)
            self.content_panel.add_component(AllDocsForm())

        def load_doc_details_form(self):
            """ Load AddDocsForm in the main content panel"""
            self._clear_content_panel()
            cu.update_buttons(active_button=self.button_doc_details)
            self.content_panel.add_component(DocDetailsForm())

        # Button click action methods
        def button_home_click(self, **event_args):
            """This method is called when the Home is clicked"""
            self.load_home_form()

        def button_all_docs_click(self, **event_args):
            """This method is called when the all_docs button is clicked"""
            self.load_all_docs_form()

        def button_doc_details_click(self, **event_args):
            """This method is called when the button is clicked"""
            self.load_doc_details_form()

        def button_add_doc_click(self, **event_args):
            """This method is called when the button is clicked"""
            self.load_add_docs_form()

        ```

        ```python
        # 'client_utilities' form
        # Constants
        ACTIVE_BUTTON_FG = 'theme:Tertiary'
        ACTIVE_BUTTON_BG = 'theme:Tertiary Container'
        INACTIVE_BUTTON_FG = 'theme:Primary Container'
        INACTIVE_BUTTON_BG = 'theme:Primary'

        # Initialize the `home_form` variable
        # Value will be assigned by the __init__ method in the HomeForm class
        home_form = None  


        def go_home():
            """ Navigate to the homepage. """
            home_form.load_home_form()
            return None


        def update_buttons(active_button):
            """ Recolor buttons during page navigation.

                Args:
                    active_button: HomeForm.Button
                    Button object representing the active
                    navigation button.

                Returns:
                    None.
            """

            # Loop over the set of available buttons to find a match
            for button in home_form.button_status:
                # If a match is found, color the button using the 'active' scheme
                if button.text == active_button.text:
                    button.foreground = ACTIVE_BUTTON_FG
                    button.background = ACTIVE_BUTTON_BG
                # If no match is found, color the button using the 'inactive' scheme
                else:
                    button.foreground = INACTIVE_BUTTON_FG
                    button.background = INACTIVE_BUTTON_BG

            return None
        ```

---

### :notebook: 1/21/23

- Revised the `update_buttons` function in the `client_utilities` form.
    - Removed the mouseover/hover effect on the active button/page.
    - Add the mouseover/hover effect on the inactive buttons

        ```python
        def update_buttons(active_button):
            """ Recolor buttons during page navigation.

                Args:
                    active_button: HomeForm.Button
                    Button object representing the active
                    navigation button.

                Returns:
                    None.
            """

            # Loop over the set of available buttons to find a match
            for button in home_form.button_status:
                # If a match is found, color the button using the 'active' scheme
                if button.text == active_button.text:
                    button.foreground = ACTIVE_BUTTON_FG
                    button.background = ACTIVE_BUTTON_BG

                    # Disable mouseover/hover effect on button
                    button.role = None

                # If no match is found, color the button using the 'inactive' scheme
                else:
                    button.foreground = INACTIVE_BUTTON_FG
                    button.background = INACTIVE_BUTTON_BG

                    # Enable mouseover/hover effect on button
                    button.role = 'elevated-button'

            return None
        ```

---

### :notebook: 1/22/23

- Added labels, text inputs, and dropdowns to `HomeDetailsForm`, `DocDetailsForm`, and `AddDocsForm`.
    - Applied formatting and added hidden error messages to `AddDocsForm`.

---

### :notebook: 1/23/23

- Switched color schemes to _Mykonos Dark_.
- Added labels to `AllDocsForm`.
- Added hidden error message label to `DocDetailsForm` to use for document load/display errors.
- Created database tables **categories** and **docs**.
    - The _category_ column in the **docs** table is linked, by way of single row selection, to the _name_ column in the **categories** table.
- Added data validation to the `AddDocsForm`.

---

### :notebook: 1/24/23

- Created the **server** module `db_access` to request information from the database.
    - Created the `get_categories` function to retrieve and modify category data for consumption by **client** modules:

        ```python
        # Get document categories
        @anvil.server.callable
        def get_categories() -> List:
            """ Get a list of categories from the 'categories' DB table.

                Args:
                    None.

                Returns:
                    categories (List):
                    Alphabetical list of tuples that contain 
                    categories and descriptions, sorted by the 'name' column.
            """

            # Query the categories database
            category_rows = app_tables.categories.search()
            
            # Stage the categories and descriptions in a list of tuples
            categories = [
                (c['name'], c['description']) for c in category_rows
            ]

            # Sort the 'categories' list alphabetically, based on the '0' tuple index
            categories.sort(
                key=lambda x: x[0]
            )

            return categories
        ```

- Added code to `AddDocsForm` that calls the server module function `get_categories`:

    ```python
    class AddDocsForm(AddDocsFormTemplate):
        def __init__(self, **properties):
            # Set Form properties and Data Bindings.
            self.init_components(**properties)

            """ Begin relevant code """
            # Any code you write here will run before the form opens.
            self.categories = anvil.server.call('get_categories')
            """ End relevant code """
    ```

- Created a new method in the `AddDocsForm.AddDocsForm` that runs when the 'Category` dropdown appears on screen.
    - Created a new list, `categories` to host category names only.
    - Populated `a` with the `categories` list:

```python
def drop_down_doc_category_show(self, **event_args):
    """This method is called when the DropDown is shown on the screen"""
    # Create a list object to populate 'self.drop_down_doc_category.items'
    categories = [
        c[0] for c in self.categories
    ]

    # Populate the category drop down with categories from the DB
    self.drop_down_doc_category.items = categories
```

- Next step is to move the server-side database query to a persistent value in the `client_utilities` **client** module.
    - Limits unnecessary calls to the database.
    - Shares access of the DB query to all **client** modules.

---

### :notebook: 1/25/23

- Moved server-side database query for document categories in `AddDocsForm` to the `client_utilities` form:
    - Requires the categories to load from the database only one time, using the `client_utilities.get_categories` function.
    - Uses the line `cu.get_categories()` in the `__init__` method of `HomeForm.HomeForm` to run to cache the category data.
- Next step is to setup `AddDocsForm` to add new document entries into the DB.

---

### :notebook: 1/26/23

- Added the `add_document` function to the `db_access` server module.
    - Intended to add a document to the database, for now the result of the function prints all user input.

        ```python
        @anvil.server.callable
        def add_document(
            title: str,
            category: str,
            content: str,
            created: datetime = datetime.now(),
            views: int = 0
        ) -> None:
            """ Add new documents to the database.

                Args:
                    title (str):
                        Document title.

                    category (str):
                        Document category, selected by dropdown menu populated by the 'categories' table

                    content (str):
                        Document contents.

                    views (int):
                        Number of total document views.

                    created (datetime.datetime.now()):
                        Insert a timestamp for the creation instant of a document.

                Returns:
                    None.
            """

            print(
                f'Added "{title}" in the "{category}" category.\n'
                f'Added at {created}.'
            )

            return None
        ```

- Refactored the `AddDocsForm._validate_input` method in the `AddDocsForm` form.
    - Added the `dict` object `valid_input` to track the validity of each form element.
        - The database insert operation is only called when `False` is not present in `valid_input`.

            ```python
            def _validate_input(self) -> List:
                """ Validate data entry.

                    Displays error messages for invalid inputs.

                    Args:
                        None.

                    Returns:
                        valid_input (List):
                            List object of dict_values.
                """
                # Create a dictionary object to track validity state of each form element
                valid_input = dict(
                    title=False,
                    category=False,
                    contents=False
                )

                # Title input and validation
                if self.text_box_doc_title.text == '':
                    self.label_doc_title_error.visible = True
                    valid_input.update({'title': False})
                else:
                    self.label_doc_title_error.visible = False
                    valid_input.update({'title': True})

                # Category input and validation
                if self.drop_down_doc_category.selected_value is None:
                    self.label_doc_category_error.visible = True
                    valid_input.update({'category': False})
                else:
                    self.label_doc_category_error.visible = False
                    valid_input.update({'category': True})

                # Contents input and validation
                if self.text_area_doc_contents.text == '':
                    self.label_doc_contents_error.visible = True
                    valid_input.update({'contents': False})
                else:
                    self.label_doc_contents_error.visible = False
                    valid_input.update({'contents': True})

                return valid_input.values()
            
            def drop_down_doc_category_show(self, **event_args):
                """This method is called when the DropDown is shown on the screen"""
                # Apply a list of values to populate 'self.drop_down_doc_category.items'
                self.drop_down_doc_category.items = cu.categories
            
            def outlined_button_add_doc_click(self, **event_args):
                """This method is called when the button is clicked"""
                # Data input validation
                valid_input = self._validate_input()

                # Add the document to the database only if entries are valid
                if False not in valid_input:
                    anvil.server.call(
                        'add_document',
                        title=self.text_box_doc_title.text,
                        category=self.drop_down_doc_category.selected_value,
                        content=self.text_area_doc_contents.text
                 )
            ```

- Next step is to insert docs into the database.

---

### :notebook: 1/27/23

- Wrote server module code to insert a new document into the database from the `AddDocsForm` form.
    - This implementation is a bit clunky and would benefit from refactoring.
        - Figure out a cleaner way to reference a row from the `categories` table when populating the `category` field in the `documents` table.

        ```python
        @anvil.server.callable
        def add_document(
            title: str,
            category: str,
            content: str,
            created: datetime = datetime.now(),
            views: int = 0
        ) -> None:
            """ Add new documents to the database.

                Args:
                    title (str):
                        Document title.

                    category (anvil._server.LiveObjectProxy):
                        Document category, selected by dropdown menu populated by the
                        'categories' table.

                    content (str):
                        Document contents.

                    views (int):
                        Number of total document views.

                    created (datetime.datetime.now()):
                        Insert a timestamp for the creation instant of a document.

                Returns:
                    None.
            """

            print(
                f'Added "{title}" in the "{category}" category.\n'
                f'Added at {created}.'
            )

        # Insert a document into the database
        category_row = app_tables.categories.get(name=category) or None
        app_tables.docs.add_row(
            title=title,
            category=category_row
            content=content,
            views=views,
            created=created
        )
        
        return None
        ```

---

### :notebook: 1/30/23

- Added a call to `client_utilities.go_home` (aliased as `cu.go_home`) to the `outlined_button_add_doc_click` method in the `AddDocForm` form.
    - Redirects clients to the `HomeDetailsForm` form after adding a document into the database.

        ```python
        def outlined_button_add_doc_click(self, **event_args):
            """This method is called when the button is clicked"""
            # Data input validation
            valid_input = self._validate_input()

            # Add the document to the database only if entries are valid
            if False not in valid_input:
                anvil.server.call(
                'add_document',
                title=self.text_box_doc_title.text,
                category=self.drop_down_doc_category.selected_value,
                content=self.text_area_doc_contents.text
            )

                # Return to the home page
                cu.go_home()
        ```

- Worked through using a **Repeating Panel** component to display document names in `HomeDetailsForm`.
    - Creating a **Repeating Panel** also creates a reusable, across other forms, formatting template.
    - Displaying results required the addition of the following line of code in the `HomeDetailsForm.HomeDetailsForm.__init__` method:
        - `self.repeating_panel_docs.items = anvil.server.call('get_docs')`

            ```python
            class HomeDetailsForm(HomeDetailsFormTemplate):
            def __init__(self, **properties):
                # Set Form properties and Data Bindings.
                self.init_components(**properties)

                # Any code you write here will run before the form opens.
                self.repeating_panel_docs.items = anvil.server.call('get_docs')
            ```

        - After including this line I was able to specify a **Data Binding** for `self.label_doc_title` in the `DocsDisplayTemplate`, and display a list of document titles.
