import os
from openai import OpenAI

# APIキーを直接指定する
api_key = ""
client = OpenAI(api_key=api_key)

response = client.completions.create(
    model="text-davinci-003",  # 使用するモデルを指定
    prompt="ここにプロンプトを入力",  # APIに送るプロンプト
    max_tokens=50  # 応答の最大トークン数
)

print(response.choices[0].text.strip())

