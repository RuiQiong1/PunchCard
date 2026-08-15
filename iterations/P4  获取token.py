import requests

"""
方法一 直接调用
"""
# host="https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Y4VSL2OKNz8KIeDQAsZEIZVG&client_secret=TRjUnvZkWNbmPUySEzWj3PQcCY8goUsO"
# response=requests.get(host)
# if response:
#     result=response.json()
#     access_token=result['access_token']
#     print('access_token:',access_token)


"""
方法二 封装成函数
"""
def access_tokens():
    # 此处的AK和SK，需要替换成自己的
    ak = 'OnwhWhjUpBELvGgGsT1aQYEE'
    sk = 'bLagl3cLV6IIVuFVR6mv4Ai6CqP8Ae2n'

    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(
        ak, sk)
    response = requests.get(host)
    if response:
        return response.json()['access_token']

my_token=access_tokens()
print(my_token)