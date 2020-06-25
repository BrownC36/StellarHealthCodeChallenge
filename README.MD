# Log File Cleaner

This project is a solution to the Stellar Health take home coding test

## How to run the code

After downloading the code from github, you can run the program from the command line
'''
   > python stellar_health.py
'''

The file pulls the provided file from S3 and uploads a new file to the S3 bucket. Instead of overwriting the existing log file, it creates a new file to allow for more testing. I tried to break down the functionality for expandability and to better mediate failure points. There is an issue with the Regex parsing the data. The dates are successfully changed, but the phone number and address fields have lost data. With a little more time the regex patern can be fixed to accomidate. Another opportunity for improvement is to have retry logic added with back offs when accessing S3 and writing the files.

The program will create a log file to trace the steps happening for debugging.