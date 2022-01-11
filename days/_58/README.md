# :calendar: Day 58: 1/10/2022

---

## Topics

:clipboard: Twitter Data Analysis With Python

---

## Resources

:star: [Twitter Developer API](https://developer.twitter.com/en/apps)

:star: [`tweepy` Twitter library for Python](https://pypi.org/project/tweepy/)

:star: [`wordcloud` word cloud cenerator Python package](https://pypi.org/project/wordcloud/)

---

## Tasks

:white_check_mark: Watch videos 1-3

:white_check_mark: Create a Twitter developer account

:white_check_mark: Setup an OAuth application, and obtain keys

:white_check_mark: Setup environment variables export script

:white_large_square: Watch video 4

---

## Notes

### :notebook: 1/10/22

- Watched videos 1-3.
- Setup Twitter developer account.
- Setup Twitter OAuth application and keys, tokens, secrets, etc.
- Setup environment variables export script and `.env` file.
    - Tested `.env` file import in `iPython`:

        ```python
        # Import the python_dotenv module
        import dotenv

        # Load environment vars from the .env file in the working directory
        dotenv.load_dotenv()

        # Review imported environment vars
        dotenv.dotenv_values()
        ```
