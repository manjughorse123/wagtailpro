# from wagtail.api.v2.endpoints import PagesAPIEndpoint
# from wagtail.api.v2.router import WagtailAPIRouter
# from wagtail.images.api.v2.endpoints import ImagesAPIEndpoint
# from wagtail.documents.api.v2.endpoints import DocumentsAPIEndpoint

# # Init the Wagtail Router
# api_router = WagtailAPIRouter('wagtailapi')

# # Register 3 API endpoints: Pages, Images and Documents
# api_router.register_endpoint('pages', PagesAPIEndpoint)
# api_router.register_endpoint('images', ImagesAPIEndpoint)
# api_router.register_endpoint('documents', DocumentsAPIEndpoint)

from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet

# Create the router. "wagtailapi" is the URL namespace
api_router = WagtailAPIRouter('wagtailapi')

# Add the three endpoints using the "register_endpoint" method.
# The first parameter is the name of the endpoint (eg. pages, images). This
# is used in the URL of the endpoint
# The second parameter is the endpoint class that handles the requests
api_router.register_endpoint('pages', PagesAPIViewSet)
api_router.register_endpoint('images', ImagesAPIViewSet)
api_router.register_endpoint('documents', DocumentsAPIViewSet)