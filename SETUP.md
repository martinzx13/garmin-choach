# Setup Guide

This guide will help you set up and run the Garmin Coach project.

## Prerequisites

### 1. Install Rust

```bash
# Install Rust using rustup
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Follow the prompts and restart your terminal
source $HOME/.cargo/env

# Verify installation
rustc --version
cargo --version
```

### 2. Install Python 3

**Linux/macOS:**
```bash
# Most systems come with Python 3 pre-installed
python3 --version

# If not installed, use your package manager
# Ubuntu/Debian:
sudo apt-get update
sudo apt-get install python3 python3-pip

# macOS (using Homebrew):
brew install python3
```

**Windows:**
- Download from [python.org](https://www.python.org/downloads/)
- Make sure to check "Add Python to PATH" during installation

### 3. Install Python Dependencies

```bash
cd python_client
pip install -r requirements.txt
# or use pip3 if pip points to Python 2
pip3 install -r requirements.txt
```

## Optional: AI Integration with Ollama

For real AI coaching responses, install Ollama:

### Install Ollama

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**macOS:**
```bash
# Download from https://ollama.ai/download
# or use Homebrew
brew install ollama
```

**Windows:**
- Download from [https://ollama.ai/download](https://ollama.ai/download)

### Pull an AI Model

```bash
# Start Ollama service (if not auto-started)
ollama serve

# In a new terminal, pull a model
ollama pull llama2
# or
ollama pull mistral
# or
ollama pull codellama
```

### Verify Ollama

```bash
# Test that Ollama is running
curl http://localhost:11434/api/generate -d '{
  "model": "llama2",
  "prompt": "Hello"
}'
```

## Build the Project

```bash
# Navigate to project root
cd /path/to/garmin-choach

# Build the Rust application
cargo build --release

# The binary will be at: target/release/garmin_coach
```

## Quick Start

### 1. Test Data Retrieval

```bash
# Using Rust CLI
cargo run -- example --example-type data

# Or using Python directly
python3 python_client/example.py
```

### 2. Test AI Coaching

```bash
# Using Rust CLI
cargo run -- example --example-type ai

# Or using Python directly
python3 python_client/ai_example.py
```

## Using Real Garmin Data (Optional)

To use actual Garmin Connect data instead of mock data:

### 1. Uncomment Real Dependencies

Edit `python_client/requirements.txt`:

```txt
# Uncomment these lines:
garth>=0.4.0
# or
garminconnect>=0.2.0
```

Then install:
```bash
pip install -r python_client/requirements.txt
```

### 2. Set Environment Variables

```bash
export GARMIN_EMAIL="your-email@example.com"
export GARMIN_PASSWORD="your-password"
```

Or create a `.env` file in the project root:
```
GARMIN_EMAIL=your-email@example.com
GARMIN_PASSWORD=your-password
```

### 3. Update the Client Code

Modify `python_client/garmin_data_retriever/client.py` to use the `garth` or `garminconnect` library instead of mock data.

## Troubleshooting

### Python not found

```bash
# Try python3 instead of python
python3 --version

# Or create an alias
alias python=python3
```

### Permission denied when running scripts

```bash
# Make scripts executable
chmod +x python_client/example.py
chmod +x python_client/ai_example.py
```

### Ollama connection refused

```bash
# Start Ollama service
ollama serve

# Check if running
curl http://localhost:11434/
```

### Rust compilation errors

```bash
# Update Rust toolchain
rustup update

# Clean and rebuild
cargo clean
cargo build
```

## Next Steps

1. ✅ Run the examples to see mock data
2. ✅ Install Ollama for AI coaching
3. ✅ Set up Garmin credentials for real data
4. ✅ Customize the AI prompts
5. ✅ Build new features!

## Resources

- [Rust Book](https://doc.rust-lang.org/book/)
- [Python Garmin Connect](https://github.com/cyberjunky/python-garminconnect)
- [Ollama Documentation](https://github.com/ollama/ollama)
- [Garth (Garmin Auth)](https://github.com/matin/garth)
