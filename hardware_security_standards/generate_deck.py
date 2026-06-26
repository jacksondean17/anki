#!/usr/bin/env python3
"""Generate an Anki deck for Hardware Security Standards."""
import genanki
import os

MODEL_ID = 1834207615
DECK_ID = 1958301427

model = genanki.Model(
    MODEL_ID,
    'Hardware Security Standards',
    fields=[
        {'name': 'Name'},
        {'name': 'Category'},
        {'name': 'Oneliner'},
        {'name': 'WhatToKnow'},
        {'name': 'WatchOutFor'},
    ],
    templates=[{
        'name': 'Card',
        'qfmt': (
            '<div class="category">{{Category}}</div>'
            '<div class="front">{{Name}}</div>'
        ),
        'afmt': (
            '{{FrontSide}}'
            '<hr id="answer">'
            '<div class="back">'
            '<div class="oneliner">{{Oneliner}}</div>'
            '<div class="section-label">What to know</div>'
            '<div class="whattoknow">{{WhatToKnow}}</div>'
            '{{#WatchOutFor}}'
            '<div class="watchout">'
            '<div class="watchout-label">Watch out for</div>'
            '<div class="watchout-body">{{WatchOutFor}}</div>'
            '</div>'
            '{{/WatchOutFor}}'
            '</div>'
        ),
    }],
    css='''
        .card {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", arial, sans-serif;
            font-size: 18px;
            text-align: center;
            color: #1a1a1a;
            background-color: #fafafa;
            padding: 20px;
        }
        .category {
            display: inline-block;
            background: #0f172a;
            color: #fff;
            font-size: 12px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            padding: 3px 10px;
            border-radius: 4px;
            margin-bottom: 14px;
        }
        .front {
            font-size: 28px;
            font-weight: bold;
            color: #0f172a;
        }
        .back {
            font-size: 16px;
            text-align: left;
            line-height: 1.55;
            color: #1a1a1a;
            max-width: 760px;
            margin: 0 auto;
        }
        .oneliner {
            font-size: 17px;
            font-style: italic;
            color: #0f172a;
            background: #e0e7ff;
            padding: 10px 14px;
            border-left: 4px solid #1e3a8a;
            border-radius: 4px;
            margin-bottom: 16px;
        }
        .section-label {
            font-size: 13px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: #1e3a8a;
            margin-bottom: 6px;
        }
        .whattoknow ul {
            margin: 0 0 14px 0;
            padding-left: 22px;
        }
        .whattoknow li {
            margin-bottom: 6px;
        }
        .whattoknow p {
            margin: 0 0 10px 0;
        }
        .watchout {
            margin-top: 14px;
            background: #fef3c7;
            border-left: 4px solid #d97706;
            padding: 10px 14px;
            border-radius: 4px;
        }
        .watchout-label {
            font-size: 12px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: #92400e;
            margin-bottom: 6px;
        }
        .watchout-body {
            color: #1a1a1a;
        }
        hr#answer {
            border: 0;
            border-top: 1px solid #d0d0d0;
            margin: 16px 0;
        }
        b, strong {
            color: #0f172a;
        }
    '''
)


def ul(items):
    return '<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


