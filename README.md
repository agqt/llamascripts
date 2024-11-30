# LlamaScripts
Python scripts for continuous text generation out-of-the-box with Llama-3.1-8B-Instruct from huggingface.co. Should work with 70B or lower models as well, but untested on different models. All runs locally on your machine, with a quantization parameter for lower-end graphics cards. I've designed the script to be as plug-and-play as possible, and as short as possible for maximum modularity, once everything is cloned and set up in the virtual environment. Do keep in mind that 20-30GB of disk space is required for the model and associated data.

It's highly recommended to do all this inside of a python venv.

To run, make sure you have `transformers`, `torch`, `pipeline`, `accelerate`, `bitsandbytes`, and other prerequisites installed like recommended in https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
A lot of the prerequisites can simply be installed with `pip install huggingface-hub`, then the others I listed above should be installed next.

Follow the instructions to `git clone` the Llama-3.1-(8/70/xxx)B-Instruct model to a certain directory that you plan to exclusively use for the project.

This script I made is supposed to be the easiest out-of-the-box way to get your model to run on your local graphics card. Shards are usually installed to `~/.cache/huggingface/hub/models--meta-llama--Llama-3.1-8B-Instruct`
There are instructions online on how to specify a custom shard directory to save a "snapshot" of the model, crediting Liang-ml at https://www.cnblogs.com/Liang-ml/p/18167156

A successful load of the model after running my python script should look like:

```
(lvenv) gqt@gentoo-linux ~/llama/Llama-3.1-8B-Instruct $ python 5cstest.py 
`low_cpu_mem_usage` was None, now default to True since model is quantized.
Loading checkpoint shards: 100%|██████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.23s/it]
User: 
```

Where you are able to input text under user. Responses may take a few seconds to generate, depending on how good/bad your graphics card is.

Make sure you have at least 6-7 GB of VRAM available, even with the 4-bit version of the script. Higher bits require more VRAM. I recommend following https://llamaimodel.com/requirements/, and underestimating your graphics card's capabilities, to not run into a "no VRAM available to allocate" error.

# Examples

The script provides a brief conversation history (can be extended) that is not visible when running the program, but sets the foundation for the model's subsequent generations. If, for example, you want to simulate a patient in a hospital running into House M.D., you could use the conversation_history below (remember to change `"role": "bot"` to `"role": "house"` elsewhere in the script if you do use this, and you can optionally edit the response print line to say `<name>: ` instead of `Bot: `):

```
conversation_history = [{"role": "user", "content": "Who are you? Wait, you're doctor House!"},
    {"role": "house", "content": "What are you, some amnesiac?"},
    {"role": "user", "content": "Actually I'm schizophrenic."},
    {"role": "house", "content": "Well that changes everything! Cuddy, I'm skipping clinic hours today. Busy with a schizophrenic. And not in that sense."},
]
```

I've found that the subsequent generations once the model is ran are very accurate to House's nature. Obviously, the longer the conversation history, the more accurate the model. In the future, I plan to implement a database of possible conversation histories, and have chats append to the database if the user decides to. You can place the script anywhere and run it as long as you're in the venv with `python <script>.py` but I suggest keeping everything in the cloned Llama-3.1 directory. I got it to make this gem after a few back-and-fourths:

> User: it was traumatic, nothing else is medically relevant..
> 
> House: (firmly) Oh, so now you're an expert on medical relevance? I doubt it. (pauses) Fine. If you're not going to tell me anything useful, then I'm wasting my time here. (stands up) I have better things to do than listen to your vague, nonspecific complaints. (starts to walk away)
> 
> Wait, don't think you're off the hook that easily. I'll write you a prescription for some anti-psychotics, just in case. (pulls out a prescription pad) And don't bother filling it until you've seen a real psychiatrist, or a real doctor, for that matter. (hands you the prescription)
> 
> User: my head's been hurting too though
> 
> House: (stops in his tracks, turns around) Ah, now you're telling me? A headache? That's a classic symptom of... (pauses, eyes narrowing)...of just about anything, really. (walks back to his desk, scribbles some notes) But, I suppose it's worth investigating. (looks up) What kind of pain are you experiencing? Is it a dull ache, a sharp pain, or something else? (leans forward, his expression curious)

All of this runs locally on your machine, so making it analyze/comment on sensitive data is a strong point of this model. Do keep in mind that this is just Llama-3.1-8B, it's impressive but nothing crazy. Now you should have a local AI to tinker with for free!

Any feedback is much appreciated! If any clarification for further instructions is needed on how to set it up and the documentation doesn't adequately address your concerns, let me know. This took me several hours to figure out.
