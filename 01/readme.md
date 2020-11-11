# Uptime Sensor Tool Challenge

> Create a tool that will ping a destination every 2 seconds and log the results of the ping


```python
#!/usr/bin/env python3

# Title: ops-401d1: Challenge 01
# Author: Jake Overall
# Date: 10/6/2020
# Purpose: Ping Test with log writter

log = ["\n----------------------PINGR_START----------------------\n"]

def setup(args):

def do_work(ip):

def exit_call(ip):

def delay():

def main(args=[""]):
    ip = setup(args)
    while True:
        do_work(ip)

def signal_handler(signal, frame):
  print(" Okay, Bye 👋 ")
```


### Log Output Example

```
----------------------PINGR_START----------------------
[ATTEMPTING TO PING] 8.8.8.8[2020-10-06 18:44:34.618452] ✅ Reply from 8.8.8.8, 9 bytes in 26.02ms

Round Trip Times min/avg/max is 26.02/26.02/26.02 ms | 8.8.8.8
[2020-10-06 18:44:36.665216] ✅ Reply from 8.8.8.8, 9 bytes in 23.38ms

Round Trip Times min/avg/max is 23.38/23.38/23.38 ms | 8.8.8.8
[2020-10-06 18:44:38.705934] ✅ Reply from 8.8.8.8, 9 bytes in 22.05ms

Round Trip Times min/avg/max is 22.05/22.05/22.05 ms | 8.8.8.8
[2020-10-06 18:44:40.742453] ✅ Reply from 8.8.8.8, 9 bytes in 21.31ms

Round Trip Times min/avg/max is 21.31/21.31/21.31 ms | 8.8.8.8
[2020-10-06 18:44:42.780185] ✅ Reply from 8.8.8.8, 9 bytes in 24.59ms

Round Trip Times min/avg/max is 24.59/24.59/24.59 ms | 8.8.8.8
----------------------PINGR_END----------------------

----------------------PINGR_START----------------------
[ATTEMPTING TO PING] 8.8.8.99[2020-10-06 18:45:10.901797] ❌ Request timed out

Round Trip Times min/avg/max is 2000/2000/2000 ms | 8.8.8.99
[2020-10-06 18:45:14.921648] ❌ Request timed out

Round Trip Times min/avg/max is 2000/2000/2000 ms | 8.8.8.99
[2020-10-06 18:45:18.937214] ❌ Request timed out

Round Trip Times min/avg/max is 2000/2000/2000 ms | 8.8.8.99
[2020-10-06 18:45:22.952564] ❌ Request timed out

Round Trip Times min/avg/max is 2000/2000/2000 ms | 8.8.8.99
----------------------PINGR_END----------------------
```