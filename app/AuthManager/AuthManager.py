from Models import *
import jwt
import os
import dotenv
from datetime import datetime, timedelta

class AuthManager: 
    secret_key = os.getenv("SECRET_KEY")
    algorithm = os.getenv("ALGORITHM")
    
    def __init__(self):
        pass

    def createAuthToken(self, user: User) -> str:
        token = jwt.encode({
            "user_id": user.id,
            "user_name": user.username,
            "phone_number": user.phone_number,
            "exp": datetime.now() + timedelta(minutes=30),
            "type": "access"
        }, self.secret_key, algorithm=self.algorithm)
        return token

    