# TumblrPhotoUploadr

A simple tool for uploading all the photos in a directory to Tumblr. It posts them at the date and time they were created, and can add `#tags` to all posts if desired. 

## How to use

1. Setup `virtualenvwrapper` and run it, e.g. `workon uploadr`.
2. You'll need to ensure all the requirements are loaded: `pip install -r requirements.txt`
3. Setup tumblr authentication. (Using [PyTumblr](https://github.com/tumblr/pytumblr)'s `interactive_console.py` [file](https://github.com/tumblr/pytumblr/raw/master/interactive_console.py) is easy). You'll need to add the following environment variables: `CONSUMER_KEY`, `CONSUMER_SECRET`, `OAUTH_TOKEN`, and `OAUTH_SECRET`.
4. Then run `python uploadr.py` and follow the instructions!