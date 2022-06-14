# Autogenerated by pybind stub generator
# Do not manually edit
# To regenerate:
#   $ buck run //mapillary/opensfm/opensfm/src/sfm:pysfm_stubgen
# Use proper mode, e.g. @arvr/mode/linux/dev for arvr
# @generated

import opensfm.pybundle
import opensfm.pygeometry
import opensfm.pymap
from typing import *
__all__  = [
"BAHelpers",
"add_connections",
"count_tracks_per_shot",
"realign_maps",
"remove_connections"
]
class BAHelpers:
    @staticmethod
    def add_gcp_to_bundle(arg0: opensfm.pybundle.BundleAdjuster, arg1: opensfm.pymap.Map, arg2: List[opensfm.pymap.GroundControlPoint], arg3: dict) -> int: ...
    @staticmethod
    def bundle(arg0: opensfm.pymap.Map, arg1: Dict[str, opensfm.pygeometry.Camera], arg2: Dict[str, opensfm.pymap.RigCamera], arg3: List[opensfm.pymap.GroundControlPoint], arg4: dict) -> dict: ...
    @staticmethod
    def bundle_local(arg0: opensfm.pymap.Map, arg1: Dict[str, opensfm.pygeometry.Camera], arg2: Dict[str, opensfm.pymap.RigCamera], arg3: List[opensfm.pymap.GroundControlPoint], arg4: str, arg5: dict) -> tuple: ...
    @staticmethod
    def bundle_shot_poses(arg0: opensfm.pymap.Map, arg1: Set[str], arg2: Dict[str, opensfm.pygeometry.Camera], arg3: Dict[str, opensfm.pymap.RigCamera], arg4: dict) -> dict: ...
    @staticmethod
    def bundle_to_map(arg0: opensfm.pybundle.BundleAdjuster, arg1: opensfm.pymap.Map, arg2: bool) -> None: ...
    @staticmethod
    def detect_alignment_constraints(arg0: opensfm.pymap.Map, arg1: dict, arg2: List[opensfm.pymap.GroundControlPoint]) -> str: ...
    @staticmethod
    def shot_neighborhood_ids(arg0: opensfm.pymap.Map, arg1: str, arg2: int, arg3: int, arg4: int) -> Tuple[Set[str], Set[str]]: ...
def add_connections(arg0: opensfm.pymap.TracksManager, arg1: str, arg2: List[str]) -> None:...
def count_tracks_per_shot(arg0: opensfm.pymap.TracksManager, arg1: List[str], arg2: List[str]) -> Dict[str, int]:...
def realign_maps(arg0: opensfm.pymap.Map, arg1: opensfm.pymap.Map, arg2: bool) -> None:...
def remove_connections(arg0: opensfm.pymap.TracksManager, arg1: str, arg2: List[str]) -> None:...
