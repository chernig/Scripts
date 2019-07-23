import os
import glob

print('Would you like to have a validation folder? y/n')
answer = input()
folders = []
types = ['*.jpg', '*.jpeg', '*.png']
counter = 0

if answer =='y':
    print('Please enter the desired propotion betweet training / test / validation sets (for example 0.8 0.1 0.1):')
    training_scale, test_scale, valid_scale = map(float, input().split())
    os.mkdir('training')
    os.mkdir('test')
    os.mkdir('validation')
else:
    print('Please enter the desired propotion betweet training / test / (for example 0.8/0.2):')
    training_scale, test_scale = input().split('/')
    os.mkdir('training')
    os.mkdir('test')

#Count all images in folder
for image_type in types:
    for _ in glob.glob(image_type):
        counter+=1

training_files = int(training_scale*counter)
test_files = int(test_scale*counter)
validation_files = counter - training_files - test_files

print(training_files, test_files, validation_files)
