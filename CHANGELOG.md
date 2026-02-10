# Changelog

## 0.1.0 (2025-02-10)

### Added

- Initial repository scaffold
- `JupyterMLAgent` with `inspect()` and `trace()` methods
- `jupyter_ml/runner.py` for notebook execution
- `jupyter_ml/notebook.py` for notebook utilities
- `jupyter_ml/config.py` for runtime configuration
- CLI entry point (`jml`)
- GitHub Actions CI workflow
- Pre-commit hooks (ruff, trailing-whitespace, end-of-file-fixer)
- Example notebook (`examples/basic.ipynb`)
- Test suite (`tests/test_agent.py`)

### Dependencies

- nbformat >=5.9.0

### Optional Dependencies

- dev: pytest, pytest-cov
- llm: openai, google-generativeai
