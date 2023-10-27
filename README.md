![Tests](https://github.com/ghendrickx/ANNESI/actions/workflows/tests.yml/badge.svg)

# Salt Flux Decomposition
`NumPy`-based salt flux decomposition.

## Requirements
This repository has the following requirements (see also [`requirements.txt`](requirements.txt)):
```text
numpy
```

## Usage
The basic usage of this repository is rather straightforward: Provide three-dimensional data on the flow, salinity, and 
cross-sectional area retrieved from a hydrodynamic model to the [`SFD`](src/decomposition.py)-object.
```python
# dummy data
import numpy as np

u = np.random.random((12, 10, 10))  # shape=(time, space, depth)
s = np.random.random((12, 10, 10))  # shape=(time, space, depth)
a = np.random.random((12, 10, 10))  # shape=(time, space, depth)

# initiate `SFD`-object
from src.decomposition import SFD

sfd = SFD(flow=u, salinity=s, cross_section=a)

# calculate salt flux components
fluxes = sfd.fluxes  # shape=(4, space)
```
**Note** that the three (3) input arrays must have equal size.

## Author
Gijs G. Hendrickx 
[![alt text](https://camo.githubusercontent.com/e1ec0e2167b22db46b0a5d60525c3e4a4f879590a04c370fef77e6a7e00eb234/68747470733a2f2f696e666f2e6f726369642e6f72672f77702d636f6e74656e742f75706c6f6164732f323031392f31312f6f726369645f31367831362e706e67) 0000-0001-9523-7657](https://orcid.org/0000-0001-9523-7657)
(_Delft University of Technology_).

Contact: [G.G.Hendrickx@tudelft.nl](mailto:G.G.Hendrickx@tudelft.nl?subject=[GitHub]%20ANNESI:%20).
