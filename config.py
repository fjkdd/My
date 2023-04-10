from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID  =  int ( getenv ( "API_ID" ، "7614819" )) # لا تغير هاذة القيمة
API_HASH  =  getenv ( "API_HASH" ، "0e437c9cb4386b602829ab472bd87806" ) # لا تغير هاذة القيمة
BOT_TOKEN  =  getenv ( "BOT_TOKEN" ، "5987112288:AAFzXTA1feoKH_RvaLTAus1zLJJTJ2FJdJY" )
SESSION_NAME  =  getenv ( "SESSION_NAME" ، "BAB0MWMAlMZzZVeuFD7RK9hd59EceKMqNMABE9uWW03wlApNrFQfdiw4NVEr77Qrh593oAhk5z-b2IDTaXQ6SRZnCEFHJ2NmxanWpuher14Ml9vX-hvqiRdgCUPBuXiQLOgFOv_GAKNnTNr_WWwMc97OoZ4f3rETQ7DVC49w6GIpH1G3LrmWZOjNn_PN-ylSInzaFB6Z81s8s0B9uf9EFbykq7-lp0814hNBjBrxr128EI2HdWSPcNa6d4111L1lP57U8tVmTGKdYhufGdI0zMfhI-Fzf20R3greR8bV3yFoDRTHJEJyN0yp8ou6yVLDTCpfuuVIu1bWS3k_AygFwjXDepMrKQAAAAFvj-CKAA" )

# mandatory vars
OWNER_USERNAME  =  getenv ( "OWNER_USERNAME" ، "QO0_O20" ) # @ هنا ضع يوزر حسابك بدون
ALIVE_NAME  =  getenv ( "ALIVE_NAME" ، "𝐁𝐎𝐒" ) # هنا ضع اسم حسابك
BOT_USERNAME  =  getenv ( "BOT_USERNAME" ، "siskskdbot" ) # @ هنا ضع يوزر البوت بدون
UPSTREAM_REPO  =  getenv ( "UPSTREAM_REPO" ، "https://github.com/X02lx/RrRRR" )
UPSTREAM_BRANCH  =  getenv ( "UPSTREM_BRANCH" ، "main" ) # لا تغير هاذة القيمة
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60")) #لا تغير هاذة القيمة
GROUP_SUPPORT  =  getenv ( "GROUP_SUPPORT" ، "u_f_r_nu" ) # @ هنا ضغ يوزر كروبك بدون
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xl444") # @ هنا ضغ يوزر قناتك بدون

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID  =  list ( map ( int ، getenv ( "OWNER_ID" ، "6166667402" ). split ()))
                                             #هنا ضع ايدي المطور فوق و الاعلئ
SUDO_USERS  =  قائمة ( خريطة ( int ، getenv ( "SUDO_USERS" ، "6166667402" )

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
