import feedparser
import os
from openai import OpenAI
from dotenv import load_dotenv
import datetime
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

dt_now = datetime.datetime.now()

# 論文のArXiv ID（例: 2402.10949）
arxiv_id = input("調べたいarXivのIDを入力してネ(例:2504.01234)")

def fetch_arxiv_data(arxiv_id):
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    feed = feedparser.parse(url)
    entry = feed.entries[0]
    return entry.title, entry.summary

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
#あなたのAPIキーを入れてあげてネ

def translate_to_japanese(text):
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user","content": f"以下を日本語に翻訳してください:\n{text}"}]
    )
    return response.choices[0].message.content

title, abstract = fetch_arxiv_data(arxiv_id)
title_ja = translate_to_japanese(title)
abstract_ja = translate_to_japanese(abstract)

print("【タイトル】")
print("原文:", title)
print("JA:", title_ja)
print("\n【要旨】")
print("原文:", abstract)
print("JA:", abstract_ja)

f = open(dt_now.strftime("%Y-%m-%d-%H-%M-%S")+".txt", "w",encoding="utf-8")
print("【タイトル】",file=f)
print("原文:", title,file=f)
print("JA:", title_ja,file=f)
print("\n【要旨】",file=f)
print("原文:", abstract,file=f)
print("JA:", abstract_ja,file=f)
f.close()