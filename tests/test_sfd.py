"""
Tests for `SFD` (from `src.decomposition`).

Author: Gijs G. Hendrickx
"""
import numpy as np
import pytest

from src.decomposition import SFD

"""pytest.fixtures"""


@pytest.fixture
def uniform():
    return dict(
        flow=np.ones((10, 10, 10)),
        salinity=30 * np.ones((10, 10, 10)),
        cross_section=np.ones((10, 10, 10)),
    )


@pytest.fixture
def masked():
    data = dict(
        flow=np.ones((10, 10, 10)),
        salinity=30 * np.ones((10, 10, 10)),
        cross_section=np.ones((10, 10, 10)),
    )
    for k in data:
        data[k][:, 5:, 5:] = np.ma.masked
    return data


@pytest.fixture
def wedge():
    data = dict(
        flow=np.ones((10, 10, 10)),
        salinity=30 * np.ones((10, 10, 10)),
        cross_section=np.ones((10, 10, 10)),
    )
    data['flow'][:, :, 5:] *= -1
    data['salinity'][:, :, 5:] = 0
    return data


"""TestClass"""


class TestSFD:
    """Tests for the `src.decomposition.SFD`-object."""

    """Object initiation"""

    def test_input_check(self, uniform):
        SFD(**uniform)

    def test_invalid_input(self, uniform):
        data = uniform.copy()
        data['flow'] = np.ones((10, 8, 10))

        with pytest.raises(ValueError):
            SFD(**data)

    def test_masked_input(self, masked):
        SFD(**masked)

    """Salt flux calculations"""

    def test_output_shape(self, uniform):
        fluxes = SFD(**uniform).fluxes
        assert np.array(fluxes).shape == (4, 10)

    def test_output_uniform(self, uniform):
        fluxes = SFD(**uniform).fluxes
        assert np.all(fluxes[0] == 300)
        assert np.all(fluxes[1] == 0)
        assert np.all(fluxes[2] == 0)
        assert np.all(fluxes[3] == 0)

    def test_output_wedge(self, wedge):
        fluxes = SFD(**wedge).fluxes
        assert np.all(fluxes[0] == 0)
        assert np.all(fluxes[1] == 0)
        assert np.all(fluxes[2] == 150)
        assert np.all(fluxes[3] == 0)

    def test_output_masked(self, masked):
        fluxes = SFD(**masked).fluxes
        assert np.all(fluxes[0][:5] == 300)
        assert np.all(fluxes[0][5:] == 150)
        assert np.all(fluxes[1] == 0)
        assert np.all(fluxes[2] == 0)
        assert np.all(fluxes[3] == 0)
