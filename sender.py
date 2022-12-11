import Kitten 

X = 0
在线用户数 = 0
红包个数 = 0
每份 = 0

def 发送消息():
  if Kitten.get_username() in 封禁账号 :
    Kitten.print_say_for_sec('你被封号了', 2)
  else :
    Kitten.print_ask('')
    X = str(Kitten.value_of_current_time('year')) + str('.') + str(Kitten.value_of_current_time('month')) + str('.') + str(Kitten.value_of_current_time('date')) + str(' ') + str(Kitten.value_of_current_time('week')) + str(' ') + str(Kitten.value_of_current_time('hour')) + str(':') + str(Kitten.value_of_current_time('minute')) + str(':') + str(Kitten.value_of_current_time('second')) + str(' ') + str(Kitten.get_username()) + str('说：') + str(Kitten.get_answer()
    )
    我的钱 = 我的钱 + 1;
    Kitten.send_signal('update')

def when():
  while True:
    if (Kitten.is_key_pressed(86) and Kitten.is_key_pressed(32)):
      发送消息()

def when_clicked():
  发送消息()
