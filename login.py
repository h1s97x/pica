

def main():
    env = os.environ
    PICA_ACCOUNT = env.get('PICA_ACCOUNT')
    PICA_PASSWORD = env.get('PICA_PASSWORD')

    account = PICA_ACCOUNT
    password = PICA_PASSWORD

    pica = Pica()
    pica.login(account, password)



