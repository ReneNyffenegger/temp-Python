#!/usr/bin/env python3

# this works at least with .gguf files. NOt sure if it works with others, too.

# Compare with
#   /home/rene/github/dev/lang/python/temp/libraries/transformers/AutoTokenizer/print-chat-template.py

import sys

from llama_cpp import Llama

llm = Llama(model_path=sys.argv[1], verbose=False)
print(llm.metadata['tokenizer.chat_template'])
