#!/usr/bin/env python3
# Kythonaの読み方は「かいそな」です。
import requests,json,getpass,io,sys,time,re,os
if os.name == "nt":
    pass
elif os.name == "posix":
    import readline
homedir = os.path.expanduser("~")
os.chdir(homedir)
savedir = f"{homedir}//.kythonaid.txt"
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
global logid
global logpass
global kdict
logwatch = 0
# KythoNano3
def kysend(rawmsg,logid,logpass,kdict):
        msg = str(rawmsg)
        appjson = {
"message": msg,
"user": {
"id": logid,
"password": logpass
},
"character_name": kdict
}
        headers = {"content-type": "application/json"}
        apiurl = "https://kana.renorari.net/api/v2/chat"
        data2 = requests.post(apiurl,data=json.dumps(appjson),headers=headers)
        data3 = data2.text
        data4 = json.loads(data3)
        return data4
def kyac(logid,logpass):
        appjson = {
            "user": {
            "id": logid,
            "password": logpass
         }
}
        headers = {"content-type": "application/json"}
        apiurl = "https://kana.renorari.net/api/v2/account/info"
        data2 = requests.post(apiurl,data=json.dumps(appjson),headers=headers)
        data3 = data2.text
        data4 = json.loads(data3)
        return data4
# Kythona Loader#
if os.name == "nt":
    print("* KythonaClient v3")
elif os.name == "posix":
    print("\033[36m"+"* KythonaClient"+"\033[0m"+" v3")
try:
    file = open(savedir, "r")
    fcache = file.readlines()
    logid1 = fcache[0]
    logid = re.sub("\n","",logid1)
    logpass1 = fcache[1]
    logpass = re.sub("\n","",logpass1)
    kdict = "discord"
    file.close()
except FileNotFoundError:
    print("[Login] KanaAPIのIDとパスワードを入力してください \n ※ パスワードは表示されません。")
    logid = input("ID> ")
    kdict = "discord"
    time.sleep(0.3)
    logpass = getpass.getpass("Pass> ")
   # kdict = "https://raw.githubusercontent.com/renorari/Kana-dictionary/main/discord.kana"
# Login And Test #
    print("ログインテスト中...")
    data4 = kysend("login_test",logid,logpass,kdict)
    try:
        if data4["status"] == "error":
            print("KanaAPIでエラーが発生したため、終了します。")
            print(data4["message"])
            sys.exit()
    except KeyError:
        if data4["reply_probability"] == 100:
            data4 = kyac(logid,logpass)
            name = data4["name"]
            writedata = open(savedir, "w")
            writedata.write(f"{logid}\n")
            writedata.write(f"{logpass}\n")
            writedata.close()
            print(f"ログインに成功しました。{name}さん、Kythona(かいそな)へようこそ！")
print("コマンド一覧は/helpと入力してください。")

# Bot Talk #
while True:
    rawmsg = input("Kythona3> ")
    if rawmsg == "/help":
        print("[Kythona3コマンド一覧]\n・/exit KythonaClientを終了するよ。\n・/json 直前のメッセージの詳細を表示するよ。\n・/id ログイン情報を表示するよ。\n・/logout 設定を削除してログアウトするよ。")
    elif rawmsg == "/exit":
        print("ご利用ありがとうございました。")
        sys.exit()
        print("何もしていないのに終了できなかった、ごめん^^")
    elif rawmsg == "/logout":
        os.remove(savedir)
        print("設定を削除してログアウトしました。終了します。")
        sys.exit()
    elif rawmsg.startswith("/cdict "):
        kdict = rawmsg[7:]
        print(f"辞書を{kdict}に変更しました。")
    elif rawmsg == "/id":
        if logwatch < 3:
            print(f"ログイン情報を表示するにはあと{4 - logwatch}回 /id コマンドをタイプします")
            logwatch = logwatch + 1
        elif logwatch == 3:
            print(f"最後にあと1回 /id コマンドをタイプして本当にIDとパスワードを表示します。よろしいですか？")
            logwatch = logwatch + 1
        elif logwatch == 4:
            data4 = kyac(logid,logpass)
            name = data4["name"]
            mail = data4["email"]
            print(f"ログイン情報:\n名前:{name}\nID：{logid}\nパスワード:{logpass}\n登録メールアドレス:{mail}")
    elif rawmsg == "/json":
        try:
            print(data4)
        except NameError:
            print("Kythonaでエラーが発生しました")
            print("Jsonデータがありません")
    elif rawmsg.startswith("/"):
        print("コマンドが見つかりませんでした。\n/help を確認してください")
    else:
        msg = str(rawmsg)
        try:
            data4 = kysend(rawmsg,logid,logpass,kdict)
        except:
            print("何らかのエラーが発生したようです")
            continue
        
        dataf = data4["reply"]
        # Extension Support
        if data4["extension"]["replyer"] == "timer":
            print(data4["extension"]["timer"]["start_message"])
            sys.stdout.flush()
            time.sleep(data4["extension"]["timer"]["time"])
            print(data4["extension"]["timer"]["end_message"])
        else:
            print(dataf)
