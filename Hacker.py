"""
File: Hacker.py
Description: Hacker class for IntoTheGrid assignment.
Author: Aziza Qasimi
ID: 110462000
Username: QASAY006
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset
from Rig import Rig

class Hacker:
    def __init__(self, name):
        self.name = name
        self.inventory = [Asset("CryptoToken", "Used to acquire rigs")]
        self.rig = None
        self.trace = 0

    def __str__(self):
        rig_name = self.rig.name if self.rig else "No rig"
        inv = ", ".join([str(a) for a in self.inventory]) or "Empty"
        return f"Hacker: {self.name} | Rig: {rig_name} | Trace: {self.trace} | Inventory: {inv}"

    def find_asset(self, asset_name):
        for a in self.inventory:
            if a.name == asset_name:
                return a
        return None

    def acquire_rig(self, rig_name):
        token = self.find_asset("CryptoToken")
        if not token:
            print(f"{self.name} has no CryptoToken to acquire a rig.")
            return False
        self.inventory.remove(token)
        self.rig = Rig(rig_name)
        print(f"{self.name} activated rig: {rig_name}")
        return True

    def launch_data_spike(self, target_hacker):
        if self.trace >= 5:
            print(f"{self.name} is too exposed to launch an attack! (trace {self.trace})")
            return False
        if not self.rig:
            print(f"{self.name} has no rig to launch an attack from.")
            return False
        spike = self.rig.release_asset("Data Spike")
        if not spike:
            print(f"{self.name} has no Data Spike to launch.")
            return False
        self.trace += 1
        if target_hacker.rig:
            target_hacker.rig.take_hit()
        else:
            print(f"{target_hacker.name} has no rig to be attacked.")
        print(f"{self.name} launched a Data Spike at {target_hacker.name}. Trace now {self.trace}.")
        return True

    def extract_from_broken_rig(self, target_hacker):
        # check target rig
        if not target_hacker.rig:
            print(f"{target_hacker.name} has no rig to extract from.")
            return False
        if not target_hacker.rig.broken:
            print(f"{target_hacker.rig.name} is not broken; cannot extract.")
            return False

        # look for Removable Drive in our inventory
        drive = self.find_asset("Removable Drive")
        drive_from_inventory = False
        if drive:
            drive_from_inventory = True
        else:
            # try own rig storage (consume it there)
            if self.rig:
                for i, a in enumerate(self.rig.storage):
                    if a.name == "Removable Drive":
                        drive = self.rig.storage.pop(i)
                        drive_from_inventory = False
                        break

        if not drive:
            print(f"{self.name} has no Removable Drive to extract data.")
            return False

        if drive_from_inventory:
            self.inventory.remove(drive)

        # transfer unencrypted assets
        transferred = []
        remaining = []
        for a in target_hacker.rig.storage:
            if a.encrypted:
                remaining.append(a)
            else:
                transferred.append(a)
        target_hacker.rig.storage = remaining

        if transferred:
            self.inventory.extend(transferred)
            print(f"{self.name} extracted {len(transferred)} asset(s) from {target_hacker.rig.name}.")
        else:
            print(f"{target_hacker.rig.name} had no unencrypted assets to extract.")
        return True

    def encrypt_asset(self, asset_name):
        chip = self.find_asset("Security Chip")
        if not chip:
            print(f"{self.name} lacks a Security Chip to encrypt {asset_name}.")
            return False
        for a in self.inventory:
            if a.name == asset_name:
                a.encrypted = True
                self.inventory.remove(chip)
                print(f"{asset_name} encrypted in {self.name}'s inventory.")
                return True
        if self.rig:
            for a in self.rig.storage:
                if a.name == asset_name:
                    a.encrypted = True
                    self.inventory.remove(chip)
                    print(f"{asset_name} encrypted in {self.rig.name} storage.")
                    return True
        print(f"{asset_name} not found to encrypt.")
        return False

    def decrypt_asset(self, asset_name):
        chip = self.find_asset("Security Chip")
        if not chip:
            print(f"{self.name} lacks a Security Chip to decrypt {asset_name}.")
            return False
        for a in self.inventory:
            if a.name == asset_name and a.encrypted:
                a.encrypted = False
                self.inventory.remove(chip)
                print(f"{asset_name} decrypted in inventory.")
                return True
        if self.rig:
            for a in self.rig.storage:
                if a.name == asset_name and a.encrypted:
                    a.encrypted = False
                    self.inventory.remove(chip)
                    print(f"{asset_name} decrypted in rig storage.")
                    return True
        print(f"{asset_name} not found or not encrypted.")
        return False

    def upgrade_rig(self):
        if not self.rig:
            print(f"{self.name} has no rig to upgrade.")
            return False
        patch = self.find_asset("Hardware Patch")
        if not patch:
            print(f"{self.name} lacks a Hardware Patch to upgrade the rig.")
            return False
        self.inventory.remove(patch)
        self.rig.upgrade(self)
        return True

    def store_to_rig(self, asset_name):
        if not self.rig:
            print(f"{self.name} has no rig to store assets.")
            return False
        asset = self.find_asset(asset_name)
        if not asset:
            print(f"{asset_name} not found in inventory.")
            return False
        self.inventory.remove(asset)
        self.rig.store_asset(asset)
        print(f"{asset_name} stored into {self.rig.name}.")
        return True

    def retrieve_from_rig(self, asset_name):
        if not self.rig:
            print(f"{self.name} has no rig to retrieve assets from.")
            return False
        asset = self.rig.release_asset(asset_name)
        if not asset:
            print(f"{asset_name} not available for retrieval (not found or encrypted).")
            return False
        self.inventory.append(asset)
        print(f"{asset_name} retrieved from {self.rig.name}.")
        return True
