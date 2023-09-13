Disabled Top center of bounding box check for invalidating detection in order to ensure that the features will be close to the front and bottom region of the vehicle.

Considering point for PLP for obtaining optical flow trajectory on the ground plane.

commit 93a09e7c64bbc5201fe40d8e38d6c0ae1591ce43 (HEAD -> 19-run-me-on-brnocompspeed-dataset-for-evaluation, origin/19-run-me-on-brnocompspeed-dataset-for-evaluation)
Author: RTX 3060 almond <RTX 3060 almond>
Date:   Tue Sep 12 17:38:24 2023 +0545

    Using ptForPLP to obtain the index of the point added to vPolygonsInFlow to identify the trajectory that is to be considered for obtaining optical flow trajectory on the world ground plane for evaluation.
