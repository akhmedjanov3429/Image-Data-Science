(a) Texture Classification
# import numpy as np
# import matplotlib.pyplot as plt
# def read_raw_image(filename, shape):
#     with open(filename, 'rb') as f:
#         image = np.fromfile(f, dtype=np.uint8, count=np.prod(shape))
#         image = image.reshape(shape)
#     return image

# image_files = []
# for i in range(15):
#     image_files.append(f'./Project3_Images/sample{i+1}.raw')
# image_shape = (64, 64)

# # Read and preprocess images
# images = [read_raw_image(filename, image_shape) for filename in image_files]
# # Visualize the images
# # plt.figure(figsize=(15, 5))
# # for i in range(15):
# #     plt.subplot(3, 5, i + 1)
# #     plt.imshow(images[i], cmap='gray')
# #     plt.title(f'Sample {i + 1}')
# #     plt.axis('off')

# # plt.show()

# # Assuming you visually grouped the images into 5 categories
# categories = {
#     'Category 1': [0, 1, 2],
#     'Category 2': [3, 4, 5],
#     'Category 3': [6, 7, 8],
#     'Category 4': [9, 10, 11],
#     'Category 5': [12, 13, 14]
# }

# # Visualize categorized images
# plt.figure(figsize=(15, 10))
# for category, indices in categories.items():
#     for i, index in enumerate(indices):
#         plt.subplot(5, 3, i + 1 + (list(categories.keys()).index(category) * 3))
#         plt.imshow(images[index], cmap='gray')
#         plt.title(f'{category} - Sample {index + 1}')
#         plt.axis('off')

# plt.show()


(b) Texture Segmentation
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans
# def read_raw_image(filename, shape):
#     with open(filename, 'rb') as f:
#         image = np.fromfile(f, dtype=np.uint8, count=np.prod(shape))
#         image = image.reshape(shape)
#     return image

# # Assuming you have files comb1.raw and comb2.raw
# image_files = ['./Project3_Images/comb1.raw', './Project3_Images/comb2.raw']
# image_shapes = [(256, 256), (256, 256)]

# # Read and preprocess images
# images = [read_raw_image(filename, shape) for filename, shape in zip(image_files, image_shapes)]

# def laws_filters(image):
#     # Define 1D masks
#     L5 = np.array([1, 4, 6, 4, 1])
#     E5 = np.array([-1, -2, 0, 2, 1])
#     S5 = np.array([-1, 0, 2, 0, -1])
#     W5 = np.array([-1, 2, 0, -2, 1])

#     # Create 2D masks
#     masks = [L5, E5, S5, W5]
#     filters = []

#     for i in range(4):
#         for j in range(4):
#             filters.append(np.outer(masks[i], masks[j]))

#     # Apply filters to the image
#     convolutions = [np.abs(np.convolve(image.flatten(), filter.flatten(), mode='same').reshape(image.shape))
#                     for filter in filters]

#     return np.stack(convolutions, axis=-1)

# # Apply Law's filter to the images
# filtered_images = [laws_filters(image) for image in images]

# # Flatten the features for k-means clustering
# flattened_features = [filtered_image.reshape(-1, filtered_image.shape[-1]) for filtered_image in filtered_images]

# def kmeans_segmentation(features, k):
#     kmeans = KMeans(n_clusters=k, random_state=42)
#     labels = kmeans.fit_predict(features)
#     segmented_image = labels.reshape(images[0].shape)
#     return segmented_image

# # Set K values for segmentation
# k_values = [5, 4]

# # Perform segmentation and visualize the results
# plt.figure(figsize=(12, 6))

# for i, k in enumerate(k_values):
#     segmented_image = kmeans_segmentation(flattened_features[i], k)

#     plt.subplot(1, 2, i + 1)
#     plt.imshow(segmented_image, cmap='gray')
#     plt.title(f'Segmentation (K={k})')
#     plt.axis('off')

# plt.show()
