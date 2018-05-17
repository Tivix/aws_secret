from setuptools import setup

def readme():
	with open('README.rst') as f:
		return f.read()

setup(name='aws_secret',
      version='0.3',
      description='AWS Secret wrapper',
      long_description=readme(),
      url='https://github.com/Tivix/aws_secret',
      author='Mikolaj Kosmal',
      author_email='mikolaj.kosmal@outlook.com',
      license='MIT',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
      ],
      packages=['aws_secret'],
      install_requires=[
          'boto3',
      ],
      python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
      zip_safe=False)
