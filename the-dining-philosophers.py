from threading import *
class DiningPhilosophers:
    def __init__(self):
        """
        // philosopher 0 - forks 4 and 0,
        // philosopher 1 - forks 0 and 1,
        // philosopher 2 - forks 1 and 2,
        // philosopher 3 - forks 2 and 3,
        // philosopher 4 - forks 3 and 4
        """
        self.f = [Lock(),Lock(),Lock(),Lock(),Lock()]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   p: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        if not p:
            self.f[p].acquire()
            self.f[p-1].acquire()
        else:
            self.f[p-1].acquire()
            self.f[p].acquire()
        pickLeftFork()
        pickRightFork()
        eat()
        putRightFork()
        putLeftFork()
        self.f[p].release()
        self.f[p-1].release()
