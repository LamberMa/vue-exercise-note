#!/Users/lamber/python/longfor/bin/python
import sh
import json

from dingding import DingDing

access_token = 'b0d981254af985b4420065e72837242b92c2831cefcd51904e9acea96dcff766'
ding = DingDing(access_token)
"""
钉钉模块的使用方法
# @所有人
ding.send_text('hello', at_all=True)
# @手机号为1333333333的人
ding.send_text('hello', ['13333333333'])
ding.send_link('title', 'text', 'message_url')
ding.send_markdown('title', 'text')
ding.send_action_card('title', 'text', [('title1', 'url1'), ('title2', 'url2')])
ding.send_link(
    '时代的火车向前开', 
    '这个即将发布的新版本，创始人陈航（花名“无招”）称它为“红树林”。 而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是“红树林”？', 
    'https://mp.weixin.qq.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI')
"""
headers1 = "Cookie: acw_tc=76b20f6315604061049676441e0da08812237984c33eb3fe31c8e3b020c40d; connect.sid=s%3Adu1IsBfjSSSoMXTj4341Y-Ev3nMhBuX-.FVAtmKDmftHevlQ3Niy2z5zZp214qsYYvB%2BAVQ8Y6AI; Hm_lvt_239619dd622d77b4aa84c2bc9c1d36f5=1560406106; Hm_lpvt_239619dd622d77b4aa84c2bc9c1d36f5=1560411466; u_asec=099%23KAFEtYEKEBSEhYTLEEEEEpEQz0yFD6ghDXiFS6gwDusYW6VFDu9FC6tFjYFET%2FdosyaStqMTEc35PE1laquYSpXfNVo63ya3OfYncYUquz8sDzXZ1d%2Fs4WxR6RXcaOnKPf8VNlWuV6yNSKoSLMss%2ByJkPRv3iOBT%2FfInNdbRzqk8SO2Ciou7t2wTPw2c9XyKVfp2NlVuVf3YSj%2BBaquYSpXfNVo63ya3OfYncYUquz8sDzXZ1d%2Fs4WxR6RXcaOnKPf8VNlWuV6yNSKoSLMss%2ByJkPRv3iOBT%2FfInNQOqrtxvG%2BpCaYe8SOvo6azt3%2F%2FpQt2Bvdbqztc2us2CE9%2F8SVhv4gvlEKXCVPcYU9buQ2iPCT82GJsAGuhYJcGTE1LlluZOt377llllWLaStETNllle33iSw6alluUdt37qY3llWLaStECEBEFE13lls6Xs9z8isYFETYilsslwtuYTEHIE%2BDSEjrN4kLISmQPvbht8fkv3iwl8qiUCqoCqKW6r2h5YwqVUPJK4IwkcvhWgfJ6%2FIHvkcrmo3kj2iEAkl%2BKDkxIRvwygciYZRKnyMOFYqwP%2BlYFETJDovlNXE7EFD67EE67TEEilluCV"
hospital_url = """
curl '{"mode":"2","distId":"175","outpatientId":"1316410","departmentId":"","date":"","title":"","pageNum":1,"pageSize":10,"timeout":30000,"isLoading":true}'
"""
ret = sh.curl(
    "https://m.hsyuntai.com/med/hp/hospitals/100215/registration/regList",
    "-H", headers1,
    "-H", 'Origin: https://m.hsyuntai.com',
    "-H", 'Accept-Encoding: gzip, deflate, br',
    "-H", 'Accept-Language: zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7,zh-TW;q=0.6',
    "-H", 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    "-H", 'Content-Type: application/json;charset=UTF-8',
    "-H", 'Accept: application/json, text/plain, */*',
    "-H", 'Referer: https://m.hsyuntai.com/med/hp/hospitals/100215/hos/registration/departmentDetails/2/175/1316410/',
    "-H", 'X-Requested-With: XMLHttpRequest',
    "-H", 'Connection: keep-alive',
    "--data-binary", 
    '{"mode":"2","distId":"175","outpatientId":"1316410","departmentId":"","date":"","title":"","pageNum":1,"pageSize":10,"timeout":30000,"isLoading":true}',
    "--compressed",
)

