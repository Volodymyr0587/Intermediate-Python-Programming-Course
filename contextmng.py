from contextlib import contextmanager

""" with open('notes', 'w') as file:
    file.write('some todo...') """
    
""" class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename
        
    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file
        
    def __exit__(self, exc_type, exc_value, exc_traceback):   
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handled')
        #print('exc: ', exc_type, exc_value)
        print('exit')
        return True
        
        
with ManagedFile('notes') as file:
    print('do some stuff...')
    file.write('some todo...')
    file.some()
print('continuing') """


@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()
        
        
with open_managed_file('notes2') as file:
    file.write('Some text...')