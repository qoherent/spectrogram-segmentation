"""
Download MathWorks' Spectrum Sensing dataset, if it isn't already downloaded.
"""

import hashlib
import os
import sys

import requests
from torch.utils.model_zoo import tqdm


def sha256(target: str) -> str:
    """Calculates the SHA256 hash of the target resource.

    :param target: The full path, including the filename, of the resource to hash.
    :type target: str

    :return: The SHA256 hash of the target resource.
    """
    sha256_hash = hashlib.sha256()

    with open(target, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)

    return sha256_hash.hexdigest()


mirror = "https://storage.googleapis.com/qoherent_external_drive/general_dataset_library/"
resource = "spectrum_sensing_dataset_v1.0.hdf5"
file_url = "{}{}".format(mirror, resource)
sha256_checksum = "8a93aa14145ea1a35cbc191defbbcf90c49ecdb89e6e93f3e55357f182d184c6"

target = os.path.join(os.path.dirname(os.path.abspath(__file__)), "spectrum_sensing_dataset.hdf5")

# Check if the dataset source file already exists. Only skip the download if the existing file also
# matches the expected checksum; otherwise it is an incomplete or corrupted download and we re-fetch it.
if os.path.exists(target):
    if sha256(target=target) == sha256_checksum:
        print(f"{target} already exists and matches the expected checksum. Nothing to do.")
        sys.exit(0)
    print(f"{target} already exists but does not match the expected checksum. Re-downloading.")

# Download into a temporary '.part' file first, so that an interrupted or failed download never leaves a
# corrupted file at the target path (which would otherwise block all future download attempts).
partial = target + ".part"

print(f"Downloading {file_url}")
n_bytes = int(requests.head(file_url, timeout=30).headers.get("Content-Length", 0))

try:
    with (
        requests.get(file_url, stream=True, timeout=30) as r,
        open(partial, "wb") as out_file,
        tqdm(desc="Downloading MathWorks' Spectrum Sensing Dataset", total=n_bytes, unit="B", unit_scale=True) as pbar,
    ):
        r.raise_for_status()
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                out_file.write(chunk)
                pbar.update(len(chunk))
except BaseException:
    # Remove the partial file on any error or interruption (e.g. Ctrl+C) so a retry starts clean.
    if os.path.exists(partial):
        os.remove(partial)
    raise

if sha256(target=partial) != sha256_checksum:
    os.remove(partial)
    raise RuntimeError(
        "Checksum of the downloaded file does not match expected.\n"
        "The download may be corrupted, please try again."
    )

# Atomically move the fully-downloaded, checksum-verified file into place.
os.replace(partial, target)