cards = [
    # =========================================================
    # 00 - Conceptual Map (the four questions)
    # =========================================================
    (
        "Conceptual map: the four questions",
        "Conceptual Map",
        "Hardware-security standards answer four distinct questions — and that grouping matters more than the alphabet.",
        ul([
            '<b>1. Is the crypto module trustworthy?</b> → FIPS 140-3, ISO/IEC 19790, Common Criteria, SESIP.',
            '<b>2. Can the platform boot and run without being tampered with?</b> → TPM, UEFI Secure Boot, NIST SP 800-193, DICE, Measured Boot.',
            '<b>3. Is the supply chain trustworthy?</b> → NIST SP 800-161, ISO 28000, ISO/IEC 20243 (O-TTPS), CMMC, EO 14028 / SBOMs.',
            '<b>4. Does this product meet sector rules?</b> → ISO/SAE 21434 + UN R155 (auto), IEC 62443 (industrial), ETSI EN 303 645 / NIST IR 8259 (IoT), PCI HSM/PTS (payments), DO-326A (avionics), NERC CIP (grid), FDA pre-market cyber (medical).',
            'Underneath sit the <b>algorithm standards</b> (FIPS 197/186/180/202, NIST SP 800-90A/B/C, PQC FIPS 203/204/205) and general control frameworks (NIST SP 800-53, ISO/IEC 27001, NIST CSF).',
        ]),
        "",
    ),

    # =========================================================
    # 01 - Cryptographic Module Standards
    # =========================================================
    (
        "FIPS 140-3",
        "Cryptographic Module Standards",
        "U.S./Canadian standard for validating cryptographic modules — the headline standard in this whole space.",
        ul([
            'Published by NIST + Canadian Centre for Cyber Security; tested under the <b>CMVP</b> (Cryptographic Module Validation Program) by accredited labs.',
            '<b>4 security levels</b> (1 = lowest, software-only OK; 4 = tamper-active, environmental-attack resistant).',
            'Covers <b>11 requirement areas</b>: module spec, ports/interfaces, roles &amp; auth, finite state model, physical security, operational environment, key management, EMI/EMC, self-tests, design assurance, mitigation of other attacks.',
            '<b>Aligns directly with ISO/IEC 19790</b> (140-3 incorporates it by reference) and <b>ISO/IEC 24759</b> for testing.',
            'Mandatory <b>side-channel resistance testing</b> — the single biggest practical change vs 140-2.',
            'Required by FedRAMP, CMMC 2.0, HIPAA-adjacent procurement, and many regulated industries.',
            'A "cryptographic module" can be hardware, firmware, software, or hybrid. Industry shorthand often equates a hardware module with an HSM.',
        ]),
        ul([
            'People confuse <b>"FIPS-compliant"</b> (uses approved algorithms) with <b>"FIPS-validated"</b> (has a CMVP certificate). Only validation has legal weight.',
            'Levels are not linearly more secure for all dimensions — they\'re stepwise-stricter on physical/tamper, with crypto requirements similar across levels.',
        ]),
    ),
    (
        "FIPS 140-2",
        "Cryptographic Module Standards",
        "The previous version of FIPS 140 — being sunset.",
        ul([
            'Predecessor to 140-3.',
            'Side-channel testing was largely <b>undefined</b> (the major gap 140-3 closes).',
            '<b>Sunset: September 21, 2026</b> — all 140-2 validations move to the CMVP Historical List on that date. No new 140-2 submissions accepted now.',
            'Existing validations don\'t become illegal that day, but federal procurement starts treating them as historical.',
        ]),
        "",
    ),
    (
        "ISO/IEC 19790",
        "Cryptographic Module Standards",
        "International twin of FIPS 140-3 — same requirements, different cover page.",
        ul([
            'ISO standard for security requirements for cryptographic modules. FIPS 140-3 is essentially 19790 + U.S. annexes.',
            'Adoption matters internationally: a 19790 certificate may be accepted where FIPS isn\'t.',
        ]),
        "",
    ),
    (
        "ISO/IEC 24759",
        "Cryptographic Module Standards",
        "Test methodology that goes with 19790 / FIPS 140-3.",
        ul([
            'Tells the labs how to test what 19790 requires.',
            'Cited less often than 19790 but it\'s the operational counterpart.',
        ]),
        "",
    ),
    (
        "PCI HSM",
        "Cryptographic Module Standards",
        "Payment-industry standard for HSMs handling card PINs and keys.",
        ul([
            'Issued by the PCI Security Standards Council. Required for HSMs in payment networks.',
            'Covers logical and physical security, key management, and the device\'s whole lifecycle (manufacture → decommission).',
            'Often layered with FIPS 140 — many HSMs hold both.',
        ]),
        "",
    ),
    (
        "ANSI X9.24",
        "Cryptographic Module Standards",
        "Financial-services key management standard, especially for symmetric keys and DUKPT.",
        ul([
            'Defines retail key management for payments.',
            'Worth knowing alongside PCI HSM.',
        ]),
        "",
    ),

    # =========================================================
    # 02 - Product Evaluation Regimes
    # =========================================================
    (
        "Common Criteria (CC) / ISO/IEC 15408",
        "Product Evaluation Regimes",
        "International framework for evaluating IT product security against a defined target.",
        ul([
            'An internationally recognized ISO standard used by governments and large enterprises.',
            'Two key concepts: <b>Target of Evaluation (TOE)</b> = what\'s being evaluated; <b>Protection Profile (PP)</b> = a reusable security requirements template for a class of products.',
            '<b>Evaluation Assurance Levels (EAL) 1–7</b>: EAL1 is functional testing; EAL4+ is the typical commercial sweet spot; EAL5+/6+/7 require formal methods and are rare outside smartcards/HSMs/secure elements.',
            '<b>CCRA</b> (Common Criteria Recognition Arrangement) defines mutual recognition between participating nations — but typically only up to EAL2 / collaborative PPs.',
            'Vendors often dual-stack: FIPS 140-3 for crypto module + CC EAL4+/5+ for the broader product.',
        ]),
        'Higher EAL doesn\'t mean "more secure" — it means "more rigorously evaluated against its stated target." A poorly-scoped TOE at EAL7 can be less secure in practice than a well-scoped EAL4 product.',
    ),
    (
        "SESIP (Security Evaluation Standard for IoT Platforms)",
        "Product Evaluation Regimes",
        "Lightweight CC-derived methodology for IoT platforms.",
        ul([
            'Published by GlobalPlatform.',
            'Designed to cut CC\'s cost/time for IoT, where full EAL evaluations are impractical.',
            'Five assurance levels (<b>SESIP1–SESIP5</b>).',
            'Increasingly referenced by EU Cyber Resilience Act conformity work.',
        ]),
        "",
    ),
    (
        "Protection Profiles (NIAP / collaborative PPs)",
        "Product Evaluation Regimes",
        "Standardized security requirement docs for a product class (firewalls, VPNs, mobile devices, etc.).",
        ul([
            'In the U.S., <b>NIAP</b> (National Information Assurance Partnership) runs the U.S. CC scheme and publishes PPs for federal procurement.',
            'A "PP" makes CC evaluations comparable across vendors in the same product class.',
        ]),
        "",
    ),

    # =========================================================
    # 03 - Hardware Roots of Trust & Trusted Computing
    # =========================================================
    (
        "TPM 2.0 / ISO/IEC 11889",
        "Hardware Roots of Trust",
        "Standardized hardware crypto-coprocessor providing a hardware root of trust.",
        ul([
            'Spec by <b>Trusted Computing Group (TCG)</b>; published as ISO/IEC 11889 (parts 1–4).',
            'Provides: secure key storage, RNG, hashing, sealed storage, <b>PCRs (Platform Configuration Registers)</b> for measured boot, <b>remote attestation</b>, key generation/sealing.',
            'Required for Windows 11.',
            'Implementations: discrete TPM (dTPM, most secure), integrated, firmware TPM (fTPM, runs in CPU TEE), software, virtual.',
            'Common Criteria-certified TPMs typically hit EAL4+ with AVA_VAN.5; FIPS 140-2 Level 2 with physical Level 3 is typical.',
            'Vendors: Infineon, Nuvoton, STMicro (discrete); Intel PTT, AMD fTPM (firmware).',
        ]),
        'Known attacks include <b>TPM reset/forgery via power glitching</b> (resetting PCRs) and <b>bus sniffing</b> between discrete TPM and CPU (Dolos Group 2021 — they read a BitLocker key off the SPI bus). dTPM tamper-resistance only protects the chip itself, not the wires going to it.',
    ),
    (
        "TCG DICE (Device Identifier Composition Engine)",
        "Hardware Roots of Trust",
        "TCG spec for resource-constrained devices to derive identity and attestation from a layered measurement chain.",
        ul([
            'A simpler root-of-trust scheme than TPM, designed for MCUs/IoT where a full TPM is overkill.',
            'Each boot layer derives the next layer\'s identity from a hash of itself.',
        ]),
        "",
    ),
    (
        "UEFI Secure Boot",
        "Hardware Roots of Trust",
        "UEFI specification feature that verifies signed bootloaders/kernels.",
        ul([
            'Defined by the <b>UEFI Forum</b>, not TCG.',
            'Uses platform key (<b>PK</b>), key exchange keys (<b>KEK</b>), and <b>DB/DBX</b> for allowed/revoked signers.',
            'Static — checks signatures only. Pair with TPM-based <b>Measured Boot</b> (logging hashes to PCRs) for remote attestation.',
        ]),
        "",
    ),
    (
        "Measured Boot (S-RTM and D-RTM)",
        "Hardware Roots of Trust",
        "TCG concept where boot-stage hashes are extended into TPM PCRs to attest later what booted.",
        ul([
            '<b>S-RTM (Static Root of Trust for Measurement)</b>: chain starts at power-on, anchored in immutable boot ROM.',
            '<b>D-RTM (Dynamic Root of Trust for Measurement, "late launch")</b>: a secure-launch instruction (Intel TXT, AMD SKINIT) re-establishes a trusted chain after BIOS, reducing TCB.',
            'Underpins remote attestation: a verifier checks PCR values + attestation signature.',
        ]),
        "",
    ),
    (
        "Arm TrustZone & GlobalPlatform TEE",
        "Hardware Roots of Trust",
        "Vendor-supplied secure-world execution + standardized API.",
        ul([
            '<b>TrustZone</b> = Arm hardware feature that splits the CPU into Secure World and Normal World.',
            '<b>GlobalPlatform TEE</b> specs standardize the API/architecture for Trusted Execution Environments — vendor-neutral, not Arm-specific in principle.',
            'TEEs are <b>not the same as HSMs</b> (TEEs share silicon with the rest of the SoC; HSMs are physically separate).',
        ]),
        "",
    ),
    (
        "Intel TXT, Intel SGX, AMD SEV/SEV-SNP",
        "Hardware Roots of Trust",
        "Vendor-specific trusted execution / confidential computing extensions.",
        ul([
            'These are <b>not standards in the ISO/NIST sense</b> — they\'re vendor specs.',
            'They\'re the building blocks for confidential-computing services (Azure Confidential Computing, AWS Nitro, Google Confidential VM).',
            'Referenced by NIST guidance.',
        ]),
        "",
    ),

    # =========================================================
    # 04 - Platform Firmware & Resilience
    # =========================================================
    (
        "NIST SP 800-193 — Platform Firmware Resiliency Guidelines",
        "Platform Firmware & Resilience",
        "Three principles for platform firmware: Protect, Detect, Recover.",
        ul([
            'Published <b>2018</b>. Covers <b>all</b> platform firmware (BIOS, BMC, NIC, GPU, SSD controller, EC, TPM, etc.) — not just BIOS.',
            'Three properties a "resilient" platform must demonstrate:',
            '<b>Protected</b>: a Root of Trust for Update (<b>RTU</b>) authenticates firmware updates; firmware integrity is enforced.',
            '<b>Detection</b>: corrupted firmware can be identified.',
            '<b>Recovery</b>: corrupted firmware can be restored from a known-good copy via a Root of Trust for Recovery (<b>RTRec</b>).',
            '<b>Supersedes the older, narrower SP 800-147 (BIOS Protection) and SP 800-155 (BIOS Integrity Measurement)</b>. Both are still occasionally cited but 800-193 is the modern reference.',
        ]),
        "",
    ),
    (
        "NIST SP 800-147 (legacy)",
        "Platform Firmware & Resilience",
        "BIOS protection guidelines — superseded by 800-193 in scope.",
        ul([
            'Original BIOS Protection Guidelines (<b>2011</b>).',
            'Required signed BIOS updates and write protection.',
            'Still referenced in some procurement specs.',
        ]),
        "",
    ),
    (
        "NIST SP 800-155 (legacy)",
        "Platform Firmware & Resilience",
        "BIOS Integrity Measurement Guidelines — also subsumed by 800-193.",
        ul([
            'Specified what BIOS integrity measurements should look like.',
            'Less practically relevant today.',
        ]),
        "",
    ),
    (
        "UEFI Specification",
        "Platform Firmware & Resilience",
        "The boot firmware spec — security features ride on top.",
        ul([
            'Worth knowing because Secure Boot, capsule updates, and UEFI variables are all defined here.',
            'Not a security standard per se — but the substrate the security features attach to.',
        ]),
        "",
    ),

    # =========================================================
    # 05 - Supply Chain & Hardware Integrity
    # =========================================================
    (
        "NIST SP 800-161 — C-SCRM",
        "Supply Chain & Hardware Integrity",
        "NIST's framework for managing cyber risk in the supply chain.",
        ul([
            'Title: <i>Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations</i> (<b>Rev. 1, 2022</b>).',
            'Maps to NIST SP 800-53 controls in the <b>SR (Supply Chain Risk Management)</b> family.',
            'Heavily referenced by federal procurement after Section 889 (NDAA 2019) and EO 14028.',
        ]),
        "",
    ),
    (
        "ISO/IEC 20243 (O-TTPS)",
        "Supply Chain & Hardware Integrity",
        "Industry standard for COTS ICT product integrity, focused on counterfeits and tainted products.",
        ul([
            'Developed by <b>The Open Group\'s Trusted Technology Forum</b> (O-TTPS = Open Trusted Technology Provider Standard).',
            'Specifically targets supply-chain threats: <b>maliciously tainted and counterfeit products</b>.',
            'Has a certification scheme; popular with U.S. federal contractors.',
        ]),
        "",
    ),
    (
        "ISO 28000:2022",
        "Supply Chain & Hardware Integrity",
        "Generic supply-chain security management system (SeMS) — an ISO management-system standard.",
        ul([
            'Originally maritime-focused (2007), revised in <b>2022</b> to apply to any organization.',
            'Plan-Do-Check-Act structure aligned with ISO 27001/9001/22301. Certifiable.',
            'Less hardware-specific than 800-161 / 20243; treats security like ISO 9001 treats quality.',
        ]),
        "",
    ),
    (
        "CMMC 2.0 (Cybersecurity Maturity Model Certification)",
        "Supply Chain & Hardware Integrity",
        "DoD's certification regime for defense contractors.",
        ul([
            'Three levels (<b>Foundational, Advanced, Expert</b>), built on NIST SP 800-171 and 800-172.',
            'Mandates <b>FIPS 140-3 validated</b> encryption for protecting Controlled Unclassified Information (CUI).',
            'Required for Defense Industrial Base contracts.',
        ]),
        "",
    ),
    (
        "SBOM / HBOM (Software / Hardware Bill of Materials)",
        "Supply Chain & Hardware Integrity",
        "A machine-readable inventory of components — driven by EO 14028.",
        ul([
            '<b>SBOM</b> is mandated by Executive Order 14028 (2021) for software sold to U.S. federal government.',
            '<b>HBOM</b> is the hardware analog; more nascent. CISA published an HBOM framework in <b>2023</b>.',
            'Common formats: <b>SPDX, CycloneDX</b>.',
        ]),
        "",
    ),
    (
        "IEEE 1735",
        "Supply Chain & Hardware Integrity",
        "Standard for encrypting and protecting electronic-design IP.",
        ul([
            'Used in EDA/silicon IP licensing.',
            'Protects RTL/netlists during distribution.',
        ]),
        "",
    ),

    # =========================================================
    # 06 - Cryptographic Algorithms
    # =========================================================
    (
        "FIPS 197 — AES",
        "Cryptographic Algorithms",
        "Advanced Encryption Standard. The symmetric cipher.",
        ul([
            'Block cipher, 128/192/256-bit keys.',
            'AES-128 is broadly fine; <b>CNSA 2.0 requires AES-256</b>.',
        ]),
        "",
    ),
    (
        "FIPS 186-5 — Digital Signature Standard",
        "Cryptographic Algorithms",
        "Defines DSA, ECDSA, EdDSA.",
        ul([
            'Latest revision (<b>186-5, 2023</b>) added <b>EdDSA</b> (Ed25519/Ed448).',
            'Removed plain DSA from new use.',
        ]),
        "",
    ),
    (
        "FIPS 180-4 / FIPS 202 — SHA / SHA-3",
        "Cryptographic Algorithms",
        "Hash function standards.",
        ul([
            '<b>SHA-2</b> family (SHA-256/384/512) in <b>180-4</b>.',
            '<b>SHA-3</b> family (Keccak-based) plus <b>SHAKE128/256 XOFs</b> in <b>202</b>.',
        ]),
        "",
    ),
    (
        "NIST SP 800-90A / 800-90B / 800-90C — RBG",
        "Cryptographic Algorithms",
        "Random bit generation triad — DRBGs, entropy sources, RBG construction.",
        ul([
            '<b>800-90A</b>: deterministic RBGs (Hash_DRBG, HMAC_DRBG, CTR_DRBG). <b>Dual_EC_DRBG was removed</b> after NSA backdoor concerns.',
            '<b>800-90B</b>: entropy source validation (statistical tests, IID/non-IID tracks). Required for FIPS 140-3 modules with hardware RNGs.',
            '<b>800-90C</b>: RBG constructions combining 90A and 90B.',
        ]),
        "",
    ),
    (
        "NIST SP 800-56A/B/C — Key Establishment",
        "Cryptographic Algorithms",
        "Key agreement (DH, ECDH) and key transport (RSA), plus key derivation.",
        ul([
            'FIPS 140-3 modules must use approved key-establishment schemes from these.',
            '<b>56A</b>: discrete-log key agreement (DH, ECDH). <b>56B</b>: integer factorization (RSA key transport). <b>56C</b>: KDFs.',
        ]),
        "",
    ),
    (
        "NIST SP 800-57 — Key Management",
        "Cryptographic Algorithms",
        "General key-management recommendations (key lifecycles, sizes, transitions).",
        ul([
            'Defines <b>security strengths</b>: e.g., 128-bit security ≈ AES-128, RSA-3072, ECC-256.',
            'Reference for sizing keys, picking algorithms, planning algorithm transitions.',
        ]),
        "",
    ),
    (
        "Post-Quantum: FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA)",
        "Cryptographic Algorithms",
        "The first three NIST PQC standards, finalized August 2024.",
        ul([
            '<b>FIPS 203 / ML-KEM</b> (CRYSTALS-Kyber): lattice-based KEM. Replaces RSA/ECDH key establishment.',
            '<b>FIPS 204 / ML-DSA</b> (CRYSTALS-Dilithium): lattice-based signature.',
            '<b>FIPS 205 / SLH-DSA</b> (SPHINCS+): hash-based signature, conservative/stateless.',
            '<b>HQC and FALCON</b> are additional/forthcoming.',
            'NSA\'s <b>CNSA 2.0</b> mandates ML-KEM / ML-DSA / LMS / XMSS for national-security systems by ~2030–2035.',
        ]),
        "",
    ),

    # =========================================================
    # 07 - Sector: Automotive
    # =========================================================
    (
        "ISO/SAE 21434",
        "Sector: Automotive",
        "Process standard for automotive cybersecurity over the vehicle lifecycle.",
        ul([
            'Joint ISO/SAE standard published <b>August 2021</b>.',
            'Mandates <b>CSMS (Cybersecurity Management System)</b> in the organization and <b>TARA (Threat Analysis and Risk Assessment)</b> in the engineering process.',
            'Sibling to <b>ISO 26262</b> (functional safety) — different concerns, similar lifecycle approach.',
            'Covers concept → development → production → operation → decommissioning of E/E systems.',
        ]),
        "",
    ),
    (
        "UNECE WP.29 R155 / R156",
        "Sector: Automotive",
        "UN regulations that legally require automotive cybersecurity (R155) and software-update management (R156) for vehicle type approval.",
        ul([
            '<b>R155</b> = Cybersecurity &amp; CSMS; <b>R156</b> = Software Update Management System (SUMS).',
            'Mandatory in UNECE markets (EU, Japan, South Korea, etc.) for new vehicle <b>types since July 2022</b> and <b>all new vehicles since July 2024</b>.',
            '<b>Not mandatory in U.S./China</b> but de facto influential.',
            '<b>ISO/SAE 21434</b> is the standard most commonly used to <i>demonstrate</i> compliance with R155.',
            '<b>ISO 24089</b> covers the SUMS side (R156).',
        ]),
        "",
    ),

    # =========================================================
    # 08 - Sector: Industrial Control / OT
    # =========================================================
    (
        "IEC 62443 (= ISA/IEC 62443)",
        "Sector: Industrial / OT",
        "The big OT/ICS cybersecurity standards series.",
        ul([
            'Multi-part series in 4 groups: <b>General (-1-x), Policies &amp; Procedures (-2-x), System (-3-x), Components (-4-x)</b>.',
            'Key parts: <b>62443-2-1</b> security program for asset owners; <b>62443-3-2</b> risk assessment + zone/conduit modeling; <b>62443-3-3</b> system security requirements + 4 Security Levels (SL1–SL4); <b>62443-4-1</b> secure product development lifecycle (4 maturity levels); <b>62443-4-2</b> technical security requirements for components.',
            '<b>7 Foundational Requirements (FRs)</b>: Identification &amp; Authentication Control, Use Control, System Integrity, Data Confidentiality, Restricted Data Flow, Timely Response to Events, Resource Availability.',
            'Recognized by IEC as a <b>"horizontal" standard (2021)</b> — applies across all OT-adjacent sectors.',
            'Certification: <b>ISASecure</b> scheme (component, system, and process certifications).',
        ]),
        "",
    ),
    (
        "NERC CIP",
        "Sector: Industrial / OT",
        "Mandatory cybersecurity standards for the North American Bulk Electric System.",
        ul([
            'Enforceable, with fines.',
            'Covers <b>CIP-002 through CIP-014</b>: asset identification, security controls, incident reporting, supply chain (<b>CIP-013</b>), physical security.',
            'U.S./Canada-specific.',
        ]),
        "",
    ),
    (
        "IEC 62351",
        "Sector: Industrial / OT",
        "Security for power-system communication protocols (IEC 60870, 61850, etc.).",
        ul([
            'Sister to 62443 but specifically for power-system protocols.',
            'Covers TLS profiles, role-based access, key management for grid comms.',
        ]),
        "",
    ),

    # =========================================================
    # 09 - Sector: IoT / Consumer
    # =========================================================
    (
        "ETSI EN 303 645",
        "Sector: IoT / Consumer",
        "Baseline cybersecurity requirements for consumer IoT — the global de-facto baseline.",
        ul([
            '<b>13 high-level provisions</b>; the top three: <b>no universal default passwords</b>, <b>vulnerability disclosure policy</b>, <b>keep software updated</b>.',
            'Underpins UK PSTI Act, feeds into EU Cyber Resilience Act compliance.',
            'Has a companion test spec <b>ETSI TS 103 701</b> for conformance assessment.',
        ]),
        "",
    ),
    (
        "NIST IR 8259 series",
        "Sector: IoT / Consumer",
        "U.S. baseline guidance for IoT device manufacturers.",
        ul([
            '<b>8259</b>: foundational activities for manufacturers (pre- and post-market).',
            '<b>8259A</b>: technical core baseline (device identification, configuration, data protection, logical access, software update, cybersecurity state awareness).',
            '<b>8259B</b>: non-technical core baseline (documentation, info dissemination, education, query/complaint, vulnerability disclosure).',
            '<b>8259C/D</b>: profile-creation methodology + federal profile.',
            '<b>8425</b>: consumer IoT profile (technical foundation for FCC <b>Cyber Trust Mark</b>).',
        ]),
        "",
    ),
    (
        "PSA Certified",
        "Sector: IoT / Consumer",
        "Industry IoT certification scheme aligned to multiple regional standards.",
        ul([
            'Founded by <b>Arm</b>; runs three levels:',
            '<b>Level 1</b>: questionnaire-based.',
            '<b>Level 2</b>: lab-evaluated chip.',
            '<b>Level 3</b>: lab-evaluated SoC + side-channel.',
            'Maps to ETSI EN 303 645, NIST IR 8259A, EU CRA, IEC 62443-4-2.',
        ]),
        "",
    ),
    (
        "EU Cyber Resilience Act (CRA)",
        "Sector: IoT / Consumer",
        "EU regulation for cybersecurity of products with digital elements.",
        ul([
            'Adopted <b>October 2024</b>.',
            'Full obligations apply from <b>December 11, 2027</b>.',
            'Covers products with digital elements sold in the EU market.',
            'Feeds into / draws on ETSI EN 303 645, SESIP, and CC for conformity demonstrations.',
        ]),
        "",
    ),
]

deck = genanki.Deck(DECK_ID, 'Hardware Security Standards')

for name, category, oneliner, what_to_know, watch_out_for in cards:
    note = genanki.Note(
        model=model,
        fields=[name, category, oneliner, what_to_know, watch_out_for],
    )
    deck.add_note(note)

output_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(output_dir, 'hardware_security_standards.apkg')
deck.write_to_file(output_path)

size_kb = os.path.getsize(output_path) / 1024
print(f"Created deck with {len(cards)} cards")
print(f"Deck size: {size_kb:.1f} KB")
print(f"Saved to: {output_path}")
