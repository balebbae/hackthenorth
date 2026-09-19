"""Allow backend redirects without forwarding the shared key to another origin."""
import httpx


def check_redirect(response):
    if response.has_redirect_location:
        source = response.request.url
        target = source.join(response.headers['location'])
        if (source.scheme, source.host, source.port) != (target.scheme, target.host, target.port):
            raise httpx.RequestError('Backend redirect to another origin was refused.', request=response.request)


async def check_redirect_async(response):
    check_redirect(response)
