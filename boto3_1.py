#1.Write a program to list objects in the buckets in tree format.

import boto3
s3=boto3.resource('s3')
s4=boto3.client('s3')
'''for bucket in s3.buckets.all():
    print(bucket.name)'''

# out=s4.list_objects(Bucket='rakshithdg')
# # print(out)
# print(type(out))
# print("---------------------------------------------------------------------------------")

# print(out['Contents'][0]['Key'])
out=s3.Bucket('rakshithdg')
for my_bucket_object in out.objects.all():
    print('      |--%s' %my_bucket_object.key)
# for i in out['Contents'][0]['Key']:
    # print(i)
    #print(list['Contents'][0]['Key'])



