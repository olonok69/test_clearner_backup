from dotenv import dotenv_values
config = dotenv_values(".env") 
api-key=config.get("api-key")
email=config.get("test1@mytest.com")