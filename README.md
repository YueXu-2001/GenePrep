 # GenePrep


## What is this?

GenePrep is an automated multi-agent system that streamlines preprocessing and analysis of large-scale gene expression data from GEO and TCGA. By simply installing the GenePrep package, users can perform end-to-end workflows including data validation, trait–condition pair selection, statistical testing, and result generation. Given a dataset and trait–condition pairs, GenePrep identifies genes associated with traits while accounting for conditions. Its modular agents enable iterative planning, execution, and debugging with minimal manual scripting. GenePrep reduces preprocessing overhead and improves reproducibility. This work extends on tools to create teams of AI scientists and automate gene expression data analysis, as presented in [Toward a Team of AI-made Scientists for Scientific Discovery from Gene Expression Data](https://arxiv.org/abs/2402.12391) and [GenoTEX: An LLM Agent Benchmark for Automated Gene Expression Data Analysis](https://arxiv.org/abs/2406.15341). Please check more info on our [website](https://yuexu-2001.github.io/GenePrep/).

## How to use it?

### 1. Installation
Use the following command to install the package.
```bash
pip install geneprep
```

### 2. Data preparation
Download the input data from our Google Drive [folder](https://drive.google.com/drive/u/0/folders/1A25gqaIpcahle6TLJ81Qnd2VoluJ2NEe). \
You can verify data integrity with:
```bash
python validator.py --data-dir /path/to/data --validate
```

### 3. Set up environment
Create a conda environment with Python 3.10 and install the required packages:
```bash
conda create -n geneprep python=3.10
conda activate geneprep
pip install -r requirements.txt
```

### 4. Set up API key File(Optional)
Go to the root folder of the package, create a ".env" file(please make sure the file name is exactly ".env" without any other extension) and stores your API key and organization info.\
The following is an example for OpenAI API key and organization, so please adjust if you are using other platform.\
Note: Use space to separate, not new line.
```bash
OPENAI_API_KEY_1=sk-sample-key	OPENAI_ORGANIZATION_1=org-sample-xxx
```

### 5. Run the code
#### If you have set up the API key file
Modify `in_data_root` in `main.py` to set input data path on different devices.\
Run an experiment like this:
```bash
python main.py --version 1 --model gemini-2.0-flash-002 --api 1
```

The first time you run this, you'll get an error asking you to set up an API key, e.g. `GOOGLE_API_KEY_1` in a `.env` file. You'll need to get this API key from the LLM provider.

If you type a wrong model name, the error message will show you all the model names that work with this code.

For open-source LLMs, you can either run them locally with [Ollama Python](https://github.com/ollama/ollama-python), or use APIs (use the `--use-api` flag).

#### If you chose not to set up the File
You can use the following code template to pass your API key and org info in command line
```bash
python main.py --version 1 --model o1-mini-2024-09-12 --api_key xxxxx --organization xxxxx
```

If you type a wrong model name, the error message will show you all the model names that work with this code.

For open-source LLMs, you can either run them locally with [Ollama Python](https://github.com/ollama/ollama-python), or use APIs (use the `--use-api` flag).
## License

Internal use only. Do not distribute.
