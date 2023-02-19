# i=0
# while i<10:
#     i=i+1
#     if i==7:
#         continue 跳出本次循环 继续下一个 break是结束所有循环
#     print(i)
#求 1-100的和
# i=0
# sum=0
# while i<=100:
#     i=i+1
#     sum=sum+i
# pr

# for i in range(4):
#     age=int(input("请输入你的炼灵"))
#     if age==30:
#         print("恭喜你猜对了")
#         break
#     if i<3:
#         print("答错了，你还有%d次机会"%(3-i))
#     else:
#         print("三次都打错，退出系统")
# h=10
# sum=0
# for i in range(9):
#     h=h/2
#     sum=sum+h*2
# print(sum)
# import random
# num=random.randint(1,100)
# print(num)
# for i in range(5):
#     guess_num=int(input("请输入你的数字"))
#     if num==guess_num:
#         print("恭喜中奖")
#         break
#     else:
#         if guess_num>num:
#             print("大了")
#         else:
#             print("小了")
#
# 99乘法表
# for i in range(1,10):
#     # for j in range(i,10):
#     #     print(f"{i}*{j}={i*j}",end="\t")
#     # print()
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and i!=k and k!=j:
#                 print(i*100+j*10+k)
# for i in range(1,1000):
#     for j in range(1,i):
#         a=[]
#         if i%j==0:
#             a.append(j)
#             print(a)
# sum=0
# for i in range(1,100):
#     if i!=3 and i%10!=3:
#         sum=sum+i
# print(sum)
# zhufeng=8848130
# houdu=0.08
# count=0
# while houdu<=zhufeng:
#     houdu=houdu*2
#     count=count+1
# print(count)
# num=int(input("请输入你的数"))
# sum=0
# while num!=0:
#     sum=sum+num%10
#     num=num//10
# print(sum)
#石头0 剪刀1 布2
# import random
# sum = 0
# sum1 = 0
# while True:
#     num=int(input("石头（0） 剪刀（1） 布（2）"))
#     number=random.randint(0,2)
#     print(number)
#
#     if num>number:
#         sum=sum+1
#         if sum==2:
#             print("玩家赢得游戏")
#             break
#     else:
#         if number>num:
#             sum1=sum1+1
#             if sum1==2:
#                 print("计算机赢得游戏")
#                 break
#
# age=int(input("请输入你的年龄"))
# if age>18:
#     print("允许进入网吧嗨皮")
# else:
#     print("未满18岁，不允许进入网吧")
# has_ticket=False
# knife_length=21
# if has_ticket==True:
#     print("允许安检")
#     if knife_length<=20:
#         print("安检通过")
#     else:
#         print("安检不通过")
# else:
#     print("没有车票，不允许进门")

# a=[1,2,3,4,5,6]
# b=[1,3,4,5,7,9]
# for c in a:
#     if c in b:
#         print("adding"+str(c)+".")
#     else:
#         print("sorry,we don't have"+str(c)+".")
# d=["apple","banana","orange"]
# for i in d:
#     print("i really love %s pizza!"%(i))
#
# number=[]
# for i in range(2,4):
#     4
#     print(i)
#     for j in range(2,i):
#         2,3
#         print(j)
#         if i%j==0:
#             break
#         else:
#             number.append(i)
# print(number)
# import xlrd
# path=xlrd.open_workbook("F:\\daima\\code\\pythonProject\\venv\\Scripts\\testdata.xlsx")
# sh=path.sheet_by_index(0)
# rows=sh.nrows
# for i in range(1,rows):
#     name=sh.cell_value(i,0)
#     status=sh.cell_value(i,1)
#     url=sh.cell_value(i,2)
#     print(name,status,url)

# list=[(1,"ok"),(2,"ok"),(3,"ok"),(4,"ok")]
# for i in list:
#     name=i[0]
#     expect=i[1]
#     print(name)
# 创建列表，存储商品库
# 模拟京东购物流程
# 创建列表，存储商品信息
# lst=[]
# for i in range(0,3):
#     foods_info=input("请输入您的商品编号和商品名称")
#     lst.append(foods_info)
# print(lst)
# chart=[]
# while True:
#     flag=False
#     num=input("请输入您想要添加的商品编号")
#     for item in lst:
#         if num==item[0:3]:
#             flag=True
#             chart.append(item)
#             print("您已成功添加至购物车")
#             break
#     if flag==False and num!="q":
#         print("商品不存在")
#     if num=="q":
#         break
# print("您添加购物车的商品为：",chart)

# sites = ["Baidu", "Google","Runoob","Taobao"]
# for site in sites:
#     if site == "Runoob":
#         print("菜鸟教程!")
#         # break
#     # print("循环数据 " + site)
#  else:
#         print("没有循环数据!")
# print("完成循环!")
list=[00,30,19]
flag=False
lst=[]
for num in list:
    if num==0:
        flag=True
        year="200"+str(num)
        print(year)
    else:
        year="19"+str(num)
        print(year)
# print(lst)