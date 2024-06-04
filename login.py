import os
from sdk import Pica
# Description: 登录并获得Token
def main():
    env = os.environ
    path = os.getcwd()
    PICA_ACCOUNT = env.get('PICA_ACCOUNT')
    PICA_PASSWORD = env.get('PICA_PASSWORD')

    account = PICA_ACCOUNT
    password = PICA_PASSWORD

    pica = Pica()
    pica.login(account, password)
    with open(path + '/token.txt', 'w') as f:
        f.write(pica.headers['authorization'])
    print('Token获取成功')
    
main()

