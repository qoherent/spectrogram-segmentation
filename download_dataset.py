"""
Download MathWorks' Spectrum Sensing 5G dataset, if it isn't already downloaded.
"""

import os
import tarfile
import warnings

import requests
from torch.utils.model_zoo import tqdm

mirror = "https://www.mathworks.com/supportfiles/spc/SpectrumSensing/"
resource = "SpectrumSenseTrainingDataNetwork.tar.gz"
file_url = "{}{}".format(mirror, resource)
target_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SpectrumSensingDataset")
archive_file = os.path.join(target_dir, resource)

# Ensure the target directory exists.
if not os.path.exists(target_dir):
    os.makedirs(target_dir, exist_ok=True)

# Check if the target directory is empty, and abort the download if it's not.
if len(os.listdir(target_dir)) != 0:
    warnings.warn(f"Target directory '{target_dir}' is not empty. Aborting download.")
    exit(1)

# Download and extract the dataset into the target directory.
print(f"Downloading {format(file_url)}")
n_bytes = int(requests.head(file_url).headers.get("Content-Length", 0))

with (
    requests.get(file_url, stream=True, timeout=3) as r,
    open(archive_file, "wb") as out_file,
    tqdm(desc="Downloading", total=n_bytes, unit="B", unit_scale=True) as pbar,
):
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            out_file.write(chunk)
            pbar.update(len(chunk))

print(f"Extracting to {target_dir}")
with tarfile.open(archive_file) as tar:
    tar.extractall(target_dir)

# Remove the archive file after extraction.
os.remove(archive_file)
print(f"Archive file '{archive_file}' removed.")
