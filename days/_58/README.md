# :calendar: Day 58: 1/10/2022

---

## Topics

:clipboard: Twitter Data Analysis With Python

---

## Resources

:star: [Twitter Developer API](https://developer.twitter.com/en/apps)

:star: [`tweepy` Twitter library for Python](https://pypi.org/project/tweepy/)

:star: [`wordcloud` word cloud generator Python package](https://pypi.org/project/wordcloud/)

:star: [Twitter Elevated API access application](https://developer.twitter.com/en/portal/products/elevated)

---

## Tasks

:white_check_mark: Watch videos 1-3

:white_check_mark: Create a Twitter developer account

:white_check_mark: Setup an OAuth application, and obtain keys

:white_check_mark: Setup environment variables export script

:white_check_mark: Watch video 4

:white_large_square: Create an application within a Jupyter Notebook that colllects PyBites tweets

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

---

### :notebook: 1/11/22

- Created the file [twitter_app/twitter.ipynb](twitter_app/twitter.ipynb) that collects information from the Twitter API.
    - Unable to authenticate to the twitter API, [Elevated API access required](https://developer.twitter.com/en/portal/products/elevated):

        ```text
        Forbidden: 403 Forbidden
        453 - You currently have Essential access which includes access to Twitter API v2 endpoints only. If you need access to this endpoint, you’ll need to apply for Elevated access via the Developer Portal. You can learn more here: https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-leve
        ```

        - The elevated access application page would not load, will attempt again tomorrow.
