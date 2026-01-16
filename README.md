# TechStart Cloud Backend Project

## Problem Statement
Build a secure, scalable backend system using AWS services with real integrations.

## Architecture
- EC2 for application runtime
- RDS (MySQL) for transactional data
- DynamoDB for event logging
- S3 for object storage
- Lambda + SNS for asynchronous notifications

## Data Flow
1. User request hits EC2
2. User data stored in RDS
3. Event metadata written to DynamoDB
4. User file stored in S3
5. Lambda triggered asynchronously
6. SNS sends email notification

## Security
- IAM roles (no static credentials)
- Security-group-based access
- Encrypted storage (RDS, S3)

## What I Learned
- IAM role separation (EC2 vs Lambda)
- Debugging security groups and ports
- OS-level package compatibility
- Event-driven architecture

## Future Improvements
- Secrets Manager
- API Gateway
- Auto Scaling

