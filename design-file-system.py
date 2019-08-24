import os
class FileSystem(object):

    def __init__(self):
        self.h = {}
        self.h['/'] = 0

    def create(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        if os.path.dirname(path) not in h: return False
        if path in h: return False
        h[path] = value
        return True

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        if path not in h:return -1
        else: return h[path]
        
