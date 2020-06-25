import logging
import importlib
import re

import s3

BUCKET_NAME='stellar.health.test.colin.brown'
S3_OBJECT='patients.log'

def run():
    logging.info('process running')
    process_file()


def parse_line(t):
    d = dict()
    for item in t:
        if "=" in item:
            i = item.split("=")
            d[i[0].strip()] = i[1].strip()      
    return d


def clean_date(info):
    if "DOB" in info:
        date = info["DOB"]
        date = date.replace("'","")
        new_date = "X/X/" + date[-4:]
        info["DOB"] = new_date
    elif "DATE_OF_BIRTH" in info:
        date = info["DATE_OF_BIRTH"]
        date = date.replace("'","")
        new_date = "X/X/" + date[-4:]
        info["DATE_OF_BIRTH"] = new_date
    return info


def format_new_line(line, new_data):

    flattened = ''

    for k, v in new_data.items():
        flattened += k+'='+v + ' '

    return line[:29] + flattened


def process_file():
    local_file = s3.download_file(BUCKET_NAME, S3_OBJECT)
    
    logging.info('File downloaded: '+ local_file)
    

    try:
        if local_file is not None:
            with open(local_file) as fp:
                with open("pat.log", "w") as nf:
                    logging.info('Creating new file')
                    line = fp.readline()
                    while line:
                        line = fp.readline()
                        if line.startswith('['):
                            trim_line = line[29:]
                            t = re.findall(r"[\S]+\S+\S",trim_line)
                            res = parse_line(t)
                            new_data = clean_date(res)
                            nf.write(format_new_line(line, new_data)+'\n')
                        else:
                            nf.write(line +'\n')
                        

    except Exception as e:
        logging.error(e)
    
    finally:
        nf.close()
        fp.close()
        logging.info('New log file completed')

