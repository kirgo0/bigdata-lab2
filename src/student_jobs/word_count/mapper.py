from src.core.job.mapper import Mapper


class WordCountMapper(Mapper):
    def map(self, record, emit):
        for token in str(record).split():
            emit(token.lower(), 1)

