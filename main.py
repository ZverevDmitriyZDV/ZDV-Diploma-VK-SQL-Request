from VKbot import VkBotLovers
from settings import token
if __name__ == '__main__':
    session = VkBotLovers(token_bot=token)
    session.start_bot()
