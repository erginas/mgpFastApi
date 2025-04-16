from jose import jwt

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
    except jwt.JWTError as e:
        print(f"Error: {str(e)}")

# Token'ı decode et
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJhZG1pbiIsImV4cCI6MTc0NTAxNjA5Mn0.1HX-_bUdVQCRmnrxPNAuANQ0N5kSbNWNukvxGNCsWVI"
decode_token(token)