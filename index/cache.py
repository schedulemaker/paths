def exports():
    local = locals()
    globa = globals()

    if 'Day' not in local and 'Day' not in globa:
        from day import Day
    if 'Week' not in local and 'Week' not in globa:
        from week import Week
    if 'requests' not in local and 'requests' not in globa:
        import requests
    if 'json' not in local and 'json' not in globa:
        import json
    if 'asyncio' not in local and 'asyncio' not in globa:
        import asyncio
    if 'os' not in local and 'os' not in globa:
        import os

    return Day, Week, requests, json, asyncio, os