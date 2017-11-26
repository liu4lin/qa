"""Defines constants used for data preprocessing.
"""

VOCAB_CHARS_FILE = "vocab.chars.npy"
TRAIN_SQUAD_FILE = "train-v1.1.json"
DEV_SQUAD_FILE = "dev-v1.1.json"

# Training data is split into multiple batches of files because there is
# too much data to fit in memory at once. File patterns below index batches
# by an ordinal.
MAX_SAMPLES_PER_SPLIT = 20000
TRAIN_FOLDER_NAME = "train"
DEV_FOLDER_NAME = "dev"
CONTEXT_FILE_PATTERN = "context.%d.npy"
QUESTION_FILE_PATTERN = "question.%d.npy"
SPAN_FILE_PATTERN = "span.%d.npy"
WORD_IN_QUESTION_FILE_PATTERN = "word_in_question.%d.npy"
WORD_IN_CONTEXT_FILE_PATTERN = "word_in_context.%d.npy"
QUESTION_IDS_FILE_PATTERN = "question_ids.%d.npy"
QUESTION_IDS_TO_GND_TRUTHS_FILE_PATTERN = "question_ids_to_gnd_truths.%d"
CONTEXT_POS_FILE_PATTERN = "context.pos.%d.npy"
CONTEXT_NER_FILE_PATTERN = "context.ner.%d.npy"
QUESTION_POS_FILE_PATTERN = "question.pos.%d.npy"
QUESTION_NER_FILE_PATTERN = "question.ner.%d.npy"
CONTEXT_COVE_FILE_PATTERN = "context.cove.%d.npy"
QUESTION_COVE_FILE_PATTERN = "question.cove.%d.npy"
TEXT_TOKENS_FILE_PATTERN = "text_tokens.%d"
COVE_QST_FILE = "cove.qst.npy"
COVE_CTX_FILE = "cove.ctx.npy"

CORENLP_URL = "http://nlp.stanford.edu/software/stanford-corenlp-full-2017-06-09.zip"
CORENLP_ZIP_FILE_NAME = "stanford-corenlp-full-2017-06-09.zip"

VECTORS_URL = "http://nlp.stanford.edu/data/glove.840B.300d.zip"
WORD_VEC_DIM = 300
MAX_WORD_LEN = 25
VECTOR_FILE = "glove.840B.300d.txt"
VECTOR_ZIP_FILE = "glove.840B.300d.zip"
SQUAD_TRAIN_URL = "https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v1.1.json"
SQUAD_TRAIN_FILE = "train-v1.1.json"
SQUAD_DEV_URL = "https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v1.1.json"
SQUAD_DEV_FILE = "dev-v1.1.json"

EMBEDDING_FILE = "glove.embedding.npy"
VOCAB_FILE = "vocab.txt"

STANFORD_CORENLP_PORT = "9000"
