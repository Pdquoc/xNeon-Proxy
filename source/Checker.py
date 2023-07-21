import requests
import colorama
import concurrent.futures

def check_proxy(proxy, timeout):
    try:
        proxies = {
            'http': f'http://{proxy}',
            'https': f'http://{proxy}',
            'socks4': f'socks4://{proxy}',
            'socks5': f'socks5://{proxy}'
        }
        response = requests.get('https://www.google.com', proxies=proxies, timeout=timeout)
        if response.status_code == 200:
            speed = response.elapsed.total_seconds()
            print(f'[xNeon] \x1b[38;5;46mLIVE\x1b[38;5;255m: {proxy}\x1b[38;5;255m | Speed: \x1b[38;5;46m{speed} \x1b[38;5;255mseconds')
            if proxy.startswith('socks'):
                with open("socks_proxies.txt", "a") as socks_file:
                    socks_file.write(proxy + "\n")
            else:
                with open("http_proxies.txt", "a") as http_file:
                    http_file.write(proxy + "\n")
    except:
        pass

def main():
    file_path = input("Nhập đường dẫn của file proxy: ")
    timeout = int(input("Nhập timeout (giây): "))
    num_threads = int(input("Nhập số lượng luồng (threads): "))

    print("[xNeon] Proxy Checker - Đang kiểm tra proxy...")

    with open(file_path, 'r') as file:
        proxies = file.read().splitlines()

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = [executor.submit(check_proxy, proxy, timeout) for proxy in proxies]
        for future in concurrent.futures.as_completed(results):
            future.result()

    print("[xNeon] Proxy HTTP, HTTPS working đã được lưu vào file: http_proxies.txt")
    print("[xNeon] Proxy SOCKS4, SOCKS5 working đã được lưu vào file: socks_proxies.txt")

if __name__ == "__main__":
    main()
