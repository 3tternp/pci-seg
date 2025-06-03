
# pci-seg

**PCI DSS 4.0.1 Network Segmentation Testing Tool**

## Features
- ICMP + TCP scan of given targets
- Supports custom PCI port profiles
- OpenAI GPT-4 powered AI audit
- Generates JSON or HTML reports

## Usage
```bash
python main.py --targets 192.168.1.0/24 --profile pci-core --ai-analysis --report html
```

## Setup
```bash
# Install venv module if needed
sudo apt install python3-venv

# Create a virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies safely
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here
```

## Docker
```bash
docker build -t pci-seg .
docker run -v $(pwd)/reports:/app/reports pci-seg --targets 192.168.1.0/24
```
