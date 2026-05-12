"""
Fetch the Spectrum Sensing dataset from the internal Dawson host.

The original public mirror referenced by this repository is no longer
available. New employees should run this script from the repository root while
connected to the office network or VPN.
"""

import argparse
import hashlib
import shutil
import subprocess
from pathlib import Path


DEFAULT_SOURCE = "qrf@dawson:/home/qrf/SpectrumSensingDataset.hdf5"
DEFAULT_TARGET = "SpectrumSensingDataset.hdf5"
SHA256_CHECKSUM = "47e3590e32106f5b7420b1f0cc2051049fa61f5423d877b647a65e634f9b3c7d"


def sha256(target: Path) -> str:
    """Calculate the SHA256 hash of a local file."""
    sha256_hash = hashlib.sha256()

    with target.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            sha256_hash.update(chunk)

    return sha256_hash.hexdigest()


def validate_dataset(target: Path) -> None:
    """Validate that the local dataset matches the expected internal copy."""
    checksum = sha256(target)
    if checksum != SHA256_CHECKSUM:
        raise RuntimeError(
            f"Checksum of {target} does not match expected value.\n"
            f"Expected: {SHA256_CHECKSUM}\n"
            f"Actual:   {checksum}\n"
            "Remove the file and rerun this script, or confirm the Dawson copy was updated intentionally."
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch the Spectrum Sensing dataset from Dawson.")
    parser.add_argument(
        "--source",
        default=DEFAULT_SOURCE,
        help=f"scp source path. Defaults to {DEFAULT_SOURCE!r}.",
    )
    parser.add_argument(
        "--target",
        default=DEFAULT_TARGET,
        help=f"local output path. Defaults to {DEFAULT_TARGET!r}.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="overwrite the local target if it already exists.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    target = Path(args.target)

    if target.exists() and not args.force:
        print(f"{target} already exists. Validating checksum.")
        validate_dataset(target)
        print("Dataset is already present and valid.")
        return

    if shutil.which("scp") is None:
        raise RuntimeError("scp was not found on PATH. Install OpenSSH client tools and try again.")

    target.parent.mkdir(parents=True, exist_ok=True)
    print(f"Copying {args.source} to {target}")
    subprocess.run(["scp", args.source, str(target)], check=True)

    validate_dataset(target)
    print(f"Downloaded and validated {target}.")


if __name__ == "__main__":
    main()
