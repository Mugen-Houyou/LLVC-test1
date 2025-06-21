# LLVC Installation Guide for Complete Beginners

This document explains how to set up the LLVC (Low-Latency Voice Conversion) project even if you have no prior experience with AI or machine learning.

## 1. Install Python

1. Download and install [Anaconda](https://www.anaconda.com/download) (choose the version for your operating system). Anaconda lets you create isolated "environments" for projects.
2. Open the **Anaconda Prompt** (Windows) or a terminal (macOS/Linux).

## 2. Create an Environment

Run the following command to create a new Python environment called `llvc`:

```bash
conda create -n llvc python=3.11
```

Activate the environment:

```bash
conda activate llvc
```

## 3. Install PyTorch

Visit [PyTorch's installation page](https://pytorch.org/get-started/locally/) and follow the instructions for your system. The page will give you a command that installs **torch** and **torchaudio**. Run that command in your terminal while the `llvc` environment is active.

## 4. Install Other Requirements

With the `llvc` environment still active, install the remaining packages used by LLVC:

```bash
pip install -r requirements.txt
```

## 5. Download the Pretrained Models

The project provides a script that downloads the pretrained models from the internet. Run:

```bash
python download_models.py
```

This creates a folder called `llvc_models` containing the necessary files.

## 6. Test the Installation

You can try converting the example audio files that come with the repository:

```bash
python infer.py
```

The converted audio will be saved inside a folder named `converted_out`.

## 7. (Optional) Evaluation Tools

Evaluation tools help you measure how well the model performs. LLVC includes an
`eval.py` script for this purpose. You can skip this section if you only want to
use the provided pretrained models. If you do wish to try the evaluation, create
a **separate** Python 3.9 environment:

```bash
conda create -n llvc-eval python=3.9
conda activate llvc-eval
pip install -r eval_requirements.txt
```

## Next Steps

* To convert your own files, run `python infer.py -p my_checkpoint.pth -c my_config.json -f path/to/audio` (see `README.md` for details).
* For a simple web interface, start the Flask app with `python webui/app.py` and open `http://localhost:8000` in your browser.

That's it! You now have LLVC set up and can experiment with voice conversion.
