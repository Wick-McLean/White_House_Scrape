import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = 'SEC_ACCESS_KEY'
SECRET_KEY = 'SEC_SECRET_KEY'


def save_to_s3(local_file, bucket, s3_file, now):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    print(s3)
    response = s3.list_objects_v2(Bucket='AWS_BUCKET_HERE')
    print(response)
    try:
        s3.upload_file(local_file, bucket, s3_file + " " + now)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


