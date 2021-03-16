import tornado.web

from .BaseHandler import BaseHandler


class CreateGameHandler(BaseHandler, tornado.web.RequestHandler):
    def get(self) -> None:
        min_game_code = 000
        max_game_code = 999
        self.write({'result': 000})  # TODO: write logic for game code