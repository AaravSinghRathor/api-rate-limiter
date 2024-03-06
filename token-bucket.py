from datetime import datetime

class TokenBucket:
    def __init__(self, capacity: int, refill_tokens: int, interval: int) -> None:
        self.capacity = capacity  # this handles burst of traffic
        self.refill_tokens = refill_tokens
        self.current_tokens = self.capacity
        self.interval = interval
        self.last_refill_time = datetime.now()

    def allow_request(self):
        current_time = datetime.now()
        print(f"Current time: {current_time}")

        self.refill_token(current_time)

        if self.current_tokens > 0:
            print("request allowed")
            self.current_tokens -= 1
            return True

        print("request not allowed")
        return False

    def refill_token(self, current_time):
        diff = int((current_time - self.last_refill_time).total_seconds())
        if diff >= self.interval:
            refill_count = diff // self.interval
            self.current_tokens = min(self.capacity, self.current_tokens + refill_count * self.refill_tokens)
            self.last_refill_time = current_time


def main():
    bucket = TokenBucket(5, 3, 10)

    while True:
        print(f"Current tokens: {bucket.current_tokens}")
        _ = input()
        bucket.allow_request()

if __name__ == "__main__":
    main()


