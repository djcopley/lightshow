from setuptools import find_packages, setup

setup(
    name='lightshow',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "waitress",
        "flask",
        "flask_socketio",
        "flask_restful",
        "rpi_ws281x",
    ],
    setup_requires=[
        "setuptools_scm"
    ],
    use_scm_version={
        "relative_to": __file__,
        "write_to": "lightshow/version.py"
    },
)
