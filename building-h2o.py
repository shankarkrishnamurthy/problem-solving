from collections import deque
class H2O:
    def __init__(self):
        self.hq, self.oq = deque(), deque()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.hq.append(releaseHydrogen)
        self.h2o()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.oq.append(releaseOxygen)
        self.h2o()
        
    def h2o(self) -> None:
        if len(self.hq) > 1 and len(self.oq) > 0:
            self.hq.popleft()()
            self.hq.popleft()()
            self.oq.popleft()()
