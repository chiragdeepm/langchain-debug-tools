#from langchain_community.llms import OpenAI
#from langchain import Memory, Agent
#from langchain.chains import SequentialChain

# Step 1: Define the model


# Step 2: Set up the memory
#memory = Memory()



from langchain.memory import ConversationBufferMemory  # Correct import for memory
from langchain_community.llms import OpenAI  # Correct import for OpenAI LLM
from langchain.agents import initialize_agent, AgentType  # Correct import for agent


openai_api_key = "EMPTY FILL THIS IN"


# Step 1: Set up memory to store the conversation
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Step 2: Create your LLM (GPT-4) instance
gpt4_llm = OpenAI(model="gpt-4", temperature=0.7,api_key=openai_api_key)

# Step 3: Initialize a simple agent with memory and LLM
agent = initialize_agent(
    tools=[],  # No extra tools needed for this example
    llm=gpt4_llm,
    agent_type=AgentType.ZERO_SHOT_REACT,  # This is for general-purpose tasks
    memory=memory,
    verbose=True  # This is just for debugging, you can set it to False if you want
)

#agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION

# Step 3: Create an agent

#agent = Agent(gpt4_llm, memory=memory)

response = agent.run("Who is Albert Einstein?")

print("Agent's response is\n",response)


