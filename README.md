MapReduce Python Simulator

Quickstart
- Create venv and install requirements if needed.
- Run a sample job after scaffolding is complete:
  - python -m src.cli.main run --workers 4 --input data/input --output data/output/wordcount --job student_jobs.word_count.mapper:WordCountMapper,student_jobs.word_count.reducer:WordCountReducer --reducers 4


task 1:
 python -m src.cli.main run `
   --workers 2 `
   --reducers 2 `
   --input data/input `
   --output data/output/wordcount_clean `
   --job src.student_jobs.word_count.mapper:WordCountMapper,src.student_jobs.word_count.reducer:WordCountReducer

task 2:
python -m src.cli.main run `
  --workers 2 `
  --reducers 2 `
  --input data/input `
  --output data/output/wordcount_long `
  --job src.student_jobs.word_count.mapper:LongWordCountMapper,src.student_jobs.word_count.reducer:LongWordCountReducer

task 3:
python -m src.cli.main run `
  --workers 2 `
  --reducers 2 `
  --input data/input `
  --output data/output/word_stats `
  --job src.student_jobs.word_count.mapper:VowelConsonantStatsMapper,src.student_jobs.word_count.reducer:VowelConsonantStatsReducer
