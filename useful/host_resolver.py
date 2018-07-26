import socket

class HostResolver(object):
    """ callable class which cache hostname with ip"""
    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        """
        if host is not in cache and host ip is available, add it to cache
        if host is not in cache and host ip is also not available, raise exception
        if host is available in cache return ip"""
        if not self.has_host(host):
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        """ clear cache"""
        self._cache.clear()

    def has_host(self, host):
        """ return True if host is in cache, else False"""
        return host in self._cache
