import subprocess

fastapi_process = subprocess.Popen(['python', 'sensor_packet_generator.py'])
mongo_process = subprocess.Popen(['python', 'packet.py'])

fastapi_process.wait()
mongo_process.wait()