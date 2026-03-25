from fastapi import APIRouter
from deep_translator import GoogleTranslator

router = APIRouter()

@router.post("/translate")
def translate_text(data: dict):
    texts = data.get("texts", [])
    target_lang = data.get("target_lang", "English")

    # Language mapping
    lang_map = {
        "English": "en",
        "Hindi": "hi",
        "Telugu": "te"
    }

    target_code = lang_map.get(target_lang, "en")

    translated = []

    for text in texts:
        try:
            result = GoogleTranslator(source='auto', target=target_code).translate(text)
            translated.append(result)
        except:
            translated.append(text)

    return {"translated": translated}
