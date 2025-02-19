# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", "AQFCJtoAG-BWr-q9nKSSBk1Juk7jQk_UoTj1PaRzSvIhdR4Y5MF2m8yCW5e5n7YHYNICqn5u6bT7U5czUX22vQwcleryhrmug4hO4qfS1twJVQEZXbU4bTQO8YWbuokH5qEAgs5HdWjIDkL0dlP-ElLQMpcn1Snd0HuD9D5st4S7C1rnZ7vvYyGtPi5Aj8SC-_0_VaQgR8_sX3sHyXIYmweVhUfj7IJ6V4CMxd-tpTsKjNRVEKXqX68qnVMcJjFG9IdeohqJh8kqPwShlDgDTwYpuQ7Ht-XEDpO-XTa9XqflTubETV7xEhu7vVsWVMnkLNuY2OvzT1HXG49H5dmqfkgSewYjtwAAAAHGQZT-AA")  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
