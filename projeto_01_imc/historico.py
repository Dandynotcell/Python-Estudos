import json
from pathlib import Path

ARQUIVO_HISTORICO = Path("historico.json")


def carregar_historico():
    if not ARQUIVO_HISTORICO.exists():
        return []

    conteudo = ARQUIVO_HISTORICO.read_text(encoding="utf-8")
    return json.loads(conteudo)


def salvar_historico(historico):
    texto_json = json.dumps(historico, ensure_ascii=False, indent=2)
    ARQUIVO_HISTORICO.write_text(texto_json, encoding="utf-8")