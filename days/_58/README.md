# :calendar: Day 58: 1/10/2022-1/15/2022

---

## Topics

:clipboard: Twitter Data Analysis With Python

---

## Resources

:star: [Twitter Developer API](https://developer.twitter.com/en/apps)

:star: [`tweepy` Twitter library for Python](https://pypi.org/project/tweepy/)

:star: [`wordcloud` word cloud generator Python package](https://pypi.org/project/wordcloud/)

:star: [Twitter Elevated API access application](https://developer.twitter.com/en/portal/products/elevated)

:star: [`wordcloud` GitHub site](https://github.com/amueller/word_cloud)

---

## Tasks

:white_check_mark: Watch videos 1-3

:white_check_mark: Create a Twitter developer account

:white_check_mark: Setup an OAuth application, and obtain keys

:white_check_mark: Setup environment variables export script

:white_check_mark: Watch video 4

:white_check_mark: Create an application within a Jupyter Notebook that collects PyBites Tweets

:white_check_mark: Watch video 5

:white_check_mark: Review the `collection.Counter` class

:white_check_mark: Watch video 6

:white_check_mark: Watch videos 7-8

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

---

### :notebook: 1/12/22

- Completed application for elevated Twitter API access.
    - Application approved.
    - Successfully ran all of the Python code written to date in [twitter_app/twitter.ipynb](twitter_app/twitter.ipynb).
    - Retrieved 3196 Tweets.

---

### :notebook: 1/13/22

- Watched video 5, and refined the data set of Twitter Tweets:

    1. Removed all retweets with a list comprehension:

        ```python
        no_retweets = [tweet for tweet in tweets if not tweet.text.startswith('RT')]
        ```

    2. Sorted the `no_retweets` list by an average of the likes + retweets, using a `lambda` function:

        ```python
        top_10 = sorted(
            no_retweets,
            key=lambda tweet: (tweet.likes + tweet.re_tweets) / 2,
            reverse=True
        )
        ```

    3. Displayed the top 10 tweets by indexing the `top_10` list:

        - Learned that f-strings cannot have `\` characters in expressions (inside of {}).
        - Implemented a workaround to replace newlines (`\n`) in tweet text with a space.
            - Assign the string `\n` to a variable, and use the variable in the expression.
        - Learned that Python strings support emojis.

        ```python
        newline = '\n'
        for index, tweet in enumerate(top_10[:10], 1):
            print(
                f'{index}. Tweet: 🐦 {tweet.text.replace(newline, " ")}\n'
                f'  Likes: ♥️ {tweet.likes}\n'
                f'  Retweets: ✏️ {tweet.re_tweets}'
            )
        ```

---

### :notebook: 1/14/22

- Reviewed the `collections.Counter.most_common` method, from [Day 4](../_4/).
- Determined and displayed the most common hashtags and mentions.
    - Combined all tweets into string objects (one with, and one without retweets).
    - Used `re` to search for hashtags and mentions, respectively.
    - Used a function to display the top N mentions and retweets, in a friendly view.

---

### :notebook: 1/15/22

- **iPython Tip** - Run shell commands from within iPython or a Jupyter Notebook by preceding commands with the `!` character:

    ```python
    # From within a shell or Jupyter Notebook
    !pip freeze
    ```

- Generated a word cloud with the `wordcloud` module.
- Displayed the image, using an image mask to define the shape.
