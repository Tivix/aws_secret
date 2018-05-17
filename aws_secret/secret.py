from __future__ import absolute_import
import os
import json
import boto3
from botocore.exceptions import ClientError, NoCredentialsError

class AwsSession(object):
    def __init__(self, path=os.getenv('SECRET_PATH', default=""),
        region_name=os.getenv('SECRET_REGION', default="")):
        self.path = path
        self.region_name = region_name
        self.client = boto3.session.Session().client(
            service_name='secretsmanager',
            region_name=self.region_name
            )

    def __str__(self):
        return "session for {}".format(self.region_name)


class AwsSecret(AwsSession):
    def __init__(self, *args, **kwargs):
        super(AwsSecret, self).__init__(*args, **kwargs)
        self.secrets = self.get_secret_dict()
    
    def get_secret_dict(self):
        """calls for secret and adds it to dict"""
        try:
            secrets = json.loads(self.client.get_secret_value(SecretId=self.path)['SecretString'])
            return secrets
        except NoCredentialsError:
            print("\ncheck credentials \n")
            raise
        except ClientError as ex:
            if ex.response['Error']['Code'] == 'ResourceNotFoundException':
                print("\n{} secret was not found, check spelling or region \n".format(self.path))
                raise
            else:
                print("\ncheck credentials \n")
                raise


    def get(self, secret_name, fail=True):
        """prints secret and returns it"""
        try:
            print(secret_name + '=' + self.secrets[secret_name])
            return self.secrets[secret_name]
        except:
            print("{} not found".format(secret_name))
            raise
    def list(self):
        """prints all secrets"""
        for k, v in self.secrets.items():
            print(k + '=' + v)
        return self.secrets


    def export(self):
        """takes all secrets and exports them to env"""
        for k, v in self.secrets.items():
            os.environ[k] = v


    def __str__(self):
        return "{} secret in {} region".format(self.path, self.region_name)