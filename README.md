# MRI Diffusion Reconstruction

> Deep Learning-based MRI Reconstruction using Denoising Diffusion Probabilistic Models (DDPM)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red)
![Medical Imaging](https://img.shields.io/badge/Medical-Imaging-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Overview

Magnetic Resonance Imaging (MRI) is one of the most widely used non-invasive imaging techniques for medical diagnosis. However, patient motion during scanning often introduces artifacts that degrade image quality and affect clinical interpretation.

This project investigates the use of **Denoising Diffusion Probabilistic Models (DDPM)** for reconstructing high-quality MRI images from motion-corrupted scans. The work was carried out as part of my **Summer Research Internship at Motilal Nehru National Institute of Technology (MNNIT), Prayagraj** under the project *Generative AI in Medical Image Analysis*.

---

## Objectives

- Reconstruct motion-corrupted MRI images using diffusion models.
- Learn the distribution of clean MRI scans through iterative denoising.
- Improve image quality while preserving anatomical structures.
- Evaluate reconstruction performance using standard image quality metrics.

---

## Methodology

The reconstruction pipeline consists of:

1. MRI Dataset Preparation
2. Motion Artifact Simulation
3. DDPM Training
4. Reverse Diffusion Sampling
5. Image Reconstruction
6. Performance Evaluation

---

## Technologies Used

- Python
- PyTorch
- NumPy
- OpenCV
- Matplotlib
- Google Colab / Kaggle

---

## Results

The trained model demonstrated successful reconstruction of motion-corrupted MRI images.

### Best Performance

| Metric | Value |
|---------|------:|
| MSE | **0.0011** |
| SSIM | **0.5732** |
| PSNR | **29.69 dB** |

---

## Repository Structure

```
MRI-Diffusion-Reconstruction/
│
├── notebooks/
├── assets/
├── results/
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## Installation

```bash
git clone https://github.com/d-atharw/MRI-Diffusion-Reconstruction.git

cd MRI-Diffusion-Reconstruction

pip install -r requirements.txt
```

---

## Future Improvements

- Train on larger MRI datasets.
- Improve reconstruction fidelity.
- Explore Latent Diffusion Models.
- Reduce inference time.
- Extend to 3D volumetric MRI reconstruction.

---

## Acknowledgements

This project was completed during my Summer Research Internship at **Motilal Nehru National Institute of Technology (MNNIT), Prayagraj**, under the guidance of my research supervisor.

---

## License

This project is licensed under the MIT License.
