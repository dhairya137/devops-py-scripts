import boto3

ec2_client = boto3.client('ec2')
# ec2_client = boto3.client('ec2', region_name='us-east-1')  # Use this to specify region

ec2_resource = boto3.resource('ec2')

# Get status of all instances
reservations = ec2_client.describe_instances()
for reservation in reservations['Reservations']:
    instances = reservation['Instances']
    for instance in instances:
      print(f"Status of instance {instance['InstanceId']} is: {instance['State']['Name']}")

# System Status of all instances
statuses = ec2_client.describe_instance_status()
for status in statuses['InstanceStatuses']:
  ins_status = status['InstanceStatus']['Status']
  sys_status = status['SystemStatus']['Status']
  state = status['InstanceState']['Name']
  print(f"Instance {status['InstanceId']} is {state} with instance status {ins_status} and system status is: {sys_status}")


