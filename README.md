# Python Lambda With Layers

A dumb excercise because I wanted to see what works. No surprise that it's a 5 minute stroll through the AWS docs.

## lambda code structure

/mylambda/
--/svc/functions.py
--main.py

## lambda layer structure

python/lib/python3.11/site-packages/requests

This is acheived by this command `python3 -m pip install -r requirements.txt -t python/lib/python3.11/site-packages --no-user`

There is no "path switching" monkey business in main.py. We just put the dependency/ies in the above folder structure when we zip it.
