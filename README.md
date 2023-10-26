# README.md

## Overview

This project showcases a novel approach to generate extensive text outputs from OpenAI models, such as GPT-3.5-turbo-16k, GPT-4, and GPT-4-32k, by leveraging function calls to bypass the models' tendencies to cap their token count. The application demonstrates how to reliably produce long-form content, significantly exceeding the typical output length.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Interacting with the Application](#interacting-with-the-application)
- [How It Works](#how-it-works)
  - [Main Application](#main-application)
  - [Function Call Builder](#function-call-builder)
  - [AI Interaction](#ai-interaction)
- [License](#license)

## Project Structure

1. **main.py**: User interface for interacting with OpenAI models.
2. **function_call_builder.py**: Constructs function calls and interacts with OpenAI API.
3. **ai.py**: Contains functions for token counting and chat completion.

## Installation

Ensure Python 3.6+ is installed, then run:

```bash
pip install openai tiktoken
```

## Usage

#### Running the Application

```python
python main.py
```
## Interacting with the Application

- Premade Example: Run examples from a JSON file, `examples.json`

- Input Your Details: Manually input details to generate a function call and receive a response.

## How It Works

#### Main Application

`main.py` guides the user through the process, interacting with **FunctionCallBuilder** to generate function calls.

## Function Call Builder
`function_call_builder.py` dynamically constructs function call definitions and handles the invocation of these calls, managing extensive text outputs.

## AI Interaction

`ai.py` contains functions for token counting and chat completion, crucial for interacting with OpenAI API and managing token limits.

## License

This project is open source and freely available for use.

