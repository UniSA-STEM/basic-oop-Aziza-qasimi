"""
File: Rig.py
Description: Rig class for IntoTheGrid assignment.
Author: Aziza Qasimi
ID: 110462000
Username: Aziza Qasimi
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset

class Rig:
    def __init__(self, name):
        self.name = name
        self.damage = 0
        self.broken = False
        self.upgrade_level = 0
        # start with two Data Spikes and one Removable Drive
        self.storage = [
            Asset("Data Spike", "Used in battles"),
            Asset("Data Spike", "Used in battles"),
            Asset("Removable Drive", "Used for extraction")
        ]

    def __str__(self):
        assets = ", ".join([str(a) for a in self.storage]) or "Empty"
        return f"Rig: {self.name} | {self.get_condition()} | Assets: {assets}"

    def get_condition(self):
        if self.broken:
            return f"Broken (Level {self.upgrade_level})"
        if self.damage == 0:
            return f"Pristine (Level {self.upgrade_level})"
        threshold = 2 + self.upgrade_level
        return f"Damaged {self.damage}/{threshold} (Level {self.upgrade_level})"

    def take_hit(self):
        if self.broken:
            print(f"{self.name} is already broken; further hits do nothing.")
            return
        self.damage += 1
        threshold = 2 + self.upgrade_level
        print(f"{self.name} took a hit. Damage {self.damage}/{threshold}.")
        if self.damage >= threshold:
            self.broken = True
            print(f"{self.name} is now broken!")

    def repair(self, hacker):
        if self.damage == 0 and not self.broken:
            print(f"{self.name} does not need repair.")
            return False
        token = hacker.find_asset("CryptoToken")
        if not token:
            print(f"{hacker.name} has no CryptoToken to repair {self.name}.")
            return False
        hacker.inventory.remove(token)
        self.damage = 0
        self.broken = False
        print(f"{self.name} repaired successfully using a CryptoToken.")
        return True

    def upgrade(self, hacker):
        patch = hacker.find_asset("Hardware Patch")
        if not patch:
            print(f"{hacker.name} has no Hardware Patch to upgrade {self.name}.")
            return False
        hacker.inventory.remove(patch)
        self.upgrade_level += 1
        print(f"{self.name} upgraded to level {self.upgrade_level}!")
        return True

    def generate_asset(self):
        import random
        choices = [
            Asset("CryptoToken", "Digital currency token"),
            Asset("Security Chip", "Used to encrypt/decrypt assets"),
            Asset("Hardware Patch", "Used to upgrade rigs"),
            Asset("Data Fragment", "Random data fragment")
        ]
        new_asset = random.choice(choices)
        self.storage.append(new_asset)
        print(f"{self.name} generated asset: {new_asset}")
        return new_asset

    def store_asset(self, asset):
        self.storage.append(asset)
        print(f"{asset.name} stored into {self.name}.")

    def release_asset(self, asset_name):
        for i, a in enumerate(self.storage):
            if a.name == asset_name:
                if a.encrypted:
                    print(f"Cannot release {a.name}: it is encrypted.")
                    return None
                return self.storage.pop(i)
        return None
