# import os
# import glob
# import nibabel as nib
# import numpy as np
# import matplotlib.pyplot as plt
# from PIL import Image
# from tqdm import tqdm

# # INPUT DATASET PATH
# dataset_path = r"D:\\Atharw\\Studies\\MNNIT Internship\\Dataset\\ds004332-download"

# # OUTPUT FOLDER
# output_folder = "output_slices"

# os.makedirs(output_folder, exist_ok=True)

# # FIND MRI FILES
# nii_files = glob.glob(
#     os.path.join(dataset_path, "**", "*.nii"),
#     recursive=True
# )

# print(f"Found {len(nii_files)} MRI files")

# count = 0

# for file in tqdm(nii_files):

#     try:
#         # LOAD MRI
#         img = nib.load(file)
#         data = img.get_fdata()

#         # TAKE MIDDLE SLICE
#         middle_slice = data[:, :, data.shape[2] // 2]

#         # NORMALIZE IMAGE
#         middle_slice = middle_slice - np.min(middle_slice)
#         middle_slice = middle_slice / np.max(middle_slice)
#         middle_slice = (middle_slice * 255).astype(np.uint8)

#         # CONVERT TO IMAGE
#         image = Image.fromarray(middle_slice)

#         # RESIZE
#         image = image.resize((256, 256))

#         # SAVE IMAGE
#         save_path = os.path.join(
#             output_folder,
#             f"slice_{count}.png"
#         )

#         image.save(save_path)

#         count += 1

#     except Exception as e:
#         print(f"Error with file {file}: {e}")

# print(f"\nSaved {count} MRI slices")


import os
import glob
import nibabel as nib
import numpy as np
from PIL import Image
from tqdm import tqdm

# INPUT DATASET PATH
dataset_path = r"D:\Atharw\Studies\MNNIT Internship\Dataset\ds004332-download"

# OUTPUT FOLDER
output_folder = "better_slices"

os.makedirs(output_folder, exist_ok=True)

# FIND MRI FILES
nii_files = glob.glob(
    os.path.join(dataset_path, "**", "*.nii"),
    recursive=True
)

print(f"Found {len(nii_files)} MRI files")

count = 0

for file in tqdm(nii_files):

    try:
        img = nib.load(file)

        data = img.get_fdata()

        # TAKE MULTIPLE CENTRAL SLICES
        z_dim = data.shape[2]

        start_slice = max(0, z_dim // 2 - 15)

        end_slice = min(
            z_dim,
            z_dim // 2 + 15
        )

        slice_range = range(
            start_slice,
            end_slice,
            3
        )

        for slice_idx in slice_range:

            slice_img = data[:, :, slice_idx]

            # SKIP EMPTY / LOW DETAIL SLICES
            if np.mean(slice_img) < 10:
                continue

            # NORMALIZE
            slice_img = slice_img - np.min(slice_img)

            if np.max(slice_img) != 0:
                slice_img = slice_img / np.max(slice_img)

            slice_img = (slice_img * 255).astype(np.uint8)

            # CONVERT TO IMAGE
            image = Image.fromarray(slice_img)

            image = image.resize((128, 128))

            save_path = os.path.join(
                output_folder,
                f"slice_{count}.png"
            )

            image.save(save_path)

            count += 1

    except Exception as e:
        print(f"Error: {e}")

print(f"Saved {count} slices")