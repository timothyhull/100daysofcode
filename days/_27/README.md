# :calendar: Day 27: 9/4/2921

---

## Topics

:clipboard: Error Handling

---

## Resources

:star: TBD

---

## Tasks

:white_check_mark: Write `pytest` tests for the potential exceptions

:white_check_mark: Handle all [error conditions](../_26/README.md)

---

## Notes

### :notebook: 9/4/21

- Wrote `pytest` tests in [tests/test_program.py](tests/test_program.py) for:
  - `ImportError`, for an invalid module import.
  - `ValueError`, for invalid user input.
- Skipped wriring a `pytest` test for the `KeyboardInterrupt` exception.
  - Due to the potential complexity of testing valid `ctrl+c` input.

- Wrote `try` and `except` blocks in [program.py](program.py) to handle:
  - Failure during the use of the `import` command for `class` objects in [actors.py](actors.py).
    - `ImportError`
  - Invalid input.
    - `ValueError`
  - Keyboard interrupt sequence (`ctrl+c`).
    - 'KeyboardInterrupt`
