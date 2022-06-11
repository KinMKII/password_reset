password = 'a123456' #設定密碼
x = 3    #可錯誤次數

while True:
    input_password = input('請輸入密碼: ')
    if input_password == password:
        print('登入成功!')
        break    #逃出迴圈
    else:
        x = x - 1
        print('密碼錯誤! 還有', x , '次機會')
        if x == 0:
            break