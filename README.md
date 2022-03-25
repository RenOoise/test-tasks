### 1. Почему команды du и df могут показывать разный объем занимаемого дискового пространства? 
- df - суммирует все пространство файловой системы для инод (суммирует все иноды) и учитывает файлы, которые используются процессами, но уже могли быть удалены.
- du - суммирует пространсто занятое только реальными существующими файлами. Проверяет размер файлов и суммирует их.

### 2. Есть две директории. Допустим они называются A и B. В обеих директориях лежат тысячи файлов, в том числе одинаковые. Нужно удалить из директории B то, что есть в директории A. Как это сделать? Напишите решение на bash или python. 

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