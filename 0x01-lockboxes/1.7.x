Exception:
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/pip/basecommand.py", line 122, in main
    status = self.run(options, args)
  File "/usr/lib/python3/dist-packages/pip/commands/install.py", line 257, in run
    InstallRequirement.from_line(name, None))
  File "/usr/lib/python3/dist-packages/pip/req.py", line 173, in from_line
    return cls(req, comes_from, url=url, prereleases=prereleases)
  File "/usr/lib/python3/dist-packages/pip/req.py", line 71, in __init__
    req = pkg_resources.Requirement.parse(req)
  File "/usr/lib/python3/dist-packages/pkg_resources.py", line 2667, in parse
    reqs = list(parse_requirements(s))
  File "/usr/lib/python3/dist-packages/pkg_resources.py", line 2605, in parse_requirements
    line, p, specs = scan_list(VERSION,LINE_END,line,p,(1,2),"version spec")
  File "/usr/lib/python3/dist-packages/pkg_resources.py", line 2573, in scan_list
    raise ValueError("Expected "+item_name+" in",line,"at",line[p:])
ValueError: ('Expected version spec in', 'pycodestyle=', 'at', '=')

Storing debug log for failure in /root/.pip/pip.log
