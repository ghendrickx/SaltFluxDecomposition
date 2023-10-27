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

## References
When using this repository, please cite accordingly:
>   Hendrickx, G.G.
    (n.d.).
    SaltFluxDecomposition: NumPy-based salt flux decomposition.
    
### Related references
The salt flux decomposition in this repository is used as part of the following peer-reviewed articles:

*   [Hendrickx, G.G.](https://orcid.org/0000-0001-9523-7657),
    [Manuel, L.A.](https://orcid.org/0000-0001-5424-1270),
    [Pearson, S.G.](https://orcid.org/0000-0002-3986-4469),
    [Aarninkhof, S.G.J.](https://orcid.org/0000-0002-4591-0257), and
    [Meselhe, E.A.](https://orcid.org/0000-0002-0628-1670)
    (_in prep._).
    An earthen sill as a measure to mitigate salt intrusion in estuaries.


*   [Hendrickx, G.G.](https://orcid.org/0000-0001-9523-7657), and
    [Pearson, S.G.](https://orcid.org/0000-0002-3986-4469)
    (_in prep._).
    On the effects of intertidal area on estuarine salt intrusion.
    
The salt flux decomposition in this repository is used as part of the following conference presentations/proceedings
(_presenter in **bold**_):

*   [**Hendrickx, G.G.**](https://orcid.org/0000-0001-9523-7657),
    [Meselhe, E.A.](https://orcid.org/0000-0002-0628-1670),
    [Herman, P.M.J.](https://orcid.org/0000-0003-2188-6341), and
    [Aarninkhof, S.G.J.](https://orcid.org/0000-0002-4591-0257)
    (Apr. 2023).
    A sill as a nature-based solution to mitigate salt intrusion.
    _Coastal Sediments 2023_.
    New Orleans, LA, USA.

*   [**Hendrickx, G.G.**](https://orcid.org/0000-0001-9523-7657),
    [Meselhe, E.A.](https://orcid.org/0000-0002-0628-1670),
    [Aarninkhof, S.G.J.](https://orcid.org/0000-0002-4591-0257), and
    [Herman, P.M.J.](https://orcid.org/0000-0003-2188-6341)
    (Apr. 2023).
    Designing a sill to mitigate salt intrusion.
    _Lower Mississippi River Science Symposium_.
    New Orleans, LA, USA.
