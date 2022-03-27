from pyzabbix import ZabbixAPI, ZabbixAPIException
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-n", "--name",
                    help="имя хоста для добавления или редактирования")

parser.add_argument("-t", "--template", 
                    nargs='+', default=[], 
                    help="после ключа -t перечислить необходимые шаблоны через пробел")           

args = parser.parse_args()

api = ZabbixAPI('http://192.168.141.60', user='Admin', password='zabbix')
answer=api.do_request('apiinfo.version')

# получаем айди шаблонов по именам из аргумента -t
template_id = api.template.get(filter={"name": args.template}, output=['templateid'])

try:
    # пробуем добавить хост
    api.host.create(
        host= args.name,
        status= 1,
        interfaces=[{
            "type": 1,
            "main": "1",
            "useip": 1,
            "ip": '127.0.0.1',
            "dns": "",
            "port": 10050
        }],
        groups=[{"groupid": 2}],
        templates=template_id
        )
    print('Хост добавлен')
except ZabbixAPIException as e:
        print(e)