number_template = """
####################
时间：{}
星期: {}
是否有号：{}\n
"""

ret_json_str = str(ret)
ret_json = json.loads(ret_json_str)
doctor_list = ret_json['data']['list']
for doctor in doctor_list:
    if doctor['docName'] == '宋佩华':
        has_number = doctor.get('haveNum', None)
        if has_number == 'Y':
            number_detail_object = sh.curl(
                'https://m.hsyuntai.com/med/hp/hospitals/100215/registration/doctorDetails225?branchId=175&docId=50973460&filtrate=N&outpatientId=1316410&schListType=true&type=0',
                '-H', 'Cookie: acw_tc=76b20f6315604061049676441e0da08812237984c33eb3fe31c8e3b020c40d; connect.sid=s%3Adu1IsBfjSSSoMXTj4341Y-Ev3nMhBuX-.FVAtmKDmftHevlQ3Niy2z5zZp214qsYYvB%2BAVQ8Y6AI; Hm_lvt_239619dd622d77b4aa84c2bc9c1d36f5=1560406106; u_asec=099%23KAFEuGEKEkIEhGTLEEEEEpEQz0yFD6ghDXioA6DHZcOEW6zwDc9oa6t1DP7TEEiStEE7BYFETEEEbORuE7EFNIaHF5MTEEySl3llsyaUE7TxGhKjD5GtwEroialN61CfZDU0pu5sMNLok7Ylsn64JmZo8CrGkLHBiQg099ob060qmStrLLHoCUg08nlnRhikLmf39RA%2F0f%2FfDNN7VHAo1VA3LcQTEEyZtY7IZUgoE7EIt37EeyZvFBwbE7EUt3ilkcZdd9JStTLtsyaZW9iSh3nP%2F3wIt37MlXZdd6JStTLtsyaGSoMTEqYEqORp%2FqYWcR4f9BZVNaxV%2FRz6asBoHshnPvS6bfkB6w%2BBaIZvDs7Wbw2c9XBmhT8M8vnqrd%2BBcypawIWYSOEWPRf69yw9biencoqRUqhS6O8B%2FvnNSzeB8Kvu3uwjhKX2hETlVtqyhw7WadWvv0XBPg9qLenM6aeGPwZprt2BPOIC9oC4%2BaxnriYqasB0r0XMhRQuVf1B6RXV95WADOxVcL4pasnx6VoCbbQpzPpZbLoWGGrYGy7Zr0ou9XBx8zXM89QlQ6FMNG%3D%3D; Hm_lpvt_239619dd622d77b4aa84c2bc9c1d36f5=1560417135',
                '-H', 'Accept-Encoding: gzip, deflate, br',
                '-H', 'Accept-Language: zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7,zh-TW;q=0.6',
                '-H', 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                '-H', 'Accept: application/json, text/plain, */*',
                '-H', 'Referer: https://m.hsyuntai.com/med/hp/hospitals/100215/hos/registration/doctorDetails/0/175/1316410/50973460',
                '-H', 'X-Requested-With: XMLHttpRequest',
                '-H', 'If-None-Match: W/"cnW0yflylrxnpmQn6qyvpw=="',
                '-H', 'Connection: keep-alive', '--compressed'
            )
            available_number_dict_list = (json.loads(str(number_detail_object))[2]['data'])
            message_tpl = ''
            for available_number in available_number_dict_list:
                message_tpl += number_template.format(available_number['schDate'], available_number['weekType'], '否' if available_number['state'] == 0 else '是')

            ding.send_text('中日医院宋大夫已经有号了，请去查看\n%s' % message_tpl)

