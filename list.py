import Kitten 

X = 0
在线用户数 = 0
红包个数 = 0
每份 = 0

def when():
  while True:
    if (Kitten.is_touched('Self', 'mouse') and Kitten.is_mouse_up()):
      Kitten.show_ranking(我的钱)
