import time
from multiprocessing import Process

import boto3

ACCESS_KEY = '<your aws access key>'
SECRET_KEY = '<your aws secret key>'


class asyncAWS(object):

    def __init__(self, region='sa-east-1'):
        session = boto3.Session(
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY,
        )
        self.regions = session.get_available_regions('ec2')
        self.ec2conn = {}
        self.ec2_list = {}
        for region in self.regions:
            self.ec2conn[region] = session.resource(service_name='ec2', region_name=region)

    async def connect_region(self, region):
        session = boto3.Session(
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY,
        )
        print(f'Checking {region}...')
        self.ec2 = session.resource(service_name='ec2', region_name=region)

    def check_regions(self, region):
        instances = self.ec2conn[region].instances.all()
        ec2_list = []
        for instance in instances:
            ec2_list.append(self.check_instance(instance))

        if len(ec2_list) > 0:
            self.ec2_list[region] = ec2_list
            print(self.ec2_list[region])

    def check_instance(self, instance):
        try:

            i = {}
            i['id'] = instance._id
            i['state'] = instance.state['Name'] or 'Unknown'
            i['private_ip'] = instance.private_ip_address or 'Unknown'
            i['public_ip'] = instance.public_ip_address or 'Not assigned'
            return i

        except Exception as e:
            print(e)

    def list(self):
        processes = []
        for region in self.regions:
            process = Process(target=self.check_regions, args=(region,))
            processes.append(process)

        for process in processes:
            process.start()

        for process in processes:
            process.join()


def lambda_handler(event=None, context=None):
    aaws = asyncAWS()
    _start = time.time()
    aaws.list()
    print(f"Execution time: { time.time() - _start }")


if __name__ == '__main__':
    lambda_handler()
