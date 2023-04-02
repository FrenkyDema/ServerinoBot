from logging import Logger

from pyngrok import ngrok

from src.config.config_module import NGROK_TOKEN


class Ngrok:

    def __init__(self, logger: Logger):
        self.logger = logger
        self.url_tunnel: str = ""

    # Function to start the Ngrok tunnel
    def start_tunnel(self, port):
        try:
            # Connect to the tunnel on the specified port
            ngrok.set_auth_token(NGROK_TOKEN)
            tunnel = ngrok.connect(port, "tcp")
            self.url_tunnel = tunnel.public_url.split("tcp://")[1]
            self.logger.info(f"Ngrok tunnel created at {self.url_tunnel}")

        except Exception as e:
            self.logger.error(f"Error creating Ngrok tunnel: {e}")
