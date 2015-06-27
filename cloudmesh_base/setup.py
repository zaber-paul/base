from cloudmesh_base.Shell import Shell

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

def os_execute(commands):
    for command in commands.split("\n"):
        command = command.strip()
        print (command)
        os.system(command)

def get_version_from_git():
    return Shell.git('tag').split("\n")[-1]
