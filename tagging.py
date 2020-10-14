import boto3

def tag(resourceid,region,tags):
    ec2 = boto3.resource('ec2', region_name=region)
    ec2.create_tags(Resources=[resourceid],
                    Tags=tags)


