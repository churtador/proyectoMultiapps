import bcrypt


def encriptar(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verificarPassword(confirmPass, password):
    return bcrypt.checkpw(confirmPass.encode(), password.encode())