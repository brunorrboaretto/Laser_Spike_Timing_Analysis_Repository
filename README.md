# Laser_Spike_Timing_Analysis_Repository
 This repository hosts the code and resources associated with the recently accepted paper titled "Characterizing the spike timing of a chaotic laser by using ordinal analysis and machine learning."
<!-- a normal html comment //XXXXX INCLUDE THE INFORMATION OF THE PAPER HERE.... DOI EDICTOS PICKS BLA BLA BAL FOCUS ISSUE '  <code>DOI: 10.1063/5.0193967</code>
 -->
<!--Volume #:	34-->
<!--Issue #:	4-->
<!--Issue:	2024-04-30-->
 
## Paper Overview

Semiconductor lasers, renowned for their speed, energy efficiency, and affordability, manifest a diverse array of complex dynamic behaviors under optical feedback. This diversity stems from the interplay of three factors: nonlinear light-matter interactions within the laser cavity, high dimensionality of the phase space introduced by feedback delay time, and stochasticity due to quantum spontaneous emission noise and other sources. Leveraging these characteristics, semiconductor lasers with optical feedback offer an ideal platform for controlled experiments aimed at uncovering nonlinear, stochastic, and time delay-induced phenomena. Additionally, they hold promise for innovative photonic applications such as random number generation and information processing. One extensively studied feedback-induced dynamical regime is the low-frequency fluctuations regime, characterized by spiking laser output. In this study, we investigate the statistical properties of the timing of optical spikes by analyzing experimental sequences of inter-spike intervals (ISIs). Employing a recently proposed technique that integrates nonlinear time series analysis and machine learning, we demonstrate that the ISI sequences exhibit statistical ordinal properties akin to Flicker noise.

## Repository Contents

This repository contains: 

- **Datasets:** Instructions to download the experimental ISI sequences utilized in the analysis;
- **Codes:** Implementation of ordinal analysis and machine learning algorithms used in the paper. </br>
In the end, the user will be able to reproduce Figure 4 of the manuscript which summarizes our findings in this research.

## Dataset

We analyze experimental data from ISI sequences recorded in https://opg.optica.org/oe/fulltext.cfm?uri=oe-26-7-9298&id=385199, accessible at https://doi.org/10.5281/zenodo.5913506. Employing sinusoidal modulation, researchers systematically probe the response of semiconductor lasers with optical feedback. This modulation technique, characterized by its simplicity with only amplitude and frequency as discernible features, facilitates comprehensive investigations into nonlinear behaviors and theoretical model validations. The analysis encompasses a broad spectrum of physical parameters, including the largest modulation amplitude and a range of DC values for the laser current ($I$) spanning from 25.5 mA to 27.5 mA, with 5 values, and modulation frequencies ($\nu$) ranging from 1 MHz to 70 MHz, with 70 values. In total, the dataset comprises 350 ISI sequences, each containing approximately 5500-75000 ISIs, representing a comprehensive exploration of laser dynamics under varying experimental conditions.</br>

## Instructions for downloading and extracting the Dataset
- Download the dataset file <code>Sinusoidal_full_TS.zip</code> (210.2 MB) from https://doi.org/10.5281/zenodo.5913506.
- Extract the <code>.zip</code> file to obtain the folder <code>Sinusoidal_full_TS/</code>, which contains four folders: <code>Gain_40</code>, <code>Gain_60</code>, <code>Gain_80</code>, and <code>Gain_100</code>. Each folder corresponds to a specific modulation amplitude of the laser in arbitrary units.
- In this work, we have selected the folder <code>Gain_100</code>.
- The data is in <code>.mat</code> format. Running the command <code>python3 extract.py</code> will read the <code>.mat</code> files and convert them into <code>.dat</code> format, writing each file into the <code>Sinusoidal_full_TS/</code> directory. Following this step, the four <code>Gain_XX</code> folders can be ignored (removed). </br>
If everything works correctly, at the end of this step, it will result in 350 <code>.dat</code> files, each one representing an ISI laser sequence with 70 frequency values for 5 distinct current values.

## Python libraries:

- **NumPy**: Facilitates efficient handling and manipulation of large multi-dimensional arrays and provides a wide range of mathematical functions for numerical computations in Python;
- **matplotlib.pyplot** is a Python library commonly used for creating visualizations and plots, providing a high-level interface for generating a wide range of graphs and charts;
- **scipy.io** module in Python's SciPy library provides functions for reading and writing various file formats used in scientific computing. It allows users to load and save data from MATLAB files (.mat), as well as other file formats commonly used in scientific computing, such as NetCDF, IDL, and Harwell-Boeing files;
- **colorednoise** generates Gaussian distributed noise with a power law spectrum with arbitrary exponents.
- **TensorFlow**: TensorFlow is an open-source machine learning framework. It provides a comprehensive ecosystem of tools, libraries, and community resources for building and deploying machine-learning models across a range of platforms;
- **scikit-learn**: Scikit-learn is a simple and efficient tool for data mining and data analysis. It provides a wide range of supervised and  unsupervised learning algorithms through a consistent interface in Python;
- **Keras**: is a high-level deep learning framework designed for rapid experimentation and prototyping of neural networks. It offers an intuitive interface for building, training, and deploying models, with modular components known as layers that can be easily configured to create complex architectures. Keras seamlessly integrates with popular deep learning backends like TensorFlow, enabling efficient computation on both CPU and GPU. Its user-friendly API abstracts away low-level implementation details, allowing researchers and practitioners to focus on model design and experimentation.

