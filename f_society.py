import paramiko
import socket

def runSshCmd(hostname, username, password, cmd, timeout=None):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password,
        allow_agent=False, look_for_keys=False, timeout=timeout)

    stdin, stdout, stderr = client.exec_command(cmd)
    data = stdout.read()
    print(data)

    client.close()

fo = open("server.lst", "r")
hosts = fo.readlines()
fo.close()

for h in hosts:
    try:
        runSshCmd(h.rstrip(), "root", "", "uname -a")
    except paramiko.AuthenticationException, e:
        print("Host %s result: %s" % (h.rstrip(), e))
    except paramiko.SSHException, e:
        print(e)
    except socket.error, e:
        print(e)
