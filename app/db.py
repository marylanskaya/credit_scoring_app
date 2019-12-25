import json
from typing import Dict, Any, Union

from loguru import logger
from redis import Redis, ConnectionError


class RedisClient:

    def __init__(self, host: str = 'localhost', port: int = 6379, db=0):
        self.host = host
        self.port = port
        self.db = 0
        self._redis = Redis(host=self.host, port=self.port, db=self.db)

    def get_user(self, user_hash: str) -> Union[Dict['str', Any], None]:
        try:
            dump = self._redis.get(user_hash)
        except ConnectionError as e:
            logger.error("Lost connection to redis")
            raise e

        if dump:
            return json.loads(dump)

    def add_user(self, user_hash: str, userinfo: Dict[str, Any]):
        dump = json.dumps(obj=userinfo, ensure_ascii=False)
        try:
            self._redis.set(user_hash, dump)
        except ConnectionError as e:
            logger.error("Lost connection to redis")
            raise e


REDIS_CLIENT = RedisClient()
