import uvicorn
from base_fast_api_package.api.api import app


if __name__ == '__main__':
    config = uvicorn.Config(app, port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
