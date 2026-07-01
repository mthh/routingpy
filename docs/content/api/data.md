# Data classes

::: routingpy.direction.Directions
    options:
      members: [raw]

::: routingpy.direction.Direction
    options:
      members: [geometry, duration, distance, km, mi]

::: routingpy.isochrone.Isochrones
    options:
      members: [raw]

::: routingpy.isochrone.Isochrone
    options:
      members: [geometry, center, range]

::: routingpy.matrix.Matrix
    options:
      members: [durations, distances, raw]

::: routingpy.expansion.Expansions
    options:
      members: [expansions, center, raw]

::: routingpy.expansion.Edge
    options:
      members: [geometry, distance, duration, cost, edge_id, status]

::: routingpy.optimized.OptimizedDirection
    options:
      members: [geometry, duration, distance, km, mi, original_index]

::: routingpy.utils.decode_polyline5

::: routingpy.utils.decode_polyline6
