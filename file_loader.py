import time

def get_items(fileName):
    start = time.time()
    def elapsed():
        return time.time() - start
    items = []
    f = open(fileName, 'r')
    while True:
        block = f.read(65536)
        if not block:
             break
        block = block.split('\n')
        items.extend(block)

    linecount = len(items)

    print ('    file "%s" contains %s rows. [%.3fs]' % (fileName, linecount, elapsed()))
    return items
