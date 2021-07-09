# resume-parser

Uses: Python 3.

## Installation

### Clone repository
```
git clone https://github.com/ameybhavsar24/resume-parser.git
cd resume-parser
```

### Install packages
```
pip install -r requirements.txt
pip install resume-parser
```
For NLP operations we use spacy and nltk. Install them using below commands:
```
python -m spacy download en_core_web_sm
python -m nltk.downloader stopwords
python -m nltk.downloader punkt
python -m nltk.downloader averaged_perceptron_tagger
python -m nltk.downloader universal_tagset
python -m nltk.downloader wordnet
python -m nltk.downloader brown
python -m nltk.downloader maxent_ne_chunker
```


## Usage
```
from resume_parser import resumeparse
data = resumeparse.read_file('/path/to/resume/file')
```
