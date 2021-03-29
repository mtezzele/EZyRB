import numpy as np
from .approximation import Approximation


class NeighborsRegressor(Approximation):
    """
    A generic superclass for wrappers of *NeighborsRegressor from sklearn.

    :param kwargs: arguments passed to the internal instance of
        *NeighborsRegressor.
    """

    def __init__(self, **kwargs):
        raise NotImplementedError("This class must be extended, not used.")

    def fit(self, points, values):
        """
        Construct the interpolator given `points` and `values`.

        :param array_like points: the coordinates of the points.
        :param array_like values: the values in the points.
        """
        points = np.array(points).reshape(len(points), -1)
        values = np.array(values)

        self.regressor.fit(points, values)

    def predict(self, new_point):
        """
        Evaluate interpolator at given `new_points`.

        :param array_like new_points: the coordinates of the given points.
        :return: the interpolated values.
        :rtype: numpy.ndarray
        """
        if isinstance(new_point, np.ndarray) or isinstance(new_point, list):
            new_point = np.array(new_point).reshape(len(new_point), -1)
        else:
            new_point = np.array([new_point])

        return self.regressor.predict(new_point)
