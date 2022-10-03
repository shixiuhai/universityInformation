# from utils import get_university_information
# a=get_university_information('schoolDomainName')
# # 遍历字典value
# for value in a.values():
#     print(value)

# for key in a.keys():
#     print(key)
# print(a['www.ahcme.edu.cn'])
import tldextract
url="http://zwb.hfut.edu.cn/info/1029/4028.htm"
print(tldextract.extract(url).domain+ "."+tldextract.extract(url).suffix)
