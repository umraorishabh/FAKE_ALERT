# Import relevant packages and modules
from util import *
import random
import tensorflow as tf

# Set file names
file_train_instances = "train_stances.csv"
file_train_bodies = "train_bodies.csv"
file_test_instances = "test_stances_unlabeled.csv"
file_test_bodies = "test_bodies.csv"
file_predictions = 'predictions_test.csv'


mode = input('mode (load / train)? ')

# Load model
if mode == 'load':
	pass

if mode == 'train':
	pass
	
