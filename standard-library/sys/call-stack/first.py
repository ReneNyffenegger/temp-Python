import sys

def print_frame(frames):
    frame_addr, frame = next(iter(frames.items()))

    print(f'frame address: {frame_addr}')
    print(str(frame))


def h(i):

#   print(sys._current_frames().keys())
    for k,v in sys._current_frames().items():
        print(k)
        print(dir(v))
    print(i)

def f(a):

#   print(sys._current_frames())

    x = 42

    def g(b):
        print(sys._current_frames())
        x = 'hello world'

        h(b+3)

    g(a*2)

print_frame(sys._current_frames())
# f(3)
