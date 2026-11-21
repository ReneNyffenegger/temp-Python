#!/usr/bin/env python3


from llama_cpp import Llama

llm = Llama.from_pretrained(
   repo_id   ='bartowski/Llama-3.2-3B-Instruct-GGUF',
#  local_dir ='.',
   filename  ='Llama-3.2-3B-Instruct-Q4_K_L.gguf',
   verbose   = False,
   n_ctx     = 4096
)

response = llm.create_chat_completion(
    messages=[
        {"role": "system", "content": "The answers should make use of emojis"},
        {"role": "user"  , "content": "What are the first 20 prime numbers"},
    ],
    temperature=0.2
)

print(response['object'])
print(response['model'])
for choice in response['choices']:
    msg = choice['message']
    print(msg['role'] + ': ' + msg['content'])

# print(dir(llm))
