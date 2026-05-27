# MRI Diffusion Reconstruction

A Generative AI project focused on Brain MRI image reconstruction using Diffusion Models and Deep Learning techniques.

## Project Overview

This project implements a DDPM-based (Denoising Diffusion Probabilistic Model) pipeline for MRI image generation and reconstruction using Brain MRI datasets.

The workflow includes:

- MRI preprocessing from `.nii` medical volumes
- 2D slice extraction
- Conditional and unconditional diffusion model training
- MRI reconstruction and denoising
- Quantitative evaluation using SSIM, PSNR, and MSE metrics

The project was developed as part of a Generative AI internship in Applied Deep Learning Applications at MNNIT Allahabad.

---

# Objectives

- Learn and implement diffusion models in medical imaging
- Reconstruct cleaner MRI scans from corrupted inputs
- Experiment with conditional diffusion pipelines
- Evaluate reconstruction quality quantitatively

---

# Dataset

The dataset consists of Brain MRI volumes in `.nii` format.

Preprocessing pipeline:
- Extraction of anatomical MRI slices
- Slice normalization
- Conversion to grayscale PNG images
- Filtering low-information slices

---

# Model Architecture

The project uses:

- DDPM (Denoising Diffusion Probabilistic Model)
- U-Net based architecture
- PyTorch
- HuggingFace Diffusers

---

# Pipeline

```text
MRI Volumes (.nii)
        ↓
Slice Extraction
        ↓
Preprocessing & Normalization
        ↓
Corrupted MRI Generation
        ↓
Conditional Diffusion Training
        ↓
MRI Reconstruction
        ↓
Evaluation Metrics
