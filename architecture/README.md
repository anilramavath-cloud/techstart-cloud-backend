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

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/84d5e993-dea5-45a2-9f59-e2947e8ccd0a" />
