import boto3
from os import getenv
import argparse

ec2_client = boto3.client(
  "ec2",
  aws_access_key_id=getenv("aws_access_key_id"),
  aws_secret_access_key=getenv("aws_secret_access_key"),
  aws_session_token=getenv("aws_session_token"),
  region_name=getenv("aws_region_name")
)

COMMANDS = ["list", "create", "tag", "igw", "attach"]

def list_vpcs():
  result = ec2_client.describe_vpcs()
  vpcs = result.get("Vpcs")
  print(vpcs)

def create_vpc():
  result = ec2_client.create_vpc(CidrBlock="10.0.0.0/16")
  vpc = result.get("Vpc")
  print(vpc)

def add_name_tag(vpc_id):
  ec2_client.create_tags(Resources=[vpc_id],
                         Tags=[{
                           "Key": "Name",
                           "Value": "btuVPC"
                         }])

def create_igw():
  result = ec2_client.create_internet_gateway()
  return result.get("InternetGateway").get("InternetGatewayId")


def attach_igw_to_vpc(vpc_id, igw_id):
  ec2_client.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)

def main():
    parser = argparse.ArgumentParser(description="Manage EC2 resources")
    parser.add_argument("command", choices=COMMANDS, help="Command to execute")
    parser.add_argument("--vpc-id", help="VPC ID")
    args = parser.parse_args()

    if args.command == "list":
        list_vpcs()
    elif args.command == "create":
        create_vpc()
    elif args.command == "tag":
        if args.vpc_id:
            add_name_tag(args.vpc_id)
        else:
            print("VPC ID is required for the 'tag' command.")
    elif args.command == "igw":
        igw_id = create_igw()
        print(f"Internet Gateway created with ID: {igw_id}")
    elif args.command == "attach":
        if args.vpc_id:
            igw_id = create_igw()
            attach_igw_to_vpc(args.vpc_id, igw_id)
            print(f"Internet Gateway attached to VPC {args.vpc_id}")
        else:
            print("VPC ID is required for the 'attach' command.")

if __name__ == "__main__":
    main()