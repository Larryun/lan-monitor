import setuptools

setuptools.setup(
    name="lan_monitor",
    version="0.0.1",
    author="Larry",
    packages=setuptools.find_packages(),
    # package_dir={"": "src"},
    python_requires='>=3.6',
    install_requires=[
        "pymongo==3.12.0",
        "scapy==2.4.5",
        "jsonobject",
        "pyyaml"
    ]
)