import requests

access_token="24.ac7c8355f902d5c776dde974d55de4dd.2592000.1663656989.282335-27099465"
# 用户信息查询
def face_search():
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/get"
    params = "{\"user_id\":\"Jim\",\"group_id\":\"vip\"}"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}

    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())
        print (response.json()['error_msg'])

face_search()
