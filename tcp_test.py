import unittest
import mock
import mytcp

class TestTcp(unittest.TestCase):

  #@mock.patch('socket.socket')
  #def test_mysend(self, mock_connect):
  with mock.patch('socket.socket') as mock_socket:
    c = mytcp.myclass()
    c.mysend()
    c.s.connect.assert_called_with()


#class MyClass(object):
#  def __init__(self):
#    self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    self.tcp_socket.connect('0.0.0.0', '6767')
#
#class Testnew(unittest.TestCase):
#  @mock.patch.object('socket.socket')
#  def test_newsend(self, mock_socket):
#    n = MyClass()
#    n.tcp_socket.connect.assert_called_with()
  


if __name__ == '__main__':
  unittest.main()
