# :calendar: Days 86-87: 1/8/2023-1/20/2023

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
