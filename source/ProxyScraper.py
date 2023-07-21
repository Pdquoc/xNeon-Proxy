import aiohttp, asyncio
from re import compile

TIMEOUT: int = 15
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
REGEX = compile(
    r"(?:^|\D)?(("+ r"(?:[1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    + r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    + r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    + r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    + r"):" + (r"(?:\d|[1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{3}"
    + r"|65[0-4]\d{2}|655[0-2]\d|6553[0-5])")
    + r")(?:\D|$)"
)

scrapped_proxies = []
with open('proxies.txt', 'w') as proxies: proxies.write('')
proxies = open('proxies.txt', 'a')
errors = open('errors.txt', 'a')

async def scrap(url: str):
    temp_proxies = 0
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url, headers={'user-agent': user_agent}, 
                timeout=aiohttp.ClientTimeout(total=TIMEOUT)
            ) as response:
                html = await response.text()
                if tuple(REGEX.finditer(html)):
                    for proxy in tuple(REGEX.finditer(html)):
                        proxies.write(f'{proxy.group(1)}\n')
                        scrapped_proxies.append(proxy.group(1))
                        temp_proxies += 1
                    print(f' [~] Found: {temp_proxies} Proxies In {url}', proxy.group(1))
                else: print(f' [~] Can\'t Find At: {url}', proxy.group(1))
    except Exception as e: 
        errors.write(f'[ERROR AT]: {url} {e}\n')


async def main():
    urls = [
        "http://globalproxies.blogspot.com/",
        "http://www.cybersyndrome.net/plz.html",
        "http://www.cybersyndrome.net/plr5.html",
        "http://biskutliat.blogspot.com/",
        "http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-15-0111-am-gmt8.html",
        "http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-13-812-gmt7.html",
        "http://www.cybersyndrome.net/pla5.html",
        "http://vipprox.blogspot.com/2013_06_01_archive.html",
        "http://vipprox.blogspot.com/2013/05/us-proxy-servers-74_24.html",
        "http://vipprox.blogspot.com/p/blog-page_7.html",
        "http://vipprox.blogspot.com/2013/05/us-proxy-servers-199_20.html",
        "http://vipprox.blogspot.com/2013_02_01_archive.html",
        "http://alexa.lr2b.com/proxylist.txt",
        "http://vipprox.blogspot.com/2013_03_01_archive.html",
        "http://browse.feedreader.com/c/Proxy_Server_List-1/449196260",
        "http://browse.feedreader.com/c/Proxy_Server_List-1/449196258",
        "http://browse.feedreader.com/c/Proxy_Server_List-1/449196251",
        "http://free-ssh.blogspot.com/feeds/posts/default",
        "http://browse.feedreader.com/c/Proxy_Server_List-1/449196259",
        "http://sockproxy.blogspot.com/2013/04/11-04-13-socks-45.html",
        "http://proxyfirenet.blogspot.com/",
        "https://www.javatpoint.com/proxy-server-list",
        "https://openproxy.space/list/http",
        "http://proxydb.net/",
        "http://olaf4snow.com/public/proxy.txt",
        "http://westdollar.narod.ru/proxy.htm",
        "https://openproxy.space/list/socks4",
        "https://openproxy.space/list/socks5",
        "http://tomoney.narod.ru/help/proxi.htm",
        "http://sergei-m.narod.ru/proxy.htm",
        "http://rammstein.narod.ru/proxy.html",
        "http://greenrain.bos.ru/R_Stuff/Proxy.htm",
        "http://inav.chat.ru/ftp/proxy.txt",
        "http://johnstudio0.tripod.com/index1.htm",
        "http://atomintersoft.com/transparent_proxy_list",
        "http://atomintersoft.com/anonymous_proxy_list",
        "http://atomintersoft.com/high_anonymity_elite_proxy_list",
        "http://atomintersoft.com/products/alive-proxy/proxy-list/3128",
        "http://atomintersoft.com/products/alive-proxy/proxy-list/com",
        "http://atomintersoft.com/products/alive-proxy/proxy-list/high-anonymity/",
        "http://atomintersoft.com/products/alive-proxy/socks5-list",
        "http://atomintersoft.com/proxy_list_domain_com",
        "http://atomintersoft.com/proxy_list_domain_edu",
        "http://atomintersoft.com/proxy_list_domain_net",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
        "http://atomintersoft.com/proxy_list_domain_org",
        "http://atomintersoft.com/proxy_list_port_3128",
        "http://atomintersoft.com/proxy_list_port_80",
        "http://atomintersoft.com/proxy_list_port_8000",
        "http://atomintersoft.com/proxy_list_port_81",
        "http://hack-hack.chat.ru/proxy/allproxy.txt",
        "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
        "http://hack-hack.chat.ru/proxy/anon.txt",
        "http://hack-hack.chat.ru/proxy/p1.txt",
        "http://hack-hack.chat.ru/proxy/p2.txt",
        "http://hack-hack.chat.ru/proxy/p3.txt",
        "http://hack-hack.chat.ru/proxy/p4.txt",
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://free-proxy-list.net/",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
        "https://www.us-proxy.org/",
        "https://free-proxy-list.com/",
        "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
        "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all",
        "https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all",
        "https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all",
        "https://spys.one/",
        "https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all",
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt",
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all",
    ]

    await asyncio.wait(
        [asyncio.create_task(scrap(url)) for url in urls]
    )

    print(f'\n [!] Done Scraping...\n [~] Total Proxies: {len(scrapped_proxies)}')
    proxies.close()
    errors.close()

    filter_option = input("\nBạn Có Muốn Lọc Proxy Trùng Không? (y/n): ")
    if filter_option.lower() == 'y':
        unique_proxies = list(set(scrapped_proxies))
        print(f' [~] Tổng Proxies Hiện Có: {len(unique_proxies)}\nProxy Được Lưu Tại proxies.txt\n')
    elif filter_option.lower() == 'n':
        print(" [~] Proxy Trùng Không Được Lọc.")
    else:
        print(" [~] Lựa Chọn Không Hợp Lệ. Proxy Trùng Không Được Lọc.")


if __name__ == "__main__":
    asyncio.run(main())
