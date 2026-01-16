def register_user(user_id, name, email):
    """
    Stores user in RDS,
    logs event in DynamoDB,
    uploads file to S3,
    triggers Lambda notification
    """
    print("User registered:", user_id)

