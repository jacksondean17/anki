#!/usr/bin/env python3
"""Generate an Anki deck for megastructures and space habitats."""
import genanki
import os

MODEL_ID = 1847293056
DECK_ID = 2938471650

model = genanki.Model(
    MODEL_ID,
    'Megastructures & Space Habitats',
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
            font-family: arial, sans-serif;
            font-size: 20px;
            text-align: center;
            color: #e0e0e0;
            background-color: #1a1a2e;
            padding: 20px;
        }
        .front {
            font-size: 26px;
            font-weight: bold;
            color: #00d4ff;
        }
        .back {
            font-size: 18px;
            text-align: left;
            line-height: 1.6;
            color: #e0e0e0;
        }
        .back b {
            color: #00d4ff;
        }
        hr#answer {
            border: 1px solid #333;
        }
    '''
)

cards = [
    # --- Dyson Structures ---
    (
        "Dyson Sphere",
        "A megastructure that completely encompasses a star to capture most or all of its energy output.<br><br>"
        "Proposed by <b>Freeman Dyson</b> in 1960 in his paper <i>Search for Artificial Stellar Sources of Infrared Radiation</i>.<br><br>"
        "A solid shell is structurally impossible — Dyson himself envisioned a <b>swarm of orbiting satellites</b>. Often cited as the hallmark of a <b>Kardashev Type II</b> civilization."
    ),
    (
        "Dyson Swarm",
        "A large number of independent orbiting solar collectors around a star, collectively capturing a significant fraction of its luminosity.<br><br>"
        "The most <b>physically plausible</b> version of a Dyson Sphere.<br><br>"
        "Can be built <b>incrementally</b> over time — no need to construct a single monolithic structure."
    ),
    (
        "Dyson Ring",
        "A ring of solar collectors or habitats orbiting a star in a single plane.<br><br>"
        "Simpler than a full swarm but captures less total energy. Sometimes called a <b>Dyson Belt</b>.<br><br>"
        "A natural first step toward a full Dyson Swarm."
    ),
    (
        "Dyson Bubble",
        "A variant of the Dyson Swarm where collectors are held in place by <b>radiation pressure</b> (light sails) rather than orbital mechanics.<br><br>"
        "The collectors are <b>statites</b> — stationary satellites balanced between gravity and light pressure.<br><br>"
        "Advantage: collectors don't need to orbit, so they can be arranged in any configuration."
    ),
    # --- Rotating Habitats ---
    (
        "O'Neill Cylinder",
        "A space habitat consisting of two counter-rotating cylinders, each ~32 km long and 8 km in diameter.<br><br>"
        "Proposed by <b>Gerard K. O'Neill</b> in 1976 in his book <i>The High Frontier</i>.<br><br>"
        "Simulates gravity via rotation. Interior has land, atmosphere, and weather. Designed to house <b>millions of people</b>. Also known as <b>Island Three</b>."
    ),
    (
        "Stanford Torus",
        "A donut-shaped rotating space habitat housing 10,000–140,000 people.<br><br>"
        "Proposed in a <b>1975 NASA Summer Study</b> at Stanford University.<br><br>"
        "~1.8 km in diameter. Rotates once per minute for Earth-like gravity on the inner ring. Uses external mirrors to direct sunlight inside."
    ),
    (
        "Bernal Sphere",
        "A spherical rotating space habitat, one of the earliest detailed proposals for a permanent space colony.<br><br>"
        "Proposed by <b>J.D. Bernal</b> in 1929 in his essay <i>The World, the Flesh and the Devil</i>.<br><br>"
        "~16 km in diameter, housing ~20,000–30,000 people. Rotates to provide artificial gravity."
    ),
    (
        "McKendree Cylinder",
        "An extremely large O'Neill Cylinder variant built using <b>carbon nanotubes</b> instead of steel.<br><br>"
        "Proposed by NASA engineer <b>Tom McKendree</b> in 2000.<br><br>"
        "Could be ~460 km long and 460 km in radius — large enough to have its own <b>weather systems</b> and continental-scale land areas."
    ),
    (
        "Bishop Ring",
        "A rotating space habitat shaped like a large open ring (no roof), with atmosphere held in by walls and spin gravity.<br><br>"
        "Named after <b>Forrest Bishop</b>.<br><br>"
        "~1,000 km in radius, made possible with <b>carbon nanotubes</b>. Living area on the inner surface. Much larger than an O'Neill Cylinder but smaller than a Ringworld."
    ),
    (
        "Kalpana One",
        "A compact cylindrical space habitat designed for <b>near-term feasibility</b>.<br><br>"
        "Designed by <b>Al Globus</b> et al. at NASA Ames Research Center.<br><br>"
        "~250 m radius, ~325 m long, housing ~3,000 people. Optimized to minimize material needs while maintaining 1g gravity and a low, comfortable rotation rate."
    ),
    # --- Megastructures ---
    (
        "Ringworld",
        "A ring ~1 AU in radius orbiting a star, with a habitable inner surface providing ~3 million Earths of surface area.<br><br>"
        "Created by <b>Larry Niven</b> in his 1970 novel <i>Ringworld</i>.<br><br>"
        "Spin provides gravity. Requires <b>shadow squares</b> for day/night cycles. Structurally <b>unstable</b> without active correction — it drifts off-center."
    ),
    (
        "Banks Orbital",
        "A rotating ring habitat ~3 million km in diameter, tilted to orbit its star for natural day/night cycles.<br><br>"
        "Created by <b>Iain M. Banks</b> in his <i>Culture</i> series (1987–2012).<br><br>"
        "Much smaller and more plausible than a Ringworld. Gravity from rotation. Each Orbital has a surface area comparable to several Earths."
    ),
    (
        "Alderson Disk",
        "A giant flat disk with a star at its center (sitting in a hole), extending to roughly the orbit of Mars or Jupiter.<br><br>"
        "Proposed by <b>Dan Alderson</b> of JPL.<br><br>"
        "Surface area vastly exceeds a planet. Gravity points toward the plane of the disk. <b>Structurally implausible</b> with any known materials."
    ),
    (
        "Shellworld",
        "A megastructure consisting of multiple concentric spherical shells around a planet or star, each providing habitable surface area.<br><br>"
        "Featured in <b>Iain M. Banks'</b> novel <i>Matter</i> (2008).<br><br>"
        "Sometimes called a <b>matrioshka shellworld</b>. Each nested layer can have its own ecosystem and civilization."
    ),
    (
        "Matrioshka Brain",
        "A megastructure using nested Dyson spheres as a giant computer, converting nearly all stellar energy into computation.<br><br>"
        "Proposed by <b>Robert Bradbury</b> in 1997.<br><br>"
        "Each layer absorbs energy from the one inside and re-radiates waste heat outward to the next layer. Named after Russian nesting dolls (matryoshka)."
    ),
    (
        "Stellar Engine (Shkadov Thruster)",
        "A megastructure that uses a star's own radiation pressure to move the entire star system.<br><br>"
        "Proposed by <b>Leonid Shkadov</b> in 1987.<br><br>"
        "A giant mirror reflects light in one direction, creating asymmetric thrust. Could relocate a star over <b>millions of years</b> — useful for avoiding cosmic hazards."
    ),
    (
        "Topopolis",
        "A megastructure in the shape of a very long, thin rotating tube wound around a star. Also called a <b>Spaghetti World</b>.<br><br>"
        "Concept explored by <b>Pat Gunkel</b>.<br><br>"
        "Essentially an O'Neill Cylinder extended to extreme length — potentially millions of km. Could be looped or knotted around a star's orbit."
    ),
    # --- Concepts & Theory ---
    (
        "Kardashev Scale",
        "A method of classifying civilizations by their total energy consumption.<br><br>"
        "Proposed by <b>Nikolai Kardashev</b> in 1964 in his paper <i>Transmission of Information by Extraterrestrial Civilizations</i>.<br><br>"
        "<b>Type I</b>: All energy of its planet (~10\u00b9\u2076 W).<br>"
        "<b>Type II</b>: All energy of its star (~10\u00b2\u2076 W).<br>"
        "<b>Type III</b>: All energy of its galaxy (~10\u00b3\u2076 W)."
    ),
    (
        "Artificial Gravity (Rotation)",
        "Simulated gravity created by spinning a habitat so the inner surface pushes on inhabitants via centripetal acceleration.<br><br>"
        "Formula: <b>a = \u03c9\u00b2r</b> (angular velocity squared \u00d7 radius).<br><br>"
        "Larger radius = slower spin needed = fewer disorienting <b>Coriolis effects</b>. Most designs target <b>~1\u20132 RPM</b> maximum."
    ),
    (
        "Lagrange Points",
        "Five points (L1\u2013L5) in a two-body system where gravitational forces balance with centripetal force, allowing objects to maintain stable positions.<br><br>"
        "<b>L4 and L5</b> are the most stable (triangular points, 60\u00b0 ahead/behind the smaller body).<br><br>"
        "O'Neill proposed building colonies at the Earth-Moon <b>L5</b> point, spawning the <b>L5 Society</b> (founded 1975)."
    ),
    (
        "In-Situ Resource Utilization (ISRU)",
        "The practice of harvesting and using materials found at the construction site rather than launching them from Earth.<br><br>"
        "Critical for megastructure feasibility.<br><br>"
        "Examples: mining <b>asteroids</b> for metals, extracting water from the <b>Moon</b>, processing <b>regolith</b> into building materials. Dramatically reduces launch costs."
    ),
    (
        "Kessler Syndrome",
        "A cascade where orbital collisions create debris that causes more collisions, progressively filling an orbit with high-speed fragments.<br><br>"
        "Proposed by <b>Donald Kessler</b> in 1978.<br><br>"
        "Could make certain orbits <b>unusable</b> for habitats or satellites. <b>Whipple shields</b> (layered impact protection) are essential for space habitat designs."
    ),
    (
        "Space Elevator",
        "A structure connecting a planet's surface to orbit via a tethered cable or ribbon, dramatically reducing the cost of reaching space.<br><br>"
        "First proposed by <b>Konstantin Tsiolkovsky</b> in 1895. Modern concept developed by <b>Yuri Artsutanov</b> (1960) and <b>Jerome Pearson</b> (1975).<br><br>"
        "Requires materials with extreme <b>tensile strength</b> — carbon nanotubes or graphene are leading candidates. Anchored at the equator, extends to geostationary orbit and beyond."
    ),
    (
        "Orbital Ring",
        "A megastructure encircling Earth at low orbit altitude, supported by a magnetically levitated cable moving at orbital velocity inside a stationary sheath.<br><br>"
        "Concept developed by <b>Paul Birch</b> in 1982.<br><br>"
        "Unlike a space elevator, it can be at <b>any altitude</b> and built with <b>existing materials</b> (steel). Could support tethered platforms for cheap surface-to-orbit access."
    ),
    (
        "Lofstrom Loop (Launch Loop)",
        "A megastructure for cheap Earth-to-orbit launches using a magnetically accelerated cable forming an arc ~80 km high.<br><br>"
        "Proposed by <b>Keith Lofstrom</b> in 1985.<br><br>"
        "Payloads ride the cable to orbital velocity. Could reduce launch costs to <b>~$3/kg</b>. Buildable with current materials and technology."
    ),
    # --- Specific proposals & sci-fi ---
    (
        "O'Neill's Island Program",
        "Gerard O'Neill's three-phase plan for space colonization, from his 1976 book <i>The High Frontier</i>.<br><br>"
        "<b>Island One</b>: Bernal Sphere (~10,000 people).<br>"
        "<b>Island Two</b>: Larger Bernal Sphere (~140,000 people).<br>"
        "<b>Island Three</b>: Paired O'Neill Cylinders (~millions of people).<br><br>"
        "Each phase builds on the industrial capacity established by the previous one."
    ),
    (
        "Bubbleworld",
        "A large pressurized sphere floating in a gas giant's atmosphere at a level where external pressure equals ~1 atm.<br><br>"
        "Filled with breathable air, it would <b>float like a balloon</b> since N\u2082/O\u2082 is lighter than hydrogen/helium at the same pressure.<br><br>"
        "Could be km-scale. Requires only a thin membrane — the atmosphere itself provides structural support."
    ),
    (
        "Bussard Ramjet",
        "A proposed interstellar spacecraft that collects hydrogen from the interstellar medium with a magnetic scoop to fuel a fusion engine.<br><br>"
        "Proposed by <b>Robert Bussard</b> in 1960.<br><br>"
        "Relevant to space habitats because a <b>generation ship</b> could use this propulsion method for interstellar travel without carrying all its fuel. Later analysis suggests drag may outweigh thrust."
    ),
    (
        "Generation Ship",
        "A hypothetical starship designed for multi-generational interstellar travel, where the original crew's <b>descendants</b> arrive at the destination.<br><br>"
        "Concept dates to rocket pioneer <b>Robert Goddard</b> (1918) and <b>J.D. Bernal</b> (1929).<br><br>"
        "Essentially a self-sustaining <b>mobile space habitat</b>. Requires closed-loop life support, agriculture, and social stability over centuries or millennia."
    ),
    (
        "Penrose Process",
        "A mechanism to extract rotational energy from a spinning (Kerr) black hole.<br><br>"
        "Proposed by <b>Roger Penrose</b> in 1971.<br><br>"
        "Objects enter the <b>ergosphere</b>, split, and one fragment escapes with more energy than the original object carried in. A civilization could build a megastructure around a black hole to harvest energy — sometimes called a <b>Penrose Sphere</b>."
    ),
]

deck = genanki.Deck(DECK_ID, 'Megastructures & Space Habitats')

for front, back in cards:
    note = genanki.Note(model=model, fields=[front, back])
    deck.add_note(note)

output_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(output_dir, 'megastructures_space_habitats.apkg')
deck.write_to_file(output_path)

size_kb = os.path.getsize(output_path) / 1024
print(f"Created deck with {len(cards)} cards")
print(f"Deck size: {size_kb:.1f} KB")
print(f"Saved to: {output_path}")
