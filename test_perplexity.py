from perplexity_engine import (
    calculate_perplexity
)

text = """
Transformers are deep learning architectures that use self-attention mechanisms to process sequential information. Unlike recurrent neural networks, transformers can process tokens in parallel, making training significantly faster. They are widely used in natural language processing tasks such as machine translation, question answering, and text generation.
"""
score = calculate_perplexity(
    text
)

print(
    "Perplexity:",
    score
)