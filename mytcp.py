import socket
class myclass(object):
  def mysend(self):
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.s.connect(('localhost', 2878))
    self.s.sendall('testsend')
    self.s.close
