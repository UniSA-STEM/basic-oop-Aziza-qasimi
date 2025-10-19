"""
File: Asset.py
Description: Asset class for IntoTheGrid assignment.
Author: Aziza Qasimi
ID: 110462000
Username: QASAY006
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    def __init__(self, name, description, encrypted=False):
        self.name = name
        self.description = description
        self.encrypted = encrypted

    def __str__(self):
        status = " [Encrypted]" if self.encrypted else ""
        return f"{self.name}: {self.description}{status}"
