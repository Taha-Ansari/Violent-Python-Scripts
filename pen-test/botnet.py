#!/usr/bin/python

import paramiko
 
class Bot:
	def __init__(self, ip, username, password):
		self.ip = ip
		self.username = username
		self.password = password

class BotNet:
	def __init__(self):
		self.botlist = []

	def add_bot(self, ip,username,password):
		new_bot = Bot(ip, username, password)
		self.botlist.append(new_bot)

	def command_bot(self, ip,username, password, command):
		print("\nAttempting connection with: {}".format(ip))
		client = paramiko.SSHClient()
		try:
			client.load_system_host_keys()
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			client.connect(ip, username=username, password=password)
			stdin, stdout, stderr = client.exec_command(command)
			stdin.write(password+'\n')
			stdin.flush()
			print( "\nOutput from {}: ".format(ip))
			for line in stdout:
				print(line.replace("\n",""))
			for line in stderr:
				print(line.replace("\n",""))
			print( "-------------------------------------------------\n" )
		except:
			print("\nConnection FAILED: {}".format(ip))
		client.close()

	def command_net(self, command):
		for bot in self.botlist:
			self.command_bot(bot.ip, bot.username, bot.password, command)

# Example usage
if __name__ == "__main__":
	# Create Botnet object
	bot_net = BotNet()
	# Add bots to botnet
	bot_net.add_bot('', '', '')
	bot_net.add_bot('', '', '')
	# Commands each bot added to the net
	bot_net.command_net("ls -la")