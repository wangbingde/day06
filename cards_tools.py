# 记录所有名片字典
card_list = []


def show_menu():
    """显示功能菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("新增名片")
    # 1.提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")
    # 2.建立名片字典
    card_dict = {
        "name": name_str,
        "phone": phone,
        "qq": qq_str,
        "email": email_str
    }
    # 3.将名片字典添加到字典列表中
    card_list.append(card_dict)
    print(card_list)

    # 4.提示输入成功
    print("添加%s的名片成功！" % name_str)


def show_all():
    """显示全部"""
    print("-" * 50)
    print("功能：显示全部")

    # 判断是否有名片，如果没有提示并返回
    if len(card_list) == 0:
        print("当前没有名片，请使用功能1新增名片")
        return

    # 打印表头
    print("姓名\t\t电话\t\tqq\t\t邮箱")
    print("=" * 50)

    # 遍历名片列表，依次输出名片字典
    for card_dict in card_list:
        tuple = (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"])
        print("%s\t\t%s\t\t%s\t\t%s" % tuple)


def search_card():
    """查询名片"""
    print("-" * 50)
    print("查询名片")
    if len(card_list) == 0:
        print("当前没有名片，请使用功能1新增名片")
        return

    # 输入要搜索的姓名
    find_name = input("请输入要查询的名片姓名：")

    # 遍历名片列表，查询要搜索的姓名，有则输出，若没有则提示
    for card_dict in card_list:

        if card_dict["name"] == find_name:

            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            tuple = (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"])
            print("%s\t\t%s\t\t%s\t\t%s" % tuple)

            # TODO 针对找到的名片进行修改和删除操作
            card_deal(card_dict)

            break

        else:
            print("没有找到%s的名片" % find_name)


def card_deal(find_dict):
    """修改和删除名片"""
    # 提示用户所要执行的操作
    action_str = input("请输入要执行的操作"
                       " [1] 修改 [2] 删除 [0] 返回：")

    if action_str == "1":

        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ：")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱：")
        print("名片修改成功")

    elif action_str == "2":

        card_list.remove(find_dict)
        print("删除名片")


def input_card_info(dict_value, tip_message):

    """
    输入名片信息
    :param dict_value: 字典中原有值
    :param tip_message: 输入的提示信息
    :return: 有修改则返回修改内容，否则返回原有内容
    """
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
