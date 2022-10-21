from boto3 import Session

sess = Session(aws_access_key_id="******************",
               aws_secret_access_key="******************************",
               region = "us-east-1")

s3 = sess.resources("s3")

for bucket in s3.buckets.all():
    print(bucket.name)