from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import google.generativeai as genai
from helpers import detect_language

class Rephraser:

    def __init__(self) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained('models/arabic-t5-small-question-paraphrasing.tokenizer')
        self.model = AutoModelForSeq2SeqLM.from_pretrained('models/arabic-t5-small-question-paraphrasing.model')
        
        genai.configure(api_key='AIzaSyDgqjVRiqmUgXAKqmlV_wsa7VmEaJqXhyw')
        self.genai_model = genai.GenerativeModel(model_name='gemini-pro')

    def rephrase(self, text: str) -> str:
        try:
            if detect_language(text) == 'ar':
                response = self.genai_model.generate_content('اعد صياغة السؤال: ' + text)
            else:
                response = self.genai_model.generate_content('Rephrase the question: ' + text)
            return response.text
        except Exception as e:
            try:
                inputs = self.tokenizer(text, return_tensors='pt')
                outputs = self.model.generate(**inputs)
                return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            except Exception as e:
                return text
            


