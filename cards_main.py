#! /usr/bin/python3
# 综合应用——名片管理系统
import cards_tools

while True:

    # TODO 显示功能菜单
    cards_tools.show_menu()

    action_str = input("请输入操作功能：")
    print("您输入的是【%s】" % action_str)
    if action_str in ["1", "2", "3"]:
        # 使用pass关键字，表示一个占位符，保证程序结代码结构正确
        # 新增名片
        if action_str == "1":
            cards_tools.new_card()

        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()

        # 查询名片
        elif action_str == "3":
            cards_tools.search_card()

    # 0退出系统
    elif action_str == "0":
        print("欢迎再次使用名片管理系统")
        break

    else:

        print("您输入的不正确，请重新输入")
