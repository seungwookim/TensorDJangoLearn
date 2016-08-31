"""Example of DNNClassifier for Iris plant dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from sklearn import cross_validation
from sklearn import metrics
import tensorflow as tf
from tensorflow.contrib import learn
from tensorflow.contrib.session_bundle import exporter

FLAGS = tf.app.flags.FLAGS

class TensorIris():


    def __init__(self):



      # Load dataset.
      iris = learn.datasets.load_dataset('iris')
      x_train, x_test, y_train, y_test = cross_validation.train_test_split(
          iris.data, iris.target, test_size=0.2, random_state=42)

      sess = tf.InteractiveSession()

      sess.run(tf.initialize_all_variables())

      # Build 3 layer DNN with 10, 20, 10 units respectively.
      feature_columns = learn.infer_real_valued_columns_from_input(x_train)
      classifier = learn.DNNClassifier(
          feature_columns=feature_columns, hidden_units=[10, 20, 10], n_classes=3)

      # Fit and predict.
      classifier.fit(x_train, y_train, steps=200)
      score = metrics.accuracy_score(y_test, classifier.predict(x_test))
      print('Accuracy: {0:f}'.format(score))

      self.score = format(score)

      # print ('Exporting trained model')
      # saver = tf.train.Saver(sharded=True)
      # model_exporter = exporter.Exporter(saver)
      # #signature = exporter.classification_signature(input_tensor=x, scores_tensor=y)
      # #model_exporter.init(sess.graph.as_graph_def(), default_graph_signature=signature)
      # model_exporter.export("\\home\\ec2-user\\tensorflow\\save\\", tf.constant(FLAGS.export_version), sess)
      # print
      # 'Done exporting!'
