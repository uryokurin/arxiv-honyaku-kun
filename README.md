# arxiv-honyaku-kun 🧐
arXivのIDを入れると，タイトルと要旨を日本語訳してくれます

## どんなふうに使うの? 😊

+ あなたの環境にPythonを導入しましょう．Python 3.13.3で動作確認しています [Windowsの場合](https://sukkiri.jp/technologies/processors/python/python%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%96%B9%E6%B3%95windows%E7%B7%A8.html)
+ ```getmeta.py```の最初の方を参考に，「OpenAI」「feedparser」「python-dotenv」など必要なモジュールを```pip install XXXX```でインストールしましょう． [参考](https://qiita.com/kakari8888/items/86d9c255204b063c87ee)
+ Open AIのAPIキーを入手しましょう．使用は有料ですが，大量に使うなどしなければ，少額で済みます．(記事2本の翻訳で0.01ドルくらい) [方法](https://note.com/yon4987/n/n5d2f0bd3356c#b3ef293d-4e38-472a-a353-b1056a9d1524)
+ ```getmeta.py```の24行目の「OPENAI_API_KEY」に，入手したAPIキーを入力するか，同じ場所に".env"ファイルを作り，
```OPENAI_API_KEY = 入手したAPIキー```
と入力してみましょう [参考記事](https://zenn.dev/nakashi94/articles/9c93b6a58acdb4)
+ 準備ができたら，ターミナルで，
```python getmeta.py```
でファイルを実行しましょう
+ ターミナルの指示に従って，翻訳したいarXivのIDを入力しましょう