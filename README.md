# Spectrogram Segmentation

In this example, we use [PyTorch](https://pytorch.org/) and [PyTorch Lightening](https://lightning.ai/docs/pytorch/stable/) to train DeepLabV3 segmentation models to differentiate between 
5G NR and 4G LTE signals within wideband spectrograms.

The successful application of semantic segmentation to radio frequency (RF) spectrograms holds significant applications 
for [spectrum sensing](https://iopscience.iop.org/article/10.1088/1742-6596/2261/1/012016#:~:text=In%20cognitive%20radio%2C%20spectrum%20sensing,user%20can%20use%20the%20spectrum.) and serves as a foundational example showcasing the near-term feasibility of 
[intelligent radio](https://www.qoherent.ai/intelligentradio/) technology.

If you found this example interesting or helpful, don't forget to give it a star! ⭐ Also, be sure to check out our 
open-source project: [RIA Core](https://github.com/qoherent/ria).


## 🚀 Getting Started

This example is provided as a Jupyter Notebook. You have the option to run this example either locally or 
in Google Colab.

To run this example locally, you'll need to download this project, the spectrogram sensing dataset, 
and set up a Conda virtual environment. If this seems daunting, we recommend running this example on 
Google Colab.

### Running this example locally

Please note that running this example locally will require approximately 10 GB of free space. Please ensure you 
have sufficient space available prior to proceeding.

1. Ensure that [Python](https://www.python.org/downloads/), [Git](https://git-scm.com/downloads), and [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) are installed on the computer where you plan to run 
this example. Additionally, if you'd like to accelerate model training with a GPU, you'll require [CUDA](https://docs.nvidia.com/cuda/cuda-quick-start-guide/index.html).


2. Clone this repository to your local computer:
```commandline
https://github.com/qoherent/spectrogram-segmentation.git
```


3. Create a Conda environment using the provided `environment.yml` file:
```commandline
conda env create -f environment.yml
```
This will create a new Conda environment ...


4. Active the environment, and download the spectrum sensing dataset:
```commandline
conda activate my_environment
python download_dataset.py
conda deactivate
```
This will ...


5. Add the Conda environment to Jupyter:
```commandline
python -m ipykernel install --user --name=spectrogram-segmentation
```


5. Open the spectrogram segmentation notebook:
```commandline
jupyter notebook spectrogram-segmentation.ipynb
```


6. Give yourself a pat on the back - you're all set up and ready to run the example! For more information on 
navigating the Jupyter Notebook interface and executing code, please check out this tutorial by the Codecademy 
Team: [How To Use Jupyter Notebooks](https://www.codecademy.com/article/how-to-use-jupyter-notebooks).

Depending on your system specifications and the availability of a CUDA, running this example locally may take 
several minutes. If a cell is taking too long to execute, you can interrupt its execution by clicking the "Kernel" 
menu and selecting "Interrupt Kernel" or by pressing `Ctrl + C` in the terminal where Jupyter notebook is running.

### 📓 Running this example in Google Colab

Coming soon: Don't want the hassle of downloading the project, dataset, and setting up a Conda environment? 
We've shared the notebook on Google Colab: [Spectrogram Segmentation]().


## 🤝 Contribution

We welcome contributions from the community! Whether it's an enhancement, bug fix, or improved explanation, 
your input is valuable. For larger changes, please contact us via email at [info@qoherent.ai](mailto:info@qoherent.ai) beforehand.

If you encounter any issues or to report a security vulnerability, please submit a bug report to the GitHub Issues page
[here](https://github.com/qoherent/spectrogram-segmentation/issues).

Has this example inspired a project or reserach initive? 


## 📜 Attribution

This project was inspired by [Spectrum Sensing with Deep Learning to Identify 5G and LTE Signals](https://www.mathworks.com/help/comm/ug/spectrum-sensing-with-deep-learning-to-identify-5g-and-lte-signals.html) by MathWork's.

The dataset used in this example was prepared by MathWorks and is publicly available [here](https://www.mathworks.com/supportfiles/spc/SpectrumSensing/SpectrumSenseTrainingDataNetwork.tar.gz). For more information 
on how the dataset was generated or to generate further data, please refer to the aforementioned MathWork's article 
on Spectrum Sensing.

The models employed in this example were initially proposed by Chen _et al._ in their 2017 paper titled
'[Rethinking Atrous Convolution for Semantic Image Segmentation](https://arxiv.org/abs/1706.05587)' and accessed 
through [`torchvision`](https://pytorch.org/vision/stable/models/deeplabv3.html).
