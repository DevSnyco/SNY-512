import json

from typing import Optional
from pathlib import Path

class User:
	def __init__(
			self,
			asterisk: str,
			username: str,
			session_token: Optional[str],
			direct_connection: Optional[bool] = False
		):
		self.asterisk = asterisk
		self.username = username
		self.session_token = session_token
		self.direct_connection = direct_connection

	def fetch_local(self):
		user_data: dict | None = json.load(open("./resources/user_data.json")) if Path("./resources/user_data.json").is_file() else None
		self.asterisk: str | None = user_data.get("asterisk")
		self.username: str | None = user_data.get("username")
		self.direct_connection: str | None = user_data.get("direct_connection")

	def offload_json(self) -> None:
		json.dump(
			{
				"asterisk": self.asterisk,
				"username": self.username,
				"direct_connection": self.direct_connection
			},
			open("./resources/user_data.json", "w", encoding = "utf-8"),
			ensure_ascii = False,
			indent = 4
		)