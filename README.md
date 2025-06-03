
# pci-seg-ai

**PCI DSS 4.0.1 Network Segmentation Testing Tool with AI Analysis**

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
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here
```

## Docker
```bash
docker build -t pci-seg-ai .
docker run -v $(pwd)/reports:/app/reports pci-seg-ai --targets 192.168.1.0/24
```
