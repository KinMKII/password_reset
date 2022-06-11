password = 'a123456' #設定密碼
x = 3 #可錯誤次數

while x > 0:
    x = x - 1
    input_password = input('請輸入密碼: ')
    if input_password == password:
        print('登入成功!')
        break #逃出迴圈
    else:
        print('密碼錯誤! ')
        if x > 0 :
            print('還有', x , '次機會')
        else:
            print('多次錯誤, 請於24小時後重試')