# Laser_Spike_Timing_Analysis_Repository
 This repository hosts the code and resources associated with the recently accepted paper titled "Characterizing the spike timing of a chaotic laser by using ordinal analysis and machine learning."

## Paper Overview

Semiconductor lasers, known for being fast, energy efficient and low cost, exhibit, under the influence of optical feedback, a rich variety of complex dynamic behaviors. This diversity arises from the interplay of three factors: nonlinear light-matter interactions in the laser cavity, high dimensionality of the phase space, introduced by feedback delay time and stochasticity, due to the presence of quantum } spontaneous emission noise and other noise sources. Exploiting these characteristics, semiconductor lasers with optical feedback serve as ideal systems for conducting controlled experiments aimed at unraveling nonlinear, stochastic, and time delay-induced phenomena. Moreover, they present an appealing prospect for innovative photonic applications, including random number generation and information processing. One extensively studied feedback-induced dynamical regime is the low-frequency fluctuations regime, characterized by spiking laser output. In this study, we investigate the statistical properties of the timing of optical spikes, analyzing experimental sequences of inter-spike intervals (ISIs). Employing a recently proposed technique that integrates nonlinear time series analysis and machine learning, we demonstrate that the ISI sequences exhibit statistical ordinal properties akin to Flicker noise.

## Repository Contents

This repository contains: XXXXX

- **Datasets:** Instructions to download the experimental ISI sequences utilized in the analysis.
- **Codes:** Implementation of ordinal analysis and machine learning algorithms used in the paper.
- **Documentation:** Detailed instructions on running the code and reproducing the results.

## Dataset

We analyze experimental data from ISI sequences recorded in https://opg.optica.org/oe/fulltext.cfm?uri=oe-26-7-9298&id=385199], accessible at https://doi.org/10.5281/zenodo.5913506. Employing sinusoidal modulation, we systematically probe the response of semiconductor lasers with optical feedback. This modulation technique, characterized by its simplicity with only amplitude and frequency as discernible features, facilitates comprehensive investigations into nonlinear behaviors and theoretical model validations. Our analysis encompasses a broad spectrum of physical parameters, including the largest modulation amplitude and a range of DC values for the laser current ($I$) spanning from 25.5 mA to 27.5 mA, with 5 values, and modulation frequencies ($\nu$) ranging from 1 MHz to 70 MHz, with 70 values. In total, our dataset comprises 350 ISI sequences, each containing approximately 5500-75000 ISIs, representing a comprehensive exploration of laser dynamics under varying experimental conditions.
- Download the dataset (file <code>Sinusoidal_full_TS.zip</code> 210.2 MB) from https://doi.org/10.5281/zenodo.5913506;
- Extract the <code>.zip</code> file to obtain the folder <code>Sinusoidal_full_TS/</code>, which contains four folders <code>Gain_40</code>, <code>Gain_60</code>, <code>Gain_80</code>, and <code>Gain_100</code>, each folder correspond to a value of modulation amplitude of the laser in arbitrary units;
- In this work we selected the folder <code>Gain_100</code>;
- The data is in <code>.mat</code> form, by running the command <code>python3 extract.py</code> will read the <code>.mat</code> files and convert it into <code>.dat</code> form, writing one by one into the <code>Sinusoidal_full_TS/</code> directory. From here the four <code>Gain_XX</code> can be removed;
- If everything works, by running the code <code>python3 extract.py</code>, it will result in a dataset composed of 350 <code>.dat</code> files which comprise ISI laser sequences (70 frequency values for 5 distinct current values).

## Python libraries:

