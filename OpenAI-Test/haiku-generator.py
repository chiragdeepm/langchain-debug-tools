from openai import OpenAI

client = OpenAI(
  api_key="OPEN AI API KEY GOES HERE"
)

response = client.responses.create(
  model="gpt-5-nano",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text);

