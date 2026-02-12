# -*- coding: utf-8 -*-
# Copyright (C) 2021 GIS OPS UG
#
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
#

import json
import warnings
from typing import List, Optional, Tuple, Union  # noqa: F401

from .. import convert, utils
from ..client_base import DEFAULT
from ..client_default import Client
from ..direction import Direction
from ..isochrone import Isochrone, Isochrones


class IGN:
    """Performs requests to the IGN Geoportail "itineraire" geoservices"""

    _DEFAULT_BASE_URL = "https://data.geopf.fr/navigation"

    def __init__(
        self,
        base_url: Optional[str] = _DEFAULT_BASE_URL,
        user_agent: Optional[str] = None,
        timeout: Optional[int] = DEFAULT,
        retry_timeout: Optional[int] = None,
        retry_over_query_limit: Optional[bool] = False,
        skip_api_error: Optional[bool] = None,
        client=Client,
        **client_kwargs,
    ):
        """
        Initializes an IGN client.

        :param base_url: The base URL for the request. Defaults to the official address
            instance for "car". Should not have a trailing slash.

        :param user_agent: User Agent to be used when requesting.
            Default :attr:`routingpy.routers.options.default_user_agent`.

        :param timeout: Combined connect and read timeout for HTTP requests, in
            seconds. Specify ``None`` for no timeout. Default :attr:`routingpy.routers.options.default_timeout`.

        :param retry_timeout: Timeout across multiple retriable requests, in
            seconds.  Default :attr:`routingpy.routers.options.default_retry_timeout`.

        :param retry_over_query_limit: If True, client will not raise an exception
            on HTTP 429, but instead jitter a sleeping timer to pause between
            requests until HTTP 200 or retry_timeout is reached.
            Default :attr:`routingpy.routers.options.default_retry_over_query_limit`.

        :param skip_api_error: Continue with batch processing if a :class:`routingpy.exceptions.RouterApiError` is
            encountered (e.g. no route found). If False, processing will discontinue and raise an error.
            Default :attr:`routingpy.routers.options.default_skip_api_error`.

        :param client: A client class for request handling. Needs to be derived from :class:`routingpy.client_base.BaseClient`

        :param client_kwargs: Additional arguments passed to the client, such as headers or proxies.
        """

        self.client = client(
            base_url,
            user_agent,
            timeout,
            retry_timeout,
            retry_over_query_limit,
            skip_api_error,
            **client_kwargs,
        )

    def directions(
        self,
        locations: List[List[float]] = [],
        profile: Optional[str] = "car",
        resource: str = "bdtopo-osrm",
        optimization: Optional[str] = None,
        geometry_format: Optional[str] = None,
        constraints: Optional[Union[str, dict, List[str]]] = None,
        getSteps: Optional[bool] = None,
        getBbox: Optional[bool] = None,
        crs: Optional[str] = None,
        waysAttributes: Optional[List[str]] = None,
        dry_run: Optional[bool] = None,
        **direction_kwargs,
    ):
        """
        Get directions between an origin point and a destination point.

        For more information, visit https://www.geoportail.gouv.fr/depot/swagger/itineraire.html

        Use ``direction_kwargs`` for any missing ``directions`` request options.

        :param locations: The coordinates tuple the route should be calculated
            from in order of visit.

        :param profile: Optionally specifies the mode of transport to use when calculating
            directions. Should be "car" (default) or "pedestrian";
            resource "bdtopo-osrm" also supports "exceptionnal".

        :param resource: The routing resource to use. Should be one of
            "bdtopo-osrm", "bdtopo-pgr", "bdtopo-valhalla"

        :param optimization: Optimization mode used to compute the route
            "fastest" (default) or "shortest".

        :param geometry_format: Format of returned geometries.
            One of "geojson" (default) or "polyline"

        :param constraints: Route constraints. May be a JSON-serializable object or a pre-serialized string.

        :param getSteps: Include step-by-step instructions. Defaults to "true".

        :param getBbox: Include route bounding box in the response. Defaults to "true".

        :param crs: Coordinate reference system for returned geometries.
            Default is "EPSG:4326" (WGS84 : latitude/longitude),
            other options depend on resource used.

        :param dry_run: Print URL and parameters without sending the request.

        :param direction_kwargs: any additional keyword arguments which will override parameters

        :returns: A route from provided coordinates and restrictions.
        :rtype: :class:`routingpy.direction.Direction`
        """

        params = self.get_direction_params(
            locations,
            profile,
            resource,
            optimization,
            geometry_format,
            constraints,
            getSteps,
            getBbox,
            crs,
            waysAttributes,
            **direction_kwargs,
        )

        return self.parse_direction_json(
            self.client._request("/itineraire", get_params=params, dry_run=dry_run),
            geometry_format=geometry_format,
        )

    @staticmethod
    def get_direction_params(
        locations: List[List[float]],
        profile: Optional[str] = "car",
        resource: str = "bdtopo-osrm",
        optimization: Optional[str] = None,
        geometry_format: Optional[str] = None,
        constraints: Optional[Union[str, dict, List[str]]] = None,
        getSteps: Optional[bool] = None,
        getBbox: Optional[bool] = None,
        crs: Optional[str] = None,
        waysAttributes: Optional[List[str]] = None,
        **direction_kwargs,
    ):
        """
        Builds and returns the router's route parameters. It's a separate function so that
        bindings can use routingpy's functionality. See documentation of .directions().
        """

        params = dict()

        if isinstance(locations, list) and len(locations) >= 2:
            start = locations[0]
            end = locations[-1]
            intermediates = locations[1:-1] if len(locations) > 2 else None
        else:
            raise ValueError("locations parameter must be a list of at least two coordinate pairs")

        def format_coord(arg):
            """Formats a coordinate pair as "lon,lat" string."""
            return convert.delimit_list([convert.format_float(f) for f in arg])

        params["start"] = format_coord(start)
        params["end"] = format_coord(end)

        if intermediates:
            formatted = convert.delimit_list([format_coord(i) for i in intermediates], "|")
            params["intermediates"] = formatted

        if not resource:
            raise ValueError("resource parameter is required for IGN directions")
        params["resource"] = resource

        if profile is not None:
            params["profile"] = profile

        if optimization is not None:
            params["optimization"] = optimization

        if geometry_format is not None:
            params["geometryFormat"] = geometry_format

        if constraints is not None:
            # constraints can be provided as JSON/dict or as pre-serialized string
            if isinstance(constraints, (dict, list)):
                params["constraints"] = json.dumps(constraints)
            else:
                params["constraints"] = str(constraints)

        if getSteps is not None:
            params["getSteps"] = convert.convert_bool(getSteps)

        if getBbox is not None:
            params["getBbox"] = convert.convert_bool(getBbox)

        params["distanceUnit"] = "meter"
        params["timeUnit"] = "second"

        if crs is not None:
            params["crs"] = crs

        if waysAttributes:
            params["waysAttributes"] = convert.delimit_list(waysAttributes, ",")

        params = utils.deep_merge_dicts(params, direction_kwargs)

        return params

    @classmethod
    def parse_geometry(cls, geometry, geometry_format):
        if geometry is None:
            return None
        coo = None
        if geometry_format == "geojson" or geometry_format is None:
            coo = geometry.get("coordinates")
        elif geometry_format == "polyline":
            coo = utils.decode_polyline5(geometry, is3d=False)
        return coo

    @staticmethod
    def parse_direction_json(response, geometry_format):
        if response is None or not isinstance(response, dict):  # pragma: no cover
            return Direction()

        def key_to_int(key):
            val = response.get(key)
            if val is not None:
                return int(val)
            return None

        geometry = IGN.parse_geometry(response.get("geometry"), geometry_format)

        return Direction(
            geometry=geometry,
            duration=key_to_int("duration"),
            distance=key_to_int("distance"),
            raw=response,
        )

    def isochrones(
        self,
        locations: List[float],
        intervals: Union[List[int], Tuple[int], int],
        interval_type: Optional[str] = "time",
        profile: Optional[str] = "car",
        resource: Optional[str] = "bdtopo-valhalla",
        direction: Optional[str] = None,
        constraints: Optional[Union[str, dict, List[str]]] = None,
        geometry_format: Optional[str] = None,
        crs: Optional[str] = None,
        dry_run: Optional[bool] = None,
    ):
        """
        Get isochrone (or equidistant) around a location using the IGN Geoportail isochrone service,
        see https://www.geoportail.gouv.fr/depot/swagger/itineraire.html#/Utilisation/isochrone

        This method calls the IGN "isochrone" operation of the itineraire API and returns polygonal
        contour for the requested interval. Consult the service's GetCapabilities for valid values
        for `resource`, `profile`, and other provider-specific options.

        :param locations: One pair of lng/lat values, expressed in the resource CRS.
        :type locations: [float, float]

        :param intervals: Integer range for which to compute isochrone/equidistant. Value represents
            seconds when ``interval_type`` is "time", or meters when ``interval_type`` is "distance".
            Note that only one contour can be calculated by the API. For compatibility reasons, it
            is possible to pass this value in a list or tuple, or as a single integer.
            If multiple values are passed, only the first one will be used.
        :type intervals: int

        :param interval_type: Type of the provided ranges: "time" for isochrones (default) or "distance"
            for equidistants.
        :type interval_type: str

        :param profile: see distance method for details. Default "car".
        :type profile: str

        :param resource: one of "bdtopo-valhalla" (default), "bdtopo-pgr".
            Note: "bdtopo-osrm" does not support isochrones.

        :param direction: Directionality of the calculation. Should be "departure" (defaults,
            gives potential arrival points) or "arrival" (gives potential starting points).
        :type direction: str

        :param constraints: see `distance` method documentation.

        :param geometry_format: see `distance` method documentation.

        :param crs: see `distance` method documentation.

        :param dry_run: Print URL and parameters without sending the request.
        :param dry_run: bool

        :returns: An isochrone with the specified range.
        :rtype: :class:`routingpy.isochrone.Isochrones`

        :raises ValueError: If required parameters are missing or malformed (for example, if ``locations`` is not a
            valid coordinate pair or if ``intervals`` is empty).
        """

        params = self.get_isochrone_params(
            locations=locations,
            intervals=intervals,
            interval_type=interval_type,
            profile=profile,
            resource=resource,
            direction=direction,
            constraints=constraints,
            geometry_format=geometry_format,
            crs=crs,
        )

        return self.parse_isochrone_json(
            self.client._request("/isochrone", get_params=params, dry_run=dry_run),
            geometry_format=geometry_format,
        )

    @staticmethod
    def get_isochrone_params(
        locations: List[float],
        intervals: Union[List[int], Tuple[int], int],
        interval_type: Optional[str] = "time",
        profile: Optional[str] = "car",
        resource: Optional[str] = "bdtopo-valhalla",
        direction: Optional[str] = None,
        constraints: Optional[Union[str, dict, List[str]]] = None,
        geometry_format: Optional[str] = None,
        crs: Optional[str] = None,
    ):
        # Validate and format inputs
        if convert.is_list(intervals) and len(intervals) != 0:
            if len(intervals) > 1:
                warnings.warn(
                    "Only the first value of the intervals list/tuple "
                    "is used by the IGN isochrone service.",
                    UserWarning,
                )
            intervals = intervals[0]

        if not isinstance(intervals, int):
            raise ValueError("Intervals parameter must be an integer or list-like of integers")

        if len(locations) != 2:
            raise ValueError("locations must be a coordinate pair [lng, lat]")

        location_formatted = convert.delimit_list(
            [convert.format_float(locations[0]), convert.format_float(locations[1])]
        )
        params = {
            "point": location_formatted,
            "profile": profile,
            "costValue": intervals,
            "costType": interval_type,
            "resource": resource,
        }

        # map direction argument to the service's location_type parameter
        if direction:
            params["location_type"] = direction

        if constraints is not None:
            if isinstance(constraints, (dict, list)):
                params["constraints"] = json.dumps(constraints)
            else:
                params["constraints"] = str(constraints)

        if geometry_format is not None:
            params["geometryFormat"] = geometry_format

        if crs is not None:
            params["crs"] = crs

        return params

    @staticmethod
    def parse_isochrone_json(response, geometry_format):
        if response is None:  # pragma: no cover
            return Isochrones()

        geometry = IGN.parse_geometry(response.get("geometry"), geometry_format)
        center = [float(coo) for coo in response.get("point").split(",")]
        isochrone = Isochrone(
            geometry=geometry,
            interval=response.get("costValue"),
            center=center,
            interval_type=response.get("costType"),
        )
        return Isochrones([isochrone], raw=response)

    def matrix(self):  # pragma: no cover
        raise NotImplementedError
