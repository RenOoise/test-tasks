import re
import subprocess
import time
host = '192.168.141.158'

result = list()

# делаем 2 пинга
for i in range(2):
    time.sleep(1)
    output = subprocess.check_output(['ping', '-c', '1', '-q', '-s 150' , host])
    output = output.decode('utf8')
    # ищем первое значение из строки rtt min/avg/max/mdev
    ping_time = re.search(r'(\d+\.\d+/)', output).group(0)
    # вырезаем / в конце результата
    ping_time = ping_time[:-1]
    # кидаем в список
    result.append(float(ping_time))
# вычисляем 
jitter = round(result[0] - result[1], 1)
print('Jitter =', jitter)

