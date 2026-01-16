## Architecture Overview

EC2:
- Hosts application logic

RDS (MySQL):
- Stores user transactional data

DynamoDB:
- Stores event/audit records

S3:
- Stores user files

Lambda:
- Handles async notifications

SNS:
- Sends email notifications

