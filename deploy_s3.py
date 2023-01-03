# import boto3 library
import boto3

## import the random and string module to generate random letter    
import random
import string 

def get_random_string(bucket):
    """
    This fucntion generate a ramdom character of 25 character  length.
     
    """
    return (bucket + str(''.join(random.choices(string.ascii_lowercase + string.digits, k=25))))

bucket_suffix = "myboto-"

client = boto3.client('s3')


response = client.create_bucket(
    Bucket=get_random_string(bucket_suffix),
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2',
    },
)

print(response)