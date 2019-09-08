import os
import glob
import shutil
import random

print('Would you like to have a validation folder? y/n')
answer = input()
folders = []
#List of available extensions
types = ['*.jpg', '*.jpeg', '*.png']
counter = 0
files_lst = []
path = os.getcwd()
folders.extend(['training', 'test'])
#Validation set check (if so - split into 3 folders: training, test, validation)
if answer =='y':
    folders.append('validation')
    print('Please enter the desired propotion betweet training / test / validation sets (for example 0.8 0.1 0.1):')
    training_scale, test_scale, valid_scale = map(float, input().split())
else:
    print('Please enter the desired propotion betweet training / test (for example 0.8 0.2):')
    training_scale, test_scale = map(float, input().split())
for x in folders:
    os.mkdir(x)

#Count all images in folder and add them into list
for image_type in types:
    for x in glob.glob(image_type):
        files_lst.append(x)
        counter+=1

# Scale to actual numbers
training_files = int(training_scale*counter)
test_files = int(test_scale*counter)
i = 0

# Create necessary paths
train_path = path + '\\training'
test_path = path +'\\test'

# Copy to training folder
while i < training_files:
    i+=1
    shutil.copy(files_lst.pop(random.randint(0 , len(files_lst)-1)), train_path)
i = 0

# Copy to test folder
while i < test_files:
    i+=1
    shutil.copy(files_lst.pop(random.randint(0 , len(files_lst)-1)), test_path)
# Copy to validation folder if applicable
if 'valid_scale' in locals():
    valid_path = path + '\\validation'
    for x in files_lst:
        shutil.copy(x, valid_path)

