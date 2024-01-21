import boto3

# Set your AWS credentials and region
aws_access_key = ''
aws_secret_key = ''
aws_region = 'us-west-2'
s3_bucket = 'raw1000'
s3_path = 'data/customer.dat'


# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)


# Upload CSV file to S3
local_file_path = "D:\\DWH\\customer.dat"
s3.upload_file(local_file_path, s3_bucket, s3_path)
