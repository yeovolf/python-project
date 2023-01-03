# import modules
import boto3
import logging
import csv
from botocore.exceptions import ClientError

#import email module
from email import encoders
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#setup loggers
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Constants global
REPORT_NAME = 'ec2-report1.csv'
Bucket_Name = 'ec2-report-2023-01-01'

Message = MIMEMultipart()
Message["Subject"] = "This is an email with EC2 Report!"
Message["From"] = "yeovolf@yahoo.fr"
Message["To"] = "yeovolf@yahoo.fr"

Body = MIMEText(f""" Hello Team, 
    Writing to update you on the EC2 report.
    Find attached {REPORT_NAME}.
    Sincerely,
    """)

# list of instances
def list_all_instances(): 
    # call EC2 boto client
    ec2_client = boto3.client('ec2')

    #Retrieve all  EC2 instance in us-east-1 region
    response = ec2_client.describe_instances()

    # empty list
    ec2_instances_list = []

    # print(response['Reservations'] [0]['Instances'][2]['Tags']) 
    print(response['Reservations'])
    print(type(response['Reservations']))

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            # looking for the data needed
            server_name = instance['Tags'][0]['Value']
            instance_id = instance['InstanceId']
            image_id = instance['ImageId']
            instance_type = instance['InstanceType']

            # adding data to list
            ec2_instances_list.append([server_name, instance_id, image_id, instance_type])
            
    return ec2_instances_list 

# Generate report
def generate_excel_report(instances):
    # Python program to demonstrate
    # writing to CSV

    # Write a Header to a CSV File
    header = ['Server Name', 'Instance ID', 'Ami ID', 'Instance Type']
    try:
        with open(REPORT_NAME, 'w', newline='') as file:
            write = csv.writer(file ) #writting to CSV file
            write.writerow(header)
            write.writerows(instances)
    except FileExistsError as error:   
        logger.error(f'File not found! {error}')
        return False
    return True  

# Upload the file to s3

def upload_report_to_s3():
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    
    # call the client
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(REPORT_NAME, Bucket_Name , 'reportobject.csv')
    except ClientError as error:
        logging.error(f'The error message is {error}')
        return False
    return True    

def send_email():

    """send an email with attachment
    :return: True if file was sent, else False
    """
    # this function sends an email with attachment
    
    Message.attach(Body)

    # filename = 'ec2-report1.csv' 

    with open(REPORT_NAME, "rb") as attachment:
        csv_attachment = MIMEApplication(attachment.read(),'csv')
        csv_attachment.add_header("Content-Disposition",
                        "attachment",
                        filename=REPORT_NAME)
        
    Message.attach(csv_attachment)

    ses_client = boto3.client("ses")
    
    response2 = ses_client.send_raw_email(
        Source="yeovolf@yahoo.fr",
        Destinations=["yeovolf@yahoo.fr"],
        RawMessage={"Data": Message.as_string()}
    )
    print(response2)

if __name__ =='__main__':
    logger.info(f' our list of Servers: {list_all_instances()}')

    # retrieve date needed
    instances = list_all_instances()
    
    # we passing the instances list to the function
    generate_excel_report(instances) 
    logger.info(f'Report: {REPORT_NAME} has been generated succesfuly!')
    
    #Uploading the file to s3 bucket
    upload_report_to_s3() 
    logger.info(f'Report: {REPORT_NAME} has been uploaded to s3 bucket succesfuly!!!')

    # # send email with report attached
    send_email()
    logger.info(f'Report: {REPORT_NAME} email has been send successfully!!')
   