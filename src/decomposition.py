"""
Salt flux decomposition.

A salt flux decomposition based on three-dimensional hydrodynamic data. The resulting salt flux components only maintain
their spatial variability, i.e., the temporal and vertical dimensions are collapsed in the process of decomposing the
salt fluxes in four categories:
 1. tide-averaged and depth-integrated salt flux;
 2. tide-varying and depth-integrated salt flux;
 3. tide-averaged and depth-varying salt flux;
 4. tide- and depth-varying salt flux.
"""
import logging

import numpy as np

_LOG = logging.getLogger(__name__)


class SFD:
    """Salt flux decomposition.

    Execution of a salt flux decomposition based on deviations from the mean in different dimensions, namely the time-
    and depth-dimensions. This salt flux decomposition results in four salt fluxes:
     1. Salt flux related to the net flow: tide-averaged and depth-integrated salt flux
     2. Salt flux related to the tidal oscillation: tide-varying and depth-integrated salt flux
     3. Salt flux related to the estuarine circulation: tide-averaged and depth-varying salt flux
     4. Salt flux related to the time-dependent shear: tide- and depth-varying salt flux [residual term]

    As input, three-dimensional data of (1) the flow velocities in the dominant flow direction, i.e., the magnitude of
    the flow velocities maintaining the sign; (2) the salinity; and (3) the cross-sectional areas perpendicular to the
    flow velocities, i.e., the flow velocity vectors must be normal to the cross-sectional areas..

    The three-dimensional numpy arrays are considered to be shaped as (T, S, D): T is the time-dimension; S the space-
    dimension; and D the depth-dimension. However, different time- and depth-axes can be specified upon initiation of
    this object.

    In case the space-dimension is split in two dimensions, e.g., an x- and y-dimension, the calculations should remain
    valid. This is, however, not tested and requires additional attention.
    """

    def __init__(self, flow: np.ndarray, salinity: np.ndarray, cross_section: np.ndarray, **kwargs) -> None:
        """
        :param flow: flow velocities
        :param salinity: salinity
        :param cross_section: cross-sectional area
        :param kwargs: optional arguments
            depth_axis: array's axis of depth-dimension, defaults to -1
            time_axis: array's axis of time-dimension, defaults to 0

        :type flow: numpy.ndarray
        :type salinity: numpy.ndarray
        :type cross_section: numpy.ndarray
        :type kwargs: optional
            depth_axis: int
            time_axis: int

        :raises ValueError: if shapes of `flow`, `salinity`, and `cross_section` do not match
        """
        # input check
        if not (flow.shape == salinity.shape == cross_section.shape):
            msg = f'`flow`, `salinity`, and `cross_section` must all have the same shape; ' \
                f'`flow.shape={flow.shape}`, ' \
                f'`salinity.shape={salinity.shape}`, ' \
                f'`cross_section.shape={cross_section.shape}`'
            raise ValueError(msg)

        # model output data
        self.flow = flow
        self.salinity = salinity
        self.cross_section = cross_section

        # dimension axes
        self.time_axis: int = kwargs.get('time_axis', 0)
        self.depth_axis: int = kwargs.get('depth_axis', -1)

        # initiate flux variables
        self._flux0 = None
        self._flux1 = None
        self._flux3 = None
        self._flux4 = None

    """Matrix computations"""

    def avg_time(self, variable: np.ndarray) -> np.ndarray:
        """Average over time-dimension.

        :param variable: variable data
        :type variable: numpy.ndarray

        :return: variable averaged over time-dimension
        :rtype: numpy.ndarray
        """
        return np.ma.mean(variable, axis=self.time_axis)

    def int_depth(self, variable: np.ndarray) -> np.ndarray:
        """Integrate over depth-dimension.

        :param variable: variable data
        :type variable: numpy.ndarray

        :return: variable integrated over depth-dimension
        :rtype: numpy.ndarray
        """
        return np.ma.sum(variable, axis=self.depth_axis)

    def avg_time_int_depth(self, variable: np.ndarray) -> np.ndarray:
        """Average over time- and integrate over depth-dimension.

        :param variable: variable data
        :type variable: numpy.ndarray

        :return: variable averaged over time- and integrated over depth-dimension
        :rtype: numpy.ndarray
        """
        return self.avg_time(self.int_depth(variable))

    def expand_time(self, variable: np.ndarray) -> np.ndarray:
        """Expand over time-dimension.

        :param variable: variable data
        :type variable: numpy.ndarray

        :return: variable expanded over time-dimension
        :rtype: numpy.ndarray
        """
        return np.expand_dims(variable, axis=self.time_axis)

    def expand_depth(self, variable: np.ndarray) -> np.ndarray:
        """Expand over depth-dimension.

        :param variable: variable data
        :type variable: numpy.ndarray

        :return: variable expanded over depth-dimension
        :rtype: numpy.ndarray
        """
        return np.expand_dims(variable, axis=self.depth_axis)

    """Flux components"""

    def _component(self, func: callable, variable: np.ndarray) -> np.ndarray:
        """General component calculation.

        This method functions as a helper-method in which the general calculation of all components is encompassed,
        which is a normalisation by the cross-sectional areas in the yz-plane.

        :param func: function for specific component calculation
        :param variable: variable data

        :type func: callable
        :type variable: numpy.ndarray

        :return: variable's component
        :rtype: numpy.ndarray
        """
        return func(variable * self.cross_section) / func(self.cross_section)

    def component1(self, variable: np.ndarray) -> np.ndarray:
        """First component, which is the building block of the salt flux related to the net flow.

        :param variable: variable data
        :type variable: numpy.ndarray

        :return: component 1 of variable
        :rtype: numpy.ndarray
        """
        return self._component(self.avg_time_int_depth, variable)

    def component2(self, variable: np.ndarray, comp1: np.ndarray = None) -> np.ndarray:
        """Second component, which is the building block of the salt flux related to the tidal oscillation.

        :param variable: variable data
        :param comp1: component 1 of variable, defaults to None

        :type variable: numpy.ndarray
        :type comp1: numpy.ndarray, optional

        :return: component 2 of variable
        :rtype: numpy.ndarray
        """
        # calculate component 1
        if comp1 is None:
            comp1 = self.component1(variable)
        # return component 2
        return self._component(self.int_depth, variable) - self.expand_time(comp1)

    def component_(self, variable: np.ndarray, comp1: np.ndarray = None, comp2: np.ndarray = None) -> np.ndarray:
        """Intermediate component, which is a working parameter for components 3 and 4. In essence, it is the remainder
        after subtracting components 1 and 2.

        :param variable: variable data
        :param comp1: component 1 of variable, defaults to None
        :param comp2: component 2 of variable, defaults to None

        :type variable: numpy.ndarray
        :type comp1: numpy.ndarray, optional
        :type comp2: numpy.ndarray, optional

        :return: intermediate component of variable
        :rtype: numpy.ndarray
        """
        # calculate component 1
        if comp1 is None:
            comp1 = self.component1(variable)
        # calculate component 2
        if comp2 is None:
            comp2 = self.component2(variable, comp1=comp1)
        # return intermediate component
        return variable - self.expand_depth(comp2 + self.expand_time(comp1))

    def component3(self, variable: np.ndarray, var_is_comp_: bool = False) -> np.ndarray:
        """Third component, which is the building block of the salt flux related to the estuarine circulation.

        :param variable: variable data
        :param var_is_comp_: variable data represents intermediate component, defaults to False

        :type variable: numpy.ndarray
        :type var_is_comp_: bool, optional

        :return: component 3 of variable
        :rtype: numpy.ndarray
        """
        # calculate intermediate component
        if not var_is_comp_:
            variable = self.component_(variable)
        # return component 3
        return self._component(self.avg_time, variable)

    def component4(self, variable: np.ndarray, var_is_comp_: bool = False, comp3: np.ndarray = None) -> np.ndarray:
        """Fourth component, which is the building block of the salt flux related to the time-dependent shear.

        :param variable: variable data
        :param var_is_comp_: variable data represents intermediate component, defaults to False
        :param comp3: component 3 of variable, defaults to None

        :type variable: numpy.ndarray
        :type var_is_comp_: bool, optional
        :type comp3: numpy.ndarray, optional

        :return: component 4 of variable
        :rtype: numpy.ndarray
        """
        # calculate intermediate component
        if not var_is_comp_:
            variable = self.component_(variable)
        # calculate component 3
        if comp3 is None:
            comp3 = self.component3(variable, var_is_comp_=True)
        # return component 4
        return variable - self.expand_time(comp3)

    """Fluxes computations"""

    def _calc_flux(self, f_comp: callable, f_cross_section: callable) -> np.ndarray:
        """General calculation of salt flux components.

        This method functions as a helper-method in which the general calculation of all salt flux components is
        encompassed, which is applying the same function on the flow velocity and the salinity (namely, `f_comp`),
        applying another function on the cross-sectional area (namely, `f_cross_section`), and taking the product of
        all three variables.

        :param f_comp: component function
        :param f_cross_section: cross-section function

        :type f_comp: callable
        :type f_cross_section: callable

        :return: salt flux component
        :rtype: numpy.ndarray
        """
        return f_comp(self.flow) * f_comp(self.salinity) * f_cross_section(self.cross_section)

    @property
    def flux1(self) -> np.ndarray:
        """Salt flux component 1, related to the net flow.

        :return: salt flux component 1
        :rtype: numpy.ndarray
        """
        if self._flux0 is None:
            self._flux0 = self._calc_flux(self.component1, self.avg_time_int_depth)
        return self._flux0

    @property
    def flux2(self) -> np.ndarray:
        """Salt flux component 2, related to the tidal oscillation.

        :return: salt flux component 2
        :rtype: numpy.ndarray
        """
        if self._flux1 is None:
            self._flux1 = self.avg_time(self._calc_flux(self.component2, self.int_depth))
        return self._flux1

    @property
    def flux3(self) -> np.ndarray:
        """Salt flux component 3, related to the estuarine circulation.

        :return: salt flux component 3
        :rtype: numpy.ndarray
        """
        if self._flux3 is None:
            self._flux3 = self.int_depth(self._calc_flux(self.component3, self.avg_time))
        return self._flux3

    @property
    def flux4(self) -> np.ndarray:
        """Salt flux component 4, related to the time-dependent shear.

        :return: salt flux component 4
        :rtype: numpy.ndarray
        """
        if self._flux4 is None:
            self._flux4 = self.avg_time_int_depth(self._calc_flux(self.component4, lambda x: x))
        return self._flux4

    @property
    def fluxes(self) -> tuple:
        """Collection of all salt flux components.

        :return: salt flux components
        :rtype: tuple
        """
        return self.flux1, self.flux2, self.flux3, self.flux4
