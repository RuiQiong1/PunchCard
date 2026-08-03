import requests
import base64

access_token="24.ac7c8355f902d5c776dde974d55de4dd.2592000.1663656989.282335-27099465"
request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"
# f = open('Demo.png','rb')
f = open('Jim.png','rb')
image = base64.b64encode(f.read())
params = {'image':image, 'image_type':'BASE64','group_id_list':'vip','quality_control':'NONE'}
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/json'}
response = requests.post(request_url, data=params, headers=headers)

if response:
    result = response.json()
    print(result)
    if result['result']['user_list'][0]['score'] >= 80:
        print("姓名：",result['result']['user_list'][0]['user_id'])
        print("所在组：",result['result']['user_list'][0]['group_id'])
    else:
        print("无此用户，请通知管理员进行注册！")