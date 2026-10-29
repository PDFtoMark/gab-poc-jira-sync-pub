"""PoC stub of the `jira` package (no network, no credentials).

The real sync-jira-actions code (pinned commit) is executed verbatim; this stub
only replaces the Jira client so every Jira operation is printed.
"""

import json
import os


def _log(op, data):
    print(f"POC-JIRA-CALL {op} {json.dumps(data, sort_keys=True)}", flush=True)


class JIRAError(Exception):
    pass


class _Exceptions:
    JIRAError = JIRAError


exceptions = _Exceptions()


class _Fields:
    def __init__(self, **kw):
        self.__dict__.update(kw)


class _Issue:
    def __init__(self, key):
        self.key = key
        self.id = key
        self.fields = _Fields(
            description=os.environ.get("POC_STUB_ISSUE_DESCRIPTION", ""),
            status=os.environ.get("POC_STUB_ISSUE_STATUS", "Reviewer Approved"),
            issuetype=os.environ.get("POC_STUB_ISSUE_TYPE", "Bug"),
            labels=[],
            project=_Fields(key="DCNE"),
            components=[],
        )

    def get_field(self, name):
        return getattr(self.fields, name)

    def update(self, fields=None):
        _log("issue.update", {"key": self.key, "fields": str(fields)})


class JIRA:
    def __init__(self, *args, **kwargs):
        _log("connect", {"args": [str(a) for a in args],
                         "auth_mode": "token" if "token_auth" in kwargs else "basic"})

    def applicationlinks(self):
        return []

    def enhanced_search_issues(self, jql):
        _log("enhanced_search_issues", {"jql": jql})
        return []

    def issue(self, key):
        _log("jira.issue", {"key": key})
        return _Issue(key)

    def project(self, key, **kwargs):
        return _Fields(key=key, components=[], issueTypes=[])

    def project_components(self, project):
        return []

    def add_comment(self, key, body):
        _log("add_comment", {"key": str(key), "body": body})

    def transition_issue(self, key, transition):
        _log("transition_issue", {"key": str(key), "transition": transition})

    def remote_links(self, issue):
        return []

    def add_remote_link(self, **kwargs):
        _log("add_remote_link", {k: str(v) for k, v in kwargs.items()})

    def create_issue(self, fields):
        _log("create_issue", {"fields": str(fields)})
        return _Issue("DCNE-STUB")

    def comments(self, key):
        return []
