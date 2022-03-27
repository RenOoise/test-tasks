### 1. Почему команды du и df могут показывать разный объем занимаемого дискового пространства? 
- df - суммирует все пространство файловой системы для инод (суммирует все иноды) и учитывает файлы, которые используются процессами, но уже могли быть удалены.
- du - суммирует пространсто занятое только реальными существующими файлами. Проверяет размер файлов и суммирует их.

### 2. Есть две директории. Допустим они называются A и B. В обеих директориях лежат тысячи файлов, в том числе одинаковые. Нужно удалить из директории B то, что есть в директории A. Как это сделать? Напишите решение на bash или python. 

- [Ссылка на скрипт с директориями](https://github.com/RenOoise/test-tasks/tree/master/task%202)

```
import os

path_a = 'dirs/a'
path_b = 'dirs/b'

# получаем список файлов в директориях 
# a
files_list_a = os.listdir(path_a)
# b
files_list_b = os.listdir(path_b)

# прогоняем циклами по спискам
for a in  files_list_a:
    for b in files_list_b:
        # проверяем что это не директория
        if os.path.isfile(os.path.join(path_b, b)):
            # проверяем на совпадения в именах
            if a == b:
                os.remove(os.path.join(path_b, b))
```

### 3. Напишите скрипт (рекомендуется на python), который добавляет хост в Zabbix и навешивает ему необходимые (перечисленные в качестве параметров скрипта) шаблоны. Если такой хост с необходимыми шаблонами уже есть, то скрипт ничего не делает и сообщает нам об этом. Если хост есть, но не хватает каких-либо шаблонов, то скрипт навешивает недостающие. 

### 4. Составить SQL запрос в базу Zabbix для получения списка Топ 10 неподдерживаемых айтемов. 
 
### 5. Напишите systemd-unit, на примере сервера iperf3. Назовите его iperf3.service. В какой директории его нужно создавать? Что сделать, чтобы сервис запустить? Опишите последовательность действий. 

- Для начала скачаем iperf3 и библиотеку libiperf:
```
sudo wget -O /usr/lib/libiperf.so.0 https://iperf.fr/download/ubuntu/libiperf.so.0_3.1.3
sudo wget -O /usr/bin/iperf3 https://iperf.fr/download/ubuntu/iperf3_3.1.3
sudo chmod +x /usr/bin/iperf3
```

- Для запуска приложения в режиме сервера нужно использовать ключ -s
- В директории /etc/systemd/system создаем файл iperf3.service с описанием юнита:
```
[Unit]
Description=iperf3 Server
Requires=network.target

[Service]
ExecStart=/usr/bin/iperf3 -s
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
- Запускаем юнит командой sudo systemctl start iperf3
- Проверяем статус sudo systemctl status iperf3:
```
drop@sys-srv-development:~$ sudo systemctl status iperf3
● iperf3.service - iperf3 Server
     Loaded: loaded (/etc/systemd/system/iperf3.service; disabled; vendor preset: enabled)
     Active: active (running) since Fri 2022-03-25 22:53:12 UTC; 5s ago
   Main PID: 1292211 (iperf3)
      Tasks: 1 (limit: 2274)
     Memory: 224.0K
     CGroup: /system.slice/iperf3.service
             └─1292211 /usr/bin/iperf3 -s

мар 25 22:53:12 sys-srv-development systemd[1]: Started iperf3 Server.
```
- Так же можно включить автозагрузку при старте ОС: sudo systemctl enable iperf3

### 6.	Как можно определить MTU сетевого канала? Напишите скрипт на bash или python, который это делает. 
 
### 7.	Что такое jitter (своими словами)? Каким образом можно замониторить данную метрику? Напишите скрипт на bash или python, который это делает. 
 - Джиттер это такой параметр, отражающий изменение задержки соседних пакетов (если проще - разница во времени получения между первым и вторым пакетом, )

### 8.	Исправьте неправильно написанный Dockerfile. 
#### Есть условное Node.js приложение, и неправильно написанный Dockerfile, который не будет кэшироваться и будет занимать много места. Нужно переписать его в соответствии с best-practice. 

- [Ответ](https://github.com/RenOoise/test-tasks/blob/master/task%208/Dockerfile)

```#плохой файл  
#FROM ubuntu:20.04  
#COPY ./src /app  
#RUN apt-get update -y  
#RUN apt-get install -y nodejs  
#RUN npm install  
#ENTRYPOINT ["npm"]  
#CMD ["run", "prod"]  

# Для уменьшения размера стоит использовать альпайн
FROM node:17-alpine
# Для увеличения производительности установить ноду в продакшн
ENV NODE_ENV=production
WORKDIR /usr/src/app
COPY ["package.json", "package-lock.json", "./"]
# Ставим только зависимости нужные для нашего приложения
RUN npm ci --only=production
# Копируем все остальное, кроме node_modules (указаны в .dockerignore)
COPY . .
# запускаю тестовое приложение через cmd
CMD ["node", "prod.js"]
```

### 9.	Какие из этих команд нельзя выполнить в консоли:  
##### -	zabbix_proxy -c zabbix_proxy.conf -R log_level_increase 	
##### -	zabbix_proxy -c zabbix_proxy.conf -R config_cache_reload 	
##### -	zabbix_proxy -c zabbix_proxy.conf -R check_config 	
##### -	zabbix_proxy -c zabbix_proxy.conf -R housekeeper_execute 	
- zabbix_proxy -c zabbix_proxy.conf -R check_config 
- у zabbix_proxy нет такого параметра

### 10.	Чем отличаются утилиты zabbix_get и zabbix_sender? В каких кейсах удобно применять тип метрики zabbix trapper? 	
- zabbix_get - утилита для получения инфы от заббикс агента
- zabbix_sender - утилита для отправки данных мониторинга на заббикс сервер
- траппер можно использовать например когда данные невозможно с сервера запросить (мб из-за сетефой фильтрации на входящие запросы со стороны агента)