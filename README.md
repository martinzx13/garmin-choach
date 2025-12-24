# Garmin Coach

A personal coach for Garmin devices that retrieves data from Garmin Connect and provides AI-powered coaching feedback.

## 🎯 Project Goals

This project demonstrates:
- **Rust** - Core application built in Rust for learning and performance
- **Python** - Data retrieval from Garmin Connect using Python libraries
- **AI Integration** - Free AI API integration for personalized coaching
- **Cross-language Integration** - Rust calling Python for data operations

## 🏗️ Architecture

```
garmin-coach/
├── src/                    # Rust source code (main application)
├── python_client/          # Python modules for Garmin data retrieval
│   ├── garmin_data_retriever/
│   │   ├── client.py       # Garmin Connect API client
│   │   ├── exporter.py     # Data export utilities
│   │   └── ai_coach.py     # AI coaching module
│   ├── example.py          # Data retrieval example
│   └── ai_example.py       # AI coaching example
└── Cargo.toml              # Rust dependencies
```

## 🚀 Getting Started

### Prerequisites

- **Rust** (1.70+): Install from [rustup.rs](https://rustup.rs/)
- **Python** (3.8+): Install from [python.org](https://www.python.org/)
- **Ollama** (optional): For local AI responses - [ollama.ai](https://ollama.ai)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/martinzx13/garmin-choach.git
   cd garmin-choach
   ```

2. **Install Python dependencies**
   ```bash
   cd python_client
   pip install -r requirements.txt
   cd ..
   ```

3. **Build the Rust application**
   ```bash
   cargo build --release
   ```

### Configuration

For actual Garmin Connect data (optional):
```bash
export GARMIN_EMAIL="your-email@example.com"
export GARMIN_PASSWORD="your-password"
```

> **Note**: Currently uses mock data for demonstration. To use real Garmin data, uncomment the `garth` or `garminconnect` dependencies in `python_client/requirements.txt`.

## 📖 Usage

### Using Rust CLI

The main Rust application provides a convenient CLI:

```bash
# Run data retrieval example
cargo run -- example --example-type data

# Run AI coaching example
cargo run -- example --example-type ai

# Fetch Garmin data
cargo run -- fetch-data --data-type activities

# Get AI coaching feedback
cargo run -- coaching --coaching-type activity
```

### Using Python Directly

You can also run the Python scripts directly:

```bash
# Data retrieval example
python3 python_client/example.py

# AI coaching example
python3 python_client/ai_example.py
```

## 🤖 AI Integration

The project supports multiple free AI APIs:

### 1. Ollama (Recommended - Local & Free)

Install Ollama and pull a model:
```bash
# Install from https://ollama.ai
ollama pull llama2
# or
ollama pull mistral
```

The AI coach will automatically use Ollama if available at `http://localhost:11434`.

### 2. Mock Responses (Default)

If no AI service is available, the system uses intelligent mock responses for demonstration.

### 3. Other Free APIs (Extensible)

The `AICoach` class can be extended to support:
- HuggingFace Inference API (free tier)
- Together AI (free tier)
- Any other OpenAI-compatible API

## 📊 Features

### Data Retrieval

- ✅ Activity data (runs, cycles, swims, etc.)
- ✅ Heart rate metrics
- ✅ Sleep tracking data
- ✅ Stress level monitoring
- ✅ User statistics and profile
- ✅ Data export to JSON

### AI Coaching

- 🤖 Activity analysis and feedback
- 💪 Health metrics recommendations
- 📅 Personalized training plan generation
- 🎯 Goal-based coaching

## 🛠️ Development

### Project Structure

**Rust Components:**
- `src/main.rs` - Main CLI application
- Uses `clap` for argument parsing
- Calls Python scripts for data operations

**Python Components:**
- `client.py` - Garmin Connect API wrapper
- `exporter.py` - Data formatting and export
- `ai_coach.py` - AI-powered coaching logic

### Building

```bash
# Build in development mode
cargo build

# Build optimized release
cargo build --release

# Run tests
cargo test
```

### Python Development

```bash
cd python_client

# Install development dependencies
pip install -r requirements.txt

# Run examples
python3 example.py
python3 ai_example.py
```

## 🎓 Learning Objectives

This project demonstrates:

1. **Rust Fundamentals**
   - Command-line argument parsing with `clap`
   - Error handling with `anyhow`
   - Process execution and inter-process communication
   - JSON serialization/deserialization with `serde`

2. **Python Integration**
   - HTTP requests with `requests` library
   - Data processing and analysis
   - API client implementation
   - Mock data for development

3. **AI Integration**
   - Local AI with Ollama
   - Prompt engineering for coaching
   - Fallback strategies for API availability

4. **Cross-Language Development**
   - Rust calling Python scripts
   - Data exchange via JSON
   - Process management

## 🔮 Future Enhancements

- [ ] Real Garmin Connect authentication
- [ ] Database storage for historical data
- [ ] Web dashboard for visualization
- [ ] Advanced AI coaching algorithms
- [ ] Multi-sport support
- [ ] Training plan progression tracking
- [ ] Social features and challenges

## 📝 License

MIT License - Feel free to use this project for learning and development.

## 🤝 Contributing

Contributions are welcome! This is a learning project, so feel free to:
- Add new features
- Improve documentation
- Fix bugs
- Share ideas

## 📚 Resources

- [Garmin Connect API](https://github.com/cyberjunky/python-garminconnect)
- [Rust Book](https://doc.rust-lang.org/book/)
- [Ollama Documentation](https://github.com/ollama/ollama)
- [Python Requests](https://requests.readthedocs.io/)

## ⚠️ Disclaimer

This project is for educational purposes. Be respectful of Garmin's API terms of service when using real data retrieval.
