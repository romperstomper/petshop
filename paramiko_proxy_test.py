import paramiko

from google3.pyglib import app
from google3.pyglib import flags
from google3.pyglib.concurrent import executor_service

FLAGS = flags.FLAGS


def main(unused_argv):
  client = paramiko.SSHClient()
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  # Emulate slow-interacting network with delay of 2 seconds.
  proxy = paramiko.ProxyCommand('nc -i 2 localhost 22')

  exec_service = executor_service.ExecutorService('Killer')
  # Kill the proxy after 9 seconds to let banner exchange & kex.
  # Allow 4 packets + 1 second just in case.
  exec_service.Schedule(9, lambda: proxy.close())

  try:
    client.connect(hostname='localhost', sock=proxy, timeout=30)
    print 'connected'
  except Exception as e:
    raise
  finally:
    client.close()

if __name__ == '__main__':
  app.run()

