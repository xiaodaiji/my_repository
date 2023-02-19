import requests
class Hitest:
    def __init__(self,r,cookie):
        self.r=r
        self.cookie=cookie
    def login(self):
        url="https://user.qzone.qq.com/1436629397?ADUIN=1436629397&ADSESSION=1670132643&ADTAG=CLIENT.QQ.5911_MyInfo_PersonalInfo.0&ADPUBNO=27236&source=namecardstar"
        headers={'Cookie':cookie,
                 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'}
        res=self.r.get(url=url,headers=headers).text
        print(res)
if __name__ == '__main__':
    r=requests.session()
    cookie='pgv_pvid=5791194914; fqm_pvqid=aa3f2686-f5b0-4fa1-8ada-c2ee9b8444ae; RK=I4Hli0DBWH; ptcz=dbad8ccf03641b1dc849d624312f148b32a13f79efa5dd69c1928306058a14b3; tvfe_boss_uuid=e140e28664d730b7; uin=o1436629397; skey=@EGnFQapz9; p_uin=o1436629397; pt4_token=DAczimwvQLiHEaBAVV-WEac2DRBbAHXOOqN0eKbSPqo_; p_skey=uB1VNHNTL*goH41PQrJw8VfwfQcchrFY5c3kxDCC3qc_; Loading=Yes; x-stgw-ssl-info=8dd036ab9d6a4d2feea8ac590f791b41|0.116|-|1|.|Y|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|76500|h2|0; pgv_info=ssid=s448295798; qz_screen=1536x864; QZ_FE_WEBP_SUPPORT=1; 1436629397_todaycount=0; 1436629397_totalcount=25755; cpu_performance_v8=2'
    r1=Hitest(r,cookie)
    r2=r1.login()