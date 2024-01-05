import numpy as np

# Original 2D array
original_2d_array = np.array([[1, 2], [3, 4]])

# Define a function to determine the RGB tuple based on the current number
def determine_rgb_tuple(value):
    # Your custom logic to determine RGB tuple based on the current number
    # For example, let's use a simple logic: white if even, black if odd
    return [255, 255, 255] if value % 2 == 0 else [0, 0, 0]

# Vectorize the function
vectorized_determine_rgb_tuple = np.vectorize(determine_rgb_tuple, otypes=[object])

# Apply the vectorized function to the original 2D array
new_3d_array = vectorized_determine_rgb_tuple(original_2d_array)

# Print the original 2D array and the new 3D array
print("Original 2D array:")
print(original_2d_array)
print("\nNew 3D array:")
print(new_3d_array)
