import os  # 导入系统操作模块

def verify_name():
    """检查用户名是否正确"""
    # 获取用户输入的名字
    name = input("输入exit退出,请输入你的名字: ")
    
    # 如果输入exit就退出程序
    if name == 'exit':
        exit()
    
    # 检查名字是否是Dynamo
    if name != 'Dynamo':
        print('无此名字,登录失败,你输入的名字是:', name)
        return False
    
    print('名字正确,登录中')
    # 如果名字正确,继续验证密码
    return verify_password()

def verify_password():
    """检查密码是否正确"""
    # 获取用户输入的密码
    password = input("请输入密码: ")
    
    # 检查密码是否正确
    if password != '114514':
        print('密码错误,登录失败,你输入的密码是:', password)
        return False
    
    print("密码正确,登录中")
    print('登录成功')
    # 密码正确后进入已登录状态
    logged_in()

def operation():
    """执行系统操作"""
    print('DynamoOS v0.5')  # 显示系统版本
    # 等待用户输入命令并执行
    running = True
    while running:
        command = input("DynamoOS:$ ")
        if command == 'dlogout':
            running = False
        elif command == 'cuser':
            print("当前用户为:", os.getlogin())
        else:
            os.system(command)
def logged_in():
    """登录成功后的操作"""
    # 显示当前所在目录
    print("当前目录为:", os.getcwd())
    # 进入命令操作界面
    operation()
    return True

# 主程序循环：不断尝试登录直到成功
while not verify_name():
    continue