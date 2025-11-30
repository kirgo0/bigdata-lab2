from src.core.job.reducer import Reducer


class WordCountReducer(Reducer):
    """
    Використовується і для завдання 1, і для завдання 2.
    Просто сумує кількість появ слова.
    """

    def reduce(self, key, values, emit):
        emit(key, sum(values))


class LongWordCountReducer(Reducer):
    """
    Можна було б використати той самий WordCountReducer,
    але залишимо окремий клас для наочності.
    """

    def reduce(self, key, values, emit):
        emit(key, sum(values))


class VowelConsonantStatsReducer(Reducer):
    """
    ЗАВДАННЯ 3:
    На вхід приходить:
      key   = довжина слова (int)
      values = список кортежів (vowels, consonants)

    Потрібно:
      - просумувати всі голосні та приголосні для цієї довжини
      - порахувати % голосних і % приголосних
      - вивести у зручному для читання форматі
    """

    def reduce(self, key, values, emit):
        total_vowels = 0
        total_consonants = 0

        for v, c in values:
            total_vowels += v
            total_consonants += c

        total_letters = total_vowels + total_consonants
        if total_letters == 0:
            return

        vowels_pct = total_vowels / total_letters * 100
        consonants_pct = total_consonants / total_letters * 100

        # У файл піде щось типу:
        # 5   40.00% голосних, 60.00% приголосних
        result_str = f"{vowels_pct:.2f}% голосних, {consonants_pct:.2f}% приголосних"
        emit(key, result_str)
