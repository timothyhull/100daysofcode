# :calendar: Day 85: 12/26/2022

---

## Topics

:clipboard: Full-stack Web Apps Made Easy

---

## Resources

:star: [Anvil Home Page](https://anvil.works/?anvil_attrib=talk-python-100-days)

---

## Tasks

:white_check_mark: Watch videos 1-5

:white_large_square: Watch videos 6-24

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
        """This method is called when the link is clicked"""
        # Clear page content
        self._clear_content()

        # Add the HomeDetailsForm component to the HomeForm content panel
        self.label_title.text = 'PyPoint: Home'
        self.content_panel.add_component(HomeDetailsForm())

    def link_all_docs_click(self, **event_args):
        """This method is called when the link is clicked"""
        # Clear page content
        self._clear_content()

        # Add the AllDocs component to the HomeForm content panel
        self.label_title.text = 'PyPoint: All Docs'
        self.content_panel.add_component((AllDocsForm()))

    def link_add_doc_click(self, **event_args):
        """This method is called when the link is clicked"""
        # Clear page content
        self._clear_content()

        # Add the AllDocs component to the HomeForm content panel
        self.label_title.text = 'PyPoint: Add New Doc'
        self.content_panel.add_component(AddDocForm())
```
