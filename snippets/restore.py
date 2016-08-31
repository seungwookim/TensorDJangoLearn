# # Create some variables.
# v1 = tf.Variable(..., name="v1")
# v2 = tf.Variable(..., name="v2")
# ...
# # Add ops to save and restore all the variables.
# saver = tf.train.Saver()
#
# # Later, launch the model, use the saver to restore variables from disk, and
# # do some work with the model.
# with tf.Session() as sess:
#   # Restore variables from disk.
#   saver.restore(sess, "/tmp/model.ckpt")
#   print("Model restored.")
#   # Do some work with the model
#   ...