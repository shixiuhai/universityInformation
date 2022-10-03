import requests
from lxml import etree
# 定义一个查询子域名的函数
import json
import time
# 定义一个大学主域名字段
# https://www.dxsbb.com/news/1619.html
mainDomainDict={
    "ahu.edu.cn":"安徽大学",
    "ustc.edu.cn":"中国科学技术大学",
    "hfut.edu.cn":"合肥工业大学",
    "ahut.edu.cn":"安徽工业大学",
    "aust.edu.cn":"安徽理工大学",
    "ahpu.edu.cn":"安徽工程大学",
    "ahau.edu.cn":"安徽农业大学",
    "ahmu.edu.cn":"安徽医科大学",
    "bbmc.edu.cn":"蚌埠医学院",
    "wnmc.edu.cn":"皖南医学院",
    "ahtcm.edu.cn":"安徽中医药大学",
    "ahnu.edu.cn":"安徽师范大学",
    "fynu.edu.cn":"阜阳师范大学",
    "aqnu.edu.cn":"安庆师范大学",
    "chnu.edu.cn":"淮北师范大学",
    "hsu.edu.cn":"黄山学院",
    "wxc.edu.cn":"皖西学院",
    "chzu.edu.cn":"滁州学院",
    "aufe.edu.cn":"安徽财经大学",
    "ahszu.edu.cn":"宿州学院",
    "chtc.edu.cn":"巢湖学院",
    "hnnu.edu.cn":"淮南师范学院",
    "tlu.edu.cn":"铜陵学院",
    "ahjzu.edu.cn":"安徽建筑大学",
    "ahstu.edu.cn":"安徽科技学院",
    "hfuu.edu.cn":"合肥学院",
    "bbc.edu.cn":"蚌埠学院",
    "czu.edu.cn":"池州学院",
    "bzuu.edu.cn":"亳州学院",
    "hfnu.edu.cn":"合肥师范学院",
    "ahua.edu.cn":"安徽艺术学院",
    "slu.edu.cn":"安徽三联学院",
    "axhu.edu.cn":"安徽新华学院",
    "wenda.edu.cn":"安徽文达信息工程学院",
    "aisu.edu.cn":"安徽外国语学院",
    "zs.bctb.edu.cn":"蚌埠工商学院",
    "jhxy.ahu.edu.cn":"安徽大学江淮学院",
    "aiit.edu.cn":"安徽信息工程学院",
    "masu.edu.cn/":"马鞍山学院",
    "cuhf.edu.cn":"合肥城市学院",
    "hfue.edu.cn":"合肥经济学院",
    "ahnu.edu.cn":"安徽师范大学皖江学院",
    "cc.ahmu.edu.cn":"安徽医科大学临床医学院",
    "cie.fynu.edu.cn":"阜阳师范大学信息工程学院",
    "hblgxy.edu.cn":"淮北理工学院",
    "wjut.edu.cn":"皖江工学院",
    "uta.edu.cn":"安徽职业技术学院",
    "hbvtc.net":"淮北职业技术学院",
    "whit.edu.cn":"芜湖职业技术学院",
    "hnuu.edu.cn":"淮南联合大学",
    "abc.edu.cn":"安徽商贸职业技术学院",
    "ahsdxy.edu.cn":"安徽水利水电职业技术学院",
    "fyvtc.edu.cn":"阜阳职业技术学院",
    "tlpt.net.cn":"铜陵职业技术学院",
    "ahjgxy.edu.cn":"安徽警官职业学院",
    "hnvtc.edu.cn":"淮南职业技术学院",
    "ahiec.edu.cn":"安徽工业经济职业技术学院",
    "hftyxy.com":"合肥通用职业技术学院",
    "ahgm.edu.cn":"安徽工贸职业技术学院",
    "szzy.edu.cn":"宿州职业技术学院",
    "lvtc.edu.cn":"六安职业技术学院",
    "ahdy.edu.cn":"安徽电子信息职业技术学院",
    "acvtc.edu.cn":"安徽交通职业技术学院",
    "ahty.edu.cn":"安徽体育运动职业技术学院",
    "ahzyygz.edu.cn":"安徽中医药高等专科学校",
    "ahyz.edu.cn":"安徽医学高等专科学校",
    "ksh.htc.edu.cn":"合肥职业技术学院",
    "chzc.edu.cn":"滁州职业技术学院",
    "czvtc.edu.cn":"池州职业技术学院",
    "xcvtc.edu.cn":"宣城职业技术学院",
    "amtc.edu.cn":"安徽广播影视职业技术学院",
    "aepu.com.cn":"安徽电气工程职业技术学院",
    "avcmt.edu.cn":"安徽冶金科技职业学院",
    "cua.edu.cn":"安徽城市管理职业学院",
    "ahcme.edu.cn":"安徽机电职业技术学院",
    "ahbvc.edu.cn":"安徽工商职业学院",
    "acac.cn":"安徽中澳科技职业学院",
    "bzy.edu.cn":"亳州职业技术学院",
    "acdt.edu.cn":"安徽国防科技职业学院",
    "aqvtc.edu.cn":"安庆职业技术学院",
    "artah.cn":"安徽艺术职业学院",
    "massz.edu.cn":"马鞍山师范高等专科学校",
    "aftvc.com":"安徽财贸职业学院",
    "ahiib.edu.cn":"安徽国际商务职业学院",
    "ahgaxy.com.cn":"安徽公安职业学院",
    "ahlyxy.edu.cn":"安徽林业职业技术学院",
    "ahsjxy.edu.cn":"安徽审计职业学院",
    "zs.ahcbxy.edu.cn":"安徽新闻出版职业技术学院",
    "ahptc.cn":"安徽邮电职业技术学院",
    "ahip.cn":"安徽工业职业技术学院",
    "aqmc.edu.cn":"安庆医药高等专科学校",
    "hsxy.edu.cn":"徽商职业学院",
    "mastc.edu.cn":"马鞍山职业技术学院",
    "tctc.edu.cn":"桐城师范高等专科学校",
    "hszy.edu.cn":"黄山职业技术学院",
    "czcvc.net":"滁州城市职业学院",
    "ahavtc.edu.cn":"安徽汽车职业技术学院",
    "wahvc.edu.cn":"皖西卫生职业学院",
    "hfpec.edu.cn":"合肥幼儿师范高等专科学校",
    "hmxxy.com":"安徽黄梅戏艺术职业学院",
    "ahly.edu.cn":"安徽粮食工程职业学院",
    "ahwsjkxy.edu.cn":"安徽卫生健康职业学院",
    "wbws.edu.cn":"皖北卫生职业学院",
    "fypec.edu.cn":"阜阳幼儿师范高等专科学校",
    "wbc.edu.cn":"万博科技职业学院",
    "hfet.com":"合肥经济技术职业学院",
    "hfbhxy.com":"合肥滨湖职业技术学院",
    "fky.net.cn":"阜阳科技职业学院",
    "hfcfe.edu.cn":"合肥财经职业学院",
    "ahaec-edu.cn":"安徽涉外经济职业学院",
    "lhub.cn":"安徽绿海商务职业学院",
    "hfgdxy.cn":"合肥共达职业技术学院",
    "bjy.ah.cn":"蚌埠经济技术职业学院",
    "ahmodern.cn":"安徽现代信息工程职业学院",
    "hfitu.cn":"合肥信息技术职业学院",
    "ahyzxy.cn":"安徽扬子职业技术学院",
    "hfstu.cn":"合肥科技职业学院",
    "hsvch.cn":"黄山健康职业学院",
    "xcvtc.edu.cn":"宿州航空职业学院"
}

outDict={}
def get_sbu_domain()->dict:
    for mainDomain in mainDomainDict.keys():
        # print(mainDomain,mainDomainDict[mainDomain])
        # 给一级域名添加www
        outDict["www."+mainDomain]=mainDomainDict[mainDomain]
        # 将一级域名添加到outDict中
        outDict[mainDomain]=mainDomainDict[mainDomain]
        # 进行子域名添加
        html=requests.get(url="https://chaziyu.com/%s/"%mainDomain,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'}).text
        tree = etree.HTML(html)
        subDomainList=tree.xpath("/html/body/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr/td[2]//text()")
        for subDomain in subDomainList:
            print(subDomain)
            outDict[subDomain]=mainDomainDict[mainDomain]
        
        print("%s 获取子域名成功"%mainDomain)
        time.sleep(5)
    return outDict
result=json.dumps(get_sbu_domain(),ensure_ascii=False)
with open("./schoolDomainName.json","w",encoding="utf-8") as f:
    f.write(result)