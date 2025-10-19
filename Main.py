"""
File: main.py
Description: Runs tests for the IntoTheGrid assignment.
Author: Aziza Qasimi
ID: 110462000
Username: QASAY006
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker
from Asset import Asset
import random
random.seed(0)

def test_acquire_rig_edge_case():
    print("\n--- Test 1: Acquire rig without CryptoToken (edge case) ---")
    h = Hacker("NoTokens")
    token = h.find_asset("CryptoToken")
    if token:
        h.inventory.remove(token)
    h.acquire_rig("NoRig-1")
    print(h)

def test_acquire_rig_success():
    print("\n--- Test 2: Acquire rig with CryptoToken (happy path) ---")
    h = Hacker("ReadyRigger")
    h.acquire_rig("ReadyRig-01")
    print(h.rig)
    print(h)

def test_data_spike_and_break():
    print("\n--- Test 3: Data Spike battle and breaking a rig ---")
    attacker = Hacker("Attacker")
    defender = Hacker("Defender")
    attacker.acquire_rig("AttackerRig")
    defender.acquire_rig("DefenderRig")
    attacker.launch_data_spike(defender)
    attacker.launch_data_spike(defender)
    print(defender.rig)

def test_extract_from_broken_rig():
    print("\n--- Test 4: Extract from broken rig using Removable Drive ---")
    ex = Hacker("Extractor")
    victim = Hacker("Victim")
    ex.acquire_rig("ExtractorRig")
    victim.acquire_rig("VictimRig")
    victim.rig.storage.append(Asset("Data Fragment", "Valuable Data"))
    victim.rig.broken = True
    ex.extract_from_broken_rig(victim)
    print(f"Extractor inventory now: {', '.join([str(a) for a in ex.inventory])}")

def test_encrypt_decrypt_flow():
    print("\n--- Test 5: Encrypt and decrypt asset flow ---")
    user = Hacker("Encryptor")
    user.acquire_rig("EncryptorRig")
    user.inventory.append(Asset("Security Chip", "Used to encrypt/decrypt data"))
    user.inventory.append(Asset("Data Fragment", "Sensitive info"))
    print("Before encryption:", user)
    user.encrypt_asset("Data Fragment")
    print("After encryption:", user)
    user.inventory.append(Asset("Security Chip", "Used to encrypt/decrypt data"))
    user.decrypt_asset("Data Fragment")
    print("After decryption:", user)

def test_upgrade_and_repair():
    print("\n--- Test 6: Upgrade rig and repair ---")
    u = Hacker("Upgrader")
    u.acquire_rig("PatchRig")
    u.upgrade_rig()
    u.inventory.append(Asset("Hardware Patch", "Upgrades rigs"))
    u.upgrade_rig()
    print(u.rig)
    u.rig.take_hit()
    u.rig.take_hit()
    print("Before repair:", u.rig)
    u.inventory.append(Asset("CryptoToken", "Repair token"))
    u.rig.repair(u)
    print("After repair:", u.rig)

def test_trace_limit():
    print("\n--- Test 7: Trace limit blocks attacks ---")
    a = Hacker("Tracer")
    b = Hacker("Target")
    a.acquire_rig("TracerRig")
    b.acquire_rig("TargetRig")
    a.trace = 6
    a.launch_data_spike(b)

def run_tests():
    test_acquire_rig_edge_case()
    test_acquire_rig_success()
    test_data_spike_and_break()
    test_extract_from_broken_rig()
    test_encrypt_decrypt_flow()
    test_upgrade_and_repair()
    test_trace_limit()
    print("\n--- All tests complete ---")

if __name__ == "__main__":
    run_tests()
