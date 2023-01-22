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
