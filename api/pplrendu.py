import os
import re

def generate_report_minimal_spaces(root_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as f_out:
        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f_in:
                        lines = f_in.readlines()
                        cleaned_lines = []
                        for line in lines:
                            # Supprime espaces en début et fin, et réduit multiples espaces internes à un seul
                            line_clean = re.sub(r'\s+', ' ', line.strip())
                            cleaned_lines.append(line_clean)
                        content_clean = '\n'.join(cleaned_lines)
                except Exception as e:
                    content_clean = f"<Erreur lecture fichier : {e}>"
                
                f_out.write(f"---Fichier:{filepath}---\n")
                f_out.write(content_clean + "\n\n")

if __name__ == "__main__":
    dossier_api = r"C:\smartmaritime\api"
    sortie = r"C:\smartmaritime\rapport_minimal_spaces.txt"
    generate_report_minimal_spaces(dossier_api, sortie)
    print(f"Rapport généré dans {sortie}")
