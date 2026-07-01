# API Reference

**routingpy** exposes a small, consistent surface: one router class per provider — all
sharing the same `directions` / `isochrones` / `matrix` endpoints — plus the response
data classes they return and a common exception hierarchy.

Pick a router from the navigation, or start with the helpers below.

::: routingpy.routers.get_router_by_name

## Default options

::: routingpy.routers.options
