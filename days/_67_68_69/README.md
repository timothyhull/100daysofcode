# :calendar: Day 67+68+69: 5/15/2022-5/16/2022

---

## Topics

:clipboard: Copy and Paste with `Pyperclip`

---

## Resources

:star: [`Pyperclip` on PyPI](https://pypi.org/project/pyperclip)

:star: [`Pyperclip` on GitHub](https://github.com/asweigart/pyperclip)

:star: [`Pyperclip` documentation](https://pyperclip.readthedocs.io/en/latest/index.html)

:star: [Linux Xvfb display server](https://en.wikipedia.org/wiki/Xvfb)

:star: [Reference for simulating a virtual display in Linux](https://github.com/asweigart/pyperclip/issues/161#issuecomment-1112942799)

---

## Tasks

:white_check_mark: Watch videos 1-4

:white_check_mark: Watch video 5

:white_check_mark: Watch videos 6-7

---

## Notes

### :notebook: 5/14/22

- Watched videos 1-4

- Created two project files:
    - [./blob/main/days/_67_68_69/pyperclip/text_replacer.py](./blob/main/days/_67_68_69/pyperclip/text_replacer.py)
    - [./blob/main/days/_67_68_69/pyperclip/affiliate.py](./blob/main/days/_67_68_69/pyperclip/affiliate.py)

- `Pyperclip` installs with `pip install pyperclip`.
    - In order to run in a Docker container environment, it is necessary to install `Xfvb` and `xclip`, and simulate a virtual display with `Xfvb`:

        ```bash
        apt-get install -y xvfb xclip
        Xvfb :99 -screen 0 1280x720x16 & export DISPLAY=:99
        ```

- Successfully tested `Pyperclip` within a Docker container using code added to [./blob/main/days/_67_68_69/pyperclip/text_replacer.py](./blob/main/days/_67_68_69/pyperclip/text_replacer.py).

    ```python
    # Create a virtual display with Xvfb
    from os import system
    system('Xvfb :99 -screen 0 1280x720x16 & export DISPLAY=:99')

    # Read data from the OS clipboard into Python
    clipboard_data = pyperclip.paste()

    # Write data to the OS clipboard from Python
    pyperclip.copy(clipboard_data.upper())
    ```

---

### :notebook: 5/15/22

- Watched video 5.

- Added code to [./blob/main/days/_67_68_69/pyperclip/affiliate.py](./blob/main/days/_67_68_69/pyperclip/affiliate.py) that generates a tagged affiliate link.

---

### :notebook: 5/16/22

- Watched videos 6-7
