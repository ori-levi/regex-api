import re
from abc import ABCMeta, abstractmethod
from typing import Pattern, Optional, Tuple, Dict, Any

import falcon


class _BaseAPI(metaclass=ABCMeta):

    def on_post(self, request: falcon.Request, response: falcon.Response):
        pattern, text = self.__extract_from_request(request)

        response.media = self._do_regex_magic(pattern, text, **request.media)

    @abstractmethod
    def _do_regex_magic(self, pattern: Pattern, text: str, **kwargs) -> Dict[str, Any]:
        pass

    @staticmethod
    def __extract_from_request(request: falcon.Request) -> Optional[Tuple[Pattern, str]]:
        try:
            text = request.media.pop('text')
            pattern = re.compile(request.media.pop('pattern'))

            return pattern, text
        except Exception as ex:
            raise falcon.HTTPBadRequest(description=str(ex))
