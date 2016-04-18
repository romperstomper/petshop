import re
import sys
from collections import defaultdict
#-----------1source_ip---------2time_stamp---3uri----4status--5size
regex = r'^([(\d\.)]+).* - - \[(.*?)\] ".* (/.*?) .*" (\d+) (\d+)'
def logparse(n):
  success_count = 0
  result = {}
  result['ips'] = set()
  sizes = []
  with open(n) as fd:
    for line in fd:
      m = re.search(regex, line)
      if m:
        result['ips'].add(m.group(1))
        try:
          sizes.append(m.group(5))
        except IndexError:
          print m.groups()
        if m.group(4) == '200':
          success_count += 1
        if m.group(4) == '404':
          result['failure'] = m.group(3)
  all_sizes = [int(x) for x in sizes]
  total_size = sum(all_sizes)
  avg_size = total_size/len(sizes)
  return success_count, result.get('failure'), len(result.get('ips')), max(all_sizes), avg_size

if __name__=='__main__':
  print logparse(sys.argv[1])
