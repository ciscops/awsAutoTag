import boto3


def tag(tags, region):

    ec2 = boto3.resource('ec2', region_name=region)
    ec2.create_tags(Resources=[tags.resourceid], Tags=tags.get_tags())
