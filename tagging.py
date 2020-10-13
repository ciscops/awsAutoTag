import boto3

def tag(resourceId,region,tag):
    ec2 = boto3.resource('ec2', region_name=region)
    ec2.create_tags(Resources=[resourceId],
                    Tags=tag)


