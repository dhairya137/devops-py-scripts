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
  print(f"Instance {status['InstanceId']} status is {ins_status} and system status is: {sys_status}")

# # Create VPC
# new_vpc = ec2_resource.create_vpc(
#   CidrBlock="10.0.0.0/16"
# )
# new_vpc.create_subnet(
#   CidrBlock="10.0.1.0/24"
# )
# new_vpc.create_subnet(
#   CidrBlock="10.0.2.0/24"
# )
# new_vpc.create_tags(
#   Tags=[
#     {
#       'Key': 'Name',
#       'Value': 'my-vpc'
#     }
#   ]
# )

# print('--------')

# all_vpcs = ec2_client.describe_vpcs()
# vpcs = all_vpcs["Vpcs"]

# # Get the VPC ID
# for vpc in vpcs:
#   print(vpc["VpcId"])
#   cidr_block_assoc_sets = vpc["CidrBlockAssociationSet"]
#   for assoc_set in cidr_block_assoc_sets:
#     print(assoc_set["CidrBlock"]) 

