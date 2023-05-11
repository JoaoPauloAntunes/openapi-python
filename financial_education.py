# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: openapi
#     language: python
#     name: python3
# ---

# %%
from dotenv import load_dotenv
import time
import os
import openai


load_dotenv(".env")

# Authenticate with OpenAI API
openai.api_key = os.environ["OPENAI_API_KEY"]

# Prompt for generating article
prompt = "escreva um artigo de blog falando sobre educação financeira"

# Parameters for GPT-3
model_engine = "text-davinci-002"
max_tokens = 1024
temperature = 0.5

# Generate response from GPT-3
start = time.time()
response = openai.Completion.create(engine=model_engine,
                                    prompt=prompt,
                                    max_tokens=max_tokens,
                                    temperature=temperature)
elapsed_time = time.time() - start

# Print response
print(response.choices[0].text)
print(f"\nElapsed Time: {elapsed_time:.2f} seconds")


# %% [markdown]
# A importância da educação financeira
#
# Muitas pessoas não dão importância à educação financeira, mas ela é essencial para o sucesso financeiro. A educação financeira ensina as pessoas a gerenciar o dinheiro de forma eficiente e a fazer escolhas financeiras sábias.
#
# As pessoas que têm um bom conhecimento sobre educação financeira tendem a ganhar mais dinheiro, economizar mais dinheiro e ter menos dívidas. A educação financeira também pode ajudar as pessoas a serem mais bem-sucedidas em seus empregos e a ter uma vida financeira mais estável.
#
# A educação financeira é importante para todas as pessoas, independentemente da idade, renda ou situação financeira. Se você quer aprender mais sobre educação financeira, há muitos recursos disponíveis, incluindo livros, sites da internet, programas de televisão e cursos.
#
# Elapsed Time: 10.05 seconds
