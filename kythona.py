#!/usr/bin/env python3
# Kythonaの読み方は「かいそな」です。
# Kythona Loader#
import requests, json, getpass, io ,sys , time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print("KythonaClient Version 1.1")
print("[Login] KanaAPIのIDとパスワードを入力してください \n ※ パスワードは表示されません。")
logid = input("ID>")
time.sleep(0.3)
logpass = getpass.getpass("Pass>")
apiurl = "https://kana.renorari.net/api/api.json"
# Login And Test #
logpost = f"message=Hello&id={logid}&password={logpass}&customize_url=none"
login1 = requests.post(apiurl, data=logpost.encode("utf-8"))
login2 = login1.text
if login2.startswith("エラーが発生しました"):
	print("KanaAPIでエラーが発生したため、終了します。")
	print(login2)
	sys.exit()
print(">>Kythonaへようこそ。\nコマンド一覧は/helpと入力してください。")
# Bot Talk #
while True:
	rawmsg = input("Kythona>")
	if rawmsg == "/help":
		print("・/help 今実行したコマンドだよ。\n・/exit KythonaClientを終了するよ。")
	elif rawmsg == "/exit":
		sys.exit()
	else:
		msg = str(rawmsg)
		postd = f"message={msg}&id={logid}&password={logpass}&customize_url=none"
		data2 = requests.post(apiurl, data=postd.encode("utf-8"))
		data3 = data2.text
		data4 = json.loads(data3)
		dataf = data4["reply"]
		print(dataf)
