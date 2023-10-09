from passlib.context import CryptContext  # Its is used for hashing the password.


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # Basically all we are doind is we are telling "passlib" what is default hashing alorithm.

def hash(password: str):
    return pwd_context.hash(password)

#This function will take raw password from user and convert into hashed password ans then, compare it ot the hashed password stored in our database.

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)




