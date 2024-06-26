# Spectrogram Segmentation

The successful application of [semantic segmentation](https://www.ibm.com/topics/semantic-segmentation) to radiofrequency (RF) spectrograms holds significant applications 
for [spectrum sensing](https://iopscience.iop.org/article/10.1088/1742-6596/2261/1/012016#:~:text=In%20cognitive%20radio%2C%20spectrum%20sensing,user%20can%20use%20the%20spectrum.) and serves as a foundational example showcasing the near-term feasibility of 
[intelligent radio](https://www.qoherent.ai/intelligentradio/) technology.

In this example, we use [PyTorch](https://pytorch.org/) and [Lightning](https://lightning.ai/docs/pytorch/stable/) to train a segmentation model to identify and
differentiate between 5G NR and 4G LTE signals within wideband spectrograms.

Qoherent's mission to drive the creation of intelligent radio technology requires a combination of open-source and 
proprietary tools. This example, which leverages open-source tools and machine learning frameworks to train on 
synthetic radio data generated using MATLAB, showcases our commitment to interoperability and our tool-agnostic 
approach to innovation.

Classification results are comparable to those reported by MathWorks' AI-based network. For more information, 
please refer to the following article by MathWorks:
[Spectrum Sensing with Deep Learning to Identify 5G and LTE Signals](https://www.mathworks.com/help/comm/ug/spectrum-sensing-with-deep-learning-to-identify-5g-and-lte-signals.html).

If you found this example interesting or helpful, don't forget to give it a star! ⭐


## 🚀 Getting Started

This example is provided as a Jupyter Notebook. You have the option to either run this example locally or in Google 
Colab.

To run this example locally, you'll need to download the project and dataset and set up a Conda 
virtual environment. If this seems daunting, we recommend running this example on Google Colab.

### Running this example locally

Please note that running this example locally will require approximately 10 GB of free space. Please ensure you 
have sufficient space available prior to proceeding.

1. Ensure that [Git](https://git-scm.com/downloads) and [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) are installed on the computer where you plan to run this example. 
Additionally, if you'd like to accelerate model training with a GPU, you'll require [CUDA](https://docs.nvidia.com/cuda/cuda-quick-start-guide/index.html).


2. Clone this repository to your local computer:
```commandline
git clone https://github.com/qoherent/spectrogram-segmentation.git
```


3. Create a Conda environment using the provided `environment.yml` file:
```commandline
conda env create -f environment.yml
```
This will create a new Conda environment named `spectrogram-segmentation` within the Conda installation directory.


4. Active the environment:
```commandline
conda activate spectrogram-segmentation
```


5. Download and unpack the spectrum sensing dataset:
```commandline
python download_dataset.py
```
This command will create a new directory named `SpectrumSensingDataset` at the project's root. The 
MathWorks Spectrum Sensing dataset will be downloaded and unpacked into this directory automatically.


6. Register the environment kernel with Jupyter:
```commandline
ipython kernel install --user --name=spectrogram-segmentation
```


7. Open the notebook, `spectrogram_segmentation.ipynb`, specifying to use the `spectrogram-segmentation` kernel:
```commandline
jupyter notebook spectrogram_segmentation.ipynb --MultiKernelManager.default_kernel_name=spectrogram-segmentation
```


8. Give yourself a pat on the back - you're all set up and ready to explore the example! For more information on 
navigating the Jupyter Notebook interface and executing code, please check out this tutorial by the Codecademy 
Team: [How To Use Jupyter Notebooks](https://www.codecademy.com/article/how-to-use-jupyter-notebooks).

Depending on your system specifications and the availability of a CUDA, running this example locally may take 
several minutes. If a cell is taking too long to execute, you can interrupt its execution by clicking the "Kernel" 
menu and selecting "Interrupt Kernel" or by pressing `Ctrl + C` in the terminal where Jupyter Notebook is running.


9. After you finish exploring, consider removing the dataset from your system and deleting the Conda environment to 
free up space. You can delete the Conda environment using the following command:
```commandline
conda env remove --name spectrogram-segmentation
```

### Running this example in Google Colab

**Coming soon:** Don't want the hassle of downloading the project and dataset and setting up a Conda environment? 
We've shared the notebook on Google Colab: [Spectrogram Segmentation]().


## 🤝 Contribution

We welcome contributions from the community! Whether it's an enhancement, bug fix, or improved explanation, 
your input is valuable. For significant changes, or if you'd like to prepare a separate tutorial, kindly 
[contact us](mailto:info@qoherent.ai) beforehand.

If you encounter any issues or to report a security vulnerability, please submit a bug report to the GitHub Issues 
page [here](https://github.com/qoherent/spectrogram-segmentation/issues).

Has this example inspired a project or research initiative related to intelligent radio? Please [get in touch](mailto:info@qoherent.ai); 
we'd love to collaborate with you! 📡🚀

Finally, be sure to check out our open-source project: [RIA Core](https://github.com/qoherent/ria) (Coming soon!).


## 🖊️ Authorship

This work is a product of the collaborative efforts of the Qoherent team. Of special mention are [Wan](https://github.com/wan-sdr), 
[Madrigal](https://github.com/MadrigalDW), [Dimitrios](https://github.com/DimitriosK), and [Michael](https://github.com/mrl280).


## 🙏 Attribution

The dataset used in this example was prepared by MathWorks and is publicly available [here](https://www.mathworks.com/supportfiles/spc/SpectrumSensing/SpectrumSenseTrainingDataNetwork.tar.gz). For more information 
on how this dataset was generated or to generate further spectrum data, please refer to MathWork's article on spectrum 
sensing. For more information about Qoherent's use of MATLAB to accelerate intelligent radio research, check out our 
[customer story](https://www.mathworks.com/company/user_stories/qoherent-uses-matlab-to-accelerate-research-on-next-generation-ai-for-wireless.html).

The DeepLabv3 models used in this example were initially proposed by Chen _et al._ and are further discussed 
in their 2017 paper titled '[Rethinking Atrous Convolution for Semantic Image Segmentation](https://arxiv.org/abs/1706.05587)'. The MobileNetV3 
backbone used in this example was developed by Howard _et al._ and is further discussed in their 2019 paper titled 
'[Searching for MobileNetV3](https://arxiv.org/abs/1905.02244)'. Models were accessed through [`torchvision`](https://pytorch.org/vision/stable/models/deeplabv3.html).

A special thanks to the PyTorch and Lightning teams for providing the foundational machine learning frameworks used in 
this example.
