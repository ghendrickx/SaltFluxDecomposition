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
**Note** that the three (3) input arrays must have equal size/shape.

## Author
Gijs G. Hendrickx 
[<img src=https://info.orcid.org/wp-content/uploads/2020/12/orcid_16x16.gif alt="ORCiD" width="16" height="16">](https://orcid.org/0000-0001-9523-7657)
(_Delft University of Technology_).

Contact: [G.G.Hendrickx@tudelft.nl](mailto:G.G.Hendrickx@tudelft.nl?subject=[GitHub]%20ANNESI:%20).

## License
This repository is licensed under [Apache License 2.0](LICENSE).

## Reference
When using this repository, please cite accordingly:
>   Hendrickx, G.G.
    (2023).
    Salt Flux Decomposition: NumPy-based salt flux decomposition.
    4TU.ResearchData.
    Software.
    [doi:10.4121/bccbe767-667b-40ba-a4d1-d8fcad900772](https://doi.org/https://doi.org/10.4121/19307693).
    
### Related references
The salt flux decomposition in this repository is used as part of the following peer-reviewed articles:

 1. [Hendrickx, G.G.](https://orcid.org/0000-0001-9523-7657),
    [Manuel, L.A.](https://orcid.org/0000-0001-5424-1270),
    [Pearson, S.G.](https://orcid.org/0000-0002-3986-4469),
    [Aarninkhof, S.G.J.](https://orcid.org/0000-0002-4591-0257), and
    [Meselhe, E.A.](https://orcid.org/0000-0002-5832-8864)
    (_in prep._).
    An earthen sill as a measure to mitigate salt intrusion in estuaries.

 1. [Hendrickx, G.G.](https://orcid.org/0000-0001-9523-7657), and
    [Pearson, S.G.](https://orcid.org/0000-0002-3986-4469)
    (_in prep._).
    On the effects of intertidal area on estuarine salt intrusion.
    
The salt flux decomposition in this repository is used as part of the following conference presentations/proceedings
(_presenter in **bold**_):

 1. [**Hendrickx, G.G.**](https://orcid.org/0000-0001-9523-7657),
    [Meselhe, E.A.](https://orcid.org/0000-0002-5832-8864),
    [Herman, P.M.J.](https://orcid.org/0000-0003-2188-6341), and
    [Aarninkhof, S.G.J.](https://orcid.org/0000-0002-4591-0257)
    (Apr. 2023).
    A sill as a nature-based solution to mitigate salt intrusion.
    _Coastal Sediments 2023_.
    New Orleans, LA, USA.

 1. [**Hendrickx, G.G.**](https://orcid.org/0000-0001-9523-7657),
    [Meselhe, E.A.](https://orcid.org/0000-0002-5832-8864),
    [Aarninkhof, S.G.J.](https://orcid.org/0000-0002-4591-0257), and
    [Herman, P.M.J.](https://orcid.org/0000-0003-2188-6341)
    (Apr. 2023).
    Designing a sill to mitigate salt intrusion.
    _Lower Mississippi River Science Symposium_.
    New Orleans, LA, USA.
