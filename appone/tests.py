import requests

TOKEN_URI = "http://localhost:8001/token/"

EMP_BASE_URI = "http://localhost:8001/emp/api/v1/"
SAMPLE_BASE_URI = "http://localhost:8001/emp/api/v2/"

APP_TOKEN_GUEST = 'Token 3b51d09eb6fded1b50e6449c3774fc132922f3e2'
APP_TOKEN_AD1 = 'Token 861a17c73136810ed5027a07b0965d2769f86413'
APP_TOKEN_AD2 = 'Token a5e0de86ea4dd5cd64edb12b3f0b7b67d898d5fe'
dict_token_val1 = {'Authorization' : APP_TOKEN_GUEST}
dict_token_val2 = {'Authorization' : APP_TOKEN_AD1}
dict_token_val3 = {'Authorization' : APP_TOKEN_AD2}

#entire application
#class specific
#methods specific
#object specific -->  hashpers --> hasobjperm


def get_token_for_user(user,pwd):
    response = requests.post(TOKEN_URI,json={"username":user,"password":pwd})
    print(response.status_code)
    print(response.json())
    return response.json()



def get_all_emps_without_token():
    response = requests.get(EMP_BASE_URI) #guest token    --> should not be accessed
    print(response.status_code)
    print(response.json())


def get_all_samples_without_token():
    response = requests.get(SAMPLE_BASE_URI)  #
    print(response.status_code)
    print(response.json())


def get_all_emps(token):
    response = requests.get(EMP_BASE_URI,headers = token) #guest token    --> should not be accessed
    print(response.status_code)
    print(response.json())


def get_all_samples(token):
    emp = {
              "name": "XXXX",
              "salary": 20,
              "age": 20,
              "desig": "Manager"
        }
    response = requests.post(SAMPLE_BASE_URI,headers = token,json = emp)  # admin token --> response expected
    print(response.status_code)
    print(response.json())
import sys
if __name__ == '__main__':

    response = get_token_for_user("yogymax1","Yogymax#123")  #admin
    APP_TOKEN = 'Token {}'.format('3b51d09eb6fded1b50e6449c3774fc132922f3e2')
    dict_token_val = {'Authorization': APP_TOKEN}
   # print(dict_token_val)

    get_all_samples(dict_token_val)


    sys.exit(0)
    #get_all_emps_without_token() # response Yes--> required token
    #print('----------------------------')
    #get_all_samples_without_token() # response --No

    #import sys
    #sys.exit(0)
    print('-------------------')
    #print('From Emp Table')
    #get_all_emps()            #isauth --> guest token
    print('------------------')
    print('From sample Table')
    get_all_samples(dict_token_val)       #isauth --> admin token