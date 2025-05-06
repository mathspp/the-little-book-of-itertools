# What's this repo?

This repo contains automated tests for the tutorials on reimplementing the module `itertools`.
The exercises are taken from [my book “The little book of `itertools`”](https://mathspp.com/books/the-little-book-of-itertools).


## For PyCon US tutorial attendees

Follow these instructions if you're attending the PyCon US tutorial “Reimplementing the module `itertools` for fun & profit”:

 1. star the repository (absolutely essential; the Internet will break if you don't!);
 2. clone the repository locally or download its contents;
 3. make sure you're running Python 3.10+, but _ideally_ Python 3.12+ ([here's how to do it with `uv`](https://docs.astral.sh/uv/guides/install-python/));
 4. install the requirements (check the file `requirements.txt`, but all you need is `pytest`; with uv, run `uv tool install pytest`); and
 5. check everything is right by running `pytest count.py`, which should run `pytest` on the file `count.py`; this should show ~20 failing tests.

Make sure you do this _before_ the tutorial, since Wi-Fi at the venue is supposedly subpar.
