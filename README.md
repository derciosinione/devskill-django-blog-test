# Personal blog

The task verifies the candidates knowledge of `web development`, `Python` and `Django`.

## Introduction
You are creating an [MVP](https://en.wikipedia.org/wiki/Minimum_viable_product) of a simple personal blog. The blog displays the latest blog posts on the index page. Posts are able to use HTML formatting.

## Problem Statement

1. Make the app work in a way described below. The majority of the code is committed but there are some missing pieces to implement.
2. Make tests pass by implementing missing features.


### Technical details
Your site is made up of 2 pages: the index page (`'/'`) and the new post page (`'/add_post'`).
There are only `20` latest posts displayed. Each post is formatted as follows (pay attention to <h> tags): 
```
<h3> Title </h3>
<h5> Date (DD-MM-YYYY format) </h5>
Text (html-formatted)
<--- end of blog post --->
```
### Example:

```html
<h3>Aliens are coming!</h3>
<h5>13-02-2002</h5>
Evidence was found in Florida, USA...
<--- end of blog post --->
<h3>Welcome to my blog!</h3>
<h5>10-02-2002</h5>
This is my first blog post here, nice to see ya!!
<--- end of blog post --->
```

### Additional requirements
Posts are sorted by the date (latest on top).

The new post page includes text edit and submit buttons. (`capture="Submit"`). Pressing the submit button creates a new blog post. The date of the post should be added to the post upon creation.

There is a link to the index page on the new blog post page.
There is a link to the new post page on the the index page.

Posts contain a title, date (`DD-MM-YYYY` format) and text. Post text may contain HTML tags (*font*, *h1*, etc.) which must be rendered properly.

## Environment setup

To execute all unit tests, use:

    pip install -q -e . && python3 setup.py pytest
