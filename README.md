# Unique words counter API

## Setup
To setup virtualenv use virtualenvwrapper command:
> mkvirtualenv unique_words_counter --python=/usr/bin/python3.9

To install required packages use
> pip install -r requirements.txt

I initially used
> pip install "fastapi[all]"

## Development server
To run the server use:
> uvicorn main:app --reload

The server should start on:
> http://127.0.0.1:8000
