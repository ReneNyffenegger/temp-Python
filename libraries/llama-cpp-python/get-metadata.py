#!/usr/bin/env python3

import sys

from llama_cpp import Llama

llm = Llama(model_path=sys.argv[1], verbose=False)
for k in sorted(llm.metadata):
    print(k)

# f9e8/Llama-3.2-3B-Instruct-Q4_K_L.gguf
# general.architecture
# general.basename
# general.file_type
# general.finetune
# general.license
# general.name
# general.quantization_version
# general.size_label
# general.type
# llama.attention.head_count
# llama.attention.head_count_kv
# llama.attention.key_length
# llama.attention.layer_norm_rms_epsilon
# llama.attention.value_length
# llama.block_count
# llama.context_length
# llama.embedding_length
# llama.feed_forward_length
# llama.rope.dimension_count
# llama.rope.freq_base
# llama.vocab_size
# quantize.imatrix.chunks_count
# quantize.imatrix.dataset
# quantize.imatrix.entries_count
# quantize.imatrix.file
# tokenizer.chat_template
# tokenizer.ggml.bos_token_id
# tokenizer.ggml.eos_token_id
# tokenizer.ggml.model
# tokenizer.ggml.pre
