from typing import Pattern, Dict, Any

from regex._base import _BaseAPI


class FindAllAPI(_BaseAPI):
    def _do_regex_magic(self, pattern: Pattern, text: str, **kwargs) -> Dict[str, Any]:
        result = pattern.findall(text)
        return {'result': result}


# Pattern.finditer(string[, pos[, endpos]])
# Similar to the finditer() function, using the compiled pattern, but also accepts optional pos and endpos parameters that limit the search region like for search().
#
# Pattern.sub(repl, string, count=0)
# Identical to the sub() function, using the compiled pattern.
#
# Pattern.subn(repl, string, count=0)
# Identical to the subn() function, using the compiled pattern.
#
# Pattern.flags
# The regex matching flags. This is a combination of the flags given to compile(), any (?...) inline flags in the pattern, and implicit flags such as UNICODE if the pattern is a Unicode string.
#
# Pattern.groups
# The number of capturing groups in the pattern.
#
# Pattern.groupindex
# A dictionary mapping any symbolic group names defined by (?P<id>) to group numbers. The dictionary is empty if no symbolic groups were used in the pattern.
#
# Pattern.pattern
# The pattern string from which the pattern object was compiled.
#
# Changed in version 3.7: Added support of copy.copy() and copy.deepcopy(). Compiled regular expression objects are considered atomic.
