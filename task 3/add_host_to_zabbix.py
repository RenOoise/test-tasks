from pyzabbix import ZabbixAPI, ZabbixAPIException
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-n", "--name",
                    help="имя хоста для добавления или редактирования")
parser.add_argument("-ip", "--ip-ip_address")
parser.add_argument("-t", "--template", 
                    nargs='+', default=[], 
                    help="Пример: python add_host_to_zabbix.py -n server-02 -ip 127.0.0.1 -t 'Linux generic by Zabbix agent' 'Linux CPU by Zabbix agent'")           

args = parser.parse_args()


api = ZabbixAPI('http://192.168.141.60', user='Admin', password='zabbix')


def edit_host(host_id, template_ids):
    api.host.update(hostid=host_id, templates=template_ids)

def add_host(host_name, template_ids, ip):
    # пробуем добавить хост
    api.host.create(host=host_name, status=1,
    interfaces=[{"type": 1,
                 "main": "1",
                 "useip": 1,
                 "ip": ip,
                 "dns": "",
                 "port": 10050
                 }],
    groups=[{"groupid": 2}],
    templates=template_ids)
try:
    # получаем айди шаблонов по именам из аргумента -t
    template_ids_list = list()
    template_ids = api.template.get(filter={"name": args.template}, output=['templateid'])
    # и заносим их в список 
    for template_id in template_ids:
        template_ids_list.append(template_id)
    host_id = api.host.get(filter={"name": args.name}, output=['hostid'])
    # если хост не существует
    if host_id == []:
        # добавляем его
        add_host(args.name, template_ids_list, args.ip_address)        
        print("Хост %s добавлен." % args.name)
    else:
        host_templateids = api.host.get(filter={'host': args.name}, selectParentTemplates=['templateid'])
        if host_templateids[0]['parentTemplates'] == template_ids_list:
            print("Все перечесленные шаблоны у хоста %s уже добавлены." % args.name )
        else:
            try:
                # иначе пробуем обновить шаблоны хоста
                print('Хост %s уже существует.\nОбновляю шаблоны.' % args.name)
                edit_host(host_id[0]['hostid'], template_ids_list)
            except ZabbixAPIException as e:
                print(e)
            finally:
                print('Шаблоны хоста %s обновлены' % args.name)
except ZabbixAPIException as e:
    print(e)