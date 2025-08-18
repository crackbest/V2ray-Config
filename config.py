import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone
import pytz
import jdatetime



newaddresses = [
   "https://t.me/s/ConfigsHubPlus",
"https://t.me/s/ProxyFn",
"https://t.me/s/prrofile_purple",
"https://t.me/s/shadowproxy66",
"https://t.me/s/sinavm",
"https://t.me/s/VPNCUSTOMIZE",
"https://t.me/s/Outline_ir",
"https://t.me/s/Pruoxyi",
"https://t.me/s/v2ray_configs_pool",
"https://t.me/s/v2ray_configs_pools",
"https://t.me/s/ultrasurf_12",
"https://t.me/s/V2RAY_VMESS_free",
"https://t.me/s/FreakConfig",
"https://t.me/s/v2rayNG_Matsuri",
"https://t.me/s/meli_proxyy",
"https://t.me/s/oneclickvpnkeys",
"https://t.me/s/Outline_Vpn",
"https://t.me/s/proxy_kafee",
"https://t.me/s/v2ray_sub",
"https://t.me/s/SaghiVpnX",
"https://t.me/s/Daily_Configs",
"https://t.me/s/customv2ray",
"https://t.me/s/Fr33C0nfig ",
"https://t.me/s/UnlimitedDev",
"https://t.me/s/vmessorg",
"https://t.me/s/v2rayngvpn",
"https://t.me/s/SafeNet_Server",
"https://t.me/s/vmessprotocol ",

]

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


html_pages = []

for url in newaddresses:
    response = requests.get(url)
    html_pages.append(response.text)

codes = []

for page in html_pages:
    soup = BeautifulSoup(page, 'html.parser')
    code_tags = soup.find_all('code')

    for code_tag in code_tags:
        code_content = code_tag.text.strip()
        if "vless://" in code_content or "ss://" in code_content or "vmess://" in code_content or "trojan://" in code_content:
            codes.append(code_content)

codes = list(set(codes))  # Remove duplicates

processed_codes = []

# Get the current date and time
current_date_time = jdatetime.datetime.now(pytz.timezone('Asia/Tehran'))
# Print the current month in letters
current_month = current_date_time.strftime("%b")

# Get the current day as a string
current_day = current_date_time.strftime("%d")

# Increase the current hour by 4 hours
#new_date_time = current_date_time + timedelta(hours=4)

# Get the updated hour as a string
updated_hour = current_date_time.strftime("%H")

updated_minute = current_date_time.strftime("%M")

# Combine the strings to form the final result
final_string = f"{current_month}-{current_day} | {updated_hour}:{updated_minute}"
final_others_string = f"{current_month}-{current_day}"
config_string = "#✅ " + str(final_string) + "-"

for code in codes:
    vmess_parts = code.split("vmess://")
    vless_parts = code.split("vless://")

    for part in vmess_parts + vless_parts:
        if "ss://" in part or "vmess://" in part or "vless://" in part or "trojan://" in part:
            service_name = part.split("serviceName=")[-1].split("&")[0]
            processed_part = part.split("#")[0]
            processed_codes.append(processed_part)

processed_codes = remove_duplicates(processed_codes)

new_processed_codes = []

for code in processed_codes:
    vmess_parts = code.split("vmess://")
    vless_parts = code.split("vless://")

    for part in vmess_parts + vless_parts:
        if "ss://" in part or "vmess://" in part or "vless://" in part or "trojan://" in part:
            service_name = part.split("serviceName=")[-1].split("&")[0]
            processed_part = part.split("#")[0]
            new_processed_codes.append(processed_part)

i = 0
with open("config.txt", "w", encoding="utf-8") as file:
    for code in new_processed_codes:
        if i == 0:
            config_string = "#🌐 به روزرسانی شده در" + final_string + " | هر 15 دقیقه کانفیگ جدید داریم"
        else:
            config_string = "#🌐سرور " + str(i) + " | " + str(final_others_string) + "|t.me/Crackbest2 "
        config_final = code + config_string
        file.write(config_final + "\n")
        i += 1
