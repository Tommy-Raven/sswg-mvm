import time
from utils import log

class CLIDashboard:
    def __init__(self):
        self.start_time = time.time()
        self.cycles = 0
        self.success = 0
        self.failures = 0

    def record_cycle(self, success=True):
        self.cycles += 1
        if success:
            self.success += 1
        else:
            self.failures += 1

    def render(self):
        elapsed = time.time() - self.start_time
        success_rate = (self.success / max(1, self.cycles)) * 100
        log("----- CLI DASHBOARD -----")
        print(f"Elapsed Time: {elapsed:.2f}s")
        print(f"Total Cycles: {self.cycles}")
        print(f"Successful:  {self.success}")
        print(f"Failed:      {self.failures}")
        print(f"Success Rate: {success_rate:.1f}%")
        log("--------------------------")
