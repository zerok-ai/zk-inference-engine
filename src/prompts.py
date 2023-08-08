'''
===========================================
        Module: Prompts collection
===========================================
'''
# Note: Precise formatting of spacing and indentation of the prompt template is important for Llama-2-7B-Chat,
# as it is highly sensitive to whitespace changes. For example, it could have problems generating
# a summary from the pieces of context if the spacing is not done correctly

qa_template = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

We are using a json array to represent a network traces across different protocols.

For the following json array containing request and response payloads for all spans for a trace, we will need to find the root cause

The request and response payloads are truncated to 1000 characters for brevity.

Following are the spans:

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""
