# from utils import get_university_information
# a=get_university_information('schoolDomainName')
# # 遍历字典value
# for value in a.values():
#     print(value)

# for key in a.keys():
#     print(key)
# print(a['www.ahcme.edu.cn'])
# import tldextract
# url="http://zwb.hfut.edu.cn/info/1029/4028.htm"
# print(tldextract.extract(url).domain+ "."+tldextract.extract(url).suffix)
from gc import callbacks



def fun1(response=10):
    for i in range(response):
        print("i的结果是: "+str(i))
        yield get_response(callback=fun1)



#         fun1()
# for t in fun1():
#     print(t)
def get_response(callback):
    callback(5)

for t in fun1():
    print(t)