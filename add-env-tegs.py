import boto3

ec2_client_paris = boto3.client('ec2')  # Paris
ec2_resource_paris = boto3.resource('ec2')

reservation_instance_paris = ec2.client.describe_instances()['Reservations']

instance_ids_paris = []

for reservation in reservation_instance_paris:
  instances = reservation['Instances']
  for instance in instances:
    instance_ids_paris.append(instance['InstanceId'])

response = ec2_resource_paris.create_tags(
    Resources=instance_ids_paris,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)
