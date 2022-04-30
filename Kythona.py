#!/usr/bin/env python3
# Kythonaの読み方は「かいそな」です。
# Kythona Loader#
import requests, json, getpass, io ,sys , time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print("---KythonaClient Version 1.0---")
print("[ログイン]KanaAPIのIDとパスワードを入力してください \n ※ パスワードは表示されません。")
logid = input("ID>>")
time.sleep(0.3)
logpass = getpass.getpass("Pass>>")
apiurl = "https://kana.renorari.net/api/api.json"
# Bot Talk #
while True:
	rawmsg = input("メッセージ>>")
	msg = str(rawmsg)
	postd = f"message={msg}&id={logid}&password={logpass}&customize_url=none"
	data2 = requests.post(apiurl, data=postd.encode("utf-8"))
	data3 = data2.text
	data4 = json.loads(data3)
	
	print(data4["reply"])
