class Parser(object):
    def __init__(self, filename):
        self._filename = filename 
        self._file = file(filename, 'r')
        self._lines = self._file.readlines()
    
    @property
    def lines(self):
        return self._lines
