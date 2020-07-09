import power
import os
from dotenv import load_dotenv
load_dotenv()

power.restart(os.getenv("WEB01_ID"), 'is1a')