#!/usr/bin/env python3
"""Local validation server only; not deployed or required in production."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse
ROOT = Path(__file__).resolve().parents[1] / 'public'
class Handler(SimpleHTTPRequestHandler):
    def __init__(self,*a,**kw):super().__init__(*a,directory=str(ROOT),**kw)
    def translate_path(self,path):
        p=unquote(urlparse(path).path)
        if p=='/':p='/index.html'
        elif not Path(p).suffix and (ROOT/(p.lstrip('/')+'.html')).is_file():p+='.html'
        return super().translate_path(p)
    def list_directory(self,path):self.send_error(404);return None
ThreadingHTTPServer(('127.0.0.1',8765),Handler).serve_forever()
