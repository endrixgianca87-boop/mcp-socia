import os
import httpx
import tempfile
from mcp.server.fastmcp import FastMCP
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

mcp = FastMCP("Social Giancani", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

PAGE_ID = "100940576228423"
IG_USER_ID = "17841446465749906"
PAGE_ACCESS_TOKEN = "EAAT94kbwbaUBTM3jtlQyZae2af8Fm5LQ0Ptfx3tAsEBRYh0UXnNV6j3ZAPQXan"

GRAPH_BASE = "https://" + "graph.facebook.com/v19.0"

@mcp.tool()
async def publish_facebook_post(message: str) -> str:
    url = f"{GRAPH_BASE}/{PAGE_ID}/feed"
    payload = {"message": message, "access_token": PAGE_ACCESS_TOKEN}
    async with httpx.AsyncClient() as client:
        res = await client.post(url, data=payload)
        return str(res.json())

@mcp.tool()
async def publish_instagram_photo(image_url: str, caption: str) -> str:
    url_media = f"{GRAPH_BASE}/{IG_USER_ID}/media"
    payload_media = {"image_url": image_url, "caption": caption, "access_token": PAGE_ACCESS_TOKEN}
    async with httpx.AsyncClient() as client:
        res_media = await client.post(url_media, data=payload_media)
        media_id = res_media.json().get("id")
        if not media_id:
            return f"Errore creazione container IG: {res_media.json()}"
        
        url_publish = f"{GRAPH_BASE}/{IG_USER_ID}/media_publish"
        payload_publish = {"creation_id": media_id, "access_token": PAGE_ACCESS_TOKEN}
        res_publish = await client.post(url_publish, data=payload_publish)
        return str(res_publish.json())

@mcp.tool()
async def publish_youtube_video(video_url: str, title: str, description: str, tags: str = "Giancani Immobiliare, Real Estate, Agrigento, Favara") -> str:
    client_id = os.environ.get("YOUTUBE_CLIENT_ID")
    client_secret = os.environ.get("YOUTUBE_CLIENT_SECRET")
    refresh_token = os.environ.get("YOUTUBE_REFRESH_TOKEN")

    if not client_id or not client_secret or not refresh_token:
        return "Errore: credenziali YouTube mancanti nelle variabili d'ambiente di Render."

    token_uri = "https://" + "oauth2.googleapis.com/token"

    creds = Credentials(
        token=None,
        refresh_token=refresh_token,
        token_uri=token_uri,
        client_id=client_id,
        client_secret=client_secret,
        scopes=["https://" + "www.googleapis.com/auth/youtube.upload"]
    )

    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as tmp:
        temp_filename = tmp.name

    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            resp = aexcept Exception:
                pass

if name == "main":
    mcp.run(transport="sse")wait client.get(video_url)
            if resp.status_code != 200:
                return f"Errore scaricamento video da {video_url}: status {resp.status_code}"
            with open(temp_filename, "wb") as f:
                f.write(resp.content)

        youtube = build("youtube", "v3", credentials=creds)

        tag_list = [t.strip() for t in tags.split(",") if t.strip()]

        body = {
            "snippet": {
                "title": title,
                "description": description,
                "tags": tag_list,
                "categoryId": "22"
            },
            "status": {
                "privacyStatus": "public"
            }
        }

        media = MediaFileUpload(temp_filename, mimetype="video/mp4", resumable=True)

        request = youtube.videos().insert(
            part="snippet,status",
            body=body,
            media_body=media
        )

        response = request.execute()
        video_id = response.get("id")
        return f"Video pubblicato con successo su YouTube! ID: {video_id} - Link: 🔗 view-link.cx/c4dQA14A7oI"

    except Exception as e:
        return f"Eccezione durante il caricamento su YouTube: {str(e)}"
    finally:
        if os.path.exists(temp_filename):
            try:
                os.remove(temp_filename)
