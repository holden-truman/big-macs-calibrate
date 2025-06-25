from lsst.daf.butler import Butler
from lsst.geom import SpherePoint
import lsst.sphgeom as sphgeom

# Initialize butler
butler = Butler("embargo", collections="refcats")

# Set dataset type
datasetType = "the_monster_20250219"

ra = 150.0
dec = 2.0
coord = SpherePoint(ra, dec, sphgeom.degrees)
htm7_index = coord.htmIndex(7)

# Query the catalog
refcat = butler.get(datasetType, dataId={"htm7": htm7_id})

# Print number of sources
print(f"Number of sources in trixel {htm7_id}: {len(refcat)}")

# Example: display first few rows and columns
print(refcat[:5])
