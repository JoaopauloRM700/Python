import re
def ValidateEmail(email: str):
    padrao = re.search(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', email)

    if padrao:
        return True
    else:
        return False
