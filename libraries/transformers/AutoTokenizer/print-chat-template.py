#!/usr/bin/env python3
# vim: foldmethod=marker foldmarker={{{,}}}

# Compare with
#    /home/rene/github/dev/lang/python/temp/libraries/llama-cpp-python/print-chat-template.py

from transformers import AutoTokenizer

# Load only the tokenizer and print its Jinja chat template.
tokenizer = AutoTokenizer.from_pretrained('unsloth/Meta-Llama-3.1-8B-Instruct')
print(tokenizer.chat_template)