- **NumPy**: Facilitates efficient handling and manipulation of large multi-dimensional arrays and provides a wide range of mathematical functions for numerical computations in Python;
- **sys**: The sys module provides access to some variables used or maintained by the Python interpreter and functions that interact strongly with the interpreter;
- **matplotlib.pyplot** is a Python library commonly used for creating visualizations and plots, providing a high-level interface for generating a wide range of graphs and charts;
- **scipy.io** module in Python's SciPy library provides functions for reading and writing various file formats used in scientific computing. It allows users to load and save data from MATLAB files (.mat), as well as other file formats commonly used in scientific computing, such as NetCDF, IDL, and Harwell-Boeing files;
- **colorednoise** generates Gaussian distributed noise with a power law spectrum with arbitrary exponents.
- **TensorFlow**: TensorFlow is an open-source machine learning framework developed by Google. It provides a comprehensive ecosystem of tools, libraries, and community resources for building and deploying machine learning models across a range of platforms;
- **scikit-learn**: Scikit-learn is a simple and efficient tool for data mining and data analysis. It provides a wide range of supervised and unsupervised learning algorithms through a consistent interface in Python;
- **Keras**: is a high-level deep learning framework designed for rapid experimentation and prototyping of neural networks. It offers an intuitive interface for building, training, and deploying models, with modular components known as layers that can be easily configured to create complex architectures. Keras seamlessly integrates with popular deep learning backends like TensorFlow, enabling efficient computation on both CPU and GPU. Its user-friendly API abstracts away low-level implementation details, allowing researchers and practitioners to focus on model design and experimentation.

## Generating the colored noise dataset (optional)
- The ANN is trained in a dataset composed of colored noised signals;
- By running the code <code>generate_colored_noise.py</code> will generate 50,000 colored noises with random values of $\alpha$ varying from -4 to 4;
- The code evaluates the 24 ordinal probabilities (D=4) and the permutation entropy for each colored noise;
- The code generates three files:
1. <code>cn_a_data.dat</code> which corresponds to the values of $\alpha$ for each signal -- labels;
2. <code>cn_p_data.dat</code> which corresponds to the 24 ordinal probabilities for each signal -- features;
3. <code>cn_s_data.dat</code> which corresponds to the permutation entropy for each signal;
*Please note that when utilizing this step, it is important to cite the repository https://github.com/felixpatzelt/colorednoise for proper acknowledgment.*

This step can be skipped if you want to download the files <code>.dat</code> files directly from this repository.

## Generating the Artificial Neural Network
- To generate the ANN we use the Keras framework;
- Bu running the code <code>neural_network_0.py</code> the algorithm will read the file <code>cn_p_data.dat</code> and <code>cn_a_data.dat</code> which correspond to the features and its labels, respectively;
- This dataset is segmented into test and training groups; 
- The ANN is composed of two dense layers: the first layer has 64 neurons with <code>ReLU</code> activation function, and the second layer has a single neuron, which is the output layer. The model is then compiled using the <code>RMSprop</code> optimizer, mean squared error (MSE) as the loss function, and mean absolute error (MAE) as the evaluation metric.
- After the training stage, the ANN is ready to estimate the $\alpha$ value of an external signal just with the ordinal probabilities information;
- The final ANN and its parameters are saved in <code>model.h5</code> file, which can be loaded to be used in distinct data.</br>
*We have to mention that, as we have shown in https://doi.org/10.1038/s41598-021-95231-z, the $\alpha$ value of a colored noise (and stochastic process in general) carries information about the temporal correlations of the signal. In the case of deterministic signals, $\alpha$ carries useful information that can be used, for example, to distinguish between noise and chaos. In addition, we do not argue that the ISIs have an $\alpha$ coefficient that can be interpreted in terms of (or be consistent with) the slope of the power spectrum. We argue that the $\alpha$ value returned by the ML algorithm carries information about the ISI sequence, which in turn, encodes information about the input signal applied to the laser current.*

## Data Analysis and Figures
The code <code>data_analysis_figure_4.py</code>  is separated in X steps:
1. The code loads the ANN <code>model.keras</code> generated in the previous step;
2. The code reads the whole dataset (70 frequency values for 5 distinct current values) and estimates the $\alpha$ value for each;
3. If everything runs accordingly, a figure called <code>figu_4.png</code>, which is analogous to Figure 4 of the manuscript, is generated with the values of $\alpha$ and $H$ (permutation entropy) of the data set, which summarizes the results of the article.

### Citation

If you find this work helpful for your research, please consider citing:

\[Insert citation for your paper here\]

Thank you for your interest in our research! We hope this repository serves as a valuable resource for spike timing analysis in chaotic lasers.