## Generating the colored noise dataset (optional)
The methodology proposed in <code>10.1038/s41598-021-95231-z</code> consists in the training of an ANN in a dataset of colored noise signals.</br>
- By running the code <code>generate_colored_noise.py</code> will generate 50,000 colored noises with random values of $\alpha$ varying from -4 to 4;
- The code evaluates the 24 ordinal probabilities (with D=4) and the permutation entropy for each colored noise;
- The code generates the files:
1. <code>cn_a_data.dat</code> which corresponds to the values of $\alpha$ for each signal (labels);
2. <code>cn_p_data.dat</code> which corresponds to the 24 ordinal probabilities for each signal (features).</br>
*Please note that when utilizing this step, it is important to cite the repository https://github.com/felixpatzelt/colorednoise for proper acknowledgment.*

This step can be skipped if you want to download the <code>cn_a_data.dat</code> and <code>cn_p_data.dat</code> files directly from this repository.

## Generating the Artificial Neural Network (optional)
- To generate the ANN we utilize the Keras framework;
- Running the code <code>neural_network_0.py</code> allows the algorithm to read the files <code>cn_p_data.dat</code> and <code>cn_a_data.dat</code>, corresponding to the features and labels, respectively.
- Subsequently, the dataset is segmented into test and training groups; 
- ANN comprises two dense layers: the first layer with 64 neurons utilizing the <code>ReLU</code> activation function, and the second layer with a single neuron serving as the output layer. Following this, the model is compiled using the <code>RMSprop</code> optimizer, with mean squared error (MSE) as the loss function and mean absolute error (MAE) as the evaluation metric;
- Upon completion of the training stage, the ANN is capable of estimating the $\alpha$ value of an external signal solely based on the ordinal probabilities information;
- The final ANN and its parameters are saved in the <code>model.keras</code> file, which can be loaded for use with different data.</br>

*We have to mention that, as we have shown in https://doi.org/10.1038/s41598-021-95231-z, the* $\alpha$ *value of a colored noise (and stochastic process in general) carries information about the temporal correlations of the signal. In the case of deterministic signals,* $\alpha$ *carries useful information that can be used, for example, to distinguish between noise and chaos. In addition, we do not argue that the ISIs have an* $\alpha$ *coefficient that can be interpreted in terms of (or be consistent with) the slope of the power spectrum. We argue that the* $\alpha$ *value returned by the ML algorithm carries information about the ISI sequence, which in turn, encodes information about the input signal applied to the laser current.*

This step also can be skipped if you want to download the ANN <code>model.keras</code> directly from this repository.

## Data Analysis and Figures
The code <code>data_analysis_figure_4.py</code> is divided into 3 steps:
1. The code loads the ANN <code>model.keras</code> generated in the previous step.
2. The code reads the entire dataset (comprising 70 frequency values for 5 distinct current values) and estimates the $\alpha$ value for each.
3. If everything runs smoothly, a figure named <code>fig_4.png</code>, analogous to Figure 4 in the manuscript, is generated. This figure displays the $\alpha$ and $H$ (permutation entropy) values of the dataset, summarizing the results of the article.

### Citation

If you find this work helpful for your research, please consider reading and citing:

- Boaretto, B. R. R., Macau, E. E. N., & Masoller, C. (2024)."Characterizing the spike timing of a chaotic laser by using ordinal analysis and machine learning." *Chaos: An Interdisciplinary Journal of Nonlinear Science*,  34, 043108 (2024). </br>

In addition, the whole methodology used in this work has been originated and improved in these two works: 
- Boaretto, B. R. R., Budzinski, R. C., Rossi, K. L., Prado, T. L., Lopes, S. R., & Masoller, C. (2021). "Discriminating Chaotic and Stochastic Time Series using Permutation Entropy and Artificial Neural Networks." *Scientific Reports*, 11(1), 15789.
- Boaretto, B. R., Budzinski, R. C., Rossi, K. L., Prado, T. L., Lopes, S. R., & Masoller, C. (2021). "Evaluating temporal correlations in time series using permutation entropy, ordinal probabilities and machine learning." *Entropy*, 23(8), 1025.

--------------------------------------------------------------------------------------

Thank you for your interest in our research! </br>
We hope this repository serves as a valuable resource for spike timing analysis in chaotic lasers and data analysis in general.</br>

Sincerely,</br>
Bruno R. R. Boaretto.
