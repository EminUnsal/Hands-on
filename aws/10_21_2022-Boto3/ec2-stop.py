import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-084d7206f0b757bc9cccccccc').stop()