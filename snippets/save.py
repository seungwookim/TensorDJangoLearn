# # Create some variables.
# v1 = tf.Variable(..., name="v1")
# v2 = tf.Variable(..., name="v2")
# ...
# # Add an op to initialize the variables.
# init_op = tf.initialize_all_variables()
#
# # Add ops to save and restore all the variables.
# saver = tf.train.Saver()
#
# # Later, launch the model, initialize the variables, do some work, save the
# # variables to disk.
# with tf.Session() as sess:
#   sess.run(init_op)
#   # Do some work with the model.
#   ..
#   # Save the variables to disk.
#   save_path = saver.save(sess, "/tmp/model.ckpt")
#   print("Model saved in file: %s" % save_path)