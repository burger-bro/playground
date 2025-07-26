import pyautogui
import time

# 调整这些参数尝试
pyautogui.PAUSE = 0.1  # 默认是0.1
pyautogui.FAILSAFE = False


def move(direction, repeat=1):
    for _ in range(repeat):
        pyautogui.keyDown(direction)
        time.sleep(0.01)  # 保持按下状态
        pyautogui.keyUp(direction)
        time.sleep(0.01)
        print(direction)

key_map = {'u':"up", 'd':"down", 'l':"left", 'r':"right"}
key_map_r = {'d':"up", 'u':"down", 'l':"left", 'r':"right"}
def sequence_move(sequence, invert=False):
    seq = sequence.split(' ')
    for ss in seq:
        key = key_map[ss[0]] if not invert else key_map_r[ss[0]]
        repeat = int(ss[1:])
        move(key, repeat)

"""
1 d2 r2 u4 l2 d2
            中间
2 d2 r(2+3) u2 l2 d2 l3 u2
"""

def hanoi(n, dirc=False):  # dir: False->up  True->down
    if n == 1:
        sequence_move("d2 r2 u4 l2 d2", dirc)
        return
    else:
        hanoi(n-1, dirc)
        sequence_move(f"d2 r{2+(n-1)*3} u2 l2 d2 l{(n-1)*3} u2", dirc)
        hanoi(n-1, not dirc)
        sequence_move(f"u2 r{(n-1)*3} d2 r2 u2 l{2+(n-1)*3} d2", dirc)
        hanoi(n-1, dirc)

time.sleep(2)
hanoi(9)


