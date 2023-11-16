import openai

openai.api_key = "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"  # 実際のAPIキーに置き換えてください

response = openai.Completion.create(
    model="text-davinci-003",  # 使用するモデルを指定
    prompt="ここにプロンプトを入力",  # APIに送るプロンプト
    max_tokens=50  # 応答の最大トークン数
)

print(response.choices[0].text.strip())
