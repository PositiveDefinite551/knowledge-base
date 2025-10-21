import matplotlib.pyplot as plt
import numpy as np
from skimage.util import random_noise

# ---------------- Read the image (Example)-----------------------------------
plt.subplot(3, 2, 1)
img = plt.imread('img.tif') # EXAMPLE
plt.imshow(img)
plt.title("OG image")
plt.axis("off")

# --------------- Fourier transform of the image --------------------
plt.subplot(3, 2, 2)
F1 = np.fft.fft2(img)
magnitude = abs(np.fft.fftshift(F1))
magnitude_log = 20 * np.log1p(magnitude)
plt.imshow(magnitude_log)
plt.title("log magnitude of the Fourier Transform")
plt.axis("off")

# --------------- Noisy image ---------------------------------
img_noise = random_noise(img, mode="gaussian", var=0.1)
plt.subplot(3, 2, 3)
plt.imshow(img_noise)
plt.title("Noisy Image")
plt.axis("off")

# --------------- DFT of the noisy image ------------------
plt.subplot(3, 2, 4)
F2 = np.fft.fft2(img_noise)
F2_shift = np.fft.fftshift(F2)
magnitude_log2 = 20 * np.log1p(abs(F2_shift))
plt.imshow(magnitude_log2)
plt.title("log magnitude of the Fourier Transform")
plt.axis("off")

# ---------------- Gaussian Mask (Denoising) -----------------------------
# ---- Get the centre -----------
rows, cols = img_noise.shape
crow, ccol = img_noise.shape[0] // 2, img_noise.shape[1] // 2
sigma = 20  # sigma is filter width

# ---- create empty grid
x = np.linspace(-ccol, ccol, cols)
y = np.linspace(-crow, crow, rows)
X, Y = np.meshgrid(x, y)

# ---- compute empty Gaussian mask
gaussian_mask = np.exp(-(X**2 + Y**2) / (2 * sigma**2))

# ---- Applying our Gaussian mask to F2
F2_filtered = F2_shift * gaussian_mask  # this will be FFT of Denoised mask

# ---- inverse FFT -----------------
F2_ishift = np.fft.ifftshift(F2_filtered)
F2_inverse = np.real(np.fft.ifft2(F2_ishift))

# Visualisation
plt.subplot(3, 2, 5)
plt.imshow(F2_inverse)
plt.axis("off")
plt.title("Denoised with Gaussian Mask")

plt.subplot(3, 2, 6)
magnitude_log3 = 20 * np.log1p(abs(F2_filtered))
plt.imshow(magnitude_log3)
plt.axis("off")
plt.title("FFT of Denoised")
