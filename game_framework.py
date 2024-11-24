class GameState:

    running = None
    stack = None


def change_mode(mode):
    global stack
    if (len(stack) > 0):
        # execute the current mode's exit function
        stack[-1].exit()
        # remove the current mode
        stack.pop()
    stack.append(mode)
    mode.enter()



def push_mode(mode):
    global stack
    if (len(stack) > 0):
        stack[-1].pause()
    stack.append(mode)
    mode.enter()



def pop_mode():
    global stack
    if (len(stack) > 0):
        # execute the current mode's exit function
        stack[-1].exit()
        # remove the current mode
        stack.pop()

    # execute resume function of the previous mode
    if (len(stack) > 0):
        stack[-1].resume()



def quit():
    global running
    running = False


def run(start_mode):
    global running, stack
    running = True
    stack = [start_mode]
    start_mode.enter()
    while (running):
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()
    # repeatedly delete the top of the stack
    while (len(stack) > 0):
        stack[-1].exit()
        stack.pop()
