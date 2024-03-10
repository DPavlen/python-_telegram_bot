from dotenv import dotenv_values


class Config:
    """"""
    def __init__(self, env=".env"):
        config = dotenv_values(env)
        self.bot_token = config.get("BOT_TOKEN")
        self.admin_chat_id = config.get("ADMIN_CHAT_ID")
        self.mongodb_uri = config.get("MONGODB_URI")
        self.mongodb_db = config.get("MONGODB_DB")
        self.mongodb_collection = config.get("MONGODB_COLLECTION")

