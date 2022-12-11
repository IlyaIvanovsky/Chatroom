import Kitten 

X = 0
在线用户数 = 0
红包个数 = 0
每份 = 0

def when_clicked():
  if (Kitten.get_username() == 'H.I.M.') :
    Kitten.print_ask('请输入功能代码')
    if (Kitten.get_answer()
     == 'money') :
      Kitten.print_ask('设置自己的钱数为')
      我的钱 = Kitten.get_answer()
      ;
    elif (Kitten.get_answer()
     == 'ban') :
      Kitten.print_ask('封禁用户名')
      封禁账号.append(Kitten.get_answer()
      )
      X = str(Kitten.value_of_current_time('year')) + str('.') + str(Kitten.value_of_current_time('month')) + str('.') + str(Kitten.value_of_current_time('date')) + str(' ') + str(Kitten.value_of_current_time('week')) + str(' ') + str(Kitten.value_of_current_time('hour')) + str(':') + str(Kitten.value_of_current_time('minute')) + str(':') + str(Kitten.value_of_current_time('second')) + str(' ') + str('系统消息：') + str(Kitten.get_answer()
      ) + str('已经被封禁')
    elif (Kitten.get_answer()
     == 'pardon') :
      Kitten.print_ask('解除封禁用户名')
      del 封禁账号[封禁账号.index(Kitten.get_answer()
      ) - 1]
      X = str(Kitten.value_of_current_time('year')) + str('.') + str(Kitten.value_of_current_time('month')) + str('.') + str(Kitten.value_of_current_time('date')) + str(' ') + str(Kitten.value_of_current_time('week')) + str(' ') + str(Kitten.value_of_current_time('hour')) + str(':') + str(Kitten.value_of_current_time('minute')) + str(':') + str(Kitten.value_of_current_time('second')) + str(' ') + str('系统消息：') + str(Kitten.get_answer()
      ) + str('已经被解封')
    elif (Kitten.get_answer()
     == 'delete') :
      del 消息[0]
    else :
  else :
    Kitten.print_say_for_sec('你根本不是腐竹，点啥点', 2)
