
with open('data/gamayun_kit5k.eng', 'r', encoding='utf=8') as file:
    data_en = file.read()

with open('data/gamayun_kit5k.swa', 'r', encoding='utf=8') as file:
    data_sw = file.read()

# print(data_en)
# print(data_sw)



"""
from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments

# Load the T5 tokenizer and model
tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = T5ForConditionalGeneration.from_pretrained('t5-small')

# Prepare the training data
train_data = ...

# Prepare the validation data
val_data = ...

# Set up the training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    eval_steps=100,
    save_steps=500,
    warmup_steps=500,
    learning_rate=5e-5,
    logging_dir='./logs',
    logging_steps=100,
)

# Define the trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_data,
    eval_dataset=val_data,
    data_collator=lambda data: {'input_ids': tokenizer(data['input_text'], padding=True, truncation=True, max_length=512, return_tensors='pt').input_ids, 'attention_mask': tokenizer(data['input_text'], padding=True, truncation=True, max_length=512, return_tensors='pt').attention_mask, 'labels': tokenizer(data['target_text'], padding=True, truncation=True, max_length=512, return_tensors='pt').input_ids},
)

# Fine-tune the model
trainer.train()


"""