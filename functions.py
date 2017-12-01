from datetime import datetime

def read_file(inputfile):
    notifs = []
    inf = open(inputfile, "r")
    for line in inf:
        ll = line.split()
        ll[0] = int(ll[0])
        ll[1]= int(ll[1])
        notifs.append(ll)
        # print ll
    inf.close()
    return notifs

def sort_by_node_time(notifs):
    return sorted(notifs, cmp=lambda x,y: cmp(x[1],y[1]))

def sort_by_nonitor_time(data):
    return sorted(data, cmp=lambda x,y: cmp(y[2],x[2]))

def show(data):
    st = ''
    for row in data:
        for elem in row:
            st = st + str(elem) + " "
        st = st + "\n"
    return st

def parse(data):
    nodes = {}
    res = []
    for notif in data:
        monitor_time = notif[0]
        node = notif[2]
        msg = notif[3]
        if (len(notif) > 4):
            other_node = notif[4]
            if (msg == "LOST"):
                # implicitly node is ALIVE
                # other_node is DEAD
                nodes[node] = [node, "ALIVE", monitor_time, node, msg, other_node]
                nodes[other_node] = [other_node, "DEAD", monitor_time, node, msg, other_node]
            if (msg == "FOUND"):
                # implicitly node is ALIVE
                # other_node is ALIVE
                nodes[node] = [node, "ALIVE", monitor_time, node, msg, other_node]
                nodes[other_node] = [other_node, "ALIVE", monitor_time, node, msg, other_node]
        elif (msg == "HELLO"):
            # ALIVE
            nodes[node] = [node, "ALIVE", monitor_time, node, msg]
    for n in nodes:
        res.append(nodes[n])
    return sort_by_nonitor_time(res)
