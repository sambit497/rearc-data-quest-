import boto3
import os

# Your AWS credentials (❗ Rotate after use for security)
session = boto3.Session(
    aws_access_key_id='xxxxxxxxxx',
    aws_secret_access_key='k9J665Ysfu/4fhULpz5Y09Z8+eggYMNneJ1uNEGI',
    region_name='xxxxxxx'
)

# S3 resource and target bucket
s3 = session.resource('s3')
bucket_name = 'rearc-data-quest-sambit'
bucket = s3.Bucket(bucket_name)

# Local folder to upload (change as needed)
local_folder = r'D:\BLS CSV' 

# Optional prefix for S3 key (folder in bucket)
s3_folder_prefix = 'bls/'  # e.g., "bls/", or "" for no prefix

# Traverse and upload all files
for root, dirs, files in os.walk(local_folder):
    for file in files:
        local_path = os.path.join(root, file)
        relative_path = os.path.relpath(local_path, local_folder)
        s3_key = os.path.join(s3_folder_prefix, relative_path).replace("\\", "/")

        print(f'Uploading {local_path} → s3://{bucket_name}/{s3_key}')
        bucket.upload_file(Filename=local_path, Key=s3_key)

print(" All files uploaded successfully.")
