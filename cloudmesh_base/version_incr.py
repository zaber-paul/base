from cloudmesh_base.Shell import Shell

import fileinput
import sys
import shutil

class version_incr(object):

    filename = None

    TAG = "version ="
    #TAG = "__version__

    def which(self, name):
        if name.startswith("r"): # release
            return 2
        elif name.startswith("mi"): # minor
            return 1
        elif name.startswith("ma"): # major
            return 0
        else:
            return 2

    def __init__(self, filename, kind="release"):
        self.filename = filename
        self.version = None
        self.position = self.which(kind)

    def incr(self):
        """reads the version number"""
        print self.filename
        f_in = open(self.filename, "r")
        f_out = open("tmp", "w")
        for line in f_in:
            if line.startswith('version ='):
                v = line.split("=")[1].strip()
                v = v.replace('"', '')
                self.version = v.split('.')
                self.version[self.position] = str(int(self.version[self.position]) + 1)
                f_out.write('version = "{:}"\n'.format(".".join(self.version)))
            else:
                f_out.write(line)
        f_in.close()
        f_out.close()
        shutil.move("tmp", self.filename)

        print v
        print self.version

if __name__ == "__main__":
    v = version_incr("test.txt", kind="release")
    v.incr()