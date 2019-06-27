def visualise_classifier_performance(X_train, X_test, y_train, y_test, classifier, important_parameter = None, classifier_parameters = False):
  #import dependencies
  import matplotlib.pyplot as plt
  import numpy as np
  from matplotlib.colors import ListedColormap
  className = classifier.__class__.__name__
  print(f'{className} Classifier \n')
  if classifier_parameters:
    print(classifier)
    print('\n\n')
  # Visualising the Training set results
  if important_parameter:
    imp_feat_value = classifier.__dict__[important_parameter]
  else:
    important_parameter = 'not provided'
    imp_feat_value = ''
  X_set, y_set = X_train, y_train
  X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                       np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
  plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
               alpha = 0.75, cmap = ListedColormap(('red', 'green')))
  plt.xlim(X1.min(), X1.max())
  plt.ylim(X2.min(), X2.max())
  for i, j in enumerate(np.unique(y_set)):
      plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                  c = ListedColormap(('red', 'green'))(i), label = j)
  plt.title(f'{className}({important_parameter} = {imp_feat_value}) Classifier (Training set)')
  plt.xlabel('Age')
  plt.ylabel('Estimated Salary')
  plt.legend(loc = 'best', bbox_to_anchor=(1.2, 0.5))
  plt.show()

  # Visualising the Test set results
  from matplotlib.colors import ListedColormap
  X_set, y_set = X_test, y_test
  X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                       np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
  plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
               alpha = 0.75, cmap = ListedColormap(('red', 'green')))
  plt.xlim(X1.min(), X1.max())
  plt.ylim(X2.min(), X2.max())
  for i, j in enumerate(np.unique(y_set)):
      plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                  c = ListedColormap(('red', 'green'))(i), label = j)
  plt.title(f'{className}({important_parameter} = {imp_feat_value})Classifier (Test set)')
  plt.xlabel('Age')
  plt.ylabel('Estimated Salary')
  plt.legend(loc = 'best', bbox_to_anchor=(1.2, 0.5))
  plt.show()
