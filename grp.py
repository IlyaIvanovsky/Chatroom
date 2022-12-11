import Kitten 

X = 0
在线用户数 = 0
红包个数 = 0
每份 = 0

def when_clicked():
  if (红包 != 0) :
    我的钱 = 我的钱 + (红包);
    红包 = 0;
    X = str(Kitten.value_of_current_time('year')) + str('.') + str(Kitten.value_of_current_time('month')) + str('.') + str(Kitten.value_of_current_time('date')) + str(' ') + str(Kitten.value_of_current_time('week')) + str(' ') + str(Kitten.value_of_current_time('hour')) + str(':') + str(Kitten.value_of_current_time('minute')) + str(':') + str(Kitten.value_of_current_time('second')) + str(' ') + str('系统消息：') + str(Kitten.get_username()) + str('抢到了红包')
    上移()
  else :
    Kitten.print_say_for_sec('没红包', 0.3)
  if (红包 == 0) :
    X = str(Kitten.value_of_current_time('year')) + str('.') + str(Kitten.value_of_current_time('month')) + str('.') + str(Kitten.value_of_current_time('date')) + str(' ') + str(Kitten.value_of_current_time('week')) + str(' ') + str(Kitten.value_of_current_time('hour')) + str(':') + str(Kitten.value_of_current_time('minute')) + str(':') + str(Kitten.value_of_current_time('second')) + str(' ') + str('系统消息：红包已经抢完了')
    Kitten.send_signal('update')
