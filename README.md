# Spectrogram Segmentation

In this example, we use [PyTorch](https://pytorch.org/) and [PyTorch Lightening](https://lightning.ai/docs/pytorch/stable/) to train DeepLabV3 segmentation models to differentiate between 
5G NR and 4G LTE signals within wideband spectrograms.

The successful application of semantic segmentation to radio frequency (RF) spectrograms holds significant applications 
for [spectrum sensing](https://iopscience.iop.org/article/10.1088/1742-6596/2261/1/012016#:~:text=In%20cognitive%20radio%2C%20spectrum%20sensing,user%20can%20use%20the%20spectrum.) and serves as a foundational example showcasing the near-term feasibility of 
[intelligent radio](https://www.qoherent.ai/intelligentradio/) technology.

Qoherent's mission to drive the creation of intelligent radio technology requires a combination of open-source and 
proprietary tools. This example, which leverages open-source tools and machine learning frameworks to train on 
synthetic radio data generated with MATLAB, showcases our commitment to interoperability and our tool-agnostic approach to innovation.

Classification results are comparable to those reported by MathWorks' AI-based network. For more information, 
please refer to the following MathWorks' article: 
[Spectrum Sensing with Deep Learning to Identify 5G and LTE Signals](https://www.mathworks.com/help/comm/ug/spectrum-sensing-with-deep-learning-to-identify-5g-and-lte-signals.html).

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
This will create a new Conda environment named `spectrogram-segmentation` within the Conda installation directory.


4. Active the environment:
```commandline
conda activate spectrogram-segmentation
```


5. Download the spectrum sensing dataset:
```commandline
python download_dataset.py
```
This will ...


6. Install a new IPython kernel within the `spectrogram-segmentation` environment:
```commandline
ipython kernel install --user --name=spectrogram-segmentation
```


6. Open the notebook, `spectrogram_segmentation.ipynb`, specifying to use the `spectrogram-segmentation` kernel:
```commandline
jupyter notebook spectrogram_segmentation.ipynb --MultiKernelManager.default_kernel_name=spectrogram-segmentation
```


7. Give yourself a pat on the back - you're all set up and ready to explore the example! For more information on 
navigating the Jupyter Notebook interface and executing code, please check out this tutorial by the Codecademy 
Team: [How To Use Jupyter Notebooks](https://www.codecademy.com/article/how-to-use-jupyter-notebooks).

Depending on your system specifications and the availability of a CUDA, running this example locally may take 
several minutes. If a cell is taking too long to execute, you can interrupt its execution by clicking the "Kernel" 
menu and selecting "Interrupt Kernel" or by pressing `Ctrl + C` in the terminal where Jupyter notebook is running.


8. After you finish exploring, consider removing the sensing dataset from your system and deleting the Conda 
environment to free up space. You can delete the Conda environment using:
```commandline
conda env remove --name spectrogram-segmentation
```

### 📓 Running this example in Google Colab

Coming soon: Don't want the hassle of downloading the project, dataset, and setting up a Conda environment? 
We've shared the notebook on Google Colab: [Spectrogram Segmentation]().


## 🤝 Contribution

We welcome contributions from the community! Whether it's an enhancement, bug fix, or improved explanation, 
your input is valuable. For significant changes or to include another similar example, kindly [contact us](mailto:info@qoherent.ai)
beforehand.

If you encounter any issues or to report a security vulnerability, please submit a bug report to the GitHub Issues 
page [here](https://github.com/qoherent/spectrogram-segmentation/issues).

Has this example inspired a radio project or research initiative? Please [get in touch](mailto:info@qoherent.ai); we'd love to 
collaborate with you! 📡🚀


## 🖊️ Authorship

This work is a product of the collaborative efforts of the Qoherent team. Of special mention are [Wan](https://github.com/wan-sdr), 
who led the initial research and prototyping effort, and [Michael](https://github.com/mrl280), who clean up the 
example and prepared the repository for sharing.


## 🙏 Attribution

The dataset used in this example was prepared by MathWorks and is publicly available [here](https://www.mathworks.com/supportfiles/spc/SpectrumSensing/SpectrumSenseTrainingDataNetwork.tar.gz). For more information 
on how the dataset was generated or to generate further spectrum data, please refer to the aforementioned MathWork's 
article on Spectrum Sensing. For more information about our use of MATLAB to accelerate intelligent radio research or our investigation into 
tooling interoperability, please refer to this [customer story](https://www.mathworks.com/company/user_stories/qoherent-uses-matlab-to-accelerate-research-on-next-generation-ai-for-wireless.html).

A Special thanks to the PyTorch and PyTorch Lightning teams for providing the foundational frameworks used in 
this project.

The DeepLabv3 models employed in this example were initially proposed by Chen _et al._ and are further discussed 
in their 2017 paper titled '[Rethinking Atrous Convolution for Semantic Image Segmentation](https://arxiv.org/abs/1706.05587)'. DeepLabv3
models were accessed through [`torchvision`](https://pytorch.org/vision/stable/models/deeplabv3.html).
