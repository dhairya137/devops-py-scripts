import boto3
import schedule

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

def check_instance_status():
  statuses = ec2_client.describe_instance_status(
    IncludeAllInstances=True
  )
  for status in statuses['InstanceStatuses']:
    ins_status = status['InstanceStatus']['Status']
    sys_status = status['SystemStatus']['Status']
    state = status['InstanceState']['Name']
    print(f"Instance {status['InstanceId']} is {state} with instance status {ins_status} and system status is: {sys_status}")
  print("-------------------------")

schedule.every(5).seconds.do(check_instance_status)  # This will run above function for every 5 minutes

while True:
  schedule.run_pending()  # This will start the scheduler