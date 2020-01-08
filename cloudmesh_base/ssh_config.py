from __future__ import print_function
import os
from cloudmesh_base.Shell import Shell
import json


class ssh_config(object):

    def __init__(self, filename=None):
        if filename is not None:
            # load
            pass
        else:
            filename = "~/.ssh/config"

        self.filename = os.path.expanduser(filename)
        self.load()

    def names(self):
        found_names = []
        with open(self.filename) as f:
            content = f.readlines()
        for line in content:
            line = line.strip()
            if " " in line:
                attribute, value = line.split(" ", 1)
                attribute = attribute.strip()
                value = value.strip()
                if attribute.lower() in ['host']:
                    found_names.append(value)
        return found_names

    def load(self):
        """list the hosts defined in the ssh config file"""
        with open(self.filename) as f:
            content = f.readlines()
        content = [" ".join(x.split()) .strip('\n').lstrip().split(' ', 1) for x in content] 
        # removes duplicated spaces, and splits in two fields, removes leading spaces
        hosts = {}
        host = "NA"
        for line in content:
            if line[0].startswith('#') or line[0] is '':
                pass  # ignore line
            else:
                attribute = line[0]
                value = line[1]
                if attribute in ['Host ', 'host ']:
                    host = value
                    hosts[host] = {'host': host}
                else:
                    # In case of special configuration lines, such as port
                    # forwarding,
                    # there would be no 'Host india' line.
                    if host in hosts:
                        hosts[host][attribute] = value
                    # pass
        self.hosts = hosts

    def list(self):
        return self.hosts.keys()

    def __str__(self):
        return json.dumps(self.hosts, indent=4)
        
    def status(self):
        """executes a test with the given ssh config if a login is possible"""

    def login(self, name):
        """logs into the host defined by name in ssh config into an interactive shell"""
        os.system("ssh {0}".format(name))

    def execute(self, name, command):
        """executes the command on the named host"""
        if name in ["localhost"]:
            r = '\n'.join(Shell.sh("-c", command).split()[-1:])
        else:
            r = '\n'.join(Shell.ssh(name, command).split()[-1:])
        return r
    
    def local(self, command):
        return self.execute("localhost", command)

    def username(self, host):
        if host in self.hosts:
            return self.hosts[host]["User"]
        else:
            return None

if __name__ == "__main__":
    hosts = ssh_config()
    print(hosts.list())
    print(hosts)

    # hosts.login("india")

    r = hosts.execute("india", "hostname")
    print(r)

    r = hosts.execute("localhost", "hostname")
    print(r)

    r = hosts.local("hostname")
    print(r)
