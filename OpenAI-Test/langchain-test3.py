import os, getpass

openai_api_key = "FILL THIS IN OPKSF{AKSPKFPASKFOPSAPOF}"

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = openai_api_key

_set_env("OPENAI_API_KEY")


from langchain_openai import ChatOpenAI
gpt4o_chat = ChatOpenAI(model="gpt-4o", temperature=0)
gpt35_chat = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)


from langchain_core.messages import HumanMessage

# Create a message
msg = HumanMessage(content="Hello world", name="Lance")

# Message list
messages = [msg]

# Invoke the model with a list of messages 
print(gpt4o_chat.invoke(messages))

print(gpt4o_chat.invoke("hello world"))


print(gpt35_chat.invoke("Who is Neil Armstrong?"))