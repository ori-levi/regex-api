from typing import Pattern, Dict, Any

from regex._base import _BaseAPI


class SplitAPI(_BaseAPI):
    def _do_regex_magic(self, pattern: Pattern, text: str, **kwargs) -> Dict[str, Any]:
        result = pattern.split(text)
        if kwargs.get('remove_empties', False):
            result = [row for r in result if (row := r.strip())]

        return {'result': result}
