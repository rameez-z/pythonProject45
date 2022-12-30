import os
import re
import datetime
from pathlib import Path

with open('/home/ubuntu/Downloads/zimbralog/zimbraa', 'r') as file:
    lst = ['@avenuesschools.com', '@rpl-saga.com', '@rfcpapers.in', '@specialitypapers.in',
           '@fnetindia.com', '@mastermindmagic.in', '@techoncloud.com', '@valgeninc.com']
    s = file.read()
    result = re.findall(r'from=\S+@\S+', s)
    queue = []
    for r in result:
        queue.append(r)
sets7 = set(queue)
lst1 = []
for i in queue:
    for j in lst:
        if j in i:
            lst1.append(i)
            # sets7 = set(lst1)
sets8 = set(lst1)
# print(sets8)
file.close()
with open('/home/ubuntu/Downloads/zimbralog/zimbraa', 'r') as file2:
    queue8 = []
    for i in file2:
        for j in sets7:
            if j in i:
                # print(i)
                i = i.strip()
                a = re.findall(r':\s[a-zA-Z0-9]{10,20}:', i)
                # print(a)
                queue8.append(a)
flatList = [item for elem in queue8 for item in elem]
sets = list(set(flatList))
# print(sets)

file2.close()
# ques = {que: {"from": []} for que in sets}
with open('/home/ubuntu/Downloads/zimbralog/zimbraa', 'r') as file3:
    # ques2 = ques.copy()
    logline = []
    for j in file3:
        for k in sets:
            if k in j and ("message-id=<" in j):
                logline.append(j)
                # print(logline)
logline = list(dict.fromkeys(logline))
file3.close()
with open('/home/ubuntu/Downloads/zimbralog/zimbraa', 'r') as file4:
    message_id = []
    for j in file4:
        # message_id = []
        for i in sets:
            # print(i)
            if "message-id=" in j and i in j:
                # print(j)
                message = re.findall(r"message-id=<(.*?)>", j)
                # print(message)
                # NewList = [[x] for x in message]
                # print(NewList)
                message_id.append(message[0])
# print(message_id)

# flatList5 = [item for elem in message for item in elem]
sets1 = set(message_id)
# print(sets1)

file4.close()

with open('/home/ubuntu/Downloads/zimbralog/zimbraa', 'r') as file5:
    aligned_messages = []
    # ms_queue = []
    # for msg in sets1:
    # print(msg)
    # ms_queue = []
    for msg in sets1:
        ms_queue = []
        for i in logline:
            # ms_queue = []

            # for msg in sets1:
            # print(msg)
            if msg in i:
                a = re.findall(r':\s[a-zA-Z0-9]{10,20}:', i)
                # print(a)
                ms_queue.append({a[0]: []})
                # print(a)
                # ms_queue.append(a)
                # print(ms_queue)
        aligned_messages.append({msg: ms_queue})
        # aligned_messages.append({})
# print(aligned_messages)
file5.close()

# def res(y5):
#   return y
# def relaylogfile(path, b):
# return path, b


# def qes(y4):
# return y4

ques1 = {que: {"from": [], "to": [], "time": [], "relay": [], "status": [], "queue": [], "date": [],
               "statuss": [], "status_id": []} for que in sets}
with open('/home/ubuntu/Downloads/zimbralog/zimbraa', 'r') as file6:
    for key, value in ques1.items():
        for j in file6:
            for i in sets:

                if i in j:
                    # print(i)
                    if "from=" in j:
                        # print(j)
                        fromid = re.findall(r'from=<[a-zA-Z0-9_.-]{0,63}@[a-zA-Z0-9_.-]{0,63}.\w{2,3}', j)
                        x = ''.join(fromid)
                        y = x.replace('from=<', '')
                        y2 = y.replace('[', '')
                        y3 = y2.replace(']', '')
                        # print(y3)
                        ques1[i]['from'] = y3

                    if "to=" in j:
                        # print(j)
                        toid = re.findall(r'to=<[a-zA-Z0-9_.-]{0,63}@[a-zA-Z0-9_.-]{0,63}.\w{2,3}', j)
                        z = ''.join(toid)
                        z1 = z.replace('to=<', '')
                        # z2 = z1.replace('[]', '')
                        # print(z1)
                        # ques1[i]['to'].append(toid)
                        ques1[i]['to'].append(z1)
                    if i in j:
                        timet = re.findall(r'\d{2}:\d{2}:\d{2}', j)
                        # c = datetime.datetime.strptime(timet[0], '%H:%M:%S').strftime('HH:MM[:ss[.uuuuuu]][TZ]')
                        # print(c)
                        # print(timet)
                        ques1[i]['time'] = timet
                    if "relay=" in j:
                        # print(j)
                        relays = re.findall(
                            r'relay=[a-zA-Z0-9._-]{0,63}\[\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\]:\d{1,5}', j)
                        # print(relays)
                        x3 = ''.join(relays)
                        y4 = x3.replace('relay=', '')
                        # print(y4)
                        ques1[i]['relay'].append(y4)
                        """dict3 = {'/home/ubuntu/Downloads/zimbralog/relay3log': '149.202.225.46',
                                 '/home/ubuntu/Downloads/zimbralog/esgrelay': '167.114.73.155',
                                 'norelay': 'server1.madras'}
                        for k3, v5 in dict3.items():
                            if v5 in y4:
                                path = k3
                                val1 = qes(y4)
                                print(val1)"""

                        # return path

                    if "status=" in j:
                        statuss = re.findall(r'status=\w{4,8}\s', j)
                        x1 = ''.join(statuss)
                        x2 = x1.replace('status=', '')
                        # print(statuss)
                        ques1[i]['status'].append(x2)

                    if i in j:
                        datee = re.findall(r'[a-zA-Z0-9]{3}\s\d{2}', j)
                        b = datetime.datetime.strptime(datee[0], '%b %d').replace(year=2022).strftime('%Y-%m-%d')
                        # print(b)
                        ques1[i]['date'] = b
                    if "queued as" in j:
                        # print(j)
                        queuee = re.findall(r'queued as\s[a-zA-Z0-9]{10,20}', j)
                        # print(queuee)
                        x5 = ''.join(queuee)
                        y5 = x5.replace('queued as', '')
                        # print(y5)
                        ques1[i]['queue'] = y5
                        """val = res(y5)
                        print(val)"""
