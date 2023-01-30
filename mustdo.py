import boto3

s3 = boto3.resource('s3')
s4=boto3.client('s3')
#s3.create_bucket(Bucket='mybucket1dg2')
response = s4.put_bucket_accelerate_configuration(
    Bucket='mybucket1dg2',
    AccelerateConfiguration={
        'Status': 'Suspended'
    },
    ExpectedBucketOwner='335516814222',
    ChecksumAlgorithm='CRC32'
)