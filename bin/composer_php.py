import sys,json

def _get_max_version(lang, versions, major=None, minor=None, patch=None):
    if major is not None:
        max_major = major
        if major not in versions[lang]:
            max_major = max(versions[lang].keys())
    else:
        max_major = max(versions[lang].keys())

    if minor is not None:
        max_minor = minor
        if minor not in versions[lang][max_major].keys():
            max_minor = max(versions[lang][max_major].keys())
    else:
        max_minor = max(versions[lang][max_major].keys())

    if patch is not None:
        max_patch = patch
        if patch not in versions[lang][max_major][max_minor]:
            max_patch = max(versions[lang][max_major][max_minor])
    else:
        max_patch = max(versions[lang][max_major][max_minor])
    return "%d.%d.%d" % (max_major, max_minor, max_patch)

if len(sys.argv) == 3:
    argv = sys.argv[1]
    lang = sys.argv[2]
else:
    argv = sys.argv[1]
    lang = None
data = json.loads(argv)
result = None
fmt = "{lang}|{composer}|{choose}|{version}"
json_data = data.get("json", data.get("lock", {}))
packages = data.get("packages", [])
list_versions = {}
for p in packages:
    name, version = p.split("-")
    if name not in list_versions:
        list_versions[name] = {}
    major, minor, patch = [int(e) for e in version.split(".")]
    if major not in list_versions[name]:
        list_versions[name][major] = {}
    if minor not in list_versions[name][major]:
        list_versions[name][major][minor] = []
    list_versions[name][major][minor].append(patch)
is_php = json_data.get("platform", {}).get("php", None)
if is_php is not None:
    if is_php.startswith("~"):
        v = is_php.lstrip("~")
        vs = v.split(".")
        if len(vs) == 2:
            v = v + ".0"
        major, minor, patch = [int(e) for e in v.split(".")]
        max_version = _get_max_version(lang, list_versions, major=major, minor=minor)
    elif is_php.startswith(">="):
        v = is_php.lstrip(">=")
        vs = v.split(".")
        if len(vs) == 2:
            v = v + ".0"
        major, minor, patch = [int(e) for e in v.split(".")]
        max_version = _get_max_version(lang, list_versions, major=major, minor=minor)
    else:
        is_phps = is_php.split(".")
        if len(is_phps) == 2:
            is_php = is_php + ".0"
        major, minor, patch = [int(e) for e in is_php.split(".")]
        max_version = _get_max_version(lang, list_versions, major=major, minor=minor, patch=patch)
    result = fmt.format(lang=lang, composer="composer.json", choose=is_php, version=max_version)
else:
    max_version = _get_max_version(lang, list_versions)
    result = fmt.format(lang=lang, composer="default", choose="*", version=max_version)
print result