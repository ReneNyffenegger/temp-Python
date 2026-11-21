#!/usr/bin/env python3


from llama_cpp import Llama

llm = Llama.from_pretrained(
   repo_id   ='bartowski/Llama-3.2-3B-Instruct-GGUF',
#  local_dir ='.',
   filename  ='Llama-3.2-3B-Instruct-Q4_K_L.gguf',
   verbose   = False,
   n_ctx     = 4096
)

res = llm.create_chat_completion(
    messages=[
        {"role": "system", "content": "The answers should make use of emojis"},
        {"role": "user"  , "content": "What are the first 20 prime numbers"},
    ],
    temperature=0.2
)

print(f"Object:    {res['object' ]}")
print(f"MOdel:     {res['model'  ]}")
print(f"Created:   {res['created']}")
usg = res['usage']
print( "Token usage ")
print(f"   prompt    : {usg['prompt_tokens'    ]}")
print(f"   completion: {usg['completion_tokens']}")
print(f"   total:      {usg['total_tokens'     ]}")

print( "Choices")
for choice in res['choices']:
    msg = choice['message']
    print(f"  logprobs     : {choice['logprobs'     ]}")
    print(f"  finish reason: {choice['finish_reason']}")
    print(f"  Message role : {msg['role']}")
    print(f"  Content      : {msg['content']}")
    print('')
# print(dir(llm))
