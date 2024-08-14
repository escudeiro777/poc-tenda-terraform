import boto3

rds = boto3.client('rds')

instance_identifier = 'db-instance-id'

response = rds.delete_db_instance(
    DBInstanceIdentifier=instance_identifier,
    SkipFinalSnapshot=True
)

print(response)

