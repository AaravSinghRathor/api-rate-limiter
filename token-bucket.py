from datetime import datetime

class TokenBucket:
    def __init__(self, capacity: int, refill_rate: float) -> None:
        self.capacity = capacity  # this handles burst of traffic
        self.refill_rate = refill_rate
        self.current_tokens = self.capacity
        self.last_refill_time = datetime.now()

    def allow_request(self):
        current_time = datetime.now()
        print(f"Current time: {current_time}")

        self.refill_token(current_time)

        if self.current_tokens >= 1:
            print("request allowed")
            self.current_tokens -= 1
            return True

        print("request not allowed")
        return False

    def refill_token(self, current_time):
        time_passed = int((current_time - self.last_refill_time).total_seconds())
        self.current_tokens = min(self.capacity, self.current_tokens + time_passed * self.refill_rate)
        self.last_refill_time = current_time


def main():
    '''
    refill rate = (refill count) / (refill interval)
    tokens / sec
    '''
    bucket = TokenBucket(2, 0.5)  # capacity 5, refill rate 0.5 tokens/sec

    while True:
        print(f"Current tokens: {bucket.current_tokens}")
        _ = input()
        bucket.allow_request()

if __name__ == "__main__":
    main()


