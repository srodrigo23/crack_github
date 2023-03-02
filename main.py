
import os

# os.system("ls -l")

import subprocess
# stream = os.popen('mkdir project')
# output = stream.read()
# print(output)
# print('GIT HUB')


process = subprocess.Popen(
    ['ping', '-c 4', 'python.org'], 
    stdout=subprocess.PIPE,
    universal_newlines=True
)
process.communicate()

# while True:
#     output = process.stdout.readline()
#     print(output.strip())
#     # Do something else
#     return_code = process.poll()
#     if return_code is not None:
#         print('RETURN CODE', return_code)
#         # Process has finished, read rest of the output 
#         for output in process.stdout.readlines():
#             print(output.strip())
#         break