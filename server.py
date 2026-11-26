import os
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Social Giancani", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

PAGE_ID = "100940576228423"
IG_USER_ID = "17841446465749906"
PAGE_ACCESS_TOKEN = "EAAT94kbwbaUBTM3jtlQyZae2af8Fm5LQ0Ptfx3tAsEBRYh0UXnNV6j3ZAPQXan"

@mcp.tool()
async def publish_facebook_post(message: str) -> str:
    url = f"🔗 view-link.cx/UVd4zFsPy9h"
    payload = {"message": message, "access_token": PAGE_ACCESS_TOKEN}
    async with httpx.AsyncClient() as client:
        res = await client.post(url, data=payload)
        return str(res.json())

@mcp.tool()
async def publish_instagram_photo(image_url: str, caption: str) -> str:
    url_media = f"🔗 view-link.cx/BAaPJf1WdMH"
    payload_media = {"image_url": image_url, "caption": caption, "access_token": PAGE_ACCESS_TOKEN}
    async with httpx.AsyncClient() as client:
        res_media = await client.post(url_media, data=payload_media)
        media_id = res_media.json().get("id")
        if not media_id:
            return f"Errore creazione container IG: {res_media.json()}"
        
           
        url_publish = f"🔗 view-link.cx/Uq3IY4SExKK"
        payload_publish = {"creation_id": media_id, "access_token": PAGE_ACCESS_TOKEN}
        res_publish = await client.post(url_publish, data=payload_publish)
        return str(res_publish.json())

mcp.run(transport="sse")

import os
import asyncio
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Social Giancani", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

PAGE_ID = "100940576228423"
IG_USER_ID = "17841446465749906"
PAGE_ACCESS_TOKEN = "EAAT94kbwbaUBTM3jtlQyZae2af8Fm5LQ0Ptfx3tAsEBRYh0UXnNV6j3ZAPQXan"

@mcp.tool()
async def publish_facebook_post(message: str) -> str:
    url = f"🔗 view-link.cx/rbpMRGckjLL"
    payload = {"message": message, "access_token": PAGE_ACCESS_TOKEN}
    async with httpx.AsyncClient() as client:
        res = await client.post(url, data=payload)
        return str(res.json())

@mcp.tool()
async def publish_facebook_video(video_url: str, description: str = "") -> str:
    url = f"🔗 view-link.cx/SZ20qn8WhDj"
    payload = {"file_url": video_url, "description": description, "access_token": PAGE_ACCESS_TOKEN}
    async with httpx.AsyncClient(timeout=60.0) as client:
        res = await client.post(url, data=payload)
        return str(res.json())

@mcp.tool()
async def publish_instagram_photo(image_url: str, caption: str) -> str:
    url_media = f"🔗 view-link.cx/NoJx12qe9yp"
    payload_media = {"image_url": image_url, "caption": caption, "access_token": PAGE_ACCESS_TOKEN}
    async with httpx.AsyncClient() as client:
        res_media = awaitclient.post(url_media, data=payload_media)
        media_id = res_media.json().get("id")
        if not media_id:
            return f"Errore creazione container IG: {res_media.json()}"
        
        url_publish = f"🔗 view-link.cx/mJZIlVrFHvf"
        payload_publish = {"creation_id": media_id, "access_token": PAGE_ACCESS_TOKEN}
        res_publish = await client.post(url_publish, data=payload_publish)
        return str(res_publish.json())

@mcp.tool()
async def publish_instagram_reel(video_url: str, caption: str) -> str:
    url_media = f"🔗 view-link.cx/1HhUtIiAvhZ"
    payload_media = {
        "media_type": "REELS",
        "video_url": video_url,
        "caption": caption,
        "access_token": PAGE_ACCESS_TOKEN
    }
    async with httpx.AsyncClient(timeout=60.0) as client:
        res_media = await client.post(url_media, data=payload_media)
        media_id = res_media.json().get("id")
        if not media_id:
            return f"Errore container Reel IG: {res_media.json()}"
Attesa elaborazione video da parte dei server Meta
        await asyncio.sleep(10)
        
        url_publish = f"🔗 view-link.cx/OKgjmZGDoIM"
        payload_publish = {"creation_id": media_id, "access_token": PAGE_ACCESS_TOKEN}
        res_publish = await client.post(url_publish, data=payload_publish)
        return str(res_publish.json())

@mcp.tool()
async def publish_instagram_story(media_url: str, is_video: bool = False) -> str:
    url_media = f"🔗 view-link.cx/yLIP6fJBmBo"
    payload_media = {
        "media_type": "STORIES",
        "access_token": PAGE_ACCESS_TOKEN
    }
    if is_video:
        payload_media["video_url"] = media_url
    else:
        payload_media["image_url"] = media_url
        
    async with httpx.AsyncClient(timeout=60.0) as client:
        res_media = await client.post(url_media, data=payload_media)
        media_id = res_media.json().get("id")
        if not media_id:
            return f"Errore container Storia IG: {res_media.json()}"
        
        if is_video:
            await asyncio.sleep(10)
            
        url_publish = f"🔗 view-link.cx/UhOnnAdSDab"
        payload_publish = {"creation_id": media_id, "access_token": PAGE_ACCESS_TOKEN}
        res_publish = await client.post(url_publish, data=payload_publish)
        return str(res_publish.json())

mcp.run(transport="sse")
