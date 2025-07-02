import random
import time
from prometheus_client import Summary, start_http_server, Counter, Gauge

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
MY_COUNTER = Counter('my_counter', ["name", "age"])
MY_GAUGE = Gauge('my_gauge', 'My gauge')

@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    MY_COUNTER.labels("John", 20).inc(5)
    MY_COUNTER.labels(name="Jane", age=21).inc(10)
    MY_GAUGE.set(10)
    MY_GAUGE.inc(5)
    MY_GAUGE.dec(3)
    time.sleep(t)
    
def main():
    start_http_server(8000)
    process_request(random.random())
    while True:
        A=1

if __name__ == "__main__":
  main()