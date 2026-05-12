# Spectrogram Segmentation Quick Start

This repo is a Jupyter Notebook example for training a semantic segmentation model on RF spectrograms.

The goal is to train a model to look at a spectrogram image and label each pixel as one of:

- `Noise`
- `NR` / 5G New Radio
- `LTE` / 4G LTE

The main file is:

```text
spectrogram_segmentation.ipynb
```

That notebook loads the dataset, visualizes examples, trains a DeepLabV3 segmentation model, validates it, and runs predictions.

## 1. Clone The Repo

```bash
git clone https://github.com/qoherent/spectrogram-segmentation.git
cd spectrogram-segmentation
git checkout internal-dataset-download
```

If you already cloned the repo:

```bash
cd spectrogram-segmentation
git fetch origin
git checkout internal-dataset-download
```

## 2. Create A Virtual Environment

From inside the project folder:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

You should now see `(.venv)` at the beginning of your terminal prompt.

Check Python:

```bash
python --version
```

## 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This installs PyTorch, Lightning, Jupyter, h5py, matplotlib, sklearn, and the other packages used by the notebook.

## 4. Get The Dataset

The dataset should be named:

```text
SpectrumSensingDataset.hdf5
```

Place it in the project root:

```text
spectrogram-segmentation/
├── SpectrumSensingDataset.hdf5
├── README.md
├── download_dataset.py
├── requirements.txt
└── spectrogram_segmentation.ipynb
```

If you need to fetch it from Dawson, run:

```bash
python3 download_dataset.py
```

This runs:

```bash
scp qrf@dawson:/home/qrf/SpectrumSensingDataset.hdf5 .
```

You may be prompted for the Dawson SSH password.

To verify the file is there:

```bash
ls -lh SpectrumSensingDataset.hdf5
```

Expected size is around `1.2 GB`.

## 5. Register The Jupyter Kernel

```bash
python -m ipykernel install --user --name spectrogram-segmentation --display-name "Spectrogram Segmentation (.venv)"
```

## 6. Launch The Notebook

```bash
jupyter notebook spectrogram_segmentation.ipynb
```

Your browser should open Jupyter.

In the notebook, select:

```text
Kernel -> Change Kernel -> Spectrogram Segmentation (.venv)
```

Then run cells from top to bottom.

## 7. What The Notebook Does

### Data Loading

The notebook loads `SpectrumSensingDataset.hdf5`.

Each dataset item contains:

- A spectrogram image: `256 x 256 x 3`
- A mask image: `256 x 256`

The mask labels are:

```text
0 = Noise
1 = NR
2 = LTE
```

The notebook can handle the dataset schema used by our internal copy:

```text
Images
Masks
Metadata/Metadata
```

### Data Preprocessing

The spectrograms are converted into PyTorch tensors and normalized.

The masks are converted into integer label tensors.

The notebook first uses only individual-signal examples:

```python
combined = False
```

That means it trains on:

- LTE-only examples
- NR-only examples

It excludes combined LTE+NR examples during training.

### Train/Validation Split

The notebook splits the dataset:

```text
80% training
20% validation
```

With the current dataset, expect roughly:

```text
1800 total trainable examples
1440 training examples
360 validation examples
```

### Model

The model is:

```text
DeepLabV3 + MobileNetV3 backbone
```

It predicts a class for every pixel in the spectrogram.

Output shape is basically:

```text
batch_size x 3 x 256 x 256
```

The `3` corresponds to:

```text
Noise, NR, LTE
```

### Training

The notebook trains using:

```text
SGD optimizer
CrossEntropyLoss
class weighting
```

Class weighting matters because most pixels are usually noise, so the model needs help paying attention to LTE/NR pixels.

Default training is:

```python
n_epochs = 10
```

If running on CPU, change it to:

```python
n_epochs = 4
```

Training may take a while on CPU.

### Validation

After training, the notebook shows:

- Example spectrograms
- Ground-truth masks
- Model prediction masks
- Accuracy
- Confusion matrix
- Precision
- Recall
- F1 score
- IoU / Jaccard index

### Challenge Data

At the end, the notebook evaluates on:

```python
combined = True
```

This includes frames with both LTE and NR together.

This is harder because the model was trained only on LTE-only and NR-only examples.

## 8. Expected Things You'll See

During setup:

```text
Successfully installed ...
```

During dataset validation:

```text
Dataset is already present and valid.
```

During training:

```text
GPU available: True/False
Training model on GPU/CPU
Epoch 0 ...
Epoch 1 ...
```

During validation:

```text
val_accuracy
val_loss
```

Then plots and metric tables will appear in the notebook.

## 9. Common Issues

### Jupyter Cannot Find The Environment

Run this again:

```bash
python -m ipykernel install --user --name spectrogram-segmentation --display-name "Spectrogram Segmentation (.venv)"
```

Then restart Jupyter.

### Dataset File Not Found

Make sure this file is in the repo root:

```bash
ls -lh SpectrumSensingDataset.hdf5
```

If missing, fetch it:

```bash
python3 download_dataset.py
```

### `scp` Asks For A Password

That is normal.

The script fetches from:

```text
qrf@dawson:/home/qrf/SpectrumSensingDataset.hdf5
```

You need network/VPN access and SSH permission to Dawson.

### Training Is Very Slow

Use fewer epochs:

```python
n_epochs = 4
```

Also keep:

```python
batch_size = 4
```

unless you know your GPU/RAM can handle more.

### Torch Tries To Download Model Weights And Fails

If you are offline, change the model cell from:

```python
model = deeplabv3_mobilenet_v3_large(num_classes=n_classes)
```

to:

```python
model = deeplabv3_mobilenet_v3_large(num_classes=n_classes, weights_backbone=None)
```

## 10. Minimal Command Summary

```bash
git clone https://github.com/qoherent/spectrogram-segmentation.git
cd spectrogram-segmentation
git checkout internal-dataset-download

python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

python3 download_dataset.py

python -m ipykernel install --user --name spectrogram-segmentation --display-name "Spectrogram Segmentation (.venv)"

jupyter notebook spectrogram_segmentation.ipynb
```

Then select the correct kernel and run the notebook top to bottom.
