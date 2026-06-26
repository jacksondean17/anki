#!/usr/bin/env python3
"""Generate an Anki deck for Security & Compliance Certifications."""
import genanki
import os

MODEL_ID = 1739205847
DECK_ID = 2061739845

model = genanki.Model(
    MODEL_ID,
    'Security & Compliance Certifications',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
    ],
    templates=[{
        'name': 'Card',
        'qfmt': '<div class="front">{{Front}}</div>',
        'afmt': '{{FrontSide}}<hr id="answer"><div class="back">{{Back}}</div>',
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
        .front {
            font-size: 28px;
            font-weight: bold;
            color: #1e3a8a;
        }
        .back {
            font-size: 16px;
            text-align: left;
            line-height: 1.55;
            color: #1a1a1a;
            max-width: 760px;
            margin: 0 auto;
        }
        .back .label {
            color: #1e3a8a;
            font-weight: bold;
        }
        .back .row {
            margin-bottom: 8px;
        }
        .back .category {
            display: inline-block;
            background: #1e3a8a;
            color: #fff;
            font-size: 12px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            padding: 3px 10px;
            border-radius: 4px;
            margin-bottom: 12px;
        }
        .back .divider {
            border: 0;
            border-top: 1px dashed #c8c8c8;
            margin: 12px 0;
        }
        .back .extras .label {
            color: #4b5563;
        }
        hr#answer {
            border: 0;
            border-top: 1px solid #d0d0d0;
            margin: 16px 0;
        }
    '''
)


def back(
    category,
    type_,
    application,
    jurisdiction,
    body,
    included,
    strictness,
    commonality,
    renewal,
    cost,
    overlaps,
    cert_vs_continuous,
):
    return (
        f'<div class="category">{category}</div>'
        f'<div class="row"><span class="label">Type:</span> {type_}</div>'
        f'<div class="row"><span class="label">Application / Industry:</span> {application}</div>'
        f'<div class="row"><span class="label">Jurisdiction:</span> {jurisdiction}</div>'
        f'<div class="row"><span class="label">Governing body:</span> {body}</div>'
        f"<div class=\"row\"><span class=\"label\">What's included:</span> {included}</div>"
        f'<div class="row"><span class="label">Strictness:</span> {strictness}</div>'
        f'<div class="row"><span class="label">Commonality:</span> {commonality}</div>'
        f'<hr class="divider">'
        f'<div class="extras">'
        f'<div class="row"><span class="label">Renewal / cadence:</span> {renewal}</div>'
        f'<div class="row"><span class="label">Cost / effort:</span> {cost}</div>'
        f'<div class="row"><span class="label">Relationships / overlaps:</span> {overlaps}</div>'
        f'<div class="row"><span class="label">Certificate vs. continuous:</span> {cert_vs_continuous}</div>'
        f'</div>'
    )


cards = [
    # =========================================================
    # 01 - ISMS / General
    # =========================================================
    (
        "SOC 2",
        back(
            "ISMS / General",
            'Certification (independent audit → attestation report; "Type I" = point in time, "Type II" = over a period, usually 6–12 months)',
            'The default trust credential for US-based B2B SaaS and service providers; routinely demanded by enterprise customers during vendor due diligence.',
            'United States (recognized globally, but a US/AICPA construct)',
            'AICPA (American Institute of CPAs); report issued by a licensed CPA firm',
            'Controls mapped to the five Trust Services Criteria — Security (required), plus optionally Availability, Processing Integrity, Confidentiality, Privacy. Principles-based: you design controls, the auditor tests them.',
            'Medium — rigorous independent audit, but you define your own controls; no fixed checklist to pass.',
            'Ubiquitous in US SaaS.',
            'Type I is point-in-time; Type II covers a 6–12 month observation window and is typically refreshed annually.',
            'Moderate — readiness work + CPA audit; commonly $30k–$150k+ in year one, less after.',
            'Often crosswalked to ISO 27001, HITRUST, and NIST CSF; SOC 1 (financial reporting) and SOC 3 (public summary) are sister reports.',
            'Continuous in spirit — Type II reports tie credibility to operating effectiveness over a period.',
        ),
    ),
    (
        "ISO/IEC 27001",
        back(
            "ISMS / General",
            'Certification (accredited certification body audit → certificate, 3-year cycle with annual surveillance)',
            'The international gold standard for an Information Security Management System (ISMS); favored by global/European enterprises and anyone selling internationally.',
            'Global',
            'ISO/IEC; certificates issued by accredited certification bodies',
            'Requirements for an ISMS (clauses 4–10: context, leadership, risk management, operation, performance evaluation, improvement) plus Annex A\'s 93 controls (organizational, people, physical, technological).',
            'High — formal management system, mandatory risk assessment, third-party certification.',
            'Ubiquitous globally (the international counterpart to SOC 2).',
            '3-year certification cycle: Stage 1 + Stage 2 audit, annual surveillance audits, recertification in year 3.',
            'Moderate–High — ISMS build-out + accredited body audit; typically $30k–$100k+ for first certification.',
            'Extended by 27017 (cloud), 27018 (cloud PII), 27701 (privacy), 42001 (AI); informed by 27002 guidance; widely crosswalked to SOC 2.',
            'Continuous — a living ISMS with ongoing monitoring, internal audits, and management review.',
        ),
    ),
    (
        "ISO/IEC 27002",
        back(
            "ISMS / General",
            'Reference framework (guidance, not certifiable on its own)',
            'Implementation companion to 27001 — the detailed "how-to" for the Annex A controls.',
            'Global',
            'ISO/IEC',
            'Detailed guidance for each of the 93 information security controls (purpose, implementation guidance).',
            'N/A — guidance only; you certify against 27001, not 27002.',
            'Common (used alongside 27001).',
            'N/A — guidance document; ISO refreshes it on a multi-year cycle (last major rev 2022).',
            'Cost of purchasing the standard + the cost of implementing the controls themselves.',
            'Direct companion to ISO 27001 Annex A; basis for many sector-specific control catalogs.',
            'Neither — reference document, not an attestation.',
        ),
    ),
    (
        "ISO/IEC 27017",
        back(
            "ISMS / General",
            'Certification (extension audited alongside 27001)',
            'Cloud service providers and cloud customers wanting cloud-specific assurance.',
            'Global',
            'ISO/IEC',
            'Cloud-specific security controls and guidance layered on 27002 — shared responsibility, virtual environment segregation, admin operations, cloud monitoring.',
            'High (inherits 27001 rigor).',
            'Moderate (common among cloud providers).',
            'Audited on the parent 27001 3-year cycle with annual surveillance.',
            'Incremental to 27001 — modest add-on scope/fees.',
            'Cloud extension to ISO 27001/27002; typically paired with 27018 and SOC 2 by cloud providers.',
            'Continuous — rides on the underlying 27001 ISMS.',
        ),
    ),
    (
        "ISO/IEC 27018",
        back(
            "ISMS / General",
            'Certification (extension audited alongside 27001)',
            'Cloud providers processing personally identifiable information (PII) as processors.',
            'Global',
            'ISO/IEC',
            'Code of practice for protecting PII in public clouds — consent, transparency, data handling, return/transfer/disposal of PII.',
            'High (inherits 27001 rigor).',
            'Moderate.',
            'Audited on the parent 27001 3-year cycle with annual surveillance.',
            'Incremental to 27001 — modest add-on scope/fees.',
            'PII-in-cloud extension to 27001/27002; complements 27017 and is often used to evidence GDPR processor obligations.',
            'Continuous — rides on the underlying 27001 ISMS.',
        ),
    ),
    (
        "ISO/IEC 27701",
        back(
            "ISMS / General",
            'Certification (privacy extension to 27001/27002)',
            'Organizations wanting a certifiable Privacy Information Management System (PIMS); often used to demonstrate GDPR-style accountability.',
            'Global',
            'ISO/IEC',
            'PIMS requirements extending the ISMS to privacy; controls for data controllers and processors.',
            'High.',
            'Moderate and growing.',
            'Audited on the parent 27001 3-year cycle with annual surveillance.',
            'Incremental to 27001 — meaningful scope add for privacy controls.',
            'PIMS extension to 27001/27002; widely used to evidence GDPR Art. 5(2) accountability and to map to CCPA/CPRA.',
            'Continuous — rides on the underlying 27001 ISMS.',
        ),
    ),
    (
        "ISO/IEC 42001",
        back(
            "ISMS / General",
            'Certification (AI management system, audited like 27001)',
            'Organizations building or deploying AI systems wanting a governance credential; emerging differentiator for AI vendors.',
            'Global',
            'ISO/IEC',
            'Requirements for an AI Management System (AIMS) — AI risk/impact assessment, lifecycle controls, transparency, accountability.',
            'High (formal management system; new but rigorous).',
            'Niche but rising fast (first AI management-system standard).',
            '3-year cycle with annual surveillance, like other ISO management-system standards.',
            'Moderate–High — full AIMS build-out + third-party audit; market is new and prices are still settling.',
            'Shares the Annex SL structure with 27001/9001; complements NIST AI RMF and supports EU AI Act conformity.',
            'Continuous — requires an operating AIMS with ongoing reviews and improvements.',
        ),
    ),
    (
        "ISO 50001",
        back(
            "ISMS / General",
            'Certification (energy management system)',
            'Energy-intensive operations — data centers, manufacturing, facilities wanting to demonstrate efficiency.',
            'Global',
            'ISO',
            'Energy Management System requirements — energy policy, baselines, performance indicators, continual improvement.',
            'Medium–High.',
            'Moderate (mainly industrial/facilities).',
            '3-year cycle with annual surveillance audits.',
            'Moderate — energy baseline work + certification body fees; ROI often via reduced energy spend.',
            'Often integrated with ISO 14001 (environmental) and 9001 (quality); aligned with EU Energy Efficiency Directive reporting.',
            'Continuous — energy performance must demonstrably improve over time.',
        ),
    ),
    (
        "ISO 14001",
        back(
            "ISMS / General",
            'Certification (environmental management system)',
            'Broad — any organization demonstrating environmental responsibility; common in manufacturing, construction, data centers.',
            'Global',
            'ISO',
            'Environmental Management System requirements — environmental aspects/impacts, compliance obligations, objectives, continual improvement.',
            'Medium–High.',
            'Common (one of the most widely held ISO certs worldwide).',
            '3-year cycle with annual surveillance audits.',
            'Moderate — EMS build-out + certification body fees.',
            'Shares Annex SL structure with 9001/27001/50001; commonly integrated into combined management systems.',
            'Continuous — requires ongoing EMS operation and demonstrated improvement.',
        ),
    ),
    # =========================================================
    # 02 - Government / Defense
    # =========================================================
    (
        "NIST SP 800-53 (Rev 5)",
        back(
            "Government / Defense",
            'Reference framework (control catalog; not certifiable by itself)',
            'US federal systems and contractors; the master catalog that FedRAMP, FISMA, CJIS and others draw from.',
            'United States (federal)',
            'NIST',
            '~1,000 security and privacy controls across 20 families (Access Control, Physical & Environmental, Incident Response, etc.), applied at Low/Moderate/High baselines.',
            'Very High (the most comprehensive control set here), though applicability scales by baseline.',
            'Common in gov/defense; foundational reference everywhere.',
            'NIST updates the catalog on a multi-year cycle (Rev 5 → patches); systems re-assess per their own authorization cadence.',
            'No fee for the catalog; implementation cost is substantial — often $100k–multi-million for large federal systems.',
            'Underpins FedRAMP, FISMA, CJIS, CMMC (via 800-171), StateRAMP/TX-RAMP; widely crosswalked to ISO 27001.',
            'Reference — but the programs built on it (FedRAMP ConMon, FISMA) demand continuous monitoring.',
        ),
    ),
    (
        "NIST SP 800-171 (Rev 2 / Rev 3)",
        back(
            "Government / Defense",
            'Reference framework / mandatory by contract (basis for CMMC certification)',
            'Defense and federal contractors handling Controlled Unclassified Information (CUI).',
            'United States (federal/DoD supply chain)',
            'NIST',
            'The CUI-protection subset of 800-53 — 110 requirements (Rev 2) across 14 families; Rev 3 restructured/consolidated them.',
            'High (mandatory for CUI; enforced via CMMC).',
            'Common across the defense industrial base.',
            'NIST refreshes the standard (Rev 2 → Rev 3); contractor self-attestation or CMMC re-certification follows contract cadence.',
            'Variable — modest for small contractors with thin CUI scope, significant for large primes with broad CUI flows.',
            'Derived from 800-53 Moderate; operationalized through DFARS 252.204-7012 and the CMMC program.',
            'Reference — continuous compliance is required by contract; certification mechanism is CMMC.',
        ),
    ),
    (
        "NIST Cybersecurity Framework (CSF) 2.0",
        back(
            "Government / Defense",
            'Reference framework (voluntary, outcome-based)',
            'Cross-sector risk management and board-level communication; widely used to organize a security program.',
            'United States (used globally)',
            'NIST',
            'Outcomes organized by six Functions — Govern, Identify, Protect, Detect, Respond, Recover — pointing to catalogs like 800-53 for the "how."',
            'Low–Medium (voluntary, no pass/fail; you choose target profile).',
            'Ubiquitous as an organizing framework.',
            'No formal cycle — NIST updates the framework periodically (2.0 published 2024); organizations re-baseline as the program matures.',
            'Free to adopt; cost is internal program effort.',
            'Maps to 800-53, ISO 27001, COBIT, HIPAA, PCI DSS, and most major control catalogs; often the umbrella over them.',
            'Reference — used as a continuous program-management tool via Profiles and Tiers.',
        ),
    ),
    (
        "FISMA",
        back(
            "Government / Defense",
            'Regulation/Law (US statute)',
            'US federal agencies and their contractors/cloud providers.',
            'United States (federal)',
            'Congress (statute); implemented by NIST + OMB; overseen by agency CIOs/DHS',
            'Mandates an agency-wide information security program; categorize systems (FIPS 199), meet minimum requirements (FIPS 200), implement 800-53 controls at the relevant baseline.',
            'High (legally mandated; tied to 800-53).',
            'Common in the federal space.',
            'Continuous monitoring required; annual FISMA reporting to OMB; system reauthorization on agency cadence (typically every 3 years).',
            'Substantial for agencies — full Assessment & Authorization package, ConMon program, IG audits.',
            'Implemented via NIST RMF (800-37) and 800-53; FedRAMP satisfies FISMA for cloud services consumed by agencies.',
            'Continuous — Authorization to Operate (ATO) sustained by continuous monitoring.',
        ),
    ),
    (
        "FedRAMP",
        back(
            "Government / Defense",
            'Certification / authorization (government authorization to operate)',
            'Cloud service providers selling to US federal agencies.',
            'United States (federal)',
            'GSA FedRAMP PMO (with the FedRAMP Board); assessed by accredited 3PAOs',
            'Adopts the 800-53 control set at Low/Moderate/High; independent assessment (3PAO) leading to an Authorization to Operate (ATO).',
            'Very High (independent assessment + government authorization; lengthy and costly).',
            'Common for govcloud vendors; niche otherwise.',
            'ATO is ongoing; monthly ConMon deliverables, annual assessment, significant-change reauthorizations.',
            'High — Moderate authorization typically $500k–$2M+ including 3PAO fees, remediation, and ongoing ConMon.',
            'Built on 800-53; recognized basis for StateRAMP and DoD IL2/IL4/IL5; satisfies FISMA for federal cloud use.',
            'Continuous — the ATO is sustained by ConMon, not a point-in-time certificate.',
        ),
    ),
    (
        "CMMC",
        back(
            "Government / Defense",
            'Certification (third-party assessment, tiered)',
            'Defense contractors (DIB) handling FCI/CUI; required to win DoD contracts.',
            'United States (DoD supply chain)',
            'US Department of Defense (32 CFR Part 170); assessments by C3PAOs under the Cyber AB',
            'Three levels built on 800-171/800-172; Level 1 self-assessment, Levels 2–3 require third-party/government assessment.',
            'Very High at Levels 2–3 (certification gates contract eligibility).',
            'Becoming common across the defense industrial base.',
            'Level 1 annual self-assessment; Levels 2 & 3 every 3 years with annual affirmation of continued compliance.',
            'Level 1 minimal; Level 2 C3PAO assessment commonly $100k–$500k+; Level 3 (DIBCAC-led) substantially more.',
            'Built on NIST 800-171 (Level 2) and 800-172 (Level 3); 800-53 lineage; anchored in DFARS contract clauses.',
            'Certification — point-in-time assessment with annual affirmation between recertifications.',
        ),
    ),
    (
        "CJIS Security Policy (v6.0)",
        back(
            "Government / Defense",
            'Regulation/policy (mandatory for access to the data; compliance-audited)',
            'Law enforcement and any vendor touching Criminal Justice Information (CJI) — incl. cloud providers serving police/courts.',
            'United States',
            'FBI CJIS Division (audited by FBI/state CJIS Systems Agencies)',
            'Now aligned to 800-53; the "physically secure location" concept plus access control, monitoring, encryption, personnel screening, incident response.',
            'High (mandatory; periodic audits).',
            'Common in govtech/public safety; niche elsewhere.',
            'Audited triennially by the FBI or state CJIS Systems Agencies; policy revised on a rolling basis.',
            'Moderate — fingerprint/background screening, control implementation, and recurring audits.',
            'Now largely aligned to NIST 800-53; mandatory for any system that stores, processes, or transmits CJI.',
            'Continuous — compliance must be maintained; audits are periodic.',
        ),
    ),
    (
        "NERC CIP (e.g., CIP-006-6)",
        back(
            "Government / Defense",
            'Regulation (mandatory reliability standards; fines for non-compliance)',
            'Owners/operators of the North American Bulk Electric System (electric utilities).',
            'United States & Canada (bulk power system)',
            'NERC (enforced under FERC); regional entities audit',
            'Critical Infrastructure Protection standards — among the most prescriptive physical security here: documented physical security plan, Physical Security Perimeter, escorting/logging, alarm-on-access within 15 minutes, testing every 24 months.',
            'Very High (prescriptive, mandatory, financially enforced).',
            'Niche (utilities only) but mandatory there.',
            'Continuous compliance; spot audits, self-reports, and periodic full audits (typical 3–6 year cadence).',
            'Very High — large utilities spend tens of millions on compliance; fines reach up to $1M per day, per violation.',
            'U.S. enforcement under FERC; influences other critical-infrastructure frameworks; concepts borrowed from 800-53.',
            'Continuous — ongoing compliance with formal sanctions for lapses.',
        ),
    ),
    (
        "Sarbanes-Oxley (SOX)",
        back(
            "Government / Defense",
            'Regulation/Law (US statute)',
            'US public companies (and their auditors) — financial reporting integrity, with IT general controls in scope.',
            'United States',
            'SEC + PCAOB (statute: Pub. L. 107-204)',
            'Internal control over financial reporting; security relevance is indirect — access controls over financial systems/records (ITGCs), change management, audit trails. Minimal prescribed physical security.',
            'High for financial controls (external audit, executive liability).',
            'Ubiquitous among US public companies.',
            'Annual external audit of ICFR (Sec 404(b)); quarterly management certifications (Sec 302).',
            'High — external audit fees plus internal SOX program; commonly multi-million for large public companies.',
            'ITGCs typically follow COBIT/COSO; significant overlap with SOC 1; touches the same control domains as 27001.',
            'Continuous — controls must operate effectively throughout the fiscal year, then attested annually.',
        ),
    ),
    (
        "BSI C5:2020",
        back(
            "Government / Defense",
            'Certification (attestation, audited like SOC 2 by an auditor)',
            'Cloud service providers serving the German market (and German public sector).',
            'Germany (influential across EU)',
            'BSI (German Federal Office for Information Security)',
            'Cloud Computing Compliance Criteria Catalogue — security criteria across domains (org, physical, ops, identity, crypto, etc.), demonstrated via an ISAE 3000-style audit report.',
            'High.',
            'Common in Germany; niche elsewhere.',
            'Annual ISAE 3000/3402-style attestation; Type 2 reports cover an observation window similar to SOC 2.',
            'Moderate–High — comparable to SOC 2 Type II with a German-licensed auditor.',
            'Reuses many SOC 2 / ISO 27001 controls; effectively mandatory for German federal cloud procurement.',
            'Continuous — Type 2 attestation covers a period of operation.',
        ),
    ),
    (
        "Esquema Nacional de Seguridad (Spain ENS)",
        back(
            "Government / Defense",
            'Certification / mandatory scheme (certifiable; mandatory for public sector + suppliers)',
            'Spanish public-sector bodies and their technology suppliers.',
            'Spain',
            'Government of Spain (Royal Decree 311/2022); CCN-CERT oversight',
            'Security framework with Basic/Medium/High categories; controls across organizational, operational, and protection measures.',
            'High (mandatory for the public sector).',
            'Niche (Spain-specific).',
            'Certification valid 2 years for Medium/High (annual declaration for Basic), with periodic surveillance.',
            'Moderate — accredited certification body fees + control implementation.',
            'Aligned with ISO 27001 and EU NIS2; mandatory for Spanish public sector and their suppliers.',
            'Continuous — ongoing operation; periodic recertification.',
        ),
    ),
    (
        "UK Cyber Essentials",
        back(
            "Government / Defense",
            'Certification (two tiers: Cyber Essentials self-assessment, Cyber Essentials Plus with hands-on technical audit)',
            'UK SMEs and any supplier to UK government; an accessible baseline credential.',
            'United Kingdom',
            'UK NCSC (delivered by IASME)',
            'Five technical controls — firewalls, secure configuration, user access control, malware protection, security update management.',
            'Low (basic, self-assessed) to Medium (Plus, audited). Entry-level by design.',
            'Common in the UK (often required for public contracts).',
            'Annual recertification for both tiers.',
            'Low — Cyber Essentials ~£300–£500; Cyber Essentials Plus ~£1.5k–£6k+ depending on organisation size.',
            'A subset of broader frameworks (ISO 27001, NIST CSF); often a prerequisite for UK government contracts.',
            'Point-in-time certificate renewed annually.',
        ),
    ),
    (
        "Australian Government ISM",
        back(
            "Government / Defense",
            'Reference framework / mandatory for government (basis for assessment, e.g., IRAP)',
            'Australian government agencies and their providers; cloud providers assessed via IRAP.',
            'Australia',
            'Australian Signals Directorate (ASD) / ACSC',
            'Comprehensive cyber security manual — cyber principles plus detailed guidelines across 25 domains (incl. physical security, media, system hardening, cryptography, gateways).',
            'High (extensive controls; mandatory for government systems).',
            'Common in Australia; niche elsewhere.',
            'ISM updated quarterly; IRAP assessments typically every 2 years for government cloud workloads.',
            'Moderate–High for an IRAP assessment; substantially more for full PROTECTED-level systems.',
            'Aligned with the ASD Essential Eight; analogous role to NIST 800-53 / FedRAMP in Australia.',
            'Continuous — government systems must maintain compliance; IRAP assessments are periodic.',
        ),
    ),
    # =========================================================
    # 03 - Industry-Specific (Privacy / Sector)
    # =========================================================
    (
        "HIPAA",
        back(
            "Industry-Specific (Privacy / Sector)",
            'Regulation/Law (US statute + rules; no certification, only compliance)',
            'US healthcare — covered entities (providers, plans, clearinghouses) and their business associates (incl. health-tech vendors).',
            'United States',
            'HHS Office for Civil Rights (enforcement)',
            'Security Rule (administrative, physical, technical safeguards for ePHI), Privacy Rule (use/disclosure of PHI), Breach Notification Rule. 45 CFR Part 164.',
            'High (legally enforced; significant fines), though the Security Rule is risk-based/"addressable."',
            'Ubiquitous in US healthcare.',
            'No formal cycle — continuous compliance; risk analyses must be updated regularly; OCR audits/investigations are incident-driven.',
            'Highly variable — small practice modest; large covered entity many millions including breach response and corrective action.',
            'Often demonstrated via HITRUST CSF or SOC 2 + HIPAA mapping; complements state laws like NY SHIELD.',
            'Continuous — no certificate; compliance required at all times.',
        ),
    ),
    (
        "GDPR",
        back(
            "Industry-Specific (Privacy / Sector)",
            'Regulation/Law (EU regulation; no certificate, though certification mechanisms exist)',
            'Any organization processing personal data of people in the EU/EEA — effectively global reach.',
            'European Union / EEA (extraterritorial)',
            'EU; enforced by national Data Protection Authorities',
            'Lawful basis, data subject rights, accountability, DPIAs, breach notification (72h), data protection by design/default, transfer rules; fines up to 4% of global turnover.',
            'Very High (broad scope, large fines).',
            'Ubiquitous (anyone with EU users).',
            'Continuous compliance; DPIA refresh on changes; voluntary certifications (e.g., Europrivacy) valid up to 3 years.',
            'Variable — DPO, records of processing, DPIAs, vendor management; fines up to 4% of global turnover.',
            'Operationalized via ISO 27701, BCRs, SCCs; complemented by ePrivacy, EU AI Act, EU Data Act.',
            'Continuous — Art. 5(2) accountability requires ongoing demonstration, not a one-time certificate.',
        ),
    ),
    (
        "CCPA / CPRA",
        back(
            "Industry-Specific (Privacy / Sector)",
            'Regulation/Law (US state statute)',
            "Businesses handling California residents' personal information above set thresholds.",
            'California, USA',
            'California Privacy Protection Agency (CPPA) + state AG',
            'Consumer rights (know, delete, correct, opt-out of sale/sharing), notice requirements, data minimization, contractor obligations.',
            'High (enforced; the de facto US state-privacy baseline).',
            'Common (any consumer business with California customers).',
            'Continuous compliance; privacy notice must be reviewed and updated at least every 12 months.',
            'Moderate — privacy notices, consumer request workflow, vendor contracts, ongoing legal advisory.',
            'Increasingly aligned with other US state privacy laws (VA CDPA, CO CPA, etc.) and many GDPR concepts.',
            'Continuous — enforced by CPPA/AG; no certificate.',
        ),
    ),
    (
        "GLBA",
        back(
            "Industry-Specific (Privacy / Sector)",
            'Regulation/Law (US statute + Safeguards Rule)',
            'US financial institutions and companies "significantly engaged" in financial activities (incl. fintech).',
            'United States',
            'FTC (Safeguards Rule, 16 CFR Part 314) + banking regulators',
            'Information security program requirements (risk assessment, access controls, encryption, MFA, vendor oversight, incident response) plus privacy notices/sharing limits.',
            'High (legally mandated; the updated Safeguards Rule is prescriptive).',
            'Common in financial services.',
            'Continuous; written program must be reviewed/updated; annual board reporting; periodic risk-assessment refresh.',
            'Moderate–High depending on institution size; typically folded into broader bank examination program cost.',
            'The updated Safeguards Rule (2023) overlaps heavily with NIST CSF and 27001; pairs with NYDFS Part 500 and SOX.',
            'Continuous — ongoing program required; FTC/banking-regulator examinations.',
        ),
    ),
    (
        "FERPA",
        back(
            "Industry-Specific (Privacy / Sector)",
            'Regulation/Law (US statute)',
            'Schools/universities receiving federal funding and their ed-tech vendors.',
            'United States',
            'US Department of Education',
            'Protects privacy of student education records; consent for disclosure, rights to access/amend; security is implied via the duty to protect records. 20 USC 1232g / 34 CFR Part 99.',
            'Medium (privacy-focused; enforcement via funding withdrawal, no fixed security checklist).',
            'Common in education.',
            'Continuous; complaint-driven enforcement; no formal audit cycle.',
            'Low–Moderate — policy/training-heavy; rises with vendor contracting complexity.',
            'Often paired with state student-privacy laws (SOPIPA), COPPA, and PPRA; ed-tech vendors usually combine with SOC 2.',
            'Continuous — no certificate; the enforcement lever is loss of federal funding.',
        ),
    ),
    (
        "PCI DSS (v4.0.1)",
        back(
            "Industry-Specific (Privacy / Sector)",
            'Certification / mandatory standard (validated via SAQ or QSA assessment → AOC; contractual not legal)',
            'Any organization that stores, processes, or transmits payment card data (merchants, processors, gateways).',
            'Global (contractual, via card brands/acquirers)',
            'PCI Security Standards Council (Visa, Mastercard, etc.)',
            '12 requirements / 6 goals — network security, protect cardholder data, vuln management, strong access control (incl. physical access to card data), monitoring/testing, security policy.',
            'High (prescriptive checklist; level of validation scales with transaction volume).',
            'Ubiquitous wherever card payments are handled.',
            'Annual validation (SAQ or RoC/AoC); quarterly ASV external scans; ongoing in-scope monitoring.',
            'Wide range — small merchants $300–$5k (SAQ); large merchants/processors $100k–$1M+ for QSA engagements.',
            'Cardholder-data focus overlaps heavily with SOC 2 and ISO 27001; informs P2PE, 3DS, and PIN security standards.',
            'Continuous — must be in compliance every day; validated annually (RoC/SAQ) with quarterly scans.',
        ),
    ),
    # =========================================================
    # 04 - Data Center / Facility
    # =========================================================
    (
        "Uptime Institute Tier Standard",
        back(
            "Data Center / Facility",
            'Certification (facility certification, Tiers I–IV)',
            'Data center owners/operators and colocation providers proving availability/redundancy.',
            'Global',
            'Uptime Institute',
            'Tier I–IV ratings for site infrastructure topology (power, cooling redundancy, fault tolerance, concurrent maintainability) plus operational sustainability (staffing, maintenance, site management).',
            'High and objective (Tier IV requires fault tolerance; certified by on-site assessment).',
            'Common in the data-center industry (the recognized availability benchmark).',
            'Design (TCDD) → Constructed Facility (TCCF) are point-in-time; Operational Sustainability (TCOS) renews every 2 years.',
            'High — six figures+ for the design, constructed-facility, and operational-sustainability assessments combined.',
            'Often paired with ANSI/TIA-942 and EN 50600 design standards; complementary to ISO 27001 site/physical controls.',
            'Mixed — TCDD/TCCF are point-in-time; TCOS is renewed every 2 years to remain in good standing.',
        ),
    ),
    (
        "EN 50600 series",
        back(
            "Data Center / Facility",
            'Reference/standard (certifiable via conformity assessment)',
            'European data center design, build, and operation.',
            'Europe (CENELEC)',
            'CENELEC (European standards)',
            'Facility and infrastructure standards — building construction, power distribution, environmental control, telecom cabling, security, plus availability/energy-efficiency (KPI) classes.',
            'High (comprehensive engineering standard).',
            'Moderate in Europe; the EU counterpart to Uptime/TIA-942.',
            'Continuous compliance; conformity assessment cadence varies by scheme.',
            'Cost of the (multi-part) standard documents + significant engineering and assessment cost.',
            'Largely harmonized with ISO 22237; competes/overlaps with Uptime Tier and ANSI/TIA-942.',
            'Reference standard — third-party certification schemes built on it are continuous.',
        ),
    ),
    (
        "ANSI/TIA-942",
        back(
            "Data Center / Facility",
            'Reference/standard (certifiable via third-party schemes)',
            'Data center telecommunications infrastructure design.',
            'United States / global',
            'TIA (Telecommunications Industry Association)',
            'Data center infrastructure standard with its own Rated 1–4 reliability tiers covering telecom, architecture, electrical, mechanical, and security.',
            'High (detailed engineering spec).',
            'Common in data-center design (often used alongside/instead of Uptime).',
            'Recertification typically every 3 years under accredited schemes (e.g., EPI).',
            'High — comprehensive engineering review.',
            'Overlaps with Uptime Tier and EN 50600; specifies telecom/cabling infrastructure in more depth than either.',
            'Certification — periodic recertification.',
        ),
    ),
    (
        "ISO 22237 series",
        back(
            "Data Center / Facility",
            'Reference/standard',
            'International data center facilities and infrastructure.',
            'Global',
            'ISO/IEC',
            'Multi-part standard on data center infrastructure — general concepts, building construction, power, environmental control, cabling, security systems, availability/granularity classes.',
            'High.',
            'Moderate (the ISO analog to EN 50600).',
            'Continuous, with conformity assessment per scheme.',
            'Cost of the standard documents + assessment.',
            'ISO/IEC counterpart to EN 50600; integrates with broader ISO management-system standards.',
            'Reference standard — certifiable through third-party schemes.',
        ),
    ),
    (
        "LEED (v4.1 / v5)",
        back(
            "Data Center / Facility",
            'Certification (green-building rating, Certified→Platinum)',
            'Buildings (incl. data centers and corporate facilities) demonstrating sustainability — often a marketing/ESG credential.',
            'Global (US-origin)',
            'US Green Building Council (USGBC); certified by GBCI',
            'Points across energy, water, materials, indoor environmental quality, location, etc.; not a security standard.',
            'Medium (points-based; level depends on score).',
            'Common for real estate/facilities; tangential to security.',
            'Building Design + Construction certs are typically one-time; LEED O+M (Operations + Maintenance) recertifies every 3 years.',
            'Moderate — registration ~$1.5k, certification fees, plus design/commissioning premiums.',
            'Complements ENERGY STAR, BREEAM, WELL; relates to ISO 14001/50001 for operational sustainability.',
            'Mostly point-in-time (BD+C); the O+M variant is continuous.',
        ),
    ),
    # =========================================================
    # 05 - Emerging / AI
    # =========================================================
    (
        "EU AI Act",
        back(
            "Emerging / AI",
            'Regulation/Law (EU regulation)',
            'Providers, deployers, importers of AI systems touching the EU market — risk-tiered by use case.',
            'European Union (extraterritorial)',
            'EU; enforced via the AI Office + national authorities',
            'Risk-based rules — prohibited practices, strict obligations for "high-risk" AI (risk management, data governance, transparency, human oversight, robustness, conformity assessment), transparency duties for limited-risk, GPAI model obligations.',
            'Very High for high-risk/GPAI (fines up to 7% of global turnover); phased rollout.',
            'Becoming common (any AI vendor with EU exposure).',
            'Continuous compliance; phased applicability through 2026–2027; high-risk systems require ongoing conformity and post-market monitoring.',
            'Potentially very high for high-risk/GPAI providers — risk management, technical documentation, post-market monitoring, incident reporting.',
            'Interlocks with GDPR, EU Data Act, NIS2, Product Liability Directive; ISO 42001 can support conformity demonstrations.',
            'Continuous — conformity assessment + post-market monitoring + incident reporting throughout the lifecycle.',
        ),
    ),
    (
        "EU Data Act",
        back(
            "Emerging / AI",
            'Regulation/Law (EU regulation)',
            'Manufacturers of connected/IoT products, data holders, and cloud providers; governs access to and sharing of data.',
            'European Union',
            'EU; national authorities',
            'Rights to access/port data from connected products, B2B/B2G data sharing terms, cloud switching (anti-lock-in) obligations, interoperability, safeguards against unlawful international data access.',
            'High.',
            'Niche today, rising (IoT/cloud sectors).',
            'Continuous compliance; key obligations apply from September 2025.',
            'Moderate–High for connected-product manufacturers and cloud providers (cloud-egress redesign, interoperability work).',
            'Complements GDPR (non-personal data focus), Data Governance Act, and the EU AI Act.',
            'Continuous — no certificate, statutory obligations.',
        ),
    ),
    (
        "California SB 53 (TFAIA)",
        back(
            "Emerging / AI",
            'Regulation/Law (US state statute)',
            'Developers of large "frontier" AI models.',
            'California, USA',
            'State of California',
            'Transparency and safety obligations for frontier model developers — publish safety frameworks, report critical safety incidents, whistleblower protections.',
            'Medium–High (new; targeted at the largest model developers).',
            'Niche (very large AI labs).',
            'Continuous; periodic published safety-framework updates; incident reporting tied to events.',
            'Modest legal/disclosure cost relative to scope of regulated entities; primarily a transparency regime.',
            'Complements federal AI executive orders, NIST AI RMF, and the EU AI Act; whistleblower protections echo SOX-style provisions.',
            'Continuous — statutory obligations on covered frontier-model developers.',
        ),
    ),
]

deck = genanki.Deck(DECK_ID, 'Security & Compliance Certifications')

for front, back_html in cards:
    note = genanki.Note(model=model, fields=[front, back_html])
    deck.add_note(note)

output_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(output_dir, 'security_certifications.apkg')
deck.write_to_file(output_path)

size_kb = os.path.getsize(output_path) / 1024
print(f"Created deck with {len(cards)} cards")
print(f"Deck size: {size_kb:.1f} KB")
print(f"Saved to: {output_path}")
