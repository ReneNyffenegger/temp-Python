#!/usr/bin/env python3


from llama_cpp import Llama

llm = Llama.from_pretrained(
   repo_id   ='bartowski/Llama-3.2-3B-Instruct-GGUF',
#  local_dir ='.',
   filename  ='Llama-3.2-3B-Instruct-Q4_K_L.gguf',
   verbose   = False,
   n_ctx     = 4096
)

print(dir(llm))
