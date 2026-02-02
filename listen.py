from pynput.mouse import Listener
def display_position_of_mouse(x,y):
    print("position of current mouse is {0}".format((x,y)))

with Listener(on_move=display_position_of_mouse) as l:
    l.join()


