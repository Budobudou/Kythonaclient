#!/usr/bin/env python3
# Kythonaの読み方は「かいそな」です。
# Kythona Loader#
import requests,json,getpass,io,sys,time,re,os
if os.name == "nt":
	pass
elif os.name == "posix":
	import readline
homedir = os.path.expanduser("~")
os.chdir(homedir)
savedir = f"{homedir}//.kythonaSE.txt"
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if os.name == "nt":
	print("* KythonaClient Version 2.1")
elif os.name == "posix":
	print("\033[36m"+"* KythonaClient"+"\033[0m"+" Version 2.1")
apiurl = "https://kana.renorari.net/api/api.json"
try:
	file = open(savedir, "r")
	fcache = file.readlines()
	logid1 = fcache[0]
	logid = re.sub("\n","",logid1)
	logpass1 = fcache[1]
	logpass = re.sub("\n","",logpass1)
	kdict1 = fcache[2]
	kdict = re.sub("\n","",kdict1)
	file.close()

except FileNotFoundError:
	print("[Login] KanaAPIのIDとパスワードを入力してください \n ※ パスワードは表示されません。")
	logid = input("ID> ")
	time.sleep(0.3)
	logpass = getpass.getpass("Pass> ")
	kdict = "https://raw.githubusercontent.com/renorari/Kana-dictionary/main/discord.kana"
# Login And Test #
	print("ログインテスト中...")
	logpost = f"message=login_test&id={logid}&password={logpass}&customize_url=none"
	login1 = requests.post(apiurl, data=logpost.encode("utf-8"))
	login2 = login1.text
	if login2.startswith("エラーが発生しました"):
		print("KanaAPIでエラーが発生したため、終了します。")
		print(login2)
		sys.exit()
	else:
		writedata = open(savedir, "w")
		writedata.write(f"{logid}\n")
		writedata.write(f"{logpass}\n")
		writedata.write(f"{kdict}\n")
		writedata.close()
		print("ログインに成功しました。Kythona(かいそな)へようこそ！")
print("コマンド一覧は/helpと入力してください。")

# Bot Talk #
while True:
	rawmsg = input("Kythona> ")
	if rawmsg == "/help":
		print("・/help 今実行したコマンドだよ。\n・/exit KythonaClientを終了するよ。\n・/json 直前のメッセージの詳細を表示するよ。\n・/logout 設定を削除してログアウトするよ。")
	elif rawmsg == "/exit":
		sys.exit()
		print("何もしていないのに終了できなかった、ごめん^^")
	elif rawmsg == "/logout":
		os.remove(savedir)
		print("設定を削除してログアウトしました。終了します。")
		sys.exit()
	elif rawmsg.startswith("/cdict "):
		kdict = rawmsg[7:]
		print(f"辞書を{kdict}に変更しました。")
	elif rawmsg == "/json":
		try:
			print(data3)
		except NameError:
			print("Kythonaでエラーが発生しました")
			print("Jsonデータがありません")
	else:
		msg = str(rawmsg)
		postd = f"message={msg}&id={logid}&password={logpass}&customize_url={kdict}"
		data2 = requests.post(apiurl, data=postd.encode("utf-8"))
		data3 = data2.text
		if data3.startswith("エラーが発生しました"):
			print("KanaAPIでエラーが発生したため、終了します。")
			print(data3)
			print(f"ログイン情報：\nID:{logid}\nPass:{logpass}\nDictURL:{kdict}")
			sys.exit()
		else:
			# Extension
			data4 = json.loads(data3)
			if "timer" in data4["extension"].keys():
				print(data4["extension"]["timer"]["start_message"])
				sys.stdout.flush()
				time.sleep(data4["extension"]["timer"]["time"])
				print(data4["extension"]["timer"]["end_message"])
			else:
				dataf = data4["reply"]
				print(dataf)
