"""LLM integration stubs for notebook-centric ML agents."""

from typing import Any


def openai_completion(prompt: str, model: str = "gpt-4") -> str:
    """OpenAI completion (stub)."""
    raise NotImplementedError("Install with: pip install -e .[llm]")


def gemini_completion(prompt: str, model: str = "gemini-pro") -> str:
    """Google Gemini completion (stub)."""
    raise NotImplementedError("Install with: pip install -e .[llm]")


def local_completion(prompt: str, model: str = "llama3") -> str:
    """Local LLM completion via Ollama (stub)."""
    raise NotImplementedError("Install Ollama and run: ollama serve")
