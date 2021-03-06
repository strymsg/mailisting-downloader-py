#!/bin/python3
'''
This is a sample script to read messages downloaded and write the messages to a csv file.

This script should be called from projects root, then

python debianMailing
'''

import os
import csv
import traceback

csvHeaders = ['category', 'year','month', 'message', 'format']
# lista = ['debian-cli', 'debian-desktop', 'debian-firewall', 'debian-jobs', 'debian-legal', 'debian-mirrors', 'debian-python', 'debian-r','debian-edu']

outputDirectory = os.path.join(os.path.abspath(os.getcwd()), 'output', 'debian-mailinglist')
print('outputDir:', outputDirectory)
outputFile = os.path.join(outputDirectory, 'debian-mailinglist.csv')
print('outputFile:', outputFile)

with open(outputFile, 'w') as csvfile:
    writer = csv.DictWriter(csvfile,
                            fieldnames=csvHeaders,
                            quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    # messageWriter = csv.writer(csvfile, delimiter=',',
    #                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for roots, dirs, files in os.walk(outputDirectory, topdown=True):
        print('---------------')
        print('roots:', roots)
        # input('ver dirs>')
        # for name in dirs:
        #     print(os.path.join(roots, name))
        # if (input('ver files>') == 'o'):
        #     break
        for name in files:
            filePath = os.path.join(roots, name)
            print(filePath)
            # getting features
            try:
                slug1 = filePath.split('/')
                category = slug1[-3]
                # if category not in lista:
                #     continue
                slug2 = slug1[-1].split(category + '_')
                year = slug2[1].split('_')[0]
                month = slug2[1].split('_')[1]
                messageFormat = 'plain'
                try:
                    slug1[-1].index('.html.')
                    messageFormat = 'html'
                except:
                    pass
                
                # print('cateogory:', cateogory, 'year:', year, 'month:', month)
                # reading file contents
                message = ''
                with open(filePath) as fileMessage:
                    message = fileMessage.read()
                
                writer.writerow({
                    'category': category,
                    'year': year,
                    'month': month,
                    'message': message,
                    'format': messageFormat
                })
            except Exception as E:
                print(traceback.format_exc())
                print(E)
print('Done, check output/debian-mailinglist/debian-mailinglist.csv')

        
