#!/usr/bin/env python3
import genanki
import os

def create_model():
    return genanki.Model(
        3847291023,
        'Hardware Security Standards Q&A',
        fields=[
            {'name': 'Front'},
            {'name': 'Back'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '<div class="front">{{Front}}</div>',
                'afmt': '{{FrontSide}}<hr id="answer"><div class="back">{{Back}}</div>',
            },
        ],
        css='''
            .card {
                font-family: arial;
                font-size: 18px;
                text-align: left;
                color: black;
                background-color: white;
                padding: 20px;
                max-width: 700px;
                margin: 0 auto;
            }
            .front {
                font-size: 22px;
                font-weight: bold;
            }
            .back {
                white-space: pre-wrap;
            }
            .tag {
                display: inline-block;
                background: #e8f0fe;
                color: #1a73e8;
                border-radius: 4px;
                padding: 2px 8px;
                font-size: 13px;
                margin-bottom: 8px;
            }
            .warn {
                background: #fff3e0;
                border-left: 4px solid #f57c00;
                padding: 8px 12px;
                margin-top: 10px;
                border-radius: 2px;
            }
        '''
    )

def create_deck():
    return genanki.Deck(
        9273648510,
        'Hardware Security Standards'
    )

def get_cards():
    """Returns list of (front, back) tuples."""
    return [

        # ── CONCEPTUAL MAP ──────────────────────────────────────────────────────
        (
            "What are the 4 questions that hardware security standards answer?",
            """<span class="tag">Conceptual Map</span>

1. <b>"Is the crypto module trustworthy?"</b>
   → FIPS 140-3, ISO/IEC 19790, Common Criteria, SESIP

2. <b>"Can the platform boot and run without being tampered with?"</b>
   → TPM 2.0, UEFI Secure Boot, NIST SP 800-193, DICE, Measured Boot

3. <b>"Is the supply chain that produced the hardware trustworthy?"</b>
   → NIST SP 800-161, ISO 28000, ISO/IEC 20243 (O-TTPS), CMMC, EO 14028 / SBOMs

4. <b>"Does this product meet sector rules?"</b>
   → ISO/SAE 21434 + UN R155 (auto), IEC 62443 (industrial),
     ETSI EN 303 645 / NIST IR 8259 (IoT), PCI HSM/PTS (payments),
     DO-326A (avionics), NERC CIP (grid), FDA pre-market cyber (medical)"""
        ),

        # ── FIPS 140 FAMILY ─────────────────────────────────────────────────────
        (
            "FIPS 140-3",
            """<span class="tag">Crypto Module Standards</span>

<b>One-liner:</b> U.S./Canadian standard for validating cryptographic modules.

<b>What to know:</b>
• Published by NIST + Canadian Centre for Cyber Security; tested under <b>CMVP</b> by accredited labs.
• <b>4 security levels</b> (1 = software-only OK → 4 = tamper-active, environmental-attack resistant).
• Covers 11 requirement areas: module spec, ports/interfaces, roles &amp; auth, finite state model, physical security, operational environment, key management, EMI/EMC, self-tests, design assurance, mitigation of other attacks.
• Aligns with <b>ISO/IEC 19790</b> (incorporated by reference) and <b>ISO/IEC 24759</b> for testing.
• Mandatory <b>side-channel resistance testing</b> — the single biggest change vs 140-2.
• Required by FedRAMP, CMMC 2.0, HIPAA-adjacent procurement.
• A "cryptographic module" can be hardware, firmware, software, or hybrid.

<div class="warn"><b>Watch out for:</b> "FIPS-compliant" (uses approved algorithms) ≠ "FIPS-validated" (has a CMVP certificate). Only validation has legal weight. Levels are not linearly more secure for all dimensions — they're stepwise-stricter on physical/tamper.</div>"""
        ),
        (
            "FIPS 140-2",
            """<span class="tag">Crypto Module Standards</span>

<b>One-liner:</b> The previous version of FIPS 140 — being sunset.

<b>What to know:</b>
• Predecessor to FIPS 140-3.
• Side-channel testing was largely <b>undefined</b> (the major gap 140-3 closes).
• <b>Sunset: September 21, 2026</b> — all validations move to CMVP Historical List on that date.
• No new 140-2 submissions accepted now.
• Existing validations don't become illegal, but federal procurement treats them as historical."""
        ),
        (
            "ISO/IEC 19790",
            """<span class="tag">Crypto Module Standards</span>

<b>One-liner:</b> International twin of FIPS 140-3 — same requirements, different cover page.

<b>What to know:</b>
• ISO standard for security requirements for cryptographic modules.
• FIPS 140-3 is essentially 19790 + U.S. annexes.
• A 19790 certificate may be accepted internationally where FIPS isn't."""
        ),
        (
            "ISO/IEC 24759",
            """<span class="tag">Crypto Module Standards</span>

<b>One-liner:</b> Test methodology that goes with ISO/IEC 19790 / FIPS 140-3.

<b>What to know:</b>
• Tells accredited labs <em>how</em> to test what 19790 requires.
• The operational counterpart to 19790 — you cite it less often but it's what labs follow."""
        ),
        (
            "PCI HSM",
            """<span class="tag">Crypto Module Standards</span>

<b>One-liner:</b> Payment-industry standard for HSMs handling card PINs and keys.

<b>What to know:</b>
• Issued by the PCI Security Standards Council.
• Required for HSMs in payment networks.
• Covers logical and physical security, key management, and full device lifecycle (manufacture → decommission).
• Often layered with FIPS 140 — many HSMs hold both."""
        ),
        (
            "ANSI X9.24",
            """<span class="tag">Crypto Module Standards</span>

<b>One-liner:</b> Financial-services key management standard, especially for symmetric keys and DUKPT.

<b>What to know:</b>
• Defines retail key management for payments.
• Know alongside PCI HSM for payment-industry context."""
        ),

        # ── PRODUCT EVALUATION ──────────────────────────────────────────────────
        (
            "Common Criteria (CC) / ISO/IEC 15408",
            """<span class="tag">Product Evaluation</span>

<b>One-liner:</b> International framework for evaluating IT product security against a defined target.

<b>What to know:</b>
• ISO standard used by governments and large enterprises.
• <b>TOE</b> (Target of Evaluation) = what's being evaluated.
• <b>PP</b> (Protection Profile) = reusable security requirements template for a product class.
• <b>EAL 1–7</b>: EAL1 = functional testing; EAL4+ = typical commercial sweet spot; EAL5+/6+/7 require formal methods (rare, used for smartcards/HSMs/secure elements).
• <b>CCRA</b> = mutual recognition arrangement between nations, typically up to EAL2 / collaborative PPs.
• Vendors often dual-stack: FIPS 140-3 for the crypto module + CC EAL4+/5+ for the broader product.

<div class="warn"><b>Watch out for:</b> Higher EAL ≠ "more secure" — it means "more rigorously evaluated against its stated target." A poorly-scoped TOE at EAL7 can be less secure in practice than a well-scoped EAL4 product.</div>"""
        ),
        (
            "SESIP (Security Evaluation Standard for IoT Platforms)",
            """<span class="tag">Product Evaluation</span>

<b>One-liner:</b> Lightweight CC-derived methodology for IoT platforms.

<b>What to know:</b>
• Published by <b>GlobalPlatform</b>.
• Designed to cut CC's cost/time for IoT, where full EAL evaluations are impractical.
• Five assurance levels: <b>SESIP1–SESIP5</b>.
• Increasingly referenced in EU Cyber Resilience Act conformity work."""
        ),
        (
            "Protection Profiles (NIAP / collaborative PPs)",
            """<span class="tag">Product Evaluation</span>

<b>One-liner:</b> Standardized security requirement docs for a product class (firewalls, VPNs, mobile devices, etc.).

<b>What to know:</b>
• In the U.S., <b>NIAP</b> (National Information Assurance Partnership) runs the U.S. CC scheme and publishes PPs for federal procurement.
• Each PP defines the security requirements a product in that category must meet for evaluation."""
        ),

        # ── HARDWARE ROOTS OF TRUST ─────────────────────────────────────────────
        (
            "TPM 2.0 / ISO/IEC 11889",
            """<span class="tag">Hardware Roots of Trust</span>

<b>One-liner:</b> Standardized hardware crypto-coprocessor providing a hardware root of trust.

<b>What to know:</b>
• Spec by <b>Trusted Computing Group (TCG)</b>; published as ISO/IEC 11889 (parts 1–4).
• Provides: secure key storage, RNG, hashing, sealed storage, <b>PCRs</b> (Platform Configuration Registers) for measured boot, <b>remote attestation</b>, key generation/sealing.
• Required for Windows 11.
• Implementations: discrete TPM (dTPM, most secure), integrated, firmware TPM (fTPM, runs in CPU TEE), software, virtual.
• Typical certs: CC EAL4+ with AVA_VAN.5; FIPS 140-2 Level 2 with physical Level 3.
• Vendors: Infineon, Nuvoton, STMicro (discrete); Intel PTT, AMD fTPM (firmware).

<div class="warn"><b>Watch out for:</b> Known attacks include TPM reset via power glitching and bus sniffing between discrete TPM and CPU (Dolos Group 2021 — read a BitLocker key off the SPI bus). dTPM tamper-resistance protects the chip only, not the wires going to it.</div>"""
        ),
        (
            "TCG DICE (Device Identifier Composition Engine)",
            """<span class="tag">Hardware Roots of Trust</span>

<b>One-liner:</b> TCG spec for resource-constrained devices to derive identity and attestation from a layered measurement chain.

<b>What to know:</b>
• Simpler root-of-trust scheme than TPM — designed for MCUs/IoT where a full TPM is overkill.
• Each boot layer derives the next layer's identity from a hash of itself.
• Provides layered attestation without requiring full TPM hardware."""
        ),
        (
            "UEFI Secure Boot",
            """<span class="tag">Hardware Roots of Trust</span>

<b>One-liner:</b> UEFI specification feature that verifies signed bootloaders/kernels before execution.

<b>What to know:</b>
• Defined by the <b>UEFI Forum</b>, not TCG.
• Key hierarchy: Platform Key (PK) → Key Exchange Keys (KEK) → DB (allowed signers) / DBX (revoked).
• <b>Static</b> — checks signatures only at boot time.
• Pair with TPM-based <b>Measured Boot</b> (logging hashes to PCRs) for remote attestation capability."""
        ),
        (
            "Measured Boot / S-RTM and D-RTM",
            """<span class="tag">Hardware Roots of Trust</span>

<b>One-liner:</b> TCG concept where boot-stage hashes are extended into TPM PCRs, enabling attestation of what booted.

<b>What to know:</b>
• <b>S-RTM</b> (Static Root of Trust for Measurement): chain starts at power-on, anchored in immutable boot ROM.
• <b>D-RTM</b> (Dynamic RTM, "late launch"): a secure-launch instruction (Intel TXT, AMD SKINIT) re-establishes a trusted chain after BIOS, reducing TCB.
• Underpins remote attestation: a verifier checks PCR values + attestation signature to know exactly what software booted."""
        ),
        (
            "Arm TrustZone & GlobalPlatform TEE",
            """<span class="tag">Hardware Roots of Trust</span>

<b>One-liner:</b> Vendor-supplied secure-world hardware + standardized TEE API.

<b>What to know:</b>
• <b>TrustZone</b> = Arm hardware feature splitting the CPU into Secure World and Normal World.
• <b>GlobalPlatform TEE</b> specs standardize the API/architecture for Trusted Execution Environments — vendor-neutral.
• TEEs ≠ HSMs: TEEs share silicon with the rest of the SoC; HSMs are physically separate dedicated devices."""
        ),
        (
            "Intel TXT, Intel SGX, AMD SEV/SEV-SNP",
            """<span class="tag">Hardware Roots of Trust</span>

<b>One-liner:</b> Vendor-specific trusted execution / confidential computing extensions.

<b>What to know:</b>
• Not ISO/NIST standards — they are vendor specifications.
• Building blocks for confidential-computing services (Azure Confidential Computing, AWS Nitro, Google Confidential VM).
• Referenced by NIST guidance.
• <b>Intel TXT</b>: enables D-RTM ("late launch" measured boot). <b>Intel SGX</b>: application-level enclaves. <b>AMD SEV/SEV-SNP</b>: encrypted VM memory with attestation."""
        ),

        # ── PLATFORM FIRMWARE ───────────────────────────────────────────────────
        (
            "NIST SP 800-193 — Platform Firmware Resiliency Guidelines",
            """<span class="tag">Platform Firmware</span>

<b>One-liner:</b> Three principles for platform firmware: <b>Protect, Detect, Recover</b>.

<b>What to know:</b>
• Published 2018. Covers <em>all</em> platform firmware (BIOS, BMC, NIC, GPU, SSD controller, EC, TPM, etc.).
• Three required properties:
  – <b>Protected:</b> Root of Trust for Update (RTU) authenticates firmware updates; integrity enforced.
  – <b>Detection:</b> corrupted firmware can be identified.
  – <b>Recovery:</b> corrupted firmware can be restored via Root of Trust for Recovery (RTRec).
• <b>Supersedes SP 800-147</b> (BIOS Protection) and <b>SP 800-155</b> (BIOS Integrity Measurement)."""
        ),
        (
            "NIST SP 800-147 (legacy)",
            """<span class="tag">Platform Firmware</span>

<b>One-liner:</b> BIOS protection guidelines — superseded by 800-193 in scope.

<b>What to know:</b>
• Original BIOS Protection Guidelines (2011).
• Required signed BIOS updates and write protection.
• Still referenced in some older procurement specs, but 800-193 is the modern reference."""
        ),
        (
            "NIST SP 800-155 (legacy)",
            """<span class="tag">Platform Firmware</span>

<b>One-liner:</b> BIOS Integrity Measurement Guidelines — subsumed by 800-193.

<b>What to know:</b>
• Specified what BIOS integrity measurements should look like.
• Less practically relevant today; 800-193 covers this ground more broadly."""
        ),

        # ── SUPPLY CHAIN ────────────────────────────────────────────────────────
        (
            "NIST SP 800-161 — C-SCRM",
            """<span class="tag">Supply Chain</span>

<b>One-liner:</b> NIST's framework for managing cyber risk in the supply chain.

<b>What to know:</b>
• Full title: <em>Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations</em> (Rev. 1, 2022).
• Maps to NIST SP 800-53 controls in the <b>SR</b> (Supply Chain Risk Management) family.
• Heavily referenced by federal procurement after Section 889 (NDAA 2019) and EO 14028."""
        ),
        (
            "ISO/IEC 20243 (O-TTPS — Open Trusted Technology Provider Standard)",
            """<span class="tag">Supply Chain</span>

<b>One-liner:</b> Industry standard for COTS ICT product integrity, focused on counterfeits and tainted products.

<b>What to know:</b>
• Developed by The Open Group's Trusted Technology Forum.
• Specifically targets: maliciously tainted and counterfeit products in the supply chain.
• Has a certification scheme; popular with U.S. federal contractors."""
        ),
        (
            "ISO 28000:2022",
            """<span class="tag">Supply Chain</span>

<b>One-liner:</b> Generic supply-chain security management system (SeMS) — an ISO management-system standard.

<b>What to know:</b>
• Originally maritime-focused (2007), revised 2022 to apply to any organization.
• Plan-Do-Check-Act structure aligned with ISO 27001/9001/22301. Certifiable.
• Less hardware-specific than 800-161/20243; treats security like ISO 9001 treats quality."""
        ),
        (
            "CMMC 2.0 (Cybersecurity Maturity Model Certification)",
            """<span class="tag">Supply Chain</span>

<b>One-liner:</b> DoD's certification regime for defense contractors.

<b>What to know:</b>
• Three levels: Foundational, Advanced, Expert — built on NIST SP 800-171 and 800-172.
• Mandates <b>FIPS 140-3 validated</b> encryption for protecting Controlled Unclassified Information (CUI).
• Required for Defense Industrial Base contracts."""
        ),
        (
            "SBOM / HBOM (Software / Hardware Bill of Materials)",
            """<span class="tag">Supply Chain</span>

<b>One-liner:</b> A machine-readable inventory of components — driven by EO 14028.

<b>What to know:</b>
• <b>SBOM</b> mandated by Executive Order 14028 (2021) for software sold to U.S. federal government.
• <b>HBOM</b> is the hardware analog; more nascent. CISA published an HBOM framework in 2023.
• Common formats: <b>SPDX</b>, <b>CycloneDX</b>."""
        ),
        (
            "IEEE 1735",
            """<span class="tag">Supply Chain</span>

<b>One-liner:</b> Standard for encrypting and protecting electronic-design IP.

<b>What to know:</b>
• Used in EDA/silicon IP licensing.
• Protects RTL/netlists during distribution to prevent unauthorized use or copying."""
        ),

        # ── CRYPTO ALGORITHMS ───────────────────────────────────────────────────
        (
            "FIPS 197 — AES",
            """<span class="tag">Cryptographic Algorithms</span>

<b>One-liner:</b> Advanced Encryption Standard. The symmetric cipher.

<b>What to know:</b>
• Block cipher with 128/192/256-bit keys.
• AES-128 is broadly fine today; <b>CNSA 2.0</b> requires AES-256 for national-security systems."""
        ),
        (
            "FIPS 186-5 — Digital Signature Standard (DSS)",
            """<span class="tag">Cryptographic Algorithms</span>

<b>One-liner:</b> Defines DSA, ECDSA, EdDSA — the approved digital signature algorithms.

<b>What to know:</b>
• Latest revision 186-5 (2023) <b>added EdDSA</b> (Ed25519/Ed448) and <b>removed DSA</b> from new use.
• ECDSA remains widely used; EdDSA gaining adoption for its simplicity and security properties."""
        ),
        (
            "FIPS 180-4 / FIPS 202 — SHA / SHA-3",
            """<span class="tag">Cryptographic Algorithms</span>

<b>One-liner:</b> Hash function standards — SHA-2 family (180-4) and SHA-3 family (202).

<b>What to know:</b>
• <b>FIPS 180-4</b>: SHA-2 family — SHA-256, SHA-384, SHA-512.
• <b>FIPS 202</b>: SHA-3 family (Keccak-based) — SHA3-256/384/512 plus SHAKE128/256 (XOFs)."""
        ),
        (
            "NIST SP 800-90A / 800-90B / 800-90C — Random Bit Generation",
            """<span class="tag">Cryptographic Algorithms</span>

<b>One-liner:</b> The RBG triad: DRBGs (90A), entropy sources (90B), RBG constructions (90C).

<b>What to know:</b>
• <b>800-90A</b>: Deterministic RBGs — Hash_DRBG, HMAC_DRBG, CTR_DRBG. Dual_EC_DRBG was <em>removed</em> after NSA backdoor concerns.
• <b>800-90B</b>: Entropy source validation (statistical tests, IID/non-IID tracks). Required for FIPS 140-3 modules with hardware RNGs.
• <b>800-90C</b>: RBG constructions combining 90A and 90B."""
        ),
        (
            "NIST SP 800-56A/B/C — Key Establishment",
            """<span class="tag">Cryptographic Algorithms</span>

<b>One-liner:</b> Key agreement (DH, ECDH) and key transport (RSA), plus key derivation.

<b>What to know:</b>
• FIPS 140-3 modules must use approved key-establishment schemes from these publications.
• 56A: DH/ECDH key agreement. 56B: RSA key transport. 56C: key derivation methods."""
        ),
        (
            "NIST SP 800-57 — Key Management",
            """<span class="tag">Cryptographic Algorithms</span>

<b>One-liner:</b> General key-management recommendations: key lifecycles, sizes, and transitions.

<b>What to know:</b>
• Defines security strength equivalences:
  – 128-bit security ≈ AES-128 ≈ RSA-3072 ≈ ECC-256
  – 256-bit security ≈ AES-256 ≈ RSA-15360 ≈ ECC-512"""
        ),
        (
            "Post-Quantum Cryptography: FIPS 203, 204, 205",
            """<span class="tag">Cryptographic Algorithms</span>

<b>One-liner:</b> The first three NIST PQC standards, finalized August 2024.

<b>What to know:</b>
• <b>FIPS 203 / ML-KEM</b> (CRYSTALS-Kyber): lattice-based KEM. Replaces RSA/ECDH key establishment.
• <b>FIPS 204 / ML-DSA</b> (CRYSTALS-Dilithium): lattice-based signature.
• <b>FIPS 205 / SLH-DSA</b> (SPHINCS+): hash-based signature, conservative/stateless.
• HQC and FALCON are additional/forthcoming.
• NSA's <b>CNSA 2.0</b> mandates ML-KEM / ML-DSA / LMS / XMSS for national-security systems by ~2030–2035."""
        ),

        # ── AUTOMOTIVE ──────────────────────────────────────────────────────────
        (
            "ISO/SAE 21434 — Road Vehicles, Cybersecurity Engineering",
            """<span class="tag">Automotive</span>

<b>One-liner:</b> Process standard for automotive cybersecurity over the vehicle lifecycle.

<b>What to know:</b>
• Joint ISO/SAE standard published August 2021.
• Mandates <b>CSMS</b> (Cybersecurity Management System) in the organization and <b>TARA</b> (Threat Analysis and Risk Assessment) in engineering.
• Sibling to ISO 26262 (functional safety) — different concerns, similar lifecycle approach.
• Covers concept → development → production → operation → decommissioning of E/E systems."""
        ),
        (
            "UNECE WP.29 R155 / R156",
            """<span class="tag">Automotive</span>

<b>One-liner:</b> UN regulations that legally require automotive cybersecurity (R155) and software-update management (R156) for vehicle type approval.

<b>What to know:</b>
• <b>R155</b> = Cybersecurity &amp; CSMS; <b>R156</b> = Software Update Management System (SUMS).
• Mandatory in UNECE markets (EU, Japan, South Korea, etc.) for new vehicle types since July 2022, all new vehicles since July 2024.
• Not mandatory in U.S./China but de facto influential.
• <b>ISO/SAE 21434</b> is the standard most commonly used to demonstrate R155 compliance.
• <b>ISO 24089</b> covers the SUMS side (R156)."""
        ),

        # ── ICS / OT ────────────────────────────────────────────────────────────
        (
            "IEC 62443 (ISA/IEC 62443)",
            """<span class="tag">ICS / OT</span>

<b>One-liner:</b> The big OT/ICS cybersecurity standards series.

<b>What to know:</b>
• Multi-part series in 4 groups: General (-1-x), Policies &amp; Procedures (-2-x), System (-3-x), Components (-4-x).
• Key parts:
  – <b>62443-2-1</b>: security program for asset owners.
  – <b>62443-3-2</b>: risk assessment + zone/conduit modeling.
  – <b>62443-3-3</b>: system security requirements + 4 Security Levels (SL1–SL4).
  – <b>62443-4-1</b>: secure product development lifecycle (4 maturity levels).
  – <b>62443-4-2</b>: technical security requirements for components.
• <b>7 Foundational Requirements (FRs)</b>: Identification &amp; Auth Control, Use Control, System Integrity, Data Confidentiality, Restricted Data Flow, Timely Response to Events, Resource Availability.
• Recognized by IEC as a "horizontal" standard (2021) across all OT-adjacent sectors.
• Certification: <b>ISASecure</b> scheme."""
        ),
        (
            "NERC CIP",
            """<span class="tag">ICS / OT</span>

<b>One-liner:</b> Mandatory cybersecurity standards for the North American Bulk Electric System.

<b>What to know:</b>
• <b>Enforceable</b>, with significant fines.
• CIP-002 through CIP-014; covers asset identification, security controls, incident reporting, supply chain (CIP-013), physical security.
• U.S. and Canada-specific."""
        ),
        (
            "IEC 62351",
            """<span class="tag">ICS / OT</span>

<b>One-liner:</b> Security for power-system communication protocols (IEC 60870, 61850, etc.).

<b>What to know:</b>
• Sister standard to IEC 62443 but specifically for power-system protocols.
• Covers TLS profiles, role-based access, and key management for grid communications."""
        ),

        # ── IoT / CONSUMER ──────────────────────────────────────────────────────
        (
            "ETSI EN 303 645",
            """<span class="tag">IoT / Consumer</span>

<b>One-liner:</b> Baseline cybersecurity requirements for consumer IoT — the global de-facto baseline.

<b>What to know:</b>
• 13 high-level provisions. Top three:
  1. <b>No universal default passwords</b>
  2. <b>Vulnerability disclosure policy</b>
  3. <b>Keep software updated</b>
• Underpins UK PSTI Act; feeds into EU Cyber Resilience Act compliance.
• Companion test spec: <b>ETSI TS 103 701</b> for conformance assessment."""
        ),
        (
            "NIST IR 8259 series",
            """<span class="tag">IoT / Consumer</span>

<b>One-liner:</b> U.S. baseline guidance series for IoT device manufacturers.

<b>What to know:</b>
• <b>8259</b>: foundational manufacturer activities (pre- and post-market).
• <b>8259A</b>: technical core baseline — device identification, configuration, data protection, logical access, software update, cybersecurity state awareness.
• <b>8259B</b>: non-technical core baseline — documentation, info dissemination, vulnerability disclosure.
• <b>8259C/D</b>: profile-creation methodology + federal profile.
• <b>8425</b>: consumer IoT profile — technical foundation for FCC <b>Cyber Trust Mark</b>."""
        ),
        (
            "PSA Certified",
            """<span class="tag">IoT / Consumer</span>

<b>One-liner:</b> Industry IoT certification scheme aligned to multiple regional standards.

<b>What to know:</b>
• Founded by Arm; three levels:
  – Level 1: questionnaire-based.
  – Level 2: lab-evaluated chip.
  – Level 3: lab-evaluated SoC + side-channel testing.
• Maps to ETSI EN 303 645, NIST IR 8259A, EU CRA, IEC 62443-4-2."""
        ),
        (
            "EU Cyber Resilience Act (CRA)",
            """<span class="tag">IoT / Consumer</span>

<b>One-liner:</b> EU regulation for cybersecurity of products with digital elements.

<b>What to know:</b>
• Adopted October 2024; full obligations apply from <b>December 11, 2027</b>.
• Covers all products with digital elements sold in the EU — hardware and software.
• Manufacturers must: implement security by design, provide vulnerability support for 5 years, report actively exploited vulnerabilities within 24 hours.
• Two "important" and one "critical" product categories require third-party conformity assessment."""
        ),

        # ── BONUS: KEY DISTINCTIONS ─────────────────────────────────────────────
        (
            "FIPS 140 levels: what does each level actually guarantee?",
            """<span class="tag">Crypto Module Standards</span>

• <b>Level 1</b>: Approved algorithms and self-tests. Software-only modules allowed. No physical requirements.
• <b>Level 2</b>: Evidence of tampering required (tamper-evident coatings/seals, pick-resistant locks). Role-based auth.
• <b>Level 3</b>: Tamper <em>detection</em> and response (zeroization of keys on detection). Physical barriers. Identity-based auth.
• <b>Level 4</b>: Tamper <em>active</em> — complete envelope of protection; must detect/respond to all penetration attempts. Environmental attack resistance (voltage, temperature).

<div class="warn">Levels are stepwise stricter on physical/tamper requirements. Cryptographic algorithm requirements are similar across all levels.</div>"""
        ),
        (
            "FIPS-validated vs FIPS-compliant — what's the difference?",
            """<span class="tag">Crypto Module Standards</span>

• <b>FIPS-validated</b>: The module has been tested by a CMVP-accredited lab and received an official NIST certificate number. This has legal/contractual weight for federal procurement.

• <b>FIPS-compliant</b> (or "FIPS-mode"): The product uses FIPS-approved algorithms but has NOT gone through CMVP validation. No certificate, no legal weight.

<div class="warn">Vendors sometimes market products as "FIPS-compliant" when they mean "uses AES/SHA-2." Only a CMVP certificate number proves validation. Federal requirements (FedRAMP, CMMC) require validated modules.</div>"""
        ),
        (
            "TPM discrete vs firmware (fTPM) — security trade-offs",
            """<span class="tag">Hardware Roots of Trust</span>

• <b>Discrete TPM (dTPM)</b>: Separate chip, physically isolated. Most secure. Vulnerable to bus sniffing between TPM and CPU (see Dolos Group 2021 BitLocker attack on SPI bus).
• <b>Firmware TPM (fTPM)</b>: Runs in CPU's TEE (Intel PTT, AMD fTPM). No bus-sniffing risk but shares silicon with CPU; CPU firmware vulnerabilities can affect it.
• <b>Integrated TPM</b>: Built into chipset/SoC — between the two.
• <b>Virtual TPM</b>: Software only, for VMs; no hardware isolation."""
        ),
        (
            "Secure Boot vs Measured Boot — what's the difference?",
            """<span class="tag">Hardware Roots of Trust</span>

• <b>Secure Boot</b> (UEFI): Verifies signatures on bootloader/kernel before execution. <em>Prevents</em> unsigned code from running. Binary: pass or fail.

• <b>Measured Boot</b> (TPM/TCG): Hashes each boot component and <em>records</em> the value in TPM PCRs, but does not block anything. Provides a tamper-evident log for remote attestation.

• The two are complementary: Secure Boot enforces integrity at boot; Measured Boot enables later verification of what booted via remote attestation."""
        ),
        (
            "NIST SP 800-193 three properties — Protect, Detect, Recover",
            """<span class="tag">Platform Firmware</span>

• <b>Protected</b>: Firmware updates are authenticated by a Root of Trust for Update (RTU). Integrity enforced at runtime.
• <b>Detect</b>: The platform can identify when firmware has been corrupted or tampered with.
• <b>Recover</b>: The platform can restore from a known-good image via a Root of Trust for Recovery (RTRec) — without requiring OS involvement.

Applies to ALL platform firmware: BIOS, BMC, NIC, GPU, SSD controller, EC, TPM — not just BIOS."""
        ),
        (
            "IEC 62443 Security Levels (SL1–SL4)",
            """<span class="tag">ICS / OT</span>

• <b>SL1</b>: Protection against casual or unintentional violation.
• <b>SL2</b>: Protection against intentional violation using simple means (low resources, generic skills).
• <b>SL3</b>: Protection against intentional violation using sophisticated means (moderate resources, IACS-specific skills).
• <b>SL4</b>: Protection against intentional violation using state-of-the-art means (extended resources, advanced skills).

Applies to both system-level (62443-3-3) and component-level (62443-4-2) requirements."""
        ),
        (
            "ISO/SAE 21434 TARA — what it is and why it matters",
            """<span class="tag">Automotive</span>

<b>TARA</b> = Threat Analysis and Risk Assessment

• The core engineering process mandated by ISO/SAE 21434 for E/E systems.
• Steps: asset identification → threat scenarios → impact rating → attack path analysis → risk determination → risk treatment.
• Risk treatment options: avoid, reduce, share, accept.
• Analogous to FMEA (Failure Mode Effects Analysis) in functional safety, but for cybersecurity.
• Required to demonstrate R155 compliance via UN WP.29."""
        ),
        (
            "CNSA 2.0 — what it is and what it mandates",
            """<span class="tag">Cryptographic Algorithms</span>

<b>Commercial National Security Algorithm Suite 2.0</b> — NSA's algorithm list for national-security systems.

• Released September 2022.
• <b>Mandates post-quantum algorithms</b> for NSS by 2030–2035:
  – ML-KEM (FIPS 203) for key establishment
  – ML-DSA (FIPS 204) and LMS/XMSS for signatures
  – AES-256 for symmetric encryption
  – SHA-384 for hashing
• Timeline: plan by 2025, prototype by 2026, transition by 2030 (software), 2033 (firmware), 2035 (hardware).
• Replaces CNSA 1.0 (which relied on RSA, ECDH, AES-256)."""
        ),
    ]

def generate_deck():
    print("Generating Hardware Security Standards Anki deck...")

    model = create_model()
    deck = create_deck()
    cards = get_cards()

    for front, back in cards:
        note = genanki.Note(model=model, fields=[front, back])
        deck.add_note(note)

    output_path = 'hardware_security.apkg'
    deck.write_to_file(output_path)

    assert os.path.exists(output_path), "Deck file not created!"
    size_kb = os.path.getsize(output_path) / 1024

    print(f"✓ Created deck with {len(cards)} cards")
    print(f"✓ Deck saved as: {output_path}")
    print(f"✓ File size: {size_kb:.1f} KB")

if __name__ == '__main__':
    generate_deck()
