import Kitten 

X = 0
在线用户数 = 0
红包个数 = 0
每份 = 0

def when_clicked():
  Kitten.print_ask('发多少钱？')
  if (我的钱 >= Kitten.get_answer()
  ) :
    红包 = 红包 + (Kitten.get_answer()
    );
    我的钱 = 我的钱 - (Kitten.get_answer()
    );
    X = str(Kitten.value_of_current_time('year')) + str('.') + str(Kitten.value_of_current_time('month')) + str('.') + str(Kitten.value_of_current_time('date')) + str(' ') + str(Kitten.value_of_current_time('week')) + str(' ') + str(Kitten.value_of_current_time('hour')) + str(':') + str(Kitten.value_of_current_time('minute')) + str(':') + str(Kitten.value_of_current_time('second')) + str(':') + str('有人发了红包')
    上移()
  else :
    Kitten.print_say_for_sec('钱不够', 1)
