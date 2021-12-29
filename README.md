# AAPA-Weekly-Update

Command line program to automate weekly tasks for the Afro American Pokemon Association (AAPA) Draft League.
By using [Twython](https://twython.readthedocs.io/en/latest/usage/starting_out.html), this program allows the user to send posts on behalf of the [AAPA Twitter page](https://twitter.com/aapadraftleague) with just a list of paths for images to be posted. 

## Usage

First clone and open this repo. Then you can run this program by calling your cli with this command:

```
python . [--help, -h] [--status_id, -s] [--auto-thread, -a] {[--img_paths, -i]|[--full-img_paths, -f]}
```

You can either send the entire thread of posts with the `--auto-thread` flag, or manually create a thread by passing the last post's `status_id` to the `--status_id` flag. Make sure to include the paths to the images included in your post with the `--img_paths` flag. Only use the `--full-img_paths` flag if the images' root directory are outside your **HOME** path.'

## Twitter Authentication

There's additional scripts for generating and authenticating your tokens to use as detailed [here](https://geekyhumans.com/de/use-twitter-api-in-python/). If you're an admin of the AAPA, please reach out to Saige for the page's access tokens.