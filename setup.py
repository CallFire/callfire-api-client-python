import setuptools
from callfire.version import Version

setuptools.setup(name='callfire-api-client-python',
                 version=Version('0.0.1').number,
                 description='CallFire API v2 Python client',
                 long_description=open('README.md').read().strip(),
                 author='Vladimir Mikhailov',
                 author_email='vmikhailov@callfire.com',
                 url='https://github.com/CallFire/callfire-api-client-python',
                 py_modules=['callfire-api-client-python'],
                 install_requires=[
                     "bravado==8.4.0"
                 ],
                 license='MIT License',
                 zip_safe=False,
                 keywords='CallFire API v2 Python SDK messaging sms mms dialing calls texts',
                 classifiers=[
                     'Development Status :: 4 - Beta'
                     'Topic :: Software Development :: Libraries :: Python Modules',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python :: 3.6'
                 ])
