# Hardware Security Standards

A reference deck covering the major standards a hardware-security professional is expected to know — organized by *function* rather than alphabetically, because the relationships between standards matter more than their names.

## What's Included

**42 cards** across 10 sections: a conceptual map plus cryptographic modules, product evaluation, hardware roots of trust, platform firmware resilience, supply chain integrity, algorithms, and sector-specific regimes (automotive, industrial/OT, IoT/consumer).

## Download

- [Hardware Security Standards](https://raw.githubusercontent.com/jacksondean17/anki/main/hardware_security_standards/hardware_security_standards.apkg)

## Card Format

**Front:** Standard name (e.g., "FIPS 140-3", "ISO/SAE 21434") with a category badge.

**Back:**
- **One-liner** — a single-sentence definition (highlighted callout).
- **What to know** — the substantive bullets: scope, governing body, levels, lineage, where it shows up.
- **Watch out for** — when present, an amber callout for the things people get wrong on exams or in practice.

## Topics Covered

### Conceptual Map (1)
The four questions hardware-security standards answer

### Cryptographic Module Standards (6)
FIPS 140-3 · FIPS 140-2 · ISO/IEC 19790 · ISO/IEC 24759 · PCI HSM · ANSI X9.24

### Product Evaluation Regimes (3)
Common Criteria / ISO/IEC 15408 · SESIP · Protection Profiles (NIAP)

### Hardware Roots of Trust (6)
TPM 2.0 / ISO/IEC 11889 · TCG DICE · UEFI Secure Boot · Measured Boot (S-RTM / D-RTM) · Arm TrustZone & GlobalPlatform TEE · Intel TXT/SGX, AMD SEV/SEV-SNP

### Platform Firmware & Resilience (4)
NIST SP 800-193 · NIST SP 800-147 (legacy) · NIST SP 800-155 (legacy) · UEFI Specification

### Supply Chain & Hardware Integrity (6)
NIST SP 800-161 (C-SCRM) · ISO/IEC 20243 (O-TTPS) · ISO 28000:2022 · CMMC 2.0 · SBOM / HBOM · IEEE 1735

### Cryptographic Algorithms (7)
FIPS 197 (AES) · FIPS 186-5 (DSS) · FIPS 180-4 / 202 (SHA / SHA-3) · NIST SP 800-90A/B/C · NIST SP 800-56A/B/C · NIST SP 800-57 · Post-Quantum (FIPS 203/204/205)

### Sector: Automotive (2)
ISO/SAE 21434 · UNECE WP.29 R155 / R156

### Sector: Industrial / OT (3)
IEC 62443 · NERC CIP · IEC 62351

### Sector: IoT / Consumer (4)
ETSI EN 303 645 · NIST IR 8259 series · PSA Certified · EU Cyber Resilience Act

## How to Use

1. Download the .apkg file using the link above.
2. Import into Anki or AnkiDroid.
3. Read the **Conceptual Map** card first — it frames everything else.
4. Study the rest to internalize the standards landscape: what each is, who runs it, and how it relates to the others.

## Regenerating the Deck

```bash
cd hardware_security_standards
pip install genanki
python3 generate_deck.py
```

---

*Generated: 2026-06-26*
