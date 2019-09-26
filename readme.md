# RoboPol Artefacts

This a GitHub repo which contains codes, data and results of implementing deep convolutional neural networks for identifying artefacts in RoboPol images. RoboPol is an international collaboration of astronomers from the University of Crete and the Foundation for Research and Technology - Hellas (FORTH) in Greece, the California Institute of Technology in the United States, the Max-Planck Institute for Radioastronomy in Bonn, Germany, the Nicolaus Copernicus University in Poland, and the Inter-University Centre for Astronomy and Astrophysics, in Pune, India. Please visit [the official website](https://www.robopol.org) for more details.

## Authors
The code and documentation has been written and compiled by Dhruv Paranjpye (University of Michigan Ann Arbor). He was mentored by Dr. Ashish Mahabal (California Institute of Technology). This project was a part of Dhruv's summer internship at Caltech between May - August 2019. 

## JSON File

input_param JSON File:
This file (input_param.json) contains all the paths of the data directories and result files which are generated. You would have to edit those according to the paths in on your computer. You would find a detailed documentation on how to do so in the file 'Documentation of pipeline.pdf'

You may use the json_notebook.ipynb Jupyter Notebook to make the same. 

## Code Documentation
The codes for the entire project have primarily been written in Python 3 but also using IRAF (Image Reduction and Analysis Facility) and Sextractor. The Documentation of Pipeline.pdf file contains a very detailed documentation about the same. Please refer to this document to understand how the codes were written. 


## Usage
You may directly download the Artifact Detection with 3 layers 1 channel input images.ipynb Notebook which has all the code for the deep learning model.


## License
[MIT](https://choosealicense.com/licenses/mit/)
