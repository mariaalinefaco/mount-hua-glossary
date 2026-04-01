import csv
import os

base_dir = os.path.dirname(__file__)

# caminho do glossário
glossary_path = os.path.join(base_dir, "..", "data", "cleaned_glossary", "glossary_v1.csv")

# carregar glossário
glossary = {}

with open(glossary_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        glossary[row["wrong"]] = row["correct"]

# ler arquivo de entrada
input_path = os.path.join(base_dir, "..", "data", "sample_texts", "sample.txt")

with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

# aplicar substituições
import re

def replace_ignore_case(text, wrong, correct):
    pattern = re.compile(rf'\b{re.escape(wrong)}\b', re.IGNORECASE)
    
    def replacer(match):
        word = match.group()
        if word.isupper():
            return correct.upper()
        elif word[0].isupper():
            return correct.capitalize()
        else:
            return correct

    return pattern.sub(replacer, text)


for wrong, correct in glossary.items():
    text = replace_ignore_case(text, wrong, correct)

# salvar saída
output_path = os.path.join(base_dir, "..", "output", "sample_corrected.txt")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

print("=== TEXTO CORRIGIDO ===")
print(text)
print("\nArquivo salvo em:", output_path)