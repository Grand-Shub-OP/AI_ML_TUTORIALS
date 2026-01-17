import tensorflow as tf

# Print the installed TensorFlow version
print("TensorFlow Version:", tf.__version__)

# Check for available GPUs
gpu_devices = tf.config.list_physical_devices('GPU')
print("Num GPUs Available:", len(gpu_devices))

if gpu_devices:
  print("GPU Details:", gpu_devices)
else:
  print("No GPU found. TensorFlow will run on the CPU.")
