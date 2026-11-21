"""
Comprehensive COCO 80-Class Knowledge Base & Object Taxonomy.
Provides category classification, definitions, and real-world purposes in English.
"""

COCO_TAXONOMY = {
    # Humans
    "person": "Humans",

    # Vehicles & Transportation
    "bicycle": "Vehicles", "car": "Vehicles", "motorcycle": "Vehicles",
    "airplane": "Vehicles", "bus": "Vehicles", "train": "Vehicles",
    "truck": "Vehicles", "boat": "Vehicles",

    # Outdoor & Traffic Infrastructure
    "traffic light": "Infrastructure", "fire hydrant": "Infrastructure",
    "stop sign": "Infrastructure", "parking meter": "Infrastructure",
    "bench": "Infrastructure",

    # Animals & Wildlife
    "bird": "Animals", "cat": "Animals", "dog": "Animals", "horse": "Animals",
    "sheep": "Animals", "cow": "Animals", "elephant": "Animals", "bear": "Animals",
    "zebra": "Animals", "giraffe": "Animals",

    # Accessories & Personal Gear
    "backpack": "Accessories", "umbrella": "Accessories", "handbag": "Accessories",
    "tie": "Accessories", "suitcase": "Accessories",

    # Sports Equipment
    "frisbee": "Sports", "skis": "Sports", "snowboard": "Sports",
    "sports ball": "Sports", "kite": "Sports", "baseball bat": "Sports",
    "baseball glove": "Sports", "skateboard": "Sports", "surfboard": "Sports",
    "tennis racket": "Sports",

    # Kitchenware & Utensils
    "bottle": "Kitchenware", "wine glass": "Kitchenware", "cup": "Kitchenware",
    "fork": "Kitchenware", "knife": "Kitchenware", "spoon": "Kitchenware",
    "bowl": "Kitchenware",

    # Food & Nutrition
    "banana": "Food", "apple": "Food", "sandwich": "Food", "orange": "Food",
    "broccoli": "Food", "carrot": "Food", "hot dog": "Food", "pizza": "Food",
    "donut": "Food", "cake": "Food",

    # Furniture & Living
    "chair": "Furniture", "couch": "Furniture", "potted plant": "Furniture",
    "bed": "Furniture", "dining table": "Furniture", "toilet": "Furniture",

    # Electronics & Technology
    "tv": "Electronics", "laptop": "Electronics", "mouse": "Electronics",
    "remote": "Electronics", "keyboard": "Electronics", "cell phone": "Electronics",

    # Home Appliances
    "microwave": "Appliances", "oven": "Appliances", "toaster": "Appliances",
    "sink": "Appliances", "refrigerator": "Appliances",

    # Indoor Everyday Items
    "book": "Everyday Items", "clock": "Everyday Items", "vase": "Everyday Items",
    "scissors": "Everyday Items", "teddy bear": "Everyday Items",
    "hair drier": "Everyday Items", "toothbrush": "Everyday Items"
}

