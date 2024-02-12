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
[<img src=https://info.orcid.org/wp-content/uploads/2020/12/orcid_16x16.gif alt="ORCiD" width="16" height="16">](https://orcid.org/0000-0001-9523-7657)
(_Delft University of Technology_).

Contact: [G.G.Hendrickx@tudelft.nl](mailto:G.G.Hendrickx@tudelft.nl?subject=[GitHub]%20ANNESI:%20).

## References
When using this repository, please cite accordingly:
>   Hendrickx, G.G.
    (2023).
    Salt Flux Decomposition: NumPy-based salt flux decomposition.
    4TU.ResearchData.
    Software.
    [doi:10.4121/bccbe767-667b-40ba-a4d1-d8fcad900772](https://doi.org/https://doi.org/10.4121/19307693).


## License
This repository is licensed under [Apache License 2.0](LICENSE).
