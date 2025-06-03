# PCI SEG AI Tool

A PCI DSS segmentation testing tool with AI-enhanced analysis.

## Features
- Nmap-based segmentation testing
- AI-based result analysis using OpenAI
- JSON/HTML report generation
- Dockerized and ready for secure deployment

## Usage

### Locally
```bash
export OPENAI_API_KEY='your-api-key'
python main.py --targets 192.168.1.0/24 --ai-analysis --report html
```

### Docker
```bash
docker build -t pci-seg .
docker run --rm -e OPENAI_API_KEY=your-api-key pci-seg --targets 192.168.1.0/24 --ai-analysis --report html
```