COCO_DEFINITIONS = {
    "person": {
        "definition": "A human individual of any age or gender.",
        "purpose": "Pedestrian mobility, collaborative tasks, communication, and economic/social interaction."
    },
    "bicycle": {
        "definition": "A human-powered or electric pedal-driven two-wheeled vehicle.",
        "purpose": "Zero-emission personal urban commuting, recreation, and physical fitness."
    },
    "car": {
        "definition": "A motorized four-wheeled passenger road vehicle.",
        "purpose": "Rapid passenger transit, personal mobility, and intercity transportation."
    },
    "motorcycle": {
        "definition": "A motorized two-wheeled road vehicle designed for agile travel.",
        "purpose": "Efficient personal commuting through dense traffic networks."
    },
    "airplane": {
        "definition": "A fixed-wing powered aircraft operated in civil or commercial aviation.",
        "purpose": "Long-range international transit of passengers, logistics, and emergency cargo."
    },
    "bus": {
        "definition": "A high-capacity motor vehicle operating along designated public routes.",
        "purpose": "Mass public transit, urban congestion reduction, and accessible commuting."
    },
    "train": {
        "definition": "A series of interconnected rail cars propelled by a locomotive.",
        "purpose": "High-volume, energy-efficient intercity freight and passenger transportation."
    },
    "truck": {
        "definition": "A heavy-duty freight road vehicle built for cargo hauling.",
        "purpose": "Commercial logistics, freight distribution, and supply chain infrastructure."
    },
    "boat": {
        "definition": "A watercraft engineered to float and navigate maritime channels.",
        "purpose": "Marine freight transport, commercial fishing, recreation, and coastal monitoring."
    },
    "traffic light": {
        "definition": "An optical electronic road signaling fixture at intersections.",
        "purpose": "Regulates vehicular and pedestrian right-of-way to minimize collision risk."
    },
    "fire hydrant": {
        "definition": "A street-level pressurized municipal water discharge valve.",
        "purpose": "Supplies high-volume water for municipal firefighting and hazard suppression."
    },
    "stop sign": {
        "definition": "An octagonal red regulatory traffic control fixture.",
        "purpose": "Mandates complete vehicle stops at cross-traffic junctions."
    },
    "parking meter": {
        "definition": "A roadside electronic transaction device regulating curb parking.",
        "purpose": "Manages street-level parking turnover and municipal space usage."
    },
    "bench": {
        "definition": "A rigid outdoor seating fixture built for multiple people.",
        "purpose": "Provides resting seating in public parks, sidewalks, and transit terminals."
    },
    "bird": {
        "definition": "A feathered endothermic vertebrate capable of flight.",
        "purpose": "Maintains ecological biodiversity, seed dispersal, and insect management."
    },
    "cat": {
        "definition": "A small domesticated carnivorous mammal with agile anatomy.",
        "purpose": "Domestic companionship, mental well-being, and historical pest deterrence."
    },
    "dog": {
        "definition": "A domesticated canine mammal with high olfactory and social intelligence.",
        "purpose": "Household companionship, security monitoring, assistance for disabilities, and service."
    },
    "horse": {
        "definition": "A large domesticated odd-toed ungulate mammal.",
        "purpose": "Equestrian sports, therapeutic riding, and historical agricultural traction."
    },
    "sheep": {
        "definition": "A domesticated ruminant mammal with a fleece coat.",
        "purpose": "Agricultural wool production, dairy supply, and rural landscape grazing."
    },
    "cow": {
        "definition": "A large domesticated bovine farm mammal.",
        "purpose": "Dairy manufacturing, nutritional beef supply, and rural agrarian economy."
    },
    "elephant": {
        "definition": "A colossal pachyderm mammal with a prehensile trunk and tusks.",
        "purpose": "Keystone wildlife ecosystem engineer facilitating forest canopy pruning and waterhole creation."
    },
    "bear": {
        "definition": "A large predatory and scavenging forest mammal.",
        "purpose": "Apex ecological regulator maintaining equilibrium in wilderness biomes."
    },
    "zebra": {
        "definition": "An African wild equine mammal with high-contrast stripe patterns.",
        "purpose": "Wild grassland grazing balance and savanna ecosystem diversity."
    },
    "giraffe": {
        "definition": "The tallest terrestrial mammal with an elongated cervical vertebrae.",
        "purpose": "Browses high acacia tree canopies, dispersing vital seeds across savannas."
    },
    "backpack": {
        "definition": "A fabric load-bearing pack carried over shoulders with dual straps.",
        "purpose": "Ergonomic hands-free carriage of portable computing, books, and daily gear."
    },
    "umbrella": {
        "definition": "A collapsible circular fabric canopy on a central shaft.",
        "purpose": "Provides personal shielding against rainfall and UV solar radiation."
    },
    "handbag": {
        "definition": "A portable bag or purse for personal essentials.",
        "purpose": "Secure storage and carriage of wallets, mobile devices, keys, and cosmetics."
    },
    "tie": {
        "definition": "A tailored fabric neckwear band tied beneath a shirt collar.",
        "purpose": "Formal, academic, and business attire aesthetic convention."
    },
    "suitcase": {
        "definition": "A rigid or semi-rigid wheeled luggage container.",
        "purpose": "Protects and organizes clothing and equipment during regional and international travel."
    },
    "frisbee": {
        "definition": "An aerodynamic plastic concave disc designed for spinning flight.",
        "purpose": "Recreational outdoor tossing, athletic agility, and competitive disc sports."
    },
    "skis": {
        "definition": "A pair of narrow elongated composite runners bound to boots.",
        "purpose": "Gliding locomotion across snow-covered alpine terrain in recreation and athletics."
    },
    "snowboard": {
        "definition": "A single wide composite board clamped to specialized footwear.",
        "purpose": "Downhill winter snow sports and terrain park navigation."
    },
    "sports ball": {
        "definition": "A spherical pressurized projectile used across sporting codes.",
        "purpose": "Primary kinematic game asset in sports like soccer, basketball, and tennis."
    },
    "kite": {
        "definition": "A lightweight tethered aerodynamic sail flown on wind currents.",
        "purpose": "Recreational aerodynamics, cultural festivals, and leisure flying."
    },
    "baseball bat": {
        "definition": "A cylindrical wooden or aluminum sporting strike club.",
        "purpose": "Propels pitched baseballs through kinetic impact in competitive play."
    },
    "baseball glove": {
        "definition": "A reinforced padded leather catching mitt.",
        "purpose": "Absorbs ball kinetic energy and assists defensive fielding in baseball."
    },
    "skateboard": {
        "definition": "A multi-ply wooden deck mounted on polyurethane wheels and trucks.",
        "purpose": "Urban street transit, freestyle tricks, and youth athletic subculture."
    },
    "surfboard": {
        "definition": "A buoyant hydrodynamic composite foam board.",
        "purpose": "Enables wave-riding and aquatic balance across ocean surf breaks."
    },
    "tennis racket": {
        "definition": "An oval frame laced with high-tension string matrix.",
        "purpose": "Directs and strikes tennis balls across a court net."
    },
    "bottle": {
        "definition": "A rigid cylinder container with a narrow neck made of glass or polymer.",
        "purpose": "Hydration delivery and safe containment of consumable liquids."
    },
    "wine glass": {
        "definition": "A stemmed glassware container with a specialized aroma bowl.",
        "purpose": "Optimizes aeration, temperature control, and aromatic enjoyment of wine."
    },
    "cup": {
        "definition": "A compact drinking receptacle, often equipped with a handle.",
        "purpose": "Holds and delivers hot or cold beverages safely to the mouth."
    },
    "fork": {
        "definition": "A handheld dining implement equipped with two or more sharp tines.",
        "purpose": "Pierces and stabilizes solid culinary items during consumption."
    },
    "knife": {
        "definition": "A culinary instrument featuring a sharp metallic cutting edge.",
        "purpose": "Precise slicing, chopping, and portioning of food ingredients."
    },
    "spoon": {
        "definition": "An eating and culinary utensil with a concave shallow bowl.",
        "purpose": "Scoops, measures, and consumes liquids, broths, and granular foods."
    },
    "bowl": {
        "definition": "A hemispherical open-top dining and prep container.",
        "purpose": "Holds soups, cereals, salads, and culinary mixtures without spillage."
    },
    "banana": {
        "definition": "A curved tropical fruit with a protective peel and potassium-rich pulp.",
        "purpose": "Provides quick dietary carbohydrates, potassium, and nutritional fiber."
    },
    "apple": {
        "definition": "A pomaceous deciduous fruit high in antioxidants and dietary pectin.",
        "purpose": "Nutritional dietary consumption, fresh juice processing, and baking."
    },
    "sandwich": {
        "definition": "A handheld meal composed of fillings placed between bread slices.",
        "purpose": "Nutritious, portable, and versatile dietary sustenance."
    },
    "orange": {
        "definition": "A citrus fruit with sweet-acidic segmented pulp and fragrant rind.",
        "purpose": "Provides high dietary Vitamin C, hydration, and natural flavorings."
    },
    "broccoli": {
        "definition": "A cruciferous vegetable with dense flowering heads.",
        "purpose": "Delivers essential micronutrients, sulforaphane, and dietary fiber."
    },
    "carrot": {
        "definition": "A taproot root vegetable with vibrant orange pigmentation.",
        "purpose": "Rich dietary source of beta-carotene, Vitamin A, and culinary sweetness."
    },
    "hot dog": {
        "definition": "A seasoned sausage served inside a partially sliced soft bun.",
        "purpose": "Convenient street and stadium quick-service fast food."
    },
    "pizza": {
        "definition": "An oven-baked yeast flatbread topped with tomato marinara, cheese, and meats/vegetables.",
        "purpose": "Communal savory dining rich in cultural gastronomic tradition."
    },
    "donut": {
        "definition": "A fried leavened dough confectionery, commonly ring-shaped.",
        "purpose": "Sweet dessert confectionery enjoyed with coffee or breakfast."
    },
    "cake": {
        "definition": "A sweet baked flour confectionery layered with icing.",
        "purpose": "Centerpiece celebratory food for birthdays, graduations, and weddings."
    },
    "chair": {
        "definition": "A single-occupancy furniture seat featuring back support and legs.",
        "purpose": "Ergonomic seating support in educational, residential, and corporate spaces."
    },
    "couch": {
        "definition": "An upholstered multi-seat lounge furniture sofa with cushioning.",
        "purpose": "Comfortable seating, social relaxation, and leisure lounging."
    },
    "potted plant": {
        "definition": "A living botanical specimen cultivated inside an indoor container.",
        "purpose": "Air biophilic filtration, interior visual decoration, and psychological wellness."
    },
    "bed": {
        "definition": "A horizontal mattress and structural frame dedicated to sleep.",
        "purpose": "Supports nocturnal circadian rest, posture alignment, and recuperation."
    },
    "dining table": {
        "definition": "A large elevated horizontal furniture surface with structural legs.",
        "purpose": "Communal gathering surface for shared dining, study, and collaboration."
    },
    "toilet": {
        "definition": "A sanitary porcelain fixture with water-flush sanitation plumbing.",
        "purpose": "Hygienic disposal of human waste to maintain public and residential health."
    },
    "tv": {
        "definition": "An electronic visual display monitor receiving broadcast/streaming video.",
        "purpose": "Visual entertainment, real-time news dissemination, and gaming."
    },
    "laptop": {
        "definition": "A portable personal microcomputer with screen and keyboard integrated into a clamshell.",
        "purpose": "Enables mobile software engineering, academic study, computation, and communication."
    },
    "mouse": {
        "definition": "A handheld peripheral hardware pointing device detecting two-axis movement.",
        "purpose": "Enables tactile navigation across Graphical User Interfaces (GUIs)."
    },
    "remote": {
        "definition": "A wireless handheld electronic transmitter using infrared or Bluetooth.",
        "purpose": "Distance control of audiovisual, air conditioning, and smart home appliances."
    },
    "keyboard": {
        "definition": "A hardware alphanumeric key input peripheral.",
        "purpose": "Text composition, software code entry, and computational commands."
    },
    "cell phone": {
        "definition": "A handheld portable cellular telecommunications and computational device.",
        "purpose": "Voice calls, instant messaging, web browsing, photographic recording, and mobile computing."
    },
    "microwave": {
        "definition": "A kitchen appliance that excites water molecules using electromagnetic radiation.",
        "purpose": "Rapid thermal reheating and cooking of culinary meals."
    },
    "oven": {
        "definition": "A thermally insulated high-temperature cooking chamber.",
        "purpose": "Baking breads, roasting vegetables, and thermal food preparation."
    },
    "toaster": {
        "definition": "A compact electric appliance exposing sliced bread to radiant heat.",
        "purpose": "Toasting and crisping bread for breakfast meals."
    },
    "sink": {
        "definition": "A fixed basin plumbed with running water supply and wastewater drainage.",
        "purpose": "Hand hygiene, culinary cleaning, and domestic sanitation."
    },
    "refrigerator": {
        "definition": "A thermally insulated cooling cabinet with vapor-compression refrigeration.",
        "purpose": "Low-temperature preservation of food and pharmaceuticals to prevent bacterial spoilage."
    },
    "book": {
        "definition": "A bound collection of printed or written sheets between protective covers.",
        "purpose": "Knowledge storage, academic literature, storytelling, and cultural transmission."
    },
    "clock": {
        "definition": "An electro-mechanical time-measuring and chronometric display device.",
        "purpose": "Chronological synchronization of human schedules, transit, and daily routines."
    },
    "vase": {
        "definition": "An open decorative ceramic or glass vessel.",
        "purpose": "Floral display, botanical hydration, and interior artistic decor."
    },
    "scissors": {
        "definition": "A dual-blade shear cutting instrument pivoted at a central fulcrum.",
        "purpose": "Clean shearing of paper, textiles, packaging, and craft media."
    },
    "teddy bear": {
        "definition": "A soft plush stuffed toy model of a bear cub.",
        "purpose": "Childhood emotional comfort, imaginative play, and nostalgic gifting."
    },
    "hair drier": {
        "definition": "An electromechanical heating blower.",
        "purpose": "Accelerates moisture evaporation from damp hair for personal grooming."
    },
    "toothbrush": {
        "definition": "A handheld dental hygiene brush with fine nylon bristles.",
        "purpose": "Removes oral dental plaque and food debris to preserve teeth and gum health."
    }
}


def get_object_info(class_name: str) -> dict:
    """Returns semantic category, definition, and purpose for a given class name."""
    normalized = class_name.strip().lower()
    category = COCO_TAXONOMY.get(normalized, "General Objects")
    info = COCO_DEFINITIONS.get(normalized, {
        "definition": f"An identifiable visual object recognized as a {class_name}.",
        "purpose": "Real-world utility and functional interaction according to its domain."
    })
    return {
        "name": class_name.capitalize(),
        "category": category,
        "definition": info["definition"],
        "purpose": info["purpose"]
    }
