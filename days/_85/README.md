# :calendar: Day 85: 12/28/2022

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

:white_large_square: Watch videos 12-24

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
        results = list(app_tables.docs.search(tables.order_by("created", ascending=False)))
        return results

    # Get all categories
    @anvil.server.callable
    def all_categories():
        results = list(app_tables.categories.search(tables.order_by('name')))
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
