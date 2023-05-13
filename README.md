# VPC-IGW-CLI
AWS CLI for EC2 Resource Management
This command line interface (CLI) tool is designed to manage EC2 resources through Amazon Web Services (AWS). The CLI uses the boto3 Python library to interface with the AWS EC2 API.

Prerequisites
Before using the CLI tool, please make sure you have the following:

AWS access key ID, secret access key, and session token
Python 3.7 or higher
The following Python packages:
boto3
argparse
Getting Started
Clone this repository to your local machine.
Install the necessary Python packages by running pip install -r requirements.txt in the command line.
Create a .env file and add the following AWS credentials:
aws_access_key_id
aws_secret_access_key
aws_session_token
aws_region_name
To run the CLI, enter the following command in the command line:
bash
Copy code
python aws_cli.py <command> [--vpc-id VPC_ID]
Commands
The following commands are available:

list - Lists all VPCs in your AWS account.
create - Creates a new VPC.
tag - Adds a name tag to a VPC.
igw - Creates a new Internet Gateway.
attach - Attaches an Internet Gateway to a VPC.
To execute a command, run the CLI with the desired command name, for example:

lua
Copy code
python aws_cli.py create
If the command requires a VPC ID, include the --vpc-id flag followed by the VPC ID:

css
Copy code
python aws_cli.py tag --vpc-id vpc-123456789
