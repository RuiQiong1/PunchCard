import requests

access_token="24.ac7c8355f902d5c776dde974d55de4dd.2592000.1663656989.282335-27099465"
# 获取用户人脸列表
def face_getlist():
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/face/getlist"
    params = "{\"user_id\":\"Jim\",\"group_id\":\"vip\"}"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}

    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())
        print ("获取用户人脸列表：",response.json()['error_msg'])

# 获取用户列表
def face_getusers():
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/getusers"
    params = "{\"group_id\":\"vip\"}"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}

    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())
        print (response.json()['result']['user_id_list'])
        print ("获取用户列表：",response.json()['error_msg'])

face_getlist()
face_getusers()