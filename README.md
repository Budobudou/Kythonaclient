![Test Image 1](https://github.com/Budobudou/Kythonaclient/blob/main/Kythona256.png?raw=true)
# KythonaClient
コンソール上で動作するPythonで書かれたKanaAPIのクライアント
## 使用パッケージ
requests  
readline(Linuxのみ)
## 使い方
1.Python3と、上記パッケージがインストールされた環境で、実行します。
```
$ ./kythona.py
```
2.[こちら](https://kana.renorari.net/api/)で作成したKanaAPIのIDとパスワードを使ってログイン  
※間違ってるとエラーが出ます。  
3.楽しもう！   
## アップデート
### Version 2.1
・windows対応になりました！  
・設定ファイルを削除してログアウトする/logoutコマンドを追加！
### Version 2.0
・KanaAPIのタイマー機能に対応！！！  
・readlineモジュールの採用により、方向キーが使えるようになりました！  
・windows非対応になりました。  
・実はバージョン1.2でこっそり追加されたjsonコマンドがhelpコマンドに追加されました()  
・ログイン情報をホームディレクトリ直下に保存されるように変更。  
・その他、デザインを変更。  
### Version 1.2
・ログイン情報がカレントディレクトリに保存されるようになりました！  
毎回パスワードを入力する必要はありません！  
### Version 1.1
・ログイン時に何らかのエラーが出るとエラー内容を表示しプログラムを終了するようになりました。  
・コマンドを実装し、/exitでクライアントを終了できるようになりました。
