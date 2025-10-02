#import getpass
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

openai_api_key = "FILL THIS IN OPKSF{AKSPKFPASKFOPSAPOF}"




llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=openai_api_key,  # if you prefer to pass api key in directly instaed of using env vars
    # base_url="...",
    # organization="...",
    # other params...
)


messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
print(ai_msg)




'''
model = init_chat_model("gpt-4o-mini", model_provider="openai")

os.environ["OPENAI_API_KEY"] = openai_api_key



messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

model.invoke(messages)

#model.invoke("Hello")

#model.invoke([{"role": "user", "content": "Hello"}])

#model.invoke([HumanMessage("Hello")])



curl -X POST "https://api.smith.langchain.com/runs" \
-H "x-api-key: YOUR_LANGSMITH_API_KEY" \
-H "Content-Type: application/json" \
-d '{"name": "Test Run", "run_type": "chain"}'




'''