from decouple import AutoConfig
config = AutoConfig(search_path='./')

VIRUS_TOTAL_API_KEY = config('VIRUS_TOTAL_API_KEY')