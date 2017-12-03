from datetime import datetime

def sort_by_node_time(data):
    # sort descending by node time
    return sorted(data, cmp=lambda x,y: cmp(y.node_time, x.node_time))

def sort_by_nonitor_time(data):
    # sort descending by monitor time
    return sorted(data, cmp=lambda x,y: cmp(y[2],x[2]))

class Notification():
    def __init__(self, line):
        data = line.split()
        if (len(data)==4):
            self.monitor_time = int(data[0])
            self.node_time = int(data[1])
            self.node_name = data[2]
            self.msg = data[3]
            self.other_node_name = ''
        elif (len(data)==5):
            self.monitor_time = int(data[0])
            self.node_time = int(data[1])
            self.node_name = data[2]
            self.msg = data[3]
            self.other_node_name = data[4]
    def __repr__(self):
        return "{} {} {} {} {}".format(self.monitor_time,
                                        self.node_time,
                                        self.node_name,
                                        self.msg,
                                        self.other_node_name)
    def get_reason(self):
        return "{} {} {}".format(self.node_name,
                                    self.msg,
                                    self.other_node_name)
    def get_about(self):
        if (not self.other_node_name):
            return [self.node_name]
        else:
            return [self.node_name, self.other_node_name]
    def get_status(self, node_name):
        if (self.node_name == self.node_name):
            return "ALIVE"
        elif (self.msg == "LOST"):
                return "DEAD"
        elif (self.msg == "FOUND"):
            return "ALIVE"

class Node():
    def __init__(self, node_name, notification):
        self.name = node_name
        self.notifications = [notification]
    def __repr__(self):
        st = ''
        for n in self.notifications:
            st = st + str(n) + "\n"
        return st
    def get_status(self):
        if (len(self.notifications) > 1):
            # Check notifications to see if they agree on the state
            self.status = self.get_latest_notification().get_status(self.name)
            for notification in self.notifications:
                current = notification.get_status(self.name)
                if (self.status is not current):
                    self.status = 'UNKNOWN'
                    break;
            print(self.show_status(notification))
        else:
            latest = self.get_latest_notification()
            self.status = latest.get_status(self.name)
            print(self.show_status(latest))
    def show_status(self, notification):
        return "{} {} {} {}".format(self.name, self.status, notification.monitor_time, notification.get_reason())
    def get_latest_notification(self):
        return self.notifications[0]
    def is_later(self, notification):
        return notification.node_time - self.get_latest_notification().node_time
    def replace_notification(self, notification):
        self.notifications = [notification]
    def add_notification(self, notification):
        time_difference = self.is_later(notification)
        if (time_difference > 0):
            if (time_difference > 50):
                self.replace_notification(notification)
            else:
                self.notifications.append(notification)
                self.notifications = sort_by_node_time(self.notifications)
        # print(self.name, self.notifications)

def read_file(inputfile):
    nodes = {}
    in_file = open(inputfile, "r")
    for line in in_file:
        notification = Notification(line)
        for node_name in notification.get_about():
            if (node_name in nodes):
                nodes[node_name].add_notification(notification)
            else:
                nodes[node_name] = Node(node_name, notification)
    in_file.close()
    return nodes

def debug_show_nodes(nodes):
    for node_name in nodes:
        print(node_name)
        print(nodes[node_name])
