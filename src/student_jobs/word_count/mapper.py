import re
from src.core.job.mapper import Mapper

# Набір голосних (англ + укр)
VOWELS = set("aeiouyаеєиіїоуюяAEIOUYАЕЄИІЇОУЮЯ")

# Допоміжна функція: нормалізує слово
def normalize_word(token: str) -> str:
    """
    Видаляє всі символи, крім літер і цифр, і приводить до lower().
    Підходить і для українського, і для англійського тексту.
    """
    # Залишаємо тільки букви та цифри
    cleaned = re.sub(r"[^A-Za-zА-Яа-яЁёІіЇїЄєҐґ0-9]", "", token)
    return cleaned.lower()


class WordCountMapper(Mapper):
    """
    ЗАВДАННЯ 1:
    Порахувати слова, попередньо прибравши розділові знаки.
    """

    def map(self, record, emit):
        text = str(record)
        for raw_token in text.split():
            word = normalize_word(raw_token)
            if word:  # ігноруємо порожні строки
                emit(word, 1)


class LongWordCountMapper(Mapper):
    """
    ЗАВДАННЯ 2:
    Порахувати слова, у яких довжина > 5 символів
    (після чистки від розділових знаків).
    """

    def map(self, record, emit):
        text = str(record)
        for raw_token in text.split():
            word = normalize_word(raw_token)
            if word and len(word) > 5:
                emit(word, 1)


class VowelConsonantStatsMapper(Mapper):
    """
    ЗАВДАННЯ 3:
    Для кожного слова рахуємо кількість голосних і приголосних
    і емімо ключ: довжина слова, значення: (vowels_count, consonants_count).

    Далі ред'юсер по кожній довжині зможе порахувати відсотки.
    """

    def map(self, record, emit):
        text = str(record)
        for raw_token in text.split():
            word = normalize_word(raw_token)
            if not word:
                continue

            vowels = 0
            consonants = 0

            for ch in word:
                if ch.isalpha():
                    if ch in VOWELS:
                        vowels += 1
                    else:
                        consonants += 1
                # цифри просто ігноруємо у підрахунку голосних/приголосних

            if vowels == 0 and consonants == 0:
                continue

            length = len(word)
            emit(length, (vowels, consonants))
