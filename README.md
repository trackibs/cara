# Cara CSV Chart

Generate a Chart from exported Cara CSV

Cara is a mobile app that lets you track IBS symptoms, food, medication etc :

https://cara-app.com/

The Cara app allows you to export your data as a CSV file.

This repository contains a Python script that allows you to generate a MatPlotLib chart based off the exported Cara CSV data file.

Steps to generate chart :

1. Export your Cara CSV file and save it into this directory.

2. Install the Python script dependencies via :

```
pip install -r requirements.txt
```

3. Run the script :

```
python cara.py
```

4. A chart window should pop up and show you a stacked column graph of your data and also save in the directory a PNG image of the chart at Cara.png