# print(ques1)

file6.close()
for i in aligned_messages:
    # print(i)
    for key, value in i.items():
        # print(value)
        for j in value:
            # print(j)
            for key1, value1 in j.items():
                # print(key1)
                # lst = []
                for l, m in ques1.items():
                    # print(type(l))
                    if str(key1) == str(l):
                        j[key1] = m
# print(aligned_messages)
for i in aligned_messages:
    # print(i)
    for k, h in i.items():
        # print(k,h)
        i[k] = h[-1]
        # print(i[k])

print(aligned_messages)


def relaylogfile(path, b8):
    val = ''
    for root, dir, files in os.walk(path):
        for i9 in files:
            for j8 in open(os.path.join(root, i9), 'r'):
                if b8 in j8:
                    val = os.path.join(root, i9)
                    break

    return val


for i in aligned_messages:
    for k, v in i.items():
        # print(k,v)
        for j1, v1 in v.items():
            # print(v1)
            for j2, v2 in v1.items():
                a8 = ''.join(v1['relay'])
                # print(a8)
                b8 = ''.join(v1['queue'])
                # print(b8)
                # b9 = ''.join(v1['statuss'])
                # b10 = ''.join(v1['status_id'])
                # print(b8)
                dict3 = {'/home/ubuntu/Downloads/zimbralog/relay3log': '149.202.225.46',
                         '/home/ubuntu/Downloads/zimbralog/esgrelay': '167.114.73.155',
                         'norelay': 'server1.madras'}
                for k3, v5 in dict3.items():
                    if v5 in a8:
                        path = k3
                        vall = relaylogfile(path, b8)
                        if vall:
                            dict1 = {'from': [], 'to_id': [], 'statuss': [], 'relayss': [], 'status_id': []}

                            for i5 in open(vall, 'r'):
                                # dict1 = {'from': [], 'to_id': [], 'statuss': [], 'relayss': [], 'status_id': []}
                                if b8 in i5:
                                    if "from=" in i5:
                                        from_id = re.findall(
                                            r'from=<[a-zA-Z0-9_.-]{0,63}@[a-zA-Z0-9_.-]{0,63}.\w{2,3}',
                                            i5)
                                        x8 = ''.join(from_id)
                                        y9 = x8.replace('from=<', '')
                                        y6 = y9.replace('[', '')
                                        y7 = y6.replace(']', '')
                                        dict1['from'] = y7
                                        # print(y7)
                                    if "to=" in i5:
                                        to_id = re.findall(
                                            r'to=<[a-zA-Z0-9_.-]{0,63}@[a-zA-Z0-9_.-]{0,63}.\w{2,3}',
                                            i5)
                                        z5 = ''.join(to_id)
                                        z6 = z5.replace('to=<', '')
                                        dict1['to_id'].append(z6)
                                    if "status=" in i5:
                                        statusss = re.findall(r'status=\w{4,8}\s', i5)
                                        x10 = ''.join(statusss)
                                        x11 = x10.replace('status=', '')
                                        # v1['statuss'] = x11
                                        # print(type(x11))
                                        dict1['statuss'].append(x11)
                                        # print(type(dict1['statuss']))
                                        # ques1[i]['statusss'].append(dict1['statuss'])
                                    if "status=" in i5:
                                        status_id = re.findall(r'status=\w{0,63}.*', i5)
                                        z12 = ''.join(status_id)
                                        z13 = z12.replace('status=', '')
                                        # v1['status_id'] = z13
                                        # print(type(z13))
                                        # status_id1 = re.findall(r'\s([a-zA-Z0-9]{3,8}.*)', line5)
                                        # print(z13)
                                        dict1['status_id'].append(z13)
                                        # print(type(dict1['status_id']))
                                        # ques1[i]['statusss_id'].append(dict1['status_id'])

                                    if "relay=" in i5:
                                        relayss = re.findall(
                                            r'relay=[a-zA-Z0-9._-]{0,63}\[\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\]:\d{1,5}',
                                            i5)
                                        x12 = ''.join(relayss)
                                        y12 = x12.replace('relay=', '')
                                        # print(y4)
                                        dict1['relayss'].append(y12)

                            if j2 == 'statuss':
                                # print('hi')
                                v1[j2].append(dict1['statuss'])
                                # print(v1[j2])
                            if j2 == 'status_id':
                                v1[j2].append(dict1['status_id'])

                            # print(v1[j2])
# print(aligned_messages)