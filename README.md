# Daad: An Arabic Diacritizer

This repository contains our work on implementing a Mobile Application as our Graduation Project at Princess Sumaya For Technology.

## Table of Contents

- [Installation](#installation)
- [Data](#data)
- [Code](#code)
- [Results](#results)
- [Unsuccessful Trials](#unsuccessful-trials)
- [Flutter](#Flutter)
- [API](#API)

## Installation

Before running any script, don't forget to execute `pip install -r requirements.txt` to download all the project dependencies.

## Data

Our training data is 'Tashkeela-processed', which you can download via this [link](https://sourceforge.net/projects/tashkeela-processed/).

The data is uploaded within the repository and can be found in the 'Data' directory.

## Code

Our final submitted code can be found in the 'Final GP Code' directory.

This directory contains a Jupyter Notebook with the implementation, training, and evaluation of the model, as well as separate scripts for functions, constants, DER_WER, and prediction.

You can also find the weights of the trained models in the 'weights' directory.

## Results

Our 'results' directory contains three sub-directories:
* On 10K Lines: Contains a file with the actual text and the predicted text by each of our models.
* On Tashkeela Benchmark: Contains the test data of actual Tashkeela used to evaluate other models.
* Stats: Contains a file with the DER and WER values of our trained models.

## Unsuccessful Trials

We have included our unsuccessful trials within our repository so they can be utilized in future works and improvements.

## Flutter

We have uploaded the implementation of our Flutter Application. You can find it in the FLutterApp Directory.

## API

We used FastAPI as our local API to integrate the model and the application. 

