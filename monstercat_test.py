from lsst.daf.butler import Butler
from lsst.geom import SpherePoint
import lsst.sphgeom as sphgeom

from lsst.daf.butler import Butler

# Use the shared repo
butler = Butler("/repo/main", collections="refcats")

# Query a specific trixel
htm7_id = 203118
refcat = butler.get("the_monster_20250219", dataId={"htm7": htm7_id})

# Output the results
print(f"Number of sources in trixel {htm7_id}: {len(refcat)}")
print(refcat[:5])

