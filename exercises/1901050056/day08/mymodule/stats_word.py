def stats_text_en(text):
    if type(text)==str:
        edit_text = text.replace(',', ' ').replace('.', ' ').replace('--', ' ').replace('!', ' ').replace('*', ' ')
        edit_text = edit_text.split()
    else:
        raise ValueError ('type of argumengt is not str')

#上面两句简单的将用户输入的字符串先筛选 再切片
    dir = {}
    for i in edit_text:#遍历列表取出每个元素给空字典用
        if (i >= '\u0041' and i <= '\u005a') or (i >= '\u0061' and i <= '\u007a'):
            if i in dir:
                dir[i]+=1#创建字典key并赋值
            else:
                dir[i]=1
    for key in dir:#将数据按照格式化打印出来
        print("字符中这个：'{}'字符出现了{}次".format(key,dir[key]))



    a_dir = sorted(dir.items(),key=lambda x:x[1],reverse=True)
#上面这句话是将字典中的数据进行排序
    list = []
    for i in a_dir:#排序好之后遍历取出字符就好，数字就不要了
        list.append(i[0])#取出符合条件的字符加入新的列表
    return list#返回这个排序好之后的字符

# print('==============分割线===================')

def stats_text_cn(text):
    if type(text)==str:
        edit_text = text.replace(',', ' ').replace('.', ' ').replace('--', ' ').replace('!', ' ').replace('*', ' ')
        edit_text = edit_text.split()
    else:
        raise  ValueError ('type of argumengt is not str')

# 上面两句简单的将用户输入的字符串先筛选 再切片
    dir = {}
    for i in edit_text:#遍历列表取出每个元素给空字典用
        if u'\u4e00' <= i <= u'\u9fa5':#判断输入字符是否为汉字
            if i in dir:
                dir[i] += 1#创建字典key并赋值
            else:
                dir[i] = 1
    for key in dir:#将数据按照格式化打印出来
        print("字符中这个：'{}'字符出现了{}次".format(key, dir[key]))

    a_dir = sorted(dir.items(), key=lambda x: x[1], reverse=True)
# 上面这句话是将字典中的数据进行排序
    list = []
    for i in a_dir:#排序好之后遍历取出字符就好，数字就不要了
        list.append(i[0])#取出符合条件的字符加入新的列表
    return list

#text = 'aaa,aaa,aaa,sdafasdf,sadfasdf,asdfsadf,你好,你好,你好,世界'
def stats_text(text):#将两个函数做成一个函数
    if type(text)==str:
        print(stats_text_en(text) + stats_text_cn(text))
    else:
        raise ValueError ('type of argumengt is not str')


#stats_text()#调用