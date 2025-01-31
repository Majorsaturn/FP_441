from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))
import ollama

from ollama import chat
ollama.pull("llama3.2")
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Nicholas Novak'
model = 'llama3.2'
options = {'temperature': 0.7, 'max_tokens': 100} #
messages = [
  {'role': 'system', 'content': 'you are a dnd dungeon master and must require the user to create their character before adventuring, ensure combat encounters make sense within a situation\'s context and make sure the user is presented with an in depth character creation text line'
                                'make sure that you set a point limit for the initial starter stats'},
]


# But before here.

options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:
  response = chat(model=model, messages=messages, stream=False, options=options)
  # Add your code below
  print(f'Agent: {response.message.content}')
  messages.append({'role': 'assistant', 'content': response.message.content})
  messages.append({'role': 'user', 'content': input('You: ')})
  # But before here.
  if messages[-1]['content'] == '/exit':
    break

# Save chat
with open(Path('attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)

