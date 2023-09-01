#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random

def choose_mystery_box(box):
    mystery = random.choice(box)
    return mystery

def choose_successor_name(names):
    successor = random.choice(names)
    return successor

# List of mystery boxes
boxes = ["ece", "cse", "data science", "ai/ml"]

# List of successor names
names = ["shashi", "bhaskar", "harshit", "ritesh", "varad"]

# Call the functions to get the random selections
mystery_box = choose_mystery_box(boxes)
successor_name = choose_successor_name(names)

# Print the random mystery box and successor name
print("The mystery box is:", mystery_box)
print("The successor name is:", successor_name)

