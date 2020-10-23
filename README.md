# AWS Tagging
AWS Tagging is a Lambda function within AWS, this function is used to keep EC2 instaces in compliance with Cisco
 Security Tagging Requirements
 the function will trigger everytime 
a new EC2 insances is ran.  AWS Event Bridge looks for patters in the Cloud Trail log file and sends the log file to
 the Lambda function for proccessing.
 
 Once the defaulet set of tags are applied to the ec2 instance, a WebEx teams bot will send the user an adaptive card
  to approve and change the tags.   
  

  
### Default Tags
 
- `Data Classification: Cisco Restricted` <br />
- `Environment: dev` <br />
- `ResourceOwner: <IAMUser>` Tag is reaured for IAM permission as well <br />
- `Cisco Mail Alias:<IAMUser@cisco.com>` (Domain Name is set via envernement permissions) <br />
- `Data Taxonomy: Cisco Operations Data` <br />
- `Application Name: <EC2 TAG:Name>` <br />
- `Validated: False` Once the end user approves the tags via webex team this will become true <br />
- `Leave Running: False` If the end user changes Leave Running to True the EC2 Instance will not shutdown at night<br />
 
## Event Bridge Rule<br />

`{
  "source": [
    "aws.ec2"
  ],
  "detail-type": [
    "AWS API Call via CloudTrail"
  ],
  "detail": {
    "eventSource": [
      "ec2.amazonaws.com"
    ]
  }
}`
<br />

### Lambda Required Permissions <br /> 
`{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "TagPermissions",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateTags",
                "ec2:DeleteTags"
            ],
            "Resource": "*"
        }
    ]
}`

### Envernment Variables <br />
- `DEFAULT_EMAIL_DOMAIN` <br />
-  `DEV <True/False>` False puts the function into production mode where it will by pass the DEV_USERS list <br />
- `DEV_USERS` List of user that the function will apply on after triggered by event bridge <br />
- `TEAMS_BOT_APP_NAME`	<br />
- `TEAMS_BOT_EMAIL` <br />
- `TEAMS_BOT_URL <Webhook URL>` <br />
- `WEBEX_TEAMS_ACCESS_TOKEN` <br />