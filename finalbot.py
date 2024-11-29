from transformers import pipeline
import torch

model_id = "meta-llama/Llama-3.1-8B-Instruct"

pipe = pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={
        "torch_dtype": torch.bfloat16,
        "quantization_config": {"load_in_4bit": True} # Change this depending on your graphics card strength for a more accurate model.
    },
)

# Edit the conversation elements to make a foundation of a continuous conversation.
# These will not be printed when the model is loaded, but the following conversation will append to this history and build along its structure.
# An example will be provided with structure and outcome.

conversation_history = [{"role": "user", "content": "CONVERSATION ELEMENT 0"},
    {"role": "bot", "content": "CONVERSATION ELEMENT 1"},
    {"role": "user", "content": "CONVERSATION ELEMENT 2"},
    {"role": "bot", "content": "CONVERSATION ELEMENT 3"},
]

while True:
    user_input = input("User: ")
    conversation_history.append({"role": "user", "content": user_input})

    outputs = pipe(conversation_history, max_new_tokens=256, pad_token_id=2) #Edit max_new_tokens as you wish.

    response = outputs[0]["generated_text"][-1]["content"]

    conversation_history.append({"role": "bot", "content": response})

    print(f"\nBot: {response}\n") #"Bot:" can be changed to whatever you want
