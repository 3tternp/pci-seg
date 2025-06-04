# PCI SEG 

A PCI DSS segmentation testing tool with AI-enhanced analysis.

## Features
- Nmap-based segmentation testing
- AI-based result analysis using OpenAI
- JSON/HTML report generation
- Dockerized and ready for secure deployment

## Usage

### Locally
```bash
sudo bash setup_env.sh
**inside venv environment execute**
pip3 install -r requirements.txt
python main.py --targets 192.168.1.0/24 --ai-analysis --report html
```

### Docker
```bash
docker build -t pci-seg .
docker run --rm -e OPENAI_API_KEY=your-api-key pci-seg --targets 192.168.1.0/24 --ai-analysis --report html
```
