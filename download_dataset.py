"""
Download MathWorks' Spectrum Sensing dataset, if it isn't already downloaded.
"""

import hashlib
import os

import requests
from torch.utils.model_zoo import tqdm


def sha256(target: str) -> str:
    """Calculates the SHA256 hash of the target resource.

    :param target: The full path, including the filename, of the resource to hash.
    :type target: str

    :return: str
    """
    sha256_hash = hashlib.sha256()

    with open(target, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)

    return sha256_hash.hexdigest()


mirror = "https://storage.googleapis.com/qoherent_external_drive/general_dataset_library/"
resource = "SpectrumSensingDataset.hdf5"
file_url = "{}{}".format(mirror, resource)
sha256_checksum = "496c354fb842f1f11aa7f46741a2c937063245fc899adad7a83e5f3012e9d6cc"

target = os.path.join(os.path.dirname(os.path.abspath(__file__)), "spectrum_sensing_dataset.hdf5")

# Check if the dataset source file already exists.
if os.path.exists(target):
    print(f"{target} already exists. Aborting download.")
    exit(1)

# Download the dataset source file into the target directory.
print(f"Downloading {format(file_url)}")
n_bytes = int(requests.head(file_url).headers.get("Content-Length", 0))

with (
    requests.get(file_url, stream=True, timeout=3) as r,
    open(target, "wb") as out_file,
    tqdm(desc="Downloading MathWorks' Spectrum Sensing Dataset", total=n_bytes, unit="B", unit_scale=True) as pbar,
):
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            out_file.write(chunk)
            pbar.update(len(chunk))

if sha256_checksum != sha256(target=target):
    raise RuntimeError(
        f"Checksum of {target} does not match expected.\n"
        f"The download may be corrupted, please remove the corrupted resource and try again."
    )
