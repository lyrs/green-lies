# How to use :

## Convert the data

First you have to convert the data, for that there is a script in scripts/convert.py that will help you

You need to run the script to convert the annotated file to binary file used by spacy

This script will create a train.spacy file that you will need to put in the directory corpus/

## Create the validation set (optional)

You can create with the same script a dev.spacy file that will be used to evaluate the model.

When you have this file you can put it in the corpus/ folder

Or you can duplicate the training data if it's not important for now

## Run the model

For running the model you will need to do a command in the command line interface (cli)

command to run

```bash

python -m spacy project run all

```

This command will train,evaluate and pack the model, so it can be used by other person on other computer



# Plan B 

I always have a plan b, and you have the script in scripts/training_script.py

This script will allow you to train with data collected from the annotated file and save a model to a folder (content/) and can be packed later 