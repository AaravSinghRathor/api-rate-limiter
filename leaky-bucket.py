from datetime import datetime

class LeakyBucket:
    def __init__(self, capacity: int, outflow_rate: float) -> None:
        self.capacity = capacity  # this handles burst of traffic
        self.outflow_rate = outflow_rate
        self.current_tokens = 0
        self.last_outflow_time = datetime.now()

    def allow_request(self):
        current_time = datetime.now()
        print(f"Current time: {current_time}")

        self.process_token(current_time)

        if self.capacity - self.current_tokens >= 1:
            print("request allowed")
            self.current_tokens += 1
            return True

        print("request not allowed")
        return False

    def process_token(self, current_time):
        time_passed = int((current_time - self.last_outflow_time).total_seconds())
        print(f"time since last process: {time_passed}")
        self.current_tokens = max(0, self.current_tokens - time_passed * self.outflow_rate)
        self.last_outflow_time = current_time


def main():
    '''
    outflow rate = processed requests/sec
    tokens / sec
    '''
    bucket = LeakyBucket(5, 2)  # capacity 5, outflow rate 2 tokens/sec

    while True:
        print(f"Current tokens: {bucket.current_tokens}")
        _ = input()
        bucket.allow_request()

if __name__ == "__main__":
    main()


