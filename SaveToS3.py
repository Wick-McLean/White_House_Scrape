import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = 'SEC_ACCESS_KEY'
SECRET_KEY = 'SEC_SECRET_KEY'


def save_to_s3(local_file, bucket, s3_file, now):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    print(s3)
    response = s3.list_objects_v2(Bucket='nymag-scrape-articles-from-python')
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


# uploaded = upload_to_aws('C:\\Users\\Wick\\.PyCharmCE2019.3\\config\\scratches\\scratch_2.py',
#                          'nymag-scrape-articles-from-python', 'teste')

# botofiles = save_to_s3('speech_list.txt', 'nymag-scrape-articles-from-python', 'Whitehouse Speech')
