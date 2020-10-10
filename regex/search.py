from typing import Pattern, Dict, Any

from regex._base import _BaseAPI


class SearchAPI(_BaseAPI):
    def _do_regex_magic(self, pattern: Pattern, text: str, **kwargs) -> Dict[str, Any]:
        result = pattern.search(text)
        if result is None:
            return {}

        return {
            'group_dict': result.groupdict(),
            'groups': result.groups()
        }
