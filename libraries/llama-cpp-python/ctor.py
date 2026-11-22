#!/usr/bin/env python3

from llama_cpp import Llama

llm = Llama(
      model_path   = '/home/rene/.cache/huggingface/hub/models--bartowski--Llama-3.2-3B-Instruct-GGUF/snapshots/5ab33fa94d1d04e903623ae72c95d1696f09f9e8/Llama-3.2-3B-Instruct-Q4_K_L.gguf',
      n_gpu_layers =-1,          # Uncomment to use GPU acceleration
      seed         = 1337,       # Uncomment to set a specific seed
      n_ctx        = 2048,       # Uncomment to increase the context window
      verbose      = False       # Print or do not print model-loading diagnostics and tokenizer.chat_template inside the model metadata.
                                 # The {% … %} is Jinja2
)

#
# As far as I can tell, create_completion is called by __call__,
# so, create_completion is technically not necessary.
#
res = llm.create_completion(
      prompt      =  "Tell me some interesting facts about Switzerland's largest city.",
      max_tokens  =   1024, # Generate up to 32 tokens, set to None to generate up to the end of the context window
 #    stop        = ["Q:", "\n"], # Stop generating just before the model would generate a new question
      echo        = False # Don't echo the prompt back in the output
)

# for k, v in res.items():
#     print(f'{k} -> {v}')

print()
print()
print()

print(res['choices'][0]['text'])

# print(f"Object:    {res['object' ]}")
# print(f"MOdel:     {res['model'  ]}")
# print(f"Created:   {res['created']}")
# usg = res['usage']
# print( "Token usage ")
# print(f"   prompt    : {usg['prompt_tokens'    ]}")
# print(f"   completion: {usg['completion_tokens']}")
# print(f"   total:      {usg['total_tokens'     ]}")
# 
# print( "Choices")
# for choice in res['choices']:
#     msg = choice['message']
#     print(f"  logprobs     : {choice['logprobs'     ]}")
#     print(f"  finish reason: {choice['finish_reason']}")
#     print(f"  Message role : {msg['role']}")
#     print(f"  Content      : {msg['content']}")
#     print('')
# # print(dir(llm))
