# Convert json file to spaCy format.

#importing required modules
import logging
import argparse
import sys
import os
import json
import pickle
import random


#Creating the function for json_to_spacy to input and output
def json_to_spacy(input_file=None, output_file=None):
    try:
        training_data = []
        lines=[]
        with open(input_file, 'r') as f:
            lines = f.readlines()
            
   #load line to jsone
   #annotation point  and labels the 
        for line in lines:
            data = json.loads(line)
            text = data['content']
            entities = []
            for annotation in data['annotation']:
                point = annotation['points'][0]
                labels = annotation['label']
                if not isinstance(labels, list):
                    labels = [labels]

#labels get one by one  to start and end 
                for label in labels:
                    entities.append((point['start'], point['end'] + 1 ,label))


            training_data.append((text, {"entities" : entities}))

#print training_data
        print(training_data)

#output_file writing in binary
        with open(output_file, 'wb') as fp:
            pickle.dump(training_data, fp)


#using the logging froment
    except Exception as e:
        logging.exception("Unable to process " + input_file + "\n" + "error = " + str(e))
        return None


#import the json_to_spacy, input and output part name
json_to_spacy("/content/drive/MyDrive/gow.json","/content/drive/MyDrive/gowthwm.spacy")


#read binary to output train_data
train_data = pickle.load(open('/content/drive/MyDrive/gowthwm.spacy','rb'))

train_data