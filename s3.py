import logging
import boto3
from botocore.exceptions import ClientError


def download_file(bucket_name, object_name):
    """Downloads an object from specified S3 bucket

    :param bucket_name: S3 bucket name
    :param object_name: S3 object name
    :return: local path where the file was downloaded to and None if cannot download
    """
    s3_client = boto3.client('s3')
    try:
        with open(object_name, 'wb') as f:
            logging.info('downloading file')
            s3_client.download_file(bucket_name, object_name, object_name)
        f.close()
        logging.info('download complete')
        return f.name
    except ClientError as e:
        logging.error(e)
        return None

def upload_file(local_file_name, bucket_name,  object_name=None):
    """Uploads a file to specified S3 bucket 

    :param local_file_name: File to upload
    :param bucket_name: S3 Bucket to upload to
    :param object_name: S3 object name
    :return: True if file was uploaded, and false otherwise
    """

    # if the object_name is null then use local_file_name
    if object_name is None:
        object_name = local_file_name

    s3_client = boto3.client('s3')
    
    try:
        logging.info('Uploading file: ' + object_name)
        response = s3_client.upload_file(local_file_name, bucket_name, object_name)
        logging.info('File successfully uploaded')
    except ClientError as e:
        logging.error(e)
        return False
    return True
