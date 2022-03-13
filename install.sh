#!/bin/sh
curl -OL https://chromedriver.storage.googleapis.com/99.0.4844.51/chromedriver_mac64_m1.zip
unzip -o *.zip
conda env create --file educ.yaml
