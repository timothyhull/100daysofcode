# :calendar: Day 85: 12/18/2022-1/7/2023

---

## Topics

:clipboard: Full-stack Web Apps Made Easy

---

## Resources

:star: [Anvil Home Page](https://anvil.works/?anvil_attrib=talk-python-100-days)

---

## Tasks

:white_check_mark: Watch videos 1-5

:white_check_mark: Watch videos 6-9

:white_check_mark: Watch video 10

:white_check_mark: Watch video 11

:white_check_mark: Watch videos 12-13

:white_check_mark: Watch video 14

:white_check_mark: Watch video 15

:white_check_mark: Watch video 16

:white_check_mark: Watch video 17

:white_check_mark: Watch video 18

:white_check_mark: Watch video 19

:white_check_mark: Watch videos 20-22

:white_check_mark: Watch video 23

---

## Notes

### :notebook: 12/18/22

- Watched videos 1-5.
- Reviewed Anvil building blocks.
    - Anvil is a SaaS tool that allows developers to create full-stack web applications, exclusively using Python.

- Anvil building blocks:
    - **Forms**: HTML forms setup in a visual design tool that can include Python.
        - Python runs in the _client_ browser, after the server converts the code to Javascript.
    - **Client Modules**: Arbitrary Python that can interact with **Forms**.
        - Python that runs in the _client_ browser, after the server converts the code to Javascript.
    - **Server Modules**: Python code that runs on a web server.
    - **Data Tables**: Integrated access to data that supports a web application (database access).
    - **Services**:
        - Users (user management)
        - Secrets (secrets management)
        - Google API
        - Facebook API
        - Stripe (payments)
        - Uplink: (outbound webhooks, different from the `uplink` Python module)

---

### :notebook: 12/20/22

- Watched videos 6-9.
- Started initial Anvil project:
    - Created an **anvil.works** account.
    - Created a new app (**pypoint-100days**).
    - Added new forms with titles using the GUI.
    - Created links to load pages using the Python code interpreter:

```python
from ._anvil_designer import HomeFormTemplate
from anvil import *

# Form imports
from ..AddDocForm import AddDocForm
from ..AllDocsForm import AllDocsForm
from ..DocDetailsForm import DocDetailsForm
from ..HomeDetailsForm import HomeDetailsForm

class HomeForm(HomeFormTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        self.link_home_click()

    def _clear_content(self):
        """ Method to clear content from the Content Panel"""
        self.content_panel.clear()

    def link_home_click(self, **event_args):
        """This method is called when the 'Home' link is clicked"""
        # Clear page content
        self._clear_content()

        # Add the HomeDetailsForm component to the HomeForm content panel
        self.label_title.text = 'PyPoint: Home'
        self.content_panel.add_component(HomeDetailsForm())

    def link_all_docs_click(self, **event_args):
        """This method is called when the 'All Docs' link is clicked"""
        # Clear page content
        self._clear_content()

        # Add the AllDocs component to the HomeForm content panel
        self.label_title.text = 'PyPoint: All Docs'
        self.content_panel.add_component((AllDocsForm()))

    def link_add_doc_click(self, **event_args):
        """This method is called when the link 'Add Doc' is clicked"""
        # Clear page content
        self._clear_content()

        # Add the AllDocs component to the HomeForm content panel
        self.label_title.text = 'PyPoint: Add New Doc'
        self.content_panel.add_component(AddDocForm())
```

---

### :notebook: 12/21/22

- Watched videos 9-10.
    - Added form fields and Python content into the **Add Docs** form.

    ```python
    from ._anvil_designer import AddDocFormTemplate
    from anvil import *

    class AddDocForm(AddDocFormTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        # Document categories
        categories = [
            'docs',
            'science',
            'news',
            'social'
        ]

        # Populate default drop-down category menu with a 'None' value
        self.drop_down_category.items = [
            # The two-tuple specifies text to display and the value of the entry
            ('select a category', None),
        ]
    
        # Populate drop-down categories menu with 'categories' values
        self.drop_down_category.items += [
            (c, c) for c in categories
        ]

    def button_create_doc_click(self, **event_args):
        """This method is called when the 'Create document' button is clicked"""
        pass
    ```

---

### :notebook: 12/23/22

- Watched video 11.
    - Added data validation to the **Add Docs** form:

        ```python
        from ._anvil_designer import AddDocFormTemplate
        from anvil import *

        class AddDocForm(AddDocFormTemplate):
            def __init__(self, **properties):
                # Set Form properties and Data Bindings.
                self.init_components(**properties)

                # Any code you write here will run before the form opens.
                # Document categories
                categories = [
                    'docs',
                    'science',
                    'news',
                    'social'
                ]

                # Populate default drop-down category menu with a 'None' value
                self.drop_down_category.items = [
                    # The two-tuple specifies text to display and the value of the entry
                    ('select a category', None),
                ]
            
                # Populate drop-down categories menu with 'categories' values
                self.drop_down_category.items += [
                    (c, c) for c in categories
                ]

            def button_create_doc_click(self, **event_args):
                """This method is called when the 'Create document' button is clicked"""
            
                # Call the 'validate' method
                errors = self.validate()

                # Display or hide document name errors
                if errors.get('name'):
                    self.label_doc_name_error.visible = True
                else:
                    self.label_doc_name_error.visible = False

                # Display or hide category errors
                if errors.get('category'):
                    self.label_category_error.visible = True
                else:
                    self.label_category_error.visible = False
                
                # Display or hide contents errors
                if errors.get('contents'):
                    self.label_contents_error.visible = True
                else:
                    self.label_contents_error.visible = False

            def validate(self):
                """ Validate data entry.

                    Args:
                    None.
                    
                    Returns:
                    errors (Dict):
                        Dict object with data validation error instances.
                """
            
                # Create an 'errors' dictionary with default values
                errors = dict(
                    name='',
                    category='',
                    contents=''
                )
                
                # Validate the document name entry
                if not self.text_box_doc_name.text.strip():
                    errors.update(
                        {'name': 'Enter a name for the document.'}
                    )
            
                # Validate the category entry
                if self.drop_down_category.selected_value is None:
                    errors.update(
                        {'category': 'Select a document category.'}
                    )
            
                # Validate the document contents
                if not self.text_area_contents.text.strip():
                    errors.update(
                        {'contents': 'Enter the document contents.'}
                    )
            
                return errors
        ```

    - Originally attempted to use a Typing.NamedTuple object to store input field error status, to allow the use of dot notation (versus using the dict.update method) when displaying data validation.
        - Client-side Anvil does not support all modules in the Python Standard Library, including the `Typing` module.  **As such, the code below is unusable**.

        ```python
        from ._anvil_designer import AddDocFormTemplate
        from anvil import *
        from typing import Any, NamedTuple

        # NamedTuple object for data validation
        class InputErrors(NamedTuple):
        name: str(Any)
        category: str(Any)
        contents: str(Any)

        class AddDocForm(AddDocFormTemplate):
            def __init__(self, **properties):
                # Set Form properties and Data Bindings.
                self.init_components(**properties)

                # Any code you write here will run before the form opens.
                # Document categories
                categories = [
                    'docs',
                    'science',
                    'news',
                    'social'
                ]

                # Populate default drop-down category menu with a 'None' value
                self.drop_down_category.items = [
                    # The two-tuple specifies text to display and the value of the entry
                    ('select a category', None)
                ]

                # Populate drop-down categories menu with 'categories' values
                self.drop_down_category.items += [
                    (c, c) for c in categories
                ]

            def button_create_doc_click(self, **event_args):
                """This method is called when the 'Create document' button is clicked"""

                # Call the 'validate' method
                errors = self.validate()

                # Display or hide document name errors
                if errors.name:
                    self.label_doc_name_error.visible = True
                else:
                    self.label_doc_name_error.visible = False

                # Display or hide category errors
                if errors.category:
                    self.label_category_error.visible = True
                else:
                    self.label_category_error.visible = False
                
                # Display or hide contents errors
                if errors.contents:
                    self.label_contents_error.visible = True
                else:
                    self.label_contents_error.visible = False

            def validate(self) -> InputErrors:
                """ Validate data entry.

                    Args:
                        None.
                        
                    Returns:
                        errors (InputErrors):
                        InputErrors NamedTuple object with data validation
                        error instances.
                """

                # Create a default errors dictionary
                _errors_defaults = dict(
                    name='',
                    category='',
                    contents=''
                )

                # Validate the document name entry
                if not self.text_box_doc_name.text.strip():
                    _errors_defaults.update(
                    {'name': 'Enter a name for the document.'}
                    )

                # Validate the category entry
                if self.drop_down_category.selected_value is None:
                    _errors_defaults.update(
                    {'category': 'Select a category for the document.'}
                    )

                # Validate the document contents
                if not self.text_area_contents.text.strip():
                    _errors_defaults.update(
                    {'contents': 'Enter the document contents.'}
                    )

                # Create the 'errors' InputErrors object to return
                errors = InputErrors(**_errors_defaults)

                return errors
        ```

---

### :notebook: 12/24/22

- Updated layout of error fields to improve readability.
- Added a final data validation check to use before creating a document.
    - Creates a list comprehension from the `errors` dictionary object and compares it to a list of empty strings.
    - All empty strings indicates no error messages.

        ```python
        # Confirm no errors exist or return False
        if not [error for error in errors.values()] == ['', '', '']:
            return False
        ```

- Created `Data Tables` Anvil DB service with two tables, `categories` and `docs`.
    - Populated `categories` table with category names.
    - Established **foreign key relationship** between the `name` column in the `categories` table with the `category` column in the `docs` category.

- Wrote Anvil server-side Python to query the `Data Tables` DB.

    ```python
    import anvil.tables as tables
    import anvil.tables.query as q
    from anvil.tables import app_tables
    import anvil.server

    # Get all documents
    @anvil.server.callable
    def all_docs():
    results = list(
        app_tables.docs.search(
            tables.order_by(
                "created",
                ascending=False
            )
        )
    )
    return results

    # Get all categories
    @anvil.server.callable
    def all_categories():
    results = list(
        app_tables.categories.search(
            tables.order_by(
                'name'
            )
        )
    )
    return results

    # Get a document by name
    @anvil.server.callable
    def doc_by_name(name):
        return app_tables.docs.get(name=name)

    # Get a category by name
    @anvil.server.callable
    def category_by_name(name):
        return app_tables.categories.get(name=name)
    ```

- Replaced static categories list in the `AddDocForm` form with results returned from the server-side DB query function `all_categories`.

```python
# Static document categories
# categories = [
#   'Docs',
#   'Science',
#   'News',
#   'Social'
# ]

# Fetch raw category data from the DB
raw_categories = anvil.server.call('all_categories')

# Convert raw category data to a list of category names
categories = [c['name'] for c in raw_categories]

# Populate default drop-down category menu with a 'None' value
self.drop_down_category.items = [
  # The two-tuple specifies text to display and the value of the entry
  ('select a category', None) 
]

# Populate drop-down categories menu with 'categories' values
self.drop_down_category.items += [
  (c, c) for c in categories
]
```

---

### :notebook: 12/25/22

- Watched video 14.
- Added the server code function `add_doc` to insert a new document into the database:

    ```python
    # Add a new document
    @anvil.server.callable
    def add_doc(
    name: str,
    category_name: str,
    contents: str,
    views: int
    ):
    """ Add a new document to the database.

        Args:
            name (str):
            Name of the document.

            category_name (str):
            Category choice for the document.  Must match the name
            of a table row in the 'categories' table.

            contents (str):
            Document contents.

            views (int):
            TODO

        Returns:
            None.
    """
    
    # Display a status message
    print(
        f"Server: creating new document {name}, {category_name}, "
        f"{contents}, {views}."
    )

    # Get the row from the category table that matches the form selection
    # Required for relational table inserts (can't just add text)
    category = category_by_name(
        name=category_name
    )

    # Add the new document to the database
    app_tables.docs.add_row(
        name=name,
        category=category,
        contents=contents,
        created=datetime.datetime.now(),
        views=views
    )

    # Get the row from the docs table that matches the new doc
    doc_name = doc_by_name(
        name=name
    )

    return doc_name

    ```

- Updated the `AddDocForm` code to call the server `add_doc` function.

    ```python
    # Add a new document to the DB
    name = self.text_box_doc_name.text.strip()
    category_name = self.drop_down_category.selected_value
    contents = self.text_area_contents.text.strip()
    views = 0
    
    anvil.server.call(
        'add_doc',
        name,
        category_name,
        contents,
        views
    )
    ```

---

### :notebook: 12/26/22

- Watched video 15.
- Added **client module** named `client_utilities` in order to make common client-side Python functions available to any other client module.

    ```python
    import anvil.server
    import anvil.tables as tables
    import anvil.tables.query as q
    from anvil.tables import app_tables

    """ Begin relevant code """
    # Initialize the `home_form` variable
    # Value will be assigned by the __init__ method in the HomeForm class
    home_form = None

    # Define a function to call the HomeForm.link_home_click
    def go_home():
        home_form.link_home_click()
    """ End relevant code """
    ```

- Added code to the `HomeForm` **Form** that imports the `client_utilities` module.
    - Adding `client_utilities.home_form = self` to the `__init__` method creates an instance of the `HomeForm` class and assigns the instance to the client_utilities.home_form object.

        ```python
        class HomeForm(HomeFormTemplate):
            def __init__(self, **properties):
                # Set Form properties and Data Bindings.
                self.init_components(**properties)

                # Any code you write here will run before the form opens.
                self.link_home_click()

                """ Begin relevant code """
                # Set the value of 'utilities.home_form' to be an instance of HomeForm
                # This provides access to utilities.home_form from any other form
                client_utilities.home_form = self
                """ End relevant code. """
        ```

    - This makes an instance of the `HomeForm` class available to all **client modules** that import the `client_utilities` module.
        - For the use case of redirecting a browser to the home page, after adding a new document, it is possible for `AddDocForm` to import `client_utilities` and call the `home_form.link_home_click` function after adding a new document.

```python
# AddDocForm.AddDocForm code snippets
from .. import client_utilities

class AddDocForm(AddDocFormTemplate):
    # Code omitted for brevity

    def button_create_doc_click(self, **event_args):
        """This method is called when the 'Create document' button is clicked"""
    
        # Call the 'validate' method
        errors = self.validate()

        # Code omitted for brevity

        # Add a new document to the DB
        name = self.text_box_doc_name.text.strip()
        category_name = self.drop_down_category.selected_value
        contents = self.text_area_contents.text.strip()
        views = 0

        anvil.server.call(
            'add_doc',
            name,
            category_name,
            contents,
            views
        )

        """ Begin relevant code. """
        # Return to the home page
        client_utilities.go_home()
        """ End relevant code. """
```

---

### :notebook: 12/27/22

- Watched first half of video 16.
    - Added a **Repeating Panel** component to the `AllDocsForm` **Form**, to display results from a database query row-by-row.
        - Called a server-side database query `all_docs` from the `AllDocsForm` and applied the query results to the `items` property of the **Repeating Panel** object:

            ```python
            class AllDocsForm(AllDocsFormTemplate):
                def __init__(self, **properties):
                    # Set Form properties and Data Bindings.
                    self.init_components(**properties)

                    # Any code you write here will run before the form opens.

                    """ Begin relevant code. """
                    # Set repeating panel items using the 'all_docs' DB query results
                    self.repeating_panel_docs.items = anvil.server.call('all_docs')
                    """ End relevant code. """
            ```

        - Set the results of the **Title** column of the **Repeating Panel** to:
            - `self.item['name']`

    - Added code to the `AllDocsItemPanel` **Repeating Panel** class to format the _Created Date_ for each document explicitly when the document is shown/rendered
        - Used the `strftime` method to set the results of the **Created** column of the **Repeating Panel** to a visually-friendly version of the created date with:
            - `self.label_doc_created.text = self.item['created'].strftime('%B %d, %Y')`

            ```python
            class AllDocsItemPanel(AllDocsItemPanelTemplate):
                def __init__(self, **properties):
                    # Set Form properties and Data Bindings.
                    self.init_components(**properties)

                    # Any code you write here will run before the form opens.

                def label_doc_created_show(self, **event_args):
                    """This method is called when the Label is shown on the screen"""

                    """ Begin relevant code. """
                    # Insert the self.item['created'] text with a string time format
                    self.label_doc_created.text = self.item['created'].strftime('%B %d, %Y')
                    """ End relevant code. """
            ```

---

### :notebook: 12/28/22

- Refactored server-side database queries to `add_doc` and `all_categories` in the `AddDocForm` to client-side database queries in a way that automatically 'caches' all of the documents and categories when the app starts (on the `HomeForm` **Form**).

    - `client_utilities` client-side code **Form**

        ```python
        import anvil.server
        import anvil.tables as tables
        import anvil.tables.query as q
        from anvil.tables import app_tables

        # Initialize the `home_form` variable
        home_form = None

        # Create empty lists to cache documents and categories
        docs = []
        categories = []

        # Define a function to call the HomeForm.link_home_click
        def go_home():
            home_form.link_home_click()
            return None

        # Define a function to collect a list of all documents and categories
        def cache_db_data():
            # Declare function local variables as references to global variables
            global docs, categories

            # Fetch all documents from the database
            docs = anvil.server.call('all_docs')
            
            # Fetch raw category data from the DB
            raw_categories = anvil.server.call('all_categories')

            # Convert raw category data to a list of category names
            categories = [c['name'] for c in raw_categories]

            return None

        # Call the server-side `add_doc` function
        def add_doc(name, category, contents, views: int = 0):
            # Add a new document and refresh the cached lists of docs and categories
            anvil.server.call('add_doc', name, category, contents, views)
            cache_db_data()

        return None
        ```

    - `HomeForm` **Form** `__init__` method

        ```python
        # HomeForm __init__ method
        def __init__(self, **properties):
            # Set Form properties and Data Bindings.
            self.init_components(**properties)

            # Any code you write here will run before the form opens.
            #########################################################

            # Make a cached list of all documents available to any form
            client_utilities.cache_db_data()

            # Display the home form at app launch
            self.link_home_click()
            
            # Set the value of 'utilities.home_form' to be an instance of HomeForm
            # This provides access to utilities.home_form from any other form
            client_utilities.home_form = self
        ```

    - `AddDocForm` **Form**

        ```python
        # Populate drop-down categories menu with 'categories' values
        self.drop_down_category.items += [
            (c, c) for c in client_utilities.categories
        ]

        def button_create_doc_click(self, **event_args):
        """This method is called when the 'Create document' button is clicked"""

        """ Code omitted for brevity """

        # Add a new document to the DB
        name = self.text_box_doc_name.text.strip()
        category_name = self.drop_down_category.selected_value
        contents = self.text_area_contents.text.strip()

        # Replace the server-side function call with a client-side function call
        client_utilities.add_doc(name, category_name, contents)

        # Return to the home page
        client_utilities.go_home()
        ```

---

### :notebook: 12/29/22

- Updated repository root relative URLs with anchor tags in [README.md](/) to work properly.
    - Required the use of absolute URL paths.

---

### :notebook: 1/1/23

- Completed watching video 17.
    - Created the `link_doc_link_click` method in the `AllDocsItemPanel` class, to respond to clicks to the **details** links displayed in the **AllDocsForm** Form.

    ```python
    def link_doc_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    # Call the 'client_utilities.doc_links' function
    # The 'doc' parameter gets each DB row as an argument (self.item)
    client_utilities.doc_links(doc=self.item)
    ```

- Created the `doc_links` function in the `client_utilities` **Client Module**, to pass the document DB row (passed from `self.item` in `AllDocsItemPanel.link_doc_link_click`) to the `HomeForm.doc_links` method.

    ```python
    # Create links to display document contents
    def doc_links(doc):
    """The 'doc' parameter will pass the name of the document to the 
        HomeForm function that loads document contents."""
    home_form.doc_links(doc)

    return None
    ```

- Created the `doc_links` method in the `HomeForm` **Form**, to load the `DocDetailsForm` **Form**, passing the document DB row (passed from the `doc` parameter in `client_utilities.doc_links`) to the `DocDetailsForm` instance created by the `self.content_panel.add_component` function in the `HomeForm.doc_links` method.
    - The document DB row is passed to the `item` parameter in the `HomeForm.doc_links` method.
    - When instantiated by the `DocDetailsForm` **Form**, each DB row becomes `self.item`, with corresponding keys that match each DB column (`self.item['name']` for example)

        ```python
        def doc_links(self, doc, **event_args):
        """TODO"""
        # Clear page content
        self._clear_content()

        # Add the AllDocs component to the HomeForm content panel
        self.label_title.text = 'PyPoint: Details'
        self.content_panel.add_component(DocDetailsForm(item=doc))
        ```

- Created a `print` statement in the `DocDetailsForm` **Form** to display the name of the document clicked on in the `link_doc_link_click` method of the `AllDocsItemPanel` class.

    ```python
    class DocDetailsForm(DocDetailsFormTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

        """ Begin relevant code. """
        # Output the name of the document that will display its contents
        print(f'LOADED DOC: {self.item["name"]}')
        """ End relevant code. """
    ```

    - Successfully tested all new code for proper functionality.

---

### :notebook: 1/2/23

- Watched video 17.

- Replaced the link label text `details` with a document preview of the first N characters of the document content.
    - Set the number of display characters using a constant.
    - Set the text to be italic.
- Expanded the display format of the `created` column of the DB query in the `AllDocsItemPanel` **Form**.
    - Set the format using a constant.

    ```python
    # Constants
    DISPLAY_CHARS = 25
    TIME_FORMAT = '%B %d, %Y - %-H:%M:%S %p'

    class AllDocsItemPanel(AllDocsItemPanelTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def label_doc_created_show(self, **event_args):
        """This method is called when the Label is shown on the screen"""

        # Insert the self.item['created'] text with a string time format
        self.label_doc_created.text = self.item['created'].strftime(TIME_FORMAT)
        
        # Display the first N document words
        self.link_doc_link.italic = True
        self.link_doc_link.text = f'{self.item["contents"][0: DISPLAY_CHARS]}...'
    ```

- Created a new global variable, `docs_range` in the `client_utilities` **Form**.
    - Creates a range object from 1 to the total number of items in the `docs` list.
    - Used for displaying row numbers next to `docs` rows:

        ```python
        # Collect a list of all documents and categories
        def cache_db_data():
        """ Begin relevant code. """
        # Declare function local variables as references to global variables
        global docs, docs_range, categories
        """ End relevant code. """

        # Fetch all documents from the database
        docs = anvil.server.call('all_docs')

        """ Begin relevant code. """
        # Assign a range object to docs_range, to use as row numbers
        docs_range = range(1, len(docs) + 1)
        """ End relevant code. """
        
        # Fetch raw category data from the DB
        raw_categories = anvil.server.call('all_categories')

        # Convert raw category data to a list of category names
        categories = [c['name'] for c in raw_categories]

        return None
        ```

- Created the `AllDocsRowNumberPanel` form for a repeating panel that displays row numbers for each displayed DB result.
    - Used this repeating panel in the `HomeDetailsForm` and the `AllDocsForm` **Forms**.

        ```python
        class AllDocsRowNumberPanel(AllDocsRowNumberPanelTemplate):
        def __init__(self, **properties):
            # Set Form properties and Data Bindings.
            self.init_components(**properties)

            # Any code you write here will run before the form opens.

        """ Begin relevant code. """
        def label_row_number_show(self, **event_args):
            """This method is called when the Label is shown on the screen"""

            # Display the row number
            self.label_row_number.text = f'{self.item}.'
            """ End relevant code. """
        ```

- Expanded the design of the `HomeDetailsForm` **Form**.
    - Displays a list of the N most recent documents, sorted by descending date.
    - Included formatted column headings and repeating panels for row number and documents list.
    - Added code to populate the row number and documents list repeating panels:

        ```python
        # Constants
        RECENT_N_DOCS = 3

        class HomeDetailsForm(HomeDetailsFormTemplate):
            def __init__(self, **properties):
            # Set Form properties and Data Bindings.
            self.init_components(**properties)

            # Any code you write here will run before the form opens.

            # Sort the list of available documents by date
            docs = sorted(
                client_utilities.docs,
                key=lambda doc: doc['created'],
                reverse=True
            )

            # List the top N most recent documents
            self.repeating_panel_row_number.items = client_utilities.docs_range[0: RECENT_N_DOCS]
            self.repeating_panel_recent_docs.items = docs[0: RECENT_N_DOCS]
        ```

---

### :notebook: 1/3/23

- Watched video 18.

- Added a 'Category' column to the `HomeForm` and `AllDocsForm` **Forms** to display the document category/tag.

- Added code to support the following as a user types in the filter text box on the `AllDocsForm` **Form**:
    - Interactive document filtering.
    - Interactive updating of a 'Total Documents' count **Label**.

- The `text_box_filter_docs_change` function is an event handler that triggers every time the filter text box contents change.
    - The `__init__` function sets the initial value for the 'Total Documents' display text, based on the data from `client_utilities` that will populate the **Repeating Panel** elements on the page.
    - Each change updates:
        - The 'Total Documents' display text.
        - The **Repeating Panels** for both row numbers and for row content (document properties)
    - The `doc_to_text` function concatenates a document's title, category, and contents to a single string.
    - The `filtered_docs` function:
        - Calls the `doc_to_text` function for each document (row) in the DB.
        - Searches the concatenated string for filter matches.
        - Appends all rows that match to the `filtered_docs` list.
        - Calculates and returns the total number of filter search matches.

    ```python
    # Constants
    TOTAL_DOCS = 'Total Documents: '

    class AllDocsForm(AllDocsFormTemplate):
        def __init__(self, **properties):
            # Set Form properties and Data Bindings.
            self.init_components(**properties)

            # Any code you write here will run before the form opens.

            # Set the initial 'Total Documents' value
            try:
                self.total_docs = max(client_utilities.docs_range)
                self.label_docs_count.text = f'{TOTAL_DOCS}{self.total_docs}'
            except ValueError:
                self.label_docs_count.text = '0'
        
            # Set repeating panel items using the 'all_docs' DB query results
            self.repeating_panel_docs.items = client_utilities.docs
            self.repeating_panel_row_number.items = client_utilities.docs_range

        def text_box_filter_docs_change(self, **event_args):
            """This method is called when the text in this text box is edited"""

            # Call the 'filtered_docs' function to update the docs repeating panel
            self.repeating_panel_docs.items, \
            self.repeating_panel_row_number.items = self.filtered_docs()

            # Reset the 'Total Documents' to default if the filter text box is blank
            if not self.text_box_filter_docs.text:
                docs_count = self.total_docs
            else:
                # Set the 'Total Documents' to the max value in the row number range object
            try:
                docs_count = max(self.repeating_panel_row_number.items)
        
            # Set 'Total Documents' to 0 if no max value is found
            except ValueError:
                docs_count = 0

            # Update the docs count text box
            self.label_docs_count.text = f'{TOTAL_DOCS}{docs_count}'

        def doc_to_text(self, doc) -> str:
            """ Concatenate all searchable text for filtering.
            
                Args:
                doc (Dict):
                    Dictionary of searchable document values including
                    'name', 'category', and 'contents' of a search
                    result.
                    
                Returns:
                doc_text (str):
                    Concatenated string of searchable document values.
            """
        
            # Create a concatenated, lowercase string to search
            doc_text = (
            f'{doc["name"]} '
            f'{doc["category"]["name"]} '
            f'{doc["contents"]}'
            ).lower()

            return doc_text
            
        def filtered_docs(self):
            """ Filter the list of documents based on filter text box contents.
            
                Args:
                None.
                
                Returns:
                filtered_docs (List[Dict]):
                    List of dictionaries with a filtered list of documents.

                filtered_docs_range (range):
                    range object that provides row numbers to match the length
                    of the 'filtered_docs' list.
            """
            
            # Define a list for the filtered documents
            filtered_docs = []
        
            # Use a local variable for 'self.text_box_filter_docs.text', for brevity
            filter_text = self.text_box_filter_docs.text.lower()
        
            # Search for filter matches and add results to 'filtered_docs'
            for doc in client_utilities.docs:
                doc_text = self.doc_to_text(doc)
            if filter_text in doc_text:
                filtered_docs.append(doc)
            
            # Create a range object to provide row numbers
            filtered_docs_range = range(1, len(filtered_docs) + 1)
            
            return filtered_docs, filtered_docs_range
    ```

---

### :notebook: 1/4/23

- Watched video 19.

- Created labels in a layout on `DocDetails` **Form** that host property names (Title, Created, etc.) and blank labels for their corresponding values from the DB.
    - Added code to `DocDetails` **Form** to populate blank labels:

```python
# Constants
TIME_FORMAT = '%B %d, %Y - %-H:%M:%S %p'

class DocDetailsForm(DocDetailsFormTemplate):
     def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

        """ Assign 'self.item' assigned by `HomeForm` to the 'doc variable.
        
            From `HomeForm`:
            # Add the DocDetailsForm component to the HomeForm content panel
            self.label_title.text = 'PyPoint: Details'
            self.content_panel.add_component(DocDetailsForm(item=doc))
        """
        doc = self.item

        # Assign `doc` properties to page labels
        self.label_title.text = doc['name']
        self.label_category.text = doc['category']['name']
        self.label_created.text = doc['created'].strftime(TIME_FORMAT)
        self.label_contents.text = doc['contents']
```

- Completed demo application and saved Anvil version as _Completed Draft Version 1.0_.

---

### :notebook: 1/6/23

- Watched videos 20-22.
    - Published the app publicly using Anvil's hosting feature.
    - Successfully tested all functions via the public URL.
    - [Episode 138 of the TalkPython podcast](https://talkpython.fm/episodes/show/138/anvil-all-web-all-python) explains the inner workings of Anvil.

---

### :notebook: 1/7/23

- Watched video 20.
- Started project for 