import power
import os
from dotenv import load_dotenv
load_dotenv()

power.restart(os.getenv("WEB02_ID"), 'tk1a')