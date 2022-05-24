import boto3
import schedule

ec2_client = boto3.client('ec2')

def create_snapshots():
  volumes = ec2_client.describe_volumes(
    Filters=[
      {
        'Name': 'tag:Name',
        'Values': ['prod']
      }
    ]
  )
  for vol in volumes['Volumes']:
    new_snapshot = ec2_client.create_snapshot(VolumeId=vol['VolumeId'])
    print(new_snapshot)


schedule.every().day.do(create_snapshots)

while True:
  schedule.run_pending()