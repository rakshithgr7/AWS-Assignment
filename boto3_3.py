#build a program to upload >500MB file to S3, When you upload it wait until it uploads and 
   #then give the time it took to upload.

import boto3
import datetime
s3 = boto3.resource('s3')
s4=boto3.client('s3')
start=datetime.datetime.now()
#s3.Object('rakshithdg', '104861968_933.pdf').upload_file(r"C:\Users\Rraks\boto\104861968_933.pdf")
with open(r"C:\Users\Rraks\boto\Screenshot(1).png","rb") as f:
            s4.upload_fileobj(f, "rakshithdg", "now1.pdf")
#upload_file/upload_fileobj methods take care of the things you're looking for (i.e they wait for completion of object/file uploading).
end=datetime.datetime.now()
print(end-start)


# o=s4.head_object(rakshithdg,104861968_933.pdf)
# print(o["LastModified"])


