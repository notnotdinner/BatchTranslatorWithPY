from typing import List


class TranslationItem:
    text = str
    to = str


class DetectedLanguage:
    language = str
    score = float


class MSTranslateResult:
    detectedLanguage = DetectedLanguage
    translations = List[TranslationItem]
