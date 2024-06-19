from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class Rephraser:

    def __init__(self) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained('models/arabic-t5-small-question-paraphrasing.tokenizer')
        self.model = AutoModelForSeq2SeqLM.from_pretrained('models/arabic-t5-small-question-paraphrasing.model')

    def rephrase(self, text: str) -> str:
        inputs = self.tokenizer(text, return_tensors='pt')
        outputs = self.model.generate(**inputs)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

