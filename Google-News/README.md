# Google News API Implementation (For Google Code-In)

The program uses `requests` to call the Google News API to get the latest news related to the keywords "Android", "Linux" and "Open-Source" and uses `tkinter` for the GUI.

For each article the title, time, website and description are displayed. In the response from the API call, a url is provided for the image, which is converted to a tkinter image using `BytesIO` and `PIL`. If an image url is not provided for the article then a blank image is used instead.

There is also a button under each article description to read the full article which opens the full article in the default browser using `webbrowser`.

The screen recording of the program running is at [recording.mp4](https://github.com/suhas-arun/Google-Code-In/blob/master/Google-News/recording.mp4).