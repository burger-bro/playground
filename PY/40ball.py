import random

balls = [i for i in range(1, 21)]*2
random.shuffle(balls)

max_draw = -1

def draw_balls(balls):
    global max_draw
    random.shuffle(balls)
    draw = set()
    for b in balls:
        if b not in draw:
            draw.add(b)
        else:
            return False
        max_draw = max(max_draw, len(draw))
        if len(draw) == 20:
            break
    return True

def monte_carole():
    times = 10000000
    cnt = 0
    for i in range(times):
        if draw_balls(balls):
            cnt += 1
    print("prob: ", cnt/times)
    print("max draw: ", max_draw)

monte_carole()
