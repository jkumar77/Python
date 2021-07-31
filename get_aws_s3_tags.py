#!/usr/bin/env python

import boto3

session = boto3.session.Session(profile_name="DEVOPS")
print(session.region_name)

s3_client = session.client('s3')
for bucket in s3_client.list_buckets()['Buckets']:
    TAG = s3_client.get_bucket_tagging(Bucket=bucket['Name'])
    print(bucket['Name'], TAG['TagSet'][0]['Value'])






