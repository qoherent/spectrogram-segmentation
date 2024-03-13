"""
Download MathWorks' Spectrum Sensing 5G dataset, if it isn't already downloaded.
"""
import os
import tarfile
import warnings
import requests

from torch.utils.model_zoo import tqdm


def download_file(url: str, local_path: str, chunk_size: int = 1024) -> None:
    """Download file from the specified URL.

    :param url: The URL of the file to download.
    :param local_path: The local path where the downloaded file will be saved.
    :param chunk_size: The size of each data chunk to be downloaded, in bytes. Default is 1024.

    :return: None
    """
    response = requests.head(url)
    n_bytes = int(response.headers.get('Content-Length', 0))

    with requests.get(url, stream=True, timeout=3) as r, open(local_path, 'wb') as out_file, \
            tqdm(desc="Downloading", total=n_bytes, unit='B', unit_scale=True) as pbar:
        for chunk in r.iter_content(chunk_size=chunk_size):
            if chunk:
                out_file.write(chunk)
                pbar.update(len(chunk))


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
download_file(url=file_url, local_path=archive_file)

print(f"Extracting to {target_dir}")
with tarfile.open(archive_file) as tar:
    tar.extractall(target_dir)

# Remove the archive file after extraction.
os.remove(archive_file)
print(f"Archive file '{archive_file}' removed.")
