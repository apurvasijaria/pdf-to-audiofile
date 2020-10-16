# PDF to Audio File

Creating Audio Files from PDF Files with flexibility to choose voice type, speaking speed, and volume. 
All the PDFs to be converted to Audio to be kept in pdf_files folder, after conversion the audio files are stored in audio_files folder. 

### Notes
The ```requirements.txt``` file should list all Python libraries that your notebooks depend on, and they will be installed using:

```python
pip install -r requirements.txt
```

### Motivation

To read PDFs on the go!

### Logic
Converting PDF to text using python package [```pdfplumber```](https://github.com/jsvine/pdfplumber). Using [```pyttsx3```](https://pypi.org/project/pyttsx3/) to convert text to speech and saving as an mp3 file. 

#### Voice Properties
[```pyttsx3```](https://pypi.org/project/pyttsx3/) allows choosing between Male or Female voice, Speed of speaking and Volume. Modification can be done in the code.
#### Sample PDFs
First 10-15 pages from Ebooks have been used to test. PDFs of Books downloded from Free Ebook websites:
  - [Project Gutenberg](https://www.gutenberg.org/) 
  - [Many Books](https://manybooks.net/)
  
#### Time to covert ~40 pages of PDF to audio files ~ 5mins

### Resources

- **[jsvine/pdfplumber](https://github.com/jsvine/pdfplumber)**
- **[pyttsx3](https://pypi.org/project/pyttsx3/)**
- **[Project Gutenberg](https://www.gutenberg.org/)**
- **[Many Books](https://manybooks.net/)**

