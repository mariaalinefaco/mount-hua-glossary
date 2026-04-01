import csv
import os
import re

base_dir = os.path.dirname(__file__)

# caminhos dos arquivos
normalized_path = os.path.join(base_dir, "..", "data", "cleaned_glossary", "normalized_terms.csv")
glossary_path = os.path.join(base_dir, "..", "data", "cleaned_glossary", "glossary_v1.csv")
input_path = os.path.join(base_dir, "..", "data", "sample_texts", "sample.txt")
output_path = os.path.join(base_dir, "..", "output", "sample_corrected.txt")


def load_csv_terms(path, source_col, target_col):
    terms = {}
    with open(path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            source = row[source_col].strip()
            target = row[target_col].strip()
            if source and target:
                terms[source] = target
    return terms


def replace_ignore_case(text, wrong, correct):
    pattern = re.compile(rf"\b{re.escape(wrong)}\b", re.IGNORECASE)

    def replacer(match):
        word = match.group()
        if word.isupper():
            return correct.upper()
        elif word[0].isupper():
            return correct.capitalize()
        else:
            return correct

    return pattern.sub(replacer, text)


# carregar os CSVs
normalized_terms = load_csv_terms(normalized_path, "variant", "normalized")
glossary_terms = load_csv_terms(glossary_path, "wrong", "correct")

# ler texto de entrada
with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

# aplicar normalização primeiro
for wrong, correct in normalized_terms.items():
    text = replace_ignore_case(text, wrong, correct)

# aplicar glossário principal depois
for wrong, correct in glossary_terms.items():
    text = replace_ignore_case(text, wrong, correct)

# salvar saída
with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

print("=== TEXTO CORRIGIDO ===")
print(text)
print("\nArquivo salvo em:", output_path)