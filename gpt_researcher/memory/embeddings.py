from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings


class Memory:
    def __init__(self, **kwargs):
        self._embeddings = OpenAIEmbeddings()

    def get_embeddings(self):
        return self._embeddings

