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


## How to check if an exercise is correct

Each file contains the signature for an `itertools` object at the top of the file.
(The signature in the `.py` file might not match the full signature of the tool from `itertools`. This is on purpose.)

Each file also contains a number of automated tests to check your work.
Once you fill in the signature with your implementation of the tool, you will want to run the automated tests with pytest.
Make sure pytest is installed and then run `pytest file_to_test.py`.
For example, once you complete `count.py`, you'll run `pytest count.py`.
