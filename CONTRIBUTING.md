# Contributing to DevOps Project

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Project-1
   ```

2. **Set up Python environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Run locally**
   ```bash
   make run-local
   # or
   python app.py
   ```

## Development Workflow

1. Create a feature branch from `develop`
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes

3. Run tests and linting
   ```bash
   make test
   make lint
   ```

4. Commit your changes
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

5. Push and create a Pull Request

## Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused

## Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Aim for good test coverage

## Commit Messages

Follow conventional commits format:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes
- `refactor:` Code refactoring
- `test:` Test changes
- `chore:` Maintenance tasks

## Pull Request Process

1. Update README.md if needed
2. Ensure all CI checks pass
3. Request review from maintainers
4. Address review comments
5. Merge after approval

## Questions?

Feel free to open an issue for any questions or concerns.

