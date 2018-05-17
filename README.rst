Funniest
--------

To use simply do::

    >>> from aws_secret import AwsSecret
    >>> s = AwsSecret(secret_path, region)
    >>> s.get('secret_name')
    >>> s.export() """Moves secrets to env"""
