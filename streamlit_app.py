from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load model and tokenizer
model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Load model
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",           # Uses GPU if available
    torch_dtype="auto"           # Auto-selects appropriate dtype
)

# Create text generation pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Prompt
prompt = "Tell me a short story about a robot who wants to become human."

# Generate text
output = generator(prompt, max_new_tokens=100, do_sample=True, temperature=0.7)

# Print result
print(output[0]["generated_text"])
