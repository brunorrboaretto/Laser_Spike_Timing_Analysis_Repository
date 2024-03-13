# Laser_Spike_Timing_Analysis_Repository
 This repository hosts the code and resources associated with the recently accepted paper titled "Characterizing the spike timing of a chaotic laser by using ordinal analysis and machine learning."

## Paper Overview

Semiconductor lasers, known for being fast, energy efficient and low cost, exhibit, under the influence of optical feedback, a rich variety of complex dynamic behaviors. This diversity arises from the interplay of three factors: nonlinear light-matter interactions in the laser cavity, high dimensionality of the phase space, introduced by feedback delay time and stochasticity, due to the presence of quantum } spontaneous emission noise and other noise sources. Exploiting these characteristics, semiconductor lasers with optical feedback serve as ideal systems for conducting controlled experiments aimed at unraveling nonlinear, stochastic, and time delay-induced phenomena. Moreover, they present an appealing prospect for innovative photonic applications, including random number generation and information processing. One extensively studied feedback-induced dynamical regime is the low-frequency fluctuations regime, characterized by spiking laser output. In this study, we investigate the statistical properties of the timing of optical spikes, analyzing experimental sequences of inter-spike intervals (ISIs). Employing a recently proposed technique that integrates nonlinear time series analysis and machine learning, we demonstrate that the ISI sequences exhibit statistical ordinal properties akin to Flicker noise.

## Repository Contents

This repository contains: XXXXX

- **Code:** Implementation of ordinal analysis and machine learning algorithms used in the paper.
- **Datasets:** Instructions to download the experimental ISI sequences utilized in the analysis.
- **Documentation:** Detailed instructions on running the code and reproducing the results.

## Dataset

We analyze experimental data from ISI sequences recorded in https://opg.optica.org/oe/fulltext.cfm?uri=oe-26-7-9298&id=385199], accessible at https://doi.org/10.5281/zenodo.5913506. Employing sinusoidal modulation, we systematically probe the response of semiconductor lasers with optical feedback. This modulation technique, characterized by its simplicity with only amplitude and frequency as discernible features, facilitates comprehensive investigations into nonlinear behaviors and theoretical model validations. Our analysis encompasses a broad spectrum of physical parameters, including the largest modulation amplitude and a range of DC values for the laser current ($I$) spanning from 25.5 mA to 27.5 mA, with 5 values, and modulation frequencies ($\nu$) ranging from 1 MHz to 70 MHz, with 70 values. In total, our dataset comprises 350 ISI sequences, each containing approximately 5500-75000 ISIs, representing a comprehensive exploration of laser dynamics under varying experimental conditions.
- Download the dataset (file <code>Sinusoidal_full_TS.zip</code> 210.2 MB) from https://doi.org/10.5281/zenodo.5913506;
- Extract the <code>.zip</code> file to obtain the folder <code>Sinusoidal_full_TS/</code>, which contains four folders <code>Gain_40</code>, <code>Gain_60</code>, <code>Gain_80</code>, and <code>Gain_100</code>, each folder correspond to a value of modulation amplitude of the laser in arbitrary units;
- In this work we selected the folder <code>Gain_100</code>;
- The data is in <code>.mat</code> form, by running the command <code>python3 extract.py</code> will read the <code>.mat</code> files and convert it into <code>.dat</code> form, writing one by one into the <code>Sinusoidal_full_TS/</code> directory. From here the four <code>Gain_XX</code> can be removed;
- If everything works, by running the code <code>python3 extract.py</code>, it will result in a dataset composed of 350 <code>.dat</code> files (70 frequency values for 5 distinct current values).

## Python libraries:

- **NumPy**: Facilitates efficient handling and manipulation of large multi-dimensional arrays and provides a wide range of mathematical functions for numerical computations in Python;
- **sys**: The sys module provides access to some variables used or maintained by the Python interpreter and functions that interact strongly with the interpreter;
- **matplotlib.pyplot** is a Python library commonly used for creating visualizations and plots, providing a high-level interface for generating a wide range of graphs and charts.
- **csv**: Used to read the .csv files;
- **TensorFlow**: TensorFlow is an open-source machine learning framework developed by Google. It provides a comprehensive ecosystem of tools, libraries, and community resources for building and deploying machine learning models across a range of platforms.
- **scikit-learn**: Scikit-learn is a simple and efficient tool for data mining and data analysis. It provides a wide range of supervised and unsupervised learning algorithms through a consistent interface in Python.
- **Keras**: is a high-level deep learning framework designed for rapid experimentation and prototyping of neural networks. It offers an intuitive interface for building, training, and deploying models, with modular components known as layers that can be easily configured to create complex architectures. Keras seamlessly integrates with popular deep learning backends like TensorFlow, enabling efficient computation on both CPU and GPU. Its user-friendly API abstracts away low-level implementation details, allowing researchers and practitioners to focus on model design and experimentation.



### How to Use

Feel free to explore the code, datasets, and documentation provided in this repository. If you have any questions or suggestions, please don't hesitate to open an issue or reach out to the authors.

### Citation

If you find this work helpful for your research, please consider citing:

\[Insert citation for your paper here\]

Thank you for your interest in our research! We hope this repository serves as a valuable resource for spike timing analysis in chaotic lasers.

---

Feel free to adjust the content according to your preferences and include any additional sections or information you find necessary.
