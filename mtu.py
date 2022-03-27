import os

mtu_tested = []
# кидаем пинги с размером пакет от 1200 с шагом 8
for mtu in range(1200, 65000, 8):
    result = os.system('ping -M do -s {} {} -c 1'.format(mtu, '192.168.141.1')) 
    if result == 0:
        # если ошибки нет, то кидаем мту в список
        mtu_tested.append(mtu)
    else:
        print("Слишком жирный пакет {}".format(mtu))
        break
# берем последний мту и выводим в консоль
print("Лучший результат = {}".format(mtu_tested[-1]))