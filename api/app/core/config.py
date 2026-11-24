# from functools import lru_cache
# from pathlib import Path

# from langchain.embeddings import init_embeddings
# from langchain_core.embeddings import Embeddings
# from pydantic_settings import BaseSettings, SettingsConfigDict
# from qdrant_client import QdrantClient


# # api/.env
# ENV_FILE = Path(__file__).resolve().parents[2] / ".env"


# class Settings(BaseSettings):

#     model_config = SettingsConfigDict(
#         env_prefix="RAG_",
#         env_file=ENV_FILE,
#         extra="ignore",
#     )

#     # ======================================
#     # APP
#     # ======================================

#     app_name: str = "Clause"
#     data_path: str = "data/shop_handbook.pdf"

#     # ======================================
#     # CHAT MODEL
#     # ======================================

#     chat_provider: str = "google_genai"
#     chat_model: str = "gemini-3.1-flash-lite"
#     chat_temperature: float = 0
#     chat_api_key: str = ""


#     # ======================================
#     # EMBEDDINGS
#     # ======================================

#     embed_provider: str = "ollama"
#     embed_model: str = "nomic-embed-text:latest"
#     embed_dim: int = 768

#     # ======================================
#     # INDEXING
#     # ======================================

#     chunk_size: int = 600
#     chunk_overlap: int = 100

#     # ======================================
#     # RETRIEVAL
#     # ======================================

#     top_k: int = 3
#     score_threshold: float = 0

#     # ======================================
#     # QDRANT
#     # ======================================

#     collection_name: str = "shop_handbook"
#     qdrant_path: str = "./qdrant_data"
#     qdrant_url: str | None = None

#     # ======================================
#     # PROMPTS
#     # ======================================
#       # Prompts
#     # system_prompt: str = (
#     #     "You are a helpful Clause assistant. "
#     #     "Answer only from the provided context. "
#     #     "If the answer is not in the context, say you don't know."
#     # )

#     system_prompt: str = (
#         "You are a  Clause shop customer AI assistant. "
#         "Answer using ONLY the handbook text you are given."
#         "Find the one sentence that answers the question and copy its numbers exactly."
#         "Answer in one or two short sentences. Never mention 'the context, or 'the handbook text'."
#         "If the handbook text does not answer the question, reply exactly: "
#         "\"Clause I dont know.\""

#     )


# # ==========================================
# # SETTINGS
# # ==========================================

# @lru_cache
# def get_settings() -> Settings:
#     return Settings()


# # ==========================================
# # EMBEDDINGS
# # ==========================================

# def get_embeddings(settings: Settings) -> Embeddings:

#     return init_embeddings(
#         model=settings.embed_model,
#         provider=settings.embed_provider,
#     )


# # ==========================================
# # QDRANT CLIENT
# # ==========================================

# def get_qdrant_client(settings: Settings) -> QdrantClient:

#     if settings.qdrant_url:
#         return QdrantClient(url=settings.qdrant_url)

#     return QdrantClient(path=settings.qdrant_path)

from functools import lru_cache
from pathlib import Path

from langchain.embeddings import init_embeddings
from langchain_core.embeddings import Embeddings
from pydantic_settings import BaseSettings, SettingsConfigDict
from qdrant_client import QdrantClient

# api/.env
ENV_FILE = Path(__file__).resolve().parents[2] / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="RAG_", env_file=ENV_FILE, extra="ignore"
    )

    # App
    app_name: str = "Clause"
    data_path: str = "files/shop_handbook.pdf"

    # Chat model
    chat_provider: str = "google_genai"
    chat_model: str = "gemini-3.1-flash-lite"
    chat_temperature: float = 0
    chat_api_key: str = ""

    # Embeddings
    embed_provider: str = "ollama"
    embed_model: str = "nomic-embed-text:latest"
    embed_dim: int = 768

    # Indexing
    chunk_size: int = 600
    chunk_overlap: int = 100

    # Retrieval
    top_k: int = 3
    score_threshold: float = 0.5

    # Qdrant
    collection_name: str = "shop_handbook"
    qdrant_path: str = "./vector_stores"
    qdrant_url: str | None = None

    # Agent limit (per question)
    max_model_call: int = 5
    max_tool_call: int = 3

    # Prompts
    # system_prompt: str = (
    #     "You are a helpful Clause assistant. "
    #     "Answer only from the provided context. "
    #     "If the answer is not in the context, say you don't know."
    # )

    system_prompt_version: str = "v1"


@lru_cache
def get_settings() -> Settings:
    return Settings()


def get_embeddings(settings: Settings) -> Embeddings:
    return init_embeddings(
        model=settings.embed_model,
        provider=settings.embed_provider,
    )


def get_qdrant_client(settings: Settings) -> QdrantClient:
    return QdrantClient(path=settings.qdrant_path)
