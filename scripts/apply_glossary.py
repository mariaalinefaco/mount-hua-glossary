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
text_lower = text.lower()

for wrong, correct in glossary.items():
    text_lower = text_lower.replace(wrong.lower(), correct)

# salvar saída
output_path = os.path.join(base_dir, "..", "output", "sample_corrected.txt")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(text_lower)

print("=== TEXTO CORRIGIDO ===")
print(text_lower)
print("\nArquivo salvo em:", output_path)