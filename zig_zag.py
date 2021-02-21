import time, sys #makes our zig zag move every fraction of a second
indent = 0
IndentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('*******')
        time.sleep(0.1)

        if IndentIncreasing: #move in one direction
            indent = indent + 1
            if indent == 20:
                IndentIncreasing = False
        else: #move in the opposite direction
            indent = indent - 1
            if indent == 0:
                IndentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
