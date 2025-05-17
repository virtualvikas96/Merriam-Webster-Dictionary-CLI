# 📘 MWCLI - Merriam-Webster Dictionary CLI

A simple and intuitive command-line tool to fetch word definitions using the Merriam-Webster Collegiate Dictionary API.

---

## 🚀 Features

- 🔍 Get concise definitions for English words
- 🔊 Displays pronunciation and part of speech
- ⚙️ CLI interface powered by Python
- 🐳 Dockerized for easy usage anywhere

---

## 🛠️ Installation

## 🔧 Option 1: Run with Python

```bash
# Clone the repository
git clone https://github.com/virtualvikas96/Merriam-Webster-Dictionary-CLI.git
cd Merriam-Webster-Dictionary-CLI
```

# (Optional) Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

# Install the CLI
```bash
pip install .
```

# Set your API key
```bash
echo "MW_API_KEY=your_api_key_here" > .env
```

# Use the CLI
```bash
mwcli innovation
```

##🐳 Option 2: Run with Docker

# Build the Docker image

```bash
docker build -t mwcli .

# Run a word lookup
docker run --rm -e MW_API_KEY=your_api_key_here mwcli innovation

# Or enter the container interactively
docker run -it --rm --entrypoint /bin/sh mwcli
```

## 📦 Project Structure

```bash
mwcli/
├── mwcli/                  # CLI app: api.py, cli.py, config.py, etc.
├── tests/                 # Unit tests
├── requirements.txt       # Python dependencies
├── setup.py               # Packaging config
├── Dockerfile             # Docker build file
├── Makefile               # Build/test commands
└── .env                   # Environment variables (not committed)
```

## 📄 Example

```bash
$ mwcli innovation
```

## 📖 innovation  

📌 Pronunciation: ˌi-nə-ˈvā-shən  
🧠 Part of Speech: noun  
💬 Definition: the introduction of something new

## 🔐 Environment Variables

Variable	Description
```bash
MW_API_KEY	Your Merriam-Webster API key
```

Set this via a .env file or -e flag in Docker.

## ✅ Make Targets

```bash
make build     # Build distribution package
make test      # Run tests
make clean     # Clean up artifacts
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
1. Fork the repo
2. Create your feature branch (git checkout -b feature/foo)
3. Commit your changes (git commit -am 'Add new feature')
4. Push to the branch (git push origin feature/foo)
5. Create a new Pull Request

