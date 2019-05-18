# Gepetto
Generate new identities using thispersondoesnotexist.com and a face recognition AI

## how to use

Simple ! First install the faker and requests libraries
```pip3 install requests faker```.
Then create an account on a face recognition platform, I've added two python scripts, one for face++ and one for microsoft azure but feel free to use your own solution (just be shure to return a gender and an age).
Now just run 
```python gepetto.py```
and generate new identities.

## how does it work ?

_TLDR_ : Uses [thispersondoesnotexist](https://thispersondoesnotexist.com) to generate a face then use a face recognition API to generate coherent identities.

I'll soon write a blog post [here](https://yarienkiva.ml/whatever_this_article_is_called) to document the thought process and steps I've taken to code this project.

## soon...
This is a work in progress and (much) more while be added in the future :
* argparse to manage the parameters
* an option to save the output to a file/qr code
* an option to give a user-chosen image
