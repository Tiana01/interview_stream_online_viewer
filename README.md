# Stream online viewer

## Description 

This is a python 3.6 application that receives streams of data and allows multiple users display it in a web browser. It is based  on the python framework called Dash. Dash was built on Flask, plotly.js and React.js and it is used to create interactive web applications with python. 

## Dependencies
We use Anaconda for packaging our libraries. If you are not familiar with Anaconda, have a look at their website:
https://anaconda.org/

In order to use this repository, you will have to install the following conda packages:
- dash
- plotly
- bsread

The bsread and plotly packages are available on https://anaconda.org/ and can be installed on linux as follows:
```bash
conda install -c paulscherrerinstitute bsread

conda install -c plotly plotly 
```

The Dash framework is made up of  libraries (also available on https://anaconda.org) such as the html components and core components which can be installed  as follows:
```bash

conda install -c conda-forge dash 

conda install -c conda-forge dash-html-components
 
conda install -c conda-forge dash-core-components
```


## Installation

To install Stream Online Viewer, clone the repository and set up the anaconda environment as shown below:
```bash
git clone https://github.com/Tiana01/interview_stream_online_viewer.git

cd interview_stream_online_viewer

conda create -n yourenvname python=3.6 anaconda

source activate yourenvname

conda install -c [packages]
```

## Run

### BSread
This is the protocol we use to transfer beam synchronous data at SwissFEL: 
[https://github.com/paulscherrerinstitute/bsread_python](https://github.com/paulscherrerinstitute/bsread_python)

You will not be able to access the real BSread stream from outside of PSI. This repository has a stream generator you 
can use to simulate camera images and metadata you will later display to the clients. The generator is located in 
**stream\_online\_viewer/start\_stream.py** and can be run from the ROOT of this repository:

```bash
export PYTHONPATH=$(pwd):${PYTHONPATH}
python stream_online_viewer/start_stream.py
```
To stop the stream press **CTRL + C**.

> NOTE: Always make sure to be in the directory that contains the python scripts you are running. In this case, stream_online_viewer

### Receive stream
To run the data receiver:
```bash
export PYTHONPATH=$(pwd):${PYTHONPATH}
python stream_online_viewer/stream_receiver.py
```

## Contact
For comments and requests, contact:
```bash
christiana.uzonwanne@psi.ch
```

