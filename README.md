# Mount Hua Glossary Project

A glossary-based NLP project to improve machine-translated (MTL) English text from *Return of the Mount Hua Sect* using fan-made glossaries.

## Goal
Build a correction pipeline for MTL novel text using structured glossary replacements, starting with English corrections and later expanding to English → Portuguese post-editing.

## Features
- Loads glossary entries from CSV
- Applies glossary-based corrections to MTL text
- Reads input text files
- Saves corrected output files

## Project Structure
- `data/raw_glossaries/` → original forum glossaries
- `data/cleaned_glossary/` → cleaned structured glossary files
- `data/sample_texts/` → sample text inputs
- `scripts/` → Python scripts
- `output/` → corrected text outputs

## Current Status
Initial prototype completed:
- raw glossary collection
- first cleaned CSV glossary
- automatic text replacement
- input/output file handling

## Next Steps
- add more raw glossaries
- merge repeated glossary entries
- improve replacements with regex
- preserve capitalization
- expand pipeline to English → Portuguese

This project aims to improve machine-translated (MTL) versions of the novel \*Return of the Mount Hua Sect\* using fan-made glossaries.



\## Features

\- Applies glossary-based corrections to English MTL text

\- Supports structured CSV glossaries

\- Reads input text files and outputs corrected versions



\## Project Structure

\- `data/raw\_glossaries/` → original glossaries from forums

\- `data/cleaned\_glossary/` → structured glossary data

\- `data/sample\_texts/` → test input texts

\- `scripts/` → Python scripts

\- `output/` → corrected outputs



\## Current Status

Initial prototype working:

\- CSV glossary loading

\- Text replacement system

\- File input/output



\## Future Improvements

\- Case-insensitive replacement without losing formatting

\- Context-aware corrections

\- Korean → English → Portuguese pipeline

\- Integration with translation tools

