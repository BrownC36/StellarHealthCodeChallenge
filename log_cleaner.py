import logging
import importlib
import re
import os

import s3
import log_cleaner_utils as lc

BUCKET_NAME='stellar.health.test.colin.brown'
S3_OBJECT='patients.log'
NEW_LOG_FILE='newLog.log'

def run():
    logging.info('process running')
    process_file()

def process_file():
    """Process the file. Download from S3. Parse and upload newly formatted
       file.
    """
    local_file = s3.download_file(BUCKET_NAME, S3_OBJECT)
    logging.info('File downloaded: '+ local_file)
    try:
        if local_file is not None:
            with open(local_file) as fp:
                with open(NEW_LOG_FILE, "w") as nf:
                    logging.info('Creating new file')
                    line = fp.readline()
                    while line:
                        line = fp.readline()
                        if line.startswith('['):
                            trim_line = line[29:]
                            t = re.findall(r"[\S]+\S+\S",trim_line)
                            res = lc.parse_line(t)
                            new_data = lc.clean_date(res)
                            nf.write(lc.format_new_line(line, new_data)+'\n')
                        else:
                            nf.write(line +'\n')
                        
    except Exception as e:
        logging.error(e)
    
    finally:
        # Clean up. Close files, upload to S3 and delete temporary files
        nf.close()
        fp.close()
        logging.info('New log file completed')
        s3.upload_file(nf.name, BUCKET_NAME)
        os.remove(nf.name)
        os.remove(fp.name)