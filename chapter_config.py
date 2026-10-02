"""
Official BSEB Class 10 Chapter Taxonomy with Rich Pedagogical Criteria for Jev Classification.
Single source of truth for chapter mapping across all 6 subjects.
"""

CHAPTERS = {
    "mathematics": {
        "is_multi_section": False,
        "sections": {
            "Math": [
                {
                    "number": "1",
                    "name_en": "Real Numbers",
                    "name_hi": "वास्तविक संख्याएँ",
                    "desc": "Euclid division lemma, Fundamental theorem of arithmetic, HCF, LCM, prime factorization, proving sqrt(2), sqrt(3), sqrt(5) irrational, terminating and non-terminating recurring decimal expansions, p/q rational form"
                },
                {
                    "number": "2",
                    "name_en": "Polynomials",
                    "name_hi": "बहुपद",
                    "desc": "Zeroes of a polynomial, degree of polynomial, relationship between zeroes and coefficients of quadratic/cubic polynomials, alpha + beta = -b/a, alpha * beta = c/a, division algorithm for polynomials"
                },
                {
                    "number": "3",
                    "name_en": "Pair of Linear Equations in Two Variables",
                    "name_hi": "दो चर वाले रैखिक समीकरण युग्म",
                    "desc": "Linear equations a1x + b1y + c1 = 0, consistency, unique solution (intersecting lines), infinitely many solutions (coincident lines), no solution (parallel lines), substitution method, elimination method, cross-multiplication, speed boat/stream word problems"
                },
                {
                    "number": "4",
                    "name_en": "Quadratic Equations",
                    "name_hi": "द्विघात समीकरण",
                    "desc": "Standard form ax^2 + bx + c = 0, roots of quadratic equation, factorization, quadratic formula x = (-b +- sqrt(D))/(2a), discriminant D = b^2 - 4ac, nature of real and equal roots (D=0), real and unequal roots (D>0), no real roots (D<0)"
                },
                {
                    "number": "5",
                    "name_en": "Arithmetic Progressions",
                    "name_hi": "समांतर श्रेणियाँ",
                    "desc": "Arithmetic progression (AP), first term a, common difference d, nth term a_n = a + (n-1)d, sum of first n terms S_n = n/2[2a + (n-1)d], word problems on AP series"
                },
                {
                    "number": "6",
                    "name_en": "Triangles",
                    "name_hi": "त्रिभुज",
                    "desc": "Similar triangles, Thales theorem (Basic Proportionality Theorem - BPT), converse of BPT, criteria for similarity AAA, SSS, SAS, ratio of areas of similar triangles is equal to square of ratio of corresponding sides, Pythagoras theorem and its converse"
                },
                {
                    "number": "7",
                    "name_en": "Coordinate Geometry",
                    "name_hi": "निर्देशांक ज्यामिति",
                    "desc": "Distance formula sqrt((x2-x1)^2 + (y2-y1)^2), distance from origin sqrt(x^2+y^2), distance from x-axis/y-axis, quadrant signs (+,+), (-,+), section formula, midpoint formula, coordinates of centroid of triangle, collinear points, area of triangle using coordinates"
                },
                {
                    "number": "8",
                    "name_en": "Introduction to Trigonometry",
                    "name_hi": "त्रिकोणमिति का परिचय",
                    "desc": "Trigonometric ratios sin, cos, tan, cot, sec, cosec, values at angles 0, 30, 45, 60, 90 degrees, trigonometric ratios of complementary angles like sin(90-theta) = cos(theta), identities sin^2(theta) + cos^2(theta) = 1, 1 + tan^2(theta) = sec^2(theta), 1 + cot^2(theta) = cosec^2(theta)"
                },
                {
                    "number": "9",
                    "name_en": "Some Applications of Trigonometry",
                    "name_hi": "त्रिकोणमिति के कुछ अनुप्रयोग",
                    "desc": "Heights and distances, line of sight, angle of elevation, angle of depression, finding height of tower/tree/building, length of shadow, observer distance"
                },
                {
                    "number": "10",
                    "name_en": "Circles",
                    "name_hi": "वृत्त",
                    "desc": "Tangent to a circle, point of contact, tangent is perpendicular to radius at point of contact, lengths of tangents drawn from an external point to a circle are equal, secant"
                },
                {
                    "number": "11",
                    "name_en": "Constructions",
                    "name_hi": "रचनाएँ",
                    "desc": "Geometric constructions using compass and ruler: dividing a given line segment internally in a given ratio, constructing a tangent to a circle from a point outside it, constructing a triangle similar to a given triangle"
                },
                {
                    "number": "12",
                    "name_en": "Areas Related to Circles",
                    "name_hi": "वृत्तों से संबंधित क्षेत्रफल",
                    "desc": "Perimeter and area of circle, circumference 2*pi*r, area pi*r^2, area of sector of circle (theta/360 * pi*r^2), length of arc of sector (theta/360 * 2*pi*r), area of segment of circle, areas of combinations of plane figures (shaded regions)"
                },
                {
                    "number": "13",
                    "name_en": "Surface Areas and Volumes",
                    "name_hi": "पृष्ठीय क्षेत्रफल और आयतन",
                    "desc": "Surface areas and volumes of combinations of solids: cuboid, cube, right circular cylinder, right circular cone, sphere, hemisphere, frustum of a cone, conversion of solid from one shape to another (melting/recasting wire, sphere into cylinder)"
                },
                {
                    "number": "14",
                    "name_en": "Statistics",
                    "name_hi": "सांख्यिकी",
                    "desc": "Mean of grouped data (direct method, assumed mean method, step deviation method), mode of grouped data, median of grouped data, cumulative frequency curve (less than ogive, more than ogive), empirical relation: 3*median = mode + 2*mean"
                },
                {
                    "number": "15",
                    "name_en": "Probability",
                    "name_hi": "प्रायिकता",
                    "desc": "Classical probability P(E) = favorable outcomes / total outcomes, impossible event (P=0), sure/certain event (P=1), 0 <= P(E) <= 1, complementary event P(not E) = 1 - P(E), coin tosses, rolling single or pair of dice, deck of 52 playing cards (spades, hearts, diamonds, clubs, face cards)"
                }
            ]
        }
    },
    "science": {
        "is_multi_section": False,
        "sections": {
            "Science": [
                {
                    "number": "1",
                    "name_en": "Chemical Reactions and Equations",
                    "name_hi": "रासायनिक अभिक्रियाएं एवं समीकरण",
                    "desc": "Chemical equations, balanced chemical equations, combination reaction, decomposition reaction (thermal, electrolytic, photolytic), displacement reaction, double displacement reaction, precipitation, oxidation and reduction (redox), corrosion, rancidity"
                },
                {
                    "number": "2",
                    "name_en": "Acids, Bases and Salts",
                    "name_hi": "अम्ल, क्षारक एवं लवण",
                    "desc": "Acids, bases, litmus paper, pH scale, universal indicator, reaction of acids/bases with metals, neutralization reaction, preparation and uses of Bleaching powder (CaOCl2), Baking soda (NaHCO3), Washing soda (Na2CO3.10H2O), Plaster of Paris (CaSO4.1/2H2O), Gypsum, water of crystallization"
                },
                {
                    "number": "3",
                    "name_en": "Metals and Non-metals",
                    "name_hi": "धातु एवं अधातु",
                    "desc": "Physical and chemical properties of metals and non-metals, reactivity series, formation and properties of ionic compounds, metallurgy, roasting, calcination, refining of metals, corrosion and its prevention, alloys (brass, bronze, solder, amalgam)"
                },
                {
                    "number": "4",
                    "name_en": "Carbon and its Compounds",
                    "name_hi": "कार्बन एवं उसके यौगिक",
                    "desc": "Covalent bonding in carbon compounds, versatile nature of carbon (catenation, tetravalency), allotropes of carbon (diamond, graphite, fullerenes), homologous series, functional groups (alcohol -OH, aldehyde -CHO, ketone -CO-, carboxylic acid -COOH), saturated/unsaturated hydrocarbons (alkanes, alkenes, alkynes), chemical properties (combustion, oxidation, addition, substitution), ethanol and ethanoic acid, soaps and detergents, micelle formation"
                },
                {
                    "number": "5",
                    "name_en": "Periodic Classification of Elements",
                    "name_hi": "तत्वों का आवर्त वर्गीकरण",
                    "desc": "Early attempts at classification: Dobereiner's triads, Newlands' law of octaves, Mendeleev's periodic table and periodic law, Modern periodic table (Henry Moseley), modern periodic law, groups and periods, periodic trends: valency, atomic size, metallic and non-metallic properties, electronegativity"
                },
                {
                    "number": "6",
                    "name_en": "Life Processes",
                    "name_hi": "जैव प्रक्रम",
                    "desc": "Nutrition (autotrophic, heterotrophic, photosynthesis, stomata, human digestive system, enzymes pepsin, trypsin, bile), Respiration (aerobic, anaerobic, glycolysis, ATP, human respiratory system, alveoli), Transportation (human circulatory system, heart structure, double circulation, arteries, veins, capillaries, xylem, phloem, transpiration), Excretion (human excretory system, nephron structure and function, urine formation, dialysis)"
                },
                {
                    "number": "7",
                    "name_en": "Control and Coordination",
                    "name_hi": "नियंत्रण एवं समन्वय",
                    "desc": "Nervous system in animals, neurons, synapse, reflex arc, reflex action, human brain (forebrain, midbrain, hindbrain, cerebellum, medulla), coordination in plants, tropic movements (phototropism, geotropism, hydrotropism, thigmotropism), plant hormones (auxin, gibberellin, cytokinin, abscisic acid), endocrine glands and hormones in humans (pituitary, thyroid, pancreas/insulin, adrenaline, testosterone, estrogen)"
                },
                {
                    "number": "8",
                    "name_en": "How do Organisms Reproduce?",
                    "name_hi": "जीव जनन कैसे करते हैं?",
                    "desc": "Asexual reproduction (binary fission in Amoeba, multiple fission in Plasmodium, budding in Yeast/Hydra, spore formation in Rhizopus, regeneration in Planaria, fragmentation in Spirogyra, vegetative propagation), Sexual reproduction in flowering plants (stamen, carpel, pollination, fertilization, seed formation), Human reproduction (male reproductive system: testes, sperm, female reproductive system: ovary, fallopian tube, uterus, menstrual cycle, fertilization, placenta), Reproductive health, contraception methods (condoms, oral pills, copper-T, vasectomy, tubectomy), STDs (gonorrhea, syphilis, HIV/AIDS)"
                },
                {
                    "number": "9",
                    "name_en": "Heredity and Evolution",
                    "name_hi": "आनुवंशिकता एवं जैव विकास",
                    "desc": "Heredity, Mendel's experiments on garden peas (Pisum sativum), monohybrid cross (3:1 ratio), dihybrid cross (9:3:3:1 ratio), dominant and recessive traits, sex determination in humans (XX and XY chromosomes), speciation, evolution, homologous and analogous organs, fossils"
                },
                {
                    "number": "10",
                    "name_en": "Light – Reflection and Refraction",
                    "name_hi": "प्रकाश – परावर्तन तथा अपवर्तन",
                    "desc": "Reflection of light, spherical mirrors (concave and convex mirrors), pole, center of curvature, focus, focal length, mirror formula 1/f = 1/v + 1/u, magnification m = -v/u, Refraction of light, laws of refraction, Snell's law (sin i / sin r = constant), refractive index, spherical lenses (convex and concave lenses), lens formula 1/f = 1/v - 1/u, magnification m = v/u, power of lens P = 1/f in dioptres (D)"
                },
                {
                    "number": "11",
                    "name_en": "The Human Eye and the Colourful World",
                    "name_hi": "मानव नेत्र तथा रंगबिरंगा संसार",
                    "desc": "Human eye structure (cornea, iris, pupil, eye lens, retina, ciliary muscles), power of accommodation, defects of vision and their correction (myopia / near-sightedness using concave lens, hypermetropia / far-sightedness using convex lens, presbyopia, cataract), refraction of light through a glass prism, dispersion of white light (VIBGYOR spectrum), atmospheric refraction (twinkling of stars, advance sunrise and delayed sunset), scattering of light, Tyndall effect, blue colour of the clear sky, reddish appearance of the sun at sunrise and sunset"
                },
                {
                    "number": "12",
                    "name_en": "Electricity",
                    "name_hi": "विद्युत",
                    "desc": "Electric current (I = Q/t, Ampere), electric potential and potential difference (V = W/Q, Volt), voltmeter and ammeter, Ohm's law (V = IR), resistance (R = rho * L / A), resistivity, factors affecting resistance, series combination of resistors (R_eq = R1 + R2 + ...), parallel combination of resistors (1/R_eq = 1/R1 + 1/R2 + ...), heating effect of electric current (Joule's law of heating H = I^2*R*t), electric power (P = VI = I^2*R = V^2/R, Watt), commercial unit of electric energy (kWh / units)"
                },
                {
                    "number": "13",
                    "name_en": "Magnetic Effects of Electric Current",
                    "name_hi": "विद्युत धारा के चुंबकीय प्रभाव",
                    "desc": "Magnetic field and field lines, magnetic field due to current through a straight conductor, Right-Hand Thumb Rule, magnetic field due to a circular loop and solenoid, electromagnet and permanent magnet, force on a current-carrying conductor in a magnetic field, Fleming's Left-Hand Rule, electric motor, electromagnetic induction (Michael Faraday), Fleming's Right-Hand Rule, electric generator (AC and DC), domestic electric circuits (live wire, neutral wire, earth wire, fuse, short circuit, overloading)"
                },
                {
                    "number": "14",
                    "name_en": "Sources of Energy",
                    "name_hi": "ऊर्जा के स्रोत",
                    "desc": "Conventional sources of energy (fossil fuels: coal, petroleum, natural gas; thermal power plant, hydro power plant), biomass and bio-gas plant, wind energy (windmills), Non-conventional sources of energy (solar energy, solar cooker, solar cell, energy from the sea: tidal energy, wave energy, ocean thermal energy OTEC, geothermal energy, nuclear energy: nuclear fission and fusion), environmental consequences, renewable and non-renewable sources of energy"
                },
                {
                    "number": "15",
                    "name_en": "Improvement in Food Resources",
                    "name_hi": "खाद्य संसाधनों में सुधार",
                    "desc": "Improvement in crop yields, crop varieties (hybridization, genetic modification), crop production management, nutrients (macronutrients, micronutrients), manure and fertilizers, irrigation methods, cropping patterns (mixed cropping, intercropping, crop rotation), crop protection management (weeds, pests, storage of grains), Animal husbandry (cattle farming, poultry farming, egg and broiler production, fish production: capture fishing, aquaculture, composite fish culture, bee-keeping / apiculture, honey production)"
                },
                {
                    "number": "16",
                    "name_en": "Our Environment",
                    "name_hi": "हमारा पर्यावरण",
                    "desc": "Ecosystem and its components (biotic and abiotic), food chain, food web, trophic levels (producers, primary, secondary, tertiary consumers, decomposers), 10 percent law of energy transfer (Lindeman), biological magnification (biomagnification of pesticides/DDT), ozone layer and how it is getting depleted (CFCs, Montreal Protocol), managing garbage and solid waste, biodegradable and non-biodegradable wastes"
                }
            ]
        }
    },
    "social_science": {
        "is_multi_section": True,
        "sections": {
            "History": [
                {
                    "number": "1",
                    "name_en": "Nationalism in Europe",
                    "name_hi": "यूरोप में राष्ट्रवाद",
                    "desc": "Frederic Sorrieu vision, French Revolution, Napoleon and Napoleonic Code 1804, liberalism, Zollverein, Treaty of Vienna 1815, Duke Metternich, Giuseppe Mazzini and Young Italy, Greek War of Independence, Romanticism, Unification of Germany (Otto von Bismarck, blood and iron policy), Unification of Italy (Count Cavour, Giuseppe Garibaldi, Victor Emmanuel II)"
                },
                {
                    "number": "2",
                    "name_en": "Socialism and Communism",
                    "name_hi": "समाजवाद एवं साम्यवाद",
                    "desc": "Utopian socialists (Robert Owen, Saint-Simon, Charles Fourier), Karl Marx and Friedrich Engels, Das Kapital, Communist Manifesto, Russian Revolution 1917 (February and October/Bolshevik Revolutions), Tsar Nicholas II, Vladimir Lenin, April Theses, New Economic Policy (NEP), Joseph Stalin and collectivization, Comintern"
                },
                {
                    "number": "3",
                    "name_en": "Nationalist Movement in Indo-China",
                    "name_hi": "हिंद-चीन में राष्ट्रवादी आंदोलन",
                    "desc": "Indo-China comprising Vietnam, Laos, and Cambodia; French colonial rule, civilizing mission, Tonkin Free School, resistance movements, Phan Boi Chau and The History of the Loss of Vietnam, Ho Chi Minh, Vietnamese Communist Party, Vietminh, Dien Bien Phu battle 1954, Geneva conference, partition into North and South Vietnam, US involvement, chemical warfare (Agent Orange, Napalm), Ho Chi Minh Trail, reunification of Vietnam 1975"
                },
                {
                    "number": "4",
                    "name_en": "Nationalism in India",
                    "name_hi": "भारत में राष्ट्रवाद",
                    "desc": "First World War impact, Mahatma Gandhi and Satyagraha (Champaran 1917, Kheda 1918, Ahmedabad mill strike), Rowlatt Act 1919, Jallianwala Bagh massacre (General Dyer, 13 April 1919), Khilafat Movement (Ali brothers), Non-Cooperation Movement 1920-1922, Chauri Chaura incident, Swaraj Party, Simon Commission 1928 (Lala Lajpat Rai), Lahore Congress 1929 and Purna Swaraj, Salt March / Dandi March 1930, Civil Disobedience Movement, Gandhi-Irwin Pact, Round Table Conferences, Poona Pact (BR Ambedkar and Gandhi), Quit India Movement 1942, Bharat Mata iconography"
                },
                {
                    "number": "5",
                    "name_en": "Economy and Livelihood",
                    "name_hi": "अर्थव्यवस्था और आजीविका",
                    "desc": "Industrial Revolution in Britain and India, proto-industrialization, steam engine (James Watt), spinning jenny, factory system, textile industries, cotton mills in Bombay (Kawasji Nanabhai Davar 1854), jute mills in Bengal, Tata Iron and Steel Company (TISCO, Jamshedpur 1907 by Jamsetji Tata), working class conditions, trade unions, Factories Act"
                },
                {
                    "number": "6",
                    "name_en": "Urbanization and Urban Life",
                    "name_hi": "शहरीकरण एवं शहरी जीवन",
                    "desc": "Characteristics of cities, growth of industrial cities (London, Bombay, Calcutta), transformation from rural to urban, housing, chawls, tenements, urban sanitation, Baron Haussmann Paris rebuilding, development of modern Patna (ancient Pataliputra, Golghar, British administrative center), social life in cities"
                },
                {
                    "number": "7",
                    "name_en": "Trade and Globalization",
                    "name_hi": "व्यापार और भूमंडलीकरण",
                    "desc": "History of world trade, Silk Route, pre-modern exchange of goods, food (potato, corn), diseases (smallpox in Americas), 19th-century world economy (flow of trade, labor, capital), indentured labor migration, Great Depression 1929, post-war reconstruction, Bretton Woods institutions (IMF and World Bank), multinational corporations (MNCs)"
                },
                {
                    "number": "8",
                    "name_en": "Press, Culture and Nationalism",
                    "name_hi": "प्रेस संस्कृति एवं राष्ट्रवाद",
                    "desc": "Invention of printing, Johannes Gutenberg and printing press, spread of print culture in Europe, Protestant Reformation (Martin Luther), print culture and French Revolution, development of print in India, James Augustus Hicky and Bengal Gazette, Raja Ram Mohan Roy (Sambad Kaumudi), Vernacular Press Act 1878 (Lord Lytton), role of nationalist newspapers (Kesari by Bal Gangadhar Tilak, Amrita Bazar Patrika), censorship"
                }
            ],
            "Economics": [
                {
                    "number": "1",
                    "name_en": "History of Economy and its Development",
                    "name_hi": "अर्थव्यवस्था एवं इसके विकास का इतिहास",
                    "desc": "Economic systems: Capitalist, Socialist, Mixed economy (India's mixed economy); Sectors of economy: Primary (agriculture, dairy, forestry, fishing), Secondary (manufacturing, industry, construction), Tertiary (services: banking, transport, communication, education); Economic development, sustainable development, Human Development Index (HDI), National Development Council, NITI Aayog / Planning Commission (Five Year Plans), Bihar economic status"
                },
                {
                    "number": "2",
                    "name_en": "State and National Income",
                    "name_hi": "राज्य एवं राष्ट्र की आय",
                    "desc": "National Income (NI), Gross Domestic Product (GDP), Gross National Product (GNP), Net National Product (NNP), Per Capita Income (PCI = Total National Income / Total Population), World Bank criteria for developed and developing countries, Central Statistical Office (CSO), methods of measuring national income: production, income, and expenditure methods, economic poverty and income disparity in Bihar districts (Patna highest PCI, Sheohar lowest)"
                },
                {
                    "number": "3",
                    "name_en": "Money, Savings and Credit",
                    "name_hi": "मुद्रा, बचत एवं साख",
                    "desc": "Barter system and double coincidence of wants, evolution of money: commodity money, metallic money, paper money, credit money (cheques, drafts), plastic money (ATM card, debit card, credit card), core banking, functions of money (medium of exchange, measure of value, store of value, standard of deferred payment), Savings (income minus consumption), Credit / Loan (formal vs informal sources of credit), terms of credit (collateral, interest rate, documentation)"
                },
                {
                    "number": "4",
                    "name_en": "Our Financial Institutions",
                    "name_hi": "हमारी वित्तीय संस्थाएँ",
                    "desc": "Financial institutions in India: institutional vs non-institutional sources; Institutional: Commercial banks (SBI, PNB), Central bank (Reserve Bank of India - RBI, monetary authority), Cooperative banks, Regional Rural Banks (RRBs), NABARD, Self Help Groups (SHGs / Swayam Sahayata Samooh); Non-institutional: Mahajans, Moneylenders, Traders, Relatives; Microfinance, Grameen Bank model (Muhammad Yunus)"
                },
                {
                    "number": "5",
                    "name_en": "Employment and Services",
                    "name_hi": "रोजगार एवं सेवाएँ",
                    "desc": "Employment, relationship between employment and service sector, government vs non-government services, organized vs unorganized sectors, outsourcing (call centers, BPO, IT services in India), India as a global outsourcing destination, MGNREGA (100 days guaranteed employment scheme), challenges of unemployment in Bihar"
                },
                {
                    "number": "6",
                    "name_en": "Globalization",
                    "name_hi": "वैश्वीकरण",
                    "desc": "Globalization definition, integration of national economy with world economy; Factors promoting globalization: technology, transport, telecommunication, internet; Liberalization and Privatization (LPG reforms 1991); Multinational Corporations (MNCs / Bahurashtriya Kampaniyan) like Nike, Samsung, Coca-Cola; World Trade Organization (WTO / Vishwa Vyapar Sangathan, established 1995, Geneva); Impact of globalization on India and Bihar"
                },
                {
                    "number": "7",
                    "name_en": "Consumer Awareness and Protection",
                    "name_hi": "उपभोक्ता जागरण एवं संरक्षण",
                    "desc": "Consumer exploitation (adulteration, under-weighing, over-charging, false advertising), Consumer rights: right to safety, right to be informed, right to choose, right to be heard, right to seek redressal, right to consumer education; Consumer Protection Act 1986 (COPRA); Three-tier quasi-judicial system: District Forum (up to 20 lakhs / 1 crore), State Commission, National Commission; Consumer slogans ('Jago Grahak Jago'), standard marks: ISI mark (industrial products), AGMARK (agricultural products), Hallmark (gold jewelry), FPO (food products), National Consumer Day (24 December)"
                }
            ],
            "Geography": [
                {
                    "number": "1",
                    "name_en": "India: Resources and Utilization",
                    "name_hi": "भारत: संसाधन एवं उपयोग",
                    "desc": "Resource classification (biotic/abiotic, renewable/non-renewable, individual/community/national/international), sustainable development, Rio Earth Summit 1992, Agenda 21, Resource planning in India, Land resources and land utilization, land degradation and conservation, Soil types of India: Alluvial soil (Jalodh mitti: Khadar and Bangar), Black soil (Regur mitti - cotton cultivation), Red and yellow soils, Laterite soil, Arid/Desert soil, Forest soil, soil erosion and conservation measures"
                },
                {
                    "number": "2",
                    "name_en": "Agriculture",
                    "name_hi": "कृषि",
                    "desc": "Types of farming: Primitive subsistence farming (Jhumming / slash and burn), Intensive subsistence farming, Commercial farming (Plantation agriculture: tea, coffee, rubber); Cropping seasons: Rabi (winter crops: wheat, gram, mustard), Kharif (monsoon crops: rice/paddy, maize, cotton), Zaid (summer crops: watermelon, cucumber); Major food crops: Rice (paddy, temperature >25C, rainfall >100cm), Wheat, Millets (Jowar, Bajra, Ragi), Pulses, Sugarcane, Oilseeds; Institutional and technological reforms, Green Revolution, White Revolution (Operation Flood)"
                },
                {
                    "number": "3",
                    "name_en": "Manufacturing Industries",
                    "name_hi": "निर्माण उद्योग",
                    "desc": "Importance of manufacturing, factors influencing industrial location; Classification of industries: Agro-based industries (textiles: cotton, jute, silk; sugar industry), Mineral-based industries (Iron and steel industry: TISCO, Bhilai, Bokaro, Rourkela; Aluminum smelting, Chemical industries, Fertilizer industry, Cement industry, Automobile industry, Information Technology and electronics industry: Bengaluru silicon valley); Industrial pollution and environmental degradation"
                },
                {
                    "number": "4",
                    "name_en": "Transport, Communication and Trade",
                    "name_hi": "परिवहन, संचार एवं व्यापार",
                    "desc": "Means of transport: Roadways (Golden Quadrilateral Super Highways, National Highways NH-44, State Highways, PMGSY rural roads), Railways (broad gauge, meter gauge, railway zones, Konkan railway), Pipelines (crude oil, natural gas pipelines like HVJ pipeline), Waterways (Inland Waterways Authority, National Waterway No. 1 Ganga: Allahabad to Haldia), Major seaports (Kandla, Mumbai, Marmagao, Chennai, Visakhapatnam, Kolkata); Airways (Air India, domestic and international airports); Communication: Postal network, Telecom network, Mass communication (Radio, Television/Doordarshan, Newspapers, Internet); International trade (Balance of trade: favorable vs unfavorable trade)"
                },
                {
                    "number": "5",
                    "name_en": "Bihar: Agriculture and Forest Resources",
                    "name_hi": "बिहार: कृषि एवं वन संसाधन",
                    "desc": "Bihar's agrarian economy, cropping seasons in Bihar, major crops (rice, wheat, maize, pulses, jute in Purnea/Katihar, sugarcane in Champaran/Gopalganj, tobacco/tamaku), irrigation projects (Son river canal project, Gandak project, Kosi multipurpose project), forest cover in Bihar (around 7% forest area, protected forests in West Champaran, Kaimur, Rohtas, Valmiki National Park/Tiger Reserve), mineral resources in Bihar (pyrite in Rohtas, limestone, mica in Nawada/Jamui, sand)"
                },
                {
                    "number": "6",
                    "name_en": "Map Study",
                    "name_hi": "मानचित्र अध्ययन",
                    "desc": "Methods of representing relief on maps: Contour lines (Samochha rekhaen), Hachures (Lehman method), Hill shading, Layer tinting / coloring method; reading topographic maps, identifying mountains, plateaus, valleys, slopes, rivers on maps"
                },
                {
                    "number": "7",
                    "name_en": "Natural Disaster: An Introduction",
                    "name_hi": "प्राकृतिक आपदा: एक परिचय",
                    "desc": "Definition of disaster, difference between natural hazards and natural disasters, classification of natural disasters (geological: earthquakes, volcanoes, landslides; meteorological/climatic: floods, droughts, cyclones, tsunamis), man-made disasters (nuclear accidents, chemical leaks, wars, terrorism), vulnerable zones in India, disaster management framework"
                },
                {
                    "number": "8",
                    "name_en": "Natural Disaster Management: Flood and Drought",
                    "name_hi": "प्राकृतिक आपदा एवं प्रबंधन: बाढ़ एवं सुखाड़",
                    "desc": "Floods: Causes of floods, flood-prone areas in North Bihar, Kosi river known as the 'Sorrow of Bihar' (Bihar ka Shok), Bagmati, Gandak, Kamla Balan, embankments, flood forecasting, rescue and relief measures, safety during floods; Droughts: Causes of drought (monsoon failure, deforestation), drought-prone areas in South Bihar (Gaya, Nawada, Jamui, Aurangabad), rain-water harvesting, drip irrigation, water conservation, drought mitigation"
                },
                {
                    "number": "9",
                    "name_en": "Natural Disaster Management: Earthquake and Tsunami",
                    "name_hi": "प्राकृतिक आपदा एवं प्रबंधन: भूकंप एवं सुनामी",
                    "desc": "Earthquake: Focus (Hypocenter), Epicenter, seismic waves (P-waves, S-waves, L-waves), measurement using Seismograph and Richter Scale, earthquake zones in India (Zone I to Zone V, Bihar in high-risk seismic Zone IV and V, 1934 Bihar-Nepal earthquake), earthquake-resistant building design, safety precautions during earthquake; Tsunami: Underwater earthquake in ocean, harbor wave, 26 December 2004 Indian Ocean tsunami, tsunami warning systems"
                },
                {
                    "number": "10",
                    "name_en": "Life Saving Emergency Management",
                    "name_hi": "जीवन रक्षक आकस्मिक प्रबंधन",
                    "desc": "Emergency measures immediately following a disaster: search and rescue operations, first aid, emergency medical care, evacuation, providing safe drinking water, food packets, temporary shelters, preventing epidemic disease outbreak after flood/earthquake, role of community, local youth, civil administration and disaster relief forces (NDRF, SDRF)"
                },
                {
                    "number": "11",
                    "name_en": "Alternative Communication during Disasters",
                    "name_hi": "आपदा काल में वैकल्पिक संचार व्यवस्था",
                    "desc": "Failure of conventional communication networks (telephones, mobile towers, electricity grid collapse) during natural disasters, alternative communication systems: Radio communication, HAM radio (Amateur Radio), Satellite phones / satellite communication systems, emergency warning dissemination"
                },
                {
                    "number": "12",
                    "name_en": "Disaster and Co-existence",
                    "name_hi": "आपदा और सह-अस्तित्व",
                    "desc": "Living with disasters, building community resilience and awareness, disaster preparedness drills, constructing disaster-resilient houses (raised plinths in flood zones, light roofing in earthquake zones), integration of traditional knowledge with modern science for disaster risk reduction"
                }
            ],
            "Civics": [
                {
                    "number": "1",
                    "name_en": "Power Sharing in Democracy",
                    "name_hi": "लोकतंत्र में सत्ता की साझेदारी",
                    "desc": "Concept and necessity of power sharing, case study of Belgium (Dutch and French speaking communities, constitutional accommodation, Brussels capital model) vs case study of Sri Lanka (Sinhala majority dominance, majoritarianism, Tamil alienation, civil war), forms of power sharing: horizontal division of power (Legislature, Executive, Judiciary - checks and balances), vertical division of power (Federalism: Union, State, Local governments), power sharing among social groups (reserved constituencies), coalition governments"
                },
                {
                    "number": "2",
                    "name_en": "Federalism (Working of Power Sharing)",
                    "name_hi": "सत्ता में साझेदारी की कार्यप्रणाली (संघवाद)",
                    "desc": "What is federalism, key features of federalism, 'Coming together' federations (USA, Switzerland) vs 'Holding together' federations (India, Spain), legislative powers divided between Union and States: Union List (97 subjects: defense, foreign affairs, banking, currency), State List (66 subjects: police, trade, agriculture, irrigation), Concurrent List (47 subjects: education, forest, marriage, trade unions), Residuary powers with Center; Decentralization in India, Panchayati Raj system, 73rd and 74th Constitutional Amendment Acts 1992, Gram Panchayat, Mukhiya, Panchayat Samiti, Zila Parishad, Nagar Nigam / Municipal Corporation, Mayor, 50% reservation for women in Bihar Panchayati Raj"
                },
                {
                    "number": "3",
                    "name_en": "Democracy and Diversity",
                    "name_hi": "लोकतंत्र और विविधता",
                    "desc": "Social differences, origins of social differences (by birth vs by choice), overlapping and cross-cutting social differences (Northern Ireland vs Netherlands), Civil Rights Movement in USA (Martin Luther King Jr.), 1968 Mexico Olympics black power protest (Tommie Smith, John Carlos, Peter Norman), politics of social divisions, three determinants determining outcome of politics of social divisions"
                },
                {
                    "number": "4",
                    "name_en": "Gender, Religion and Caste",
                    "name_hi": "जाति, धर्म और लैंगिक मसले",
                    "desc": "Gender and politics: sexual division of labor, feminist movement, female literacy rate, sex ratio, political representation of women, Women's reservation in parliament and Panchayats; Religion, communalism and politics: secular state in India (no official religion, freedom of religion Articles 25-28), communal politics, religious tolerance; Caste and politics: caste system in India, social reformers (Jyotirao Phule, Gandhiji, BR Ambedkar, Periyar), caste inequalities, role of caste in elections and voting behavior, politics within caste"
                },
                {
                    "number": "5",
                    "name_en": "Popular Struggles and Movements",
                    "name_hi": "जन-संघर्ष और आंदोलन",
                    "desc": "Role of popular struggles in democracy, movement for restoration of democracy in Nepal 2006 (Seven Party Alliance - SPA, Maoists, King Gyanendra), Bolivia's water war (struggle against privatization of water by MNC in Cochabamba), Chipko Movement in Uttarakhand (Sunderlal Bahuguna, hugging trees), Narmada Bachao Andolan (Medha Patkar, Sardar Sarovar Dam), Bharatiya Kisan Union (BKU, Mahendra Singh Tikait), Anti-Arrack Movement in Andhra Pradesh, Right to Information (RTI Act 2005 movement by MKSS / Aruna Roy), Pressure groups and interest groups vs political movements"
                },
                {
                    "number": "6",
                    "name_en": "Political Parties",
                    "name_hi": "राजनीतिक दल",
                    "desc": "Meaning and necessity of political parties, components of a political party (leaders, active members, followers), functions of political parties (contesting elections, putting forward policies, making laws, forming and running government, role of opposition), party systems (one-party system: China, two-party system: USA/UK, multi-party system: India, coalition politics); National parties in India (criteria set by Election Commission of India: BJP, INC/Congress, CPI, CPI-M, BSP, AAP); Regional / State parties in Bihar (RJD - Rashtriya Janata Dal, JD(U) - Janata Dal United, LJP - Lok Janshakti Party); Challenges to political parties (lack of internal democracy, dynastic succession, money and muscle power, lack of meaningful choice); Electoral reforms, Anti-defection law (52nd Amendment)"
                },
                {
                    "number": "7",
                    "name_en": "Outcomes of Democracy",
                    "name_hi": "लोकतंत्र के परिणाम",
                    "desc": "Assessing democracy outcomes: Accountable, responsive and legitimate government; Transparency and citizens right to examine decision-making; Economic growth and development in democracies vs dictatorships; Reduction of inequality and poverty; Accommodation of social diversity and conflict resolution; Dignity and freedom of the citizens, rights of women and disadvantaged castes in democratic societies"
                },
                {
                    "number": "8",
                    "name_en": "Challenges to Democracy",
                    "name_hi": "लोकतंत्र की चुनौतियाँ",
                    "desc": "Major challenges faced by democracies globally and in India: Foundational challenge (transition to democracy), Challenge of expansion (applying democratic principles to all regions and institutions), Challenge of deepening of democracy (strengthening institutions and practices of citizen participation); Political reforms, empowering citizens, enhancing democratic participation"
                }
            ]
        }
    },
    "english": {
        "is_multi_section": True,
        "sections": {
            "Grammar": [
                {"number": "1", "name_en": "Parts of Speech (Overview)", "name_hi": "पार्ट्स ऑफ स्पीच (शब्द भेद)", "desc": "Identifying noun, pronoun, verb, adverb, adjective, preposition, conjunction, interjection in sentences"},
                {"number": "2", "name_en": "Determiners and Articles", "name_hi": "डिटरमिनर्स और आर्टिकल्स", "desc": "Articles a, an, the, definite and indefinite articles, determiners some, any, much, many, each, every, few, little"},
                {"number": "3", "name_en": "Tenses", "name_hi": "काल (टेंस)", "desc": "Present, past, future tenses: simple, continuous, perfect, perfect continuous, correct form of verbs in blanks"},
                {"number": "4", "name_en": "Subject-Verb Agreement", "name_hi": "कर्ता-क्रिया सहमति", "desc": "Singular/plural subject verb agreement, rules of either/or, neither/nor, along with, as well as, each of, collective nouns"},
                {"number": "5", "name_en": "Voice (Active and Passive)", "name_hi": "वाच्य", "desc": "Converting active voice to passive voice and passive voice to active voice across tenses, modals, imperatives"},
                {"number": "6", "name_en": "Narration (Direct and Indirect)", "name_hi": "कथन (प्रत्यक्ष और अप्रत्यक्ष)", "desc": "Direct to indirect speech, indirect to direct, reporting verbs said/told/asked, tense backshift, pronouns, interrogative/imperative sentences"},
                {"number": "7", "name_en": "Modals", "name_hi": "मोडल्स", "desc": "Modal auxiliary verbs can, could, may, might, shall, should, will, would, must, ought to, expressing permission, ability, duty, possibility"},
                {"number": "8", "name_en": "Prepositions", "name_hi": "प्रेपोजिशन्स", "desc": "Prepositions in, on, at, by, for, from, with, between, among, into, onto, fixed prepositions like look at, listen to, fond of, good at"},
                {"number": "9", "name_en": "Clauses", "name_hi": "क्लॉज (उपवाक्य)", "desc": "Noun clause, adjective clause, adverb clause, conditional clauses (if/unless), relative pronouns who, which, that"},
                {"number": "10", "name_en": "Transformation of Sentences (Simple, Complex, Compound)", "name_hi": "वाक्य रूपांतरण (सरल, मिश्रित, संयुक्त)", "desc": "Simple, complex, compound sentences, converting affirmative to negative, interrogative to assertive, removing too (so...that)"},
                {"number": "11", "name_en": "Degrees of Comparison", "name_hi": "तुलना की अवस्थाएँ (Degrees)", "desc": "Positive, comparative, superlative degrees (good, better, best; tall, taller, tallest; as...as, than)"},
                {"number": "12", "name_en": "Question Tags", "name_hi": "क्वेश्चन टैग्स", "desc": "Adding question tags to statements (isn't it, aren't they, didn't he, won't you)"},
                {"number": "13", "name_en": "Punctuation and Spelling", "name_hi": "विराम चिह्न और वर्तनी", "desc": "Finding correctly spelled word or incorrectly spelled word among four options, capitalization, commas, full stops"},
                {"number": "14", "name_en": "Synonyms and Antonyms", "name_hi": "पर्यायवाची और विलोम", "desc": "Synonyms (similar meaning words) and antonyms (opposite meaning words) vocabulary questions"},
                {"number": "15", "name_en": "Idioms and Phrases", "name_hi": "मुहावरे और वाक्यांश", "desc": "Meaning of English idioms, proverbs, and common idiomatic expressions like 'a piece of cake', 'once in a blue moon'"},
                {"number": "16", "name_en": "One Word Substitutions", "name_hi": "अनेक शब्दों के लिए एक शब्द", "desc": "Single word substituting a sentence or phrase (e.g. autobiography, atheist, omniscient, century)"},
                {"number": "17", "name_en": "Phrasal Verbs", "name_hi": "फ्रेज़ल वर्ब्स", "desc": "Verb plus preposition combinations like look after, give up, break down, call off, put out"},
                {"number": "18", "name_en": "Translation", "name_hi": "अनुवाद", "desc": "Translating Hindi sentences into English or English sentences into Hindi"},
                {"number": "19", "name_en": "Letter and Application Writing", "name_hi": "पत्र और आवेदन लेखन", "desc": "Formal letters, application to Principal/Headmaster, informal letters to friends/parents, structure and format"},
                {"number": "20", "name_en": "Paragraph and Essay Writing", "name_hi": "पैराग्राफ और निबंध लेखन", "desc": "Short essay or paragraph composition on topics like My Hobby, Pollution, Discipline, Mobile Phone, Reading comprehensions"}
            ],
            "Panorama": [
                {"number": "1", "name_en": "The Pace for Living", "name_hi": "जीवन की गति", "desc": "Prose by R. C. Hutchinson; fast-paced modern life, Irish corn merchant of Dublin, cinema play, slow thinkers, mind working in slow gear"},
                {"number": "2", "name_en": "Me and the Ecology Bit", "name_hi": "मैं और पारिस्थितिकी का अंश", "desc": "Prose by Joan Lexau; Jim advocating for ecology, paper boy, Mr. Williams, Ms. Greene, compost pile, burning leaves, pollution"},
                {"number": "3", "name_en": "Gillu", "name_hi": "गिल्लू", "desc": "Story by Mahadevi Verma; tiny baby squirrel saved from crows, Sonjuhi yellow flower creeper, small basket, glass beads, eating kaju/cashew nuts"},
                {"number": "4", "name_en": "What is Wrong with Indian Films?", "name_hi": "भारतीय फिल्मों में क्या खराबी है?", "desc": "Essay by Satyajit Ray; Indian cinema, Hollywood imitation vs Indian reality, visual movement, story and music, cinema as mature art form"},
                {"number": "5", "name_en": "Acceptance Speech", "name_hi": "स्वीकृति भाषण", "desc": "Speech delivered by Alexander Aris on behalf of his mother Aung San Suu Kyi upon winning the Nobel Peace Prize 1991 for democracy in Burma/Myanmar"},
                {"number": "6", "name_en": "Once Upon a Time", "name_hi": "एक समय की बात है", "desc": "Nobel Lecture story by Toni Morrison; old, blind, wise African-American woman, young people asking if the bird in their hand is living or dead, bird as metaphor for language"},
                {"number": "7", "name_en": "The Unity of Indian Culture", "name_hi": "भारतीय संस्कृति की एकता", "desc": "Lecture by Humayun Kabir at Baroda University; continuous unbroken Indian civilization, unity in diversity, absorption and assimilation of invaders"},
                {"number": "8", "name_en": "Little Girls Wiser than Men", "name_hi": "पुरुषों से अधिक समझदार छोटी लड़कियाँ", "desc": "Story by Leo Tolstoy; two little village girls Malasha and Akoulya, wearing new frocks at Easter, muddy puddle, mothers quarreling, grandmother, girls playing together happily"},
                {"number": "9", "name_en": "God Made the Country", "name_hi": "ईश्वर ने देहात बनाया", "desc": "Poem by William Cowper; God made the country and man made the town, rural peaceful life, groves, fields, birds singing vs noisy bustling cities, health and virtue"},
                {"number": "10", "name_en": "Ode on Solitude", "name_hi": "एकांत पर एक गीत", "desc": "Poem by Alexander Pope; happy the man whose wish and care a few paternal acres bound, self-sufficient quiet life, herds, trees, breathing quiet air, dying unlamented"},
                {"number": "11", "name_en": "Polythene Bag", "name_hi": "पॉलिथीन बैग", "desc": "Poem by Durga Prasad Panda; polythene bag never dissolves in earth crust, suffocates nature, produces pungent smell when burnt, like grief inside the heart"},
                {"number": "12", "name_en": "Thinner Than a Crescent", "name_hi": "अर्धचंद्र से भी पतला", "desc": "Poem by Maithili poet Vidyapati; Radha weeping in separation from Lord Krishna, tears carving a river, her body wasting away thinner than the crescent moon, Radha friend, Radha unable to answer, sorrow of Radha"},
                {"number": "13", "name_en": "The Empty Heart", "name_hi": "रिक्त हृदय", "desc": "Poem by Tamil poet Periasamy Thooran; greedy rich man praying to Kalpataru wishing tree, given seven pitchers full of gold, dies trying to fill the eighth half-empty pitcher, greed made him mad"},
                {"number": "14", "name_en": "Koel", "name_hi": "कोयल", "desc": "Poem by Puran Singh; black cuckoo / koel bird with high-pitched melody in mango leaves, fiery wings scorched by the spark of love, restless longing for beloved"},
                {"number": "15", "name_en": "The Sleeping Porter", "name_hi": "सोता हुआ कुली", "desc": "Poem by Nepali poet Laxmi Prasad Devkota; heavy load of 57 pounds on his back, climbing snowy mountain cliff, snow had melted, sweating in freezing cold, sweet sleep of the poor"},
                {"number": "16", "name_en": "Martha", "name_hi": "मार्था", "desc": "Poem by Walter de la Mare; Martha telling fairy stories and legends in hazel glen to listening children, her clear grey eyes, grave lovely head, tranquil fairy tales"}
            ],
            "Panorama_Reader": [
                {"number": "1", "name_en": "January Night", "name_hi": "पूस की रात", "desc": "Supplementary Reader story by Premchand; poor tenant farmer Halku, wife Munni, pet dog Jabra, landlord Sahna, chilling winter night in field, burning crop leaves, ruined harvest"},
                {"number": "2", "name_en": "Allergy", "name_hi": "एलर्जी", "desc": "Supplementary Reader essay by Dr. Rana S. P. Singh; causes of allergy, allergens, immune system, sneezing, asthma, histamine, quick reaction"},
                {"number": "3", "name_en": "The Bet", "name_hi": "शर्त", "desc": "Supplementary Reader story by Anton Chekhov; bet between banker and young lawyer over capital punishment vs life imprisonment, 2 million rubles, 15 years solitary confinement, reading books, renouncing money"},
                {"number": "4", "name_en": "Quality", "name_hi": "गुणवत्ता", "desc": "Supplementary Reader story by John Galsworthy; German bootmaker brothers Mr. Gessler in London, making finest handcrafted leather boots, dedication to quality, slow starvation"},
                {"number": "5", "name_en": "Sun and Moon", "name_hi": "सन एंड मून", "desc": "Supplementary Reader story by Katherine Mansfield; children Sun and Moon observing adult evening dinner party, ice pudding, guests, children perspective"},
                {"number": "6", "name_en": "Two Horizons", "name_hi": "दो क्षितिज", "desc": "Supplementary Reader story by Binapani Mohanty; exchange of letters between mother and married daughter, search for woman true self, domestic compromise, identity"},
                {"number": "7", "name_en": "Love Defiled", "name_hi": "प्रेम का अपमान", "desc": "Supplementary Reader story by Giridhar Jha; relationship, love, compromise, social status, IAS marriage, betrayal, broken heart"}
            ]
        }
    },
    "hindi": {
        "is_multi_section": True,
        "sections": {
            "Varnika": [
                {"number": "1", "name_en": "Dahi Wali Magamma", "name_hi": "दही वाली मगम्मा", "desc": "कन्नड़ कहानी (लेखक: श्रीनिवास, अनुवाद: बी. आर. नारायण); दही बेचने वाली मगम्मा, बहू नजम्मा से विवाद, पोते पर हक, रंगप्पा जुआरी द्वारा पैसे ऐंठने की कोशिश, सास-बहू का संबंध"},
                {"number": "2", "name_en": "Dhate Vishwas", "name_hi": "ढहते विश्वास", "desc": "उड़िया कहानी (लेखक: सातकोड़ी होता, अनुवाद: राजेंद्र प्रसाद मिश्र); उड़ीसा में महानदी और दलेई बाँध टूटना, देवी नदी का प्रकोप, लक्ष्मी, उसके पति लक्ष्मण का कोलकाता में काम, गुणनिधि स्वेच्छा सेवक दल, बाढ़ की विभीषिका"},
                {"number": "3", "name_en": "Maa", "name_hi": "माँ", "desc": "गुजराती कहानी (लेखक: ईश्वर पेटलीकर, अनुवाद: गोपालदास नागर); जन्म से पागल और गूँगी लड़की मंगु, उसकी माँ का अगाध वात्सल्य, कुसुम का अस्पताल में ठीक होना, माँ द्वारा मंगु को अस्पताल भर्ती कराना, माँ का भी पुत्री के प्रेम में पागल हो जाना"},
                {"number": "4", "name_en": "Nagar", "name_hi": "नगर", "desc": "तमिल कहानी (लेखक: सुजाता, अनुवाद: के. ए. जमुना); वल्ली अम्मल की 12 वर्षीय पुत्री पाप्पाति को मेनिनजाइटिस बुखार, मदुरै शहर के बड़े अस्पताल में इलाज की भटकन, शहरी असंवेदनशीलता और नौकरशाही"},
                {"number": "5", "name_en": "Dharti Kab Tak Ghoomegi", "name_hi": "धरती कब तक घूमेगी", "desc": "राजस्थानी कहानी (लेखक: सांवर दइया); बूढ़ी माँ सीता, उसके तीन बेटे (कैलाश, नारायण, बिज्जू) और बहुएँ (राधा, पुष्पा, भंवरी), माँ को पचास-पचास रुपये मासिक देने का फैसला, सीता का स्वाभिमान और घर छोड़कर निकल पड़ना"}
            ],
            "Godhuli": [
                {"number": "1", "name_en": "Shram Vibhajan aur Jati Pratha", "name_hi": "श्रम विभाजन और जाति प्रथा", "desc": "बाबासाहेब भीमराव आंबेडकर का भाषण 'एनिहिलेशन ऑफ कास्ट'; जाति प्रथा श्रम विभाजन नहीं बल्कि श्रमिकों का अस्वाभाविक विभाजन है, लोकतंत्र की आधारशिला स्वतंत्रता, समता, बंधुत्व"},
                {"number": "2", "name_en": "Vish ke Daant", "name_hi": "विष के दाँत", "desc": "नलीन विलोचन शर्मा की कहानी; सेन साहब, उनका बिगड़ा बेटा काशू (खोखा), गरीब किरानी का बेटा मदन, काशू के विष के दो दाँत तोड़ना, वर्ग संघर्ष और महलों-झोपड़ियों की लड़ाई"},
                {"number": "3", "name_en": "Bharat se Hum Kya Seekhe", "name_hi": "भारत से हम क्या सीखें", "desc": "मैक्स मूलर का व्याख्यान; भारत की प्राचीन संस्कृति, संस्कृत भाषा, नीति कथाएं, वारेन हेस्टिंग्स को वाराणसी में मिले दारिस नामक 172 सोने के सिक्के, सच्चा भारत गाँवों में बसता है"},
                {"number": "4", "name_en": "Nakhun Kyon Badhte Hain", "name_hi": "नाखून क्यों बढ़ते हैं", "desc": "आचार्य हजारी प्रसाद द्विवेदी का ललित निबंध; छोटी लड़की का सवाल, नाखून बर्बर पाशविक वृत्ति का प्रतीक है और उन्हें काटना मनुष्यता का लक्षण, अस्त्र-शस्त्रों की होड़"},
                {"number": "5", "name_en": "Nagari Lipi", "name_hi": "नागरी लिपि", "desc": "गुणाकर मुले का निबंध; देवनागरी लिपि का ऐतिहासिक विकास, नंदीनागरी, सिद्धम लिपि, राष्ट्रकूट, चालुक्य, प्रतिहार राजाओं के शिलालेख, हिंदी और प्राकृत भाषाओं की लिपि"},
                {"number": "6", "name_en": "Bahadur", "name_hi": "बहादुर", "desc": "अमरकांत की कहानी; नेपाल से भागा भोला नौकर बहादुर (दिलबहादुर), लेखक का परिवार, निर्मला, बेटा किशोर, बहादुर पर चोरी का झूठा आरोप, उसका बिना वेतन लिए घर छोड़कर चले जाना"},
                {"number": "7", "name_en": "Parampara ka Mulyankan", "name_hi": "परंपरा का मूल्यांकन", "desc": "रामविलास शर्मा का आलोचनात्मक निबंध; प्रगतिशील साहित्य, शेक्सपियर, वाल्मीकि, व्यास, जातीय चेतना, सामंतवाद और पूंजीवाद से अलग साहित्य की परंपरा का मूल्यांकन"},
                {"number": "8", "name_en": "Jit-Jit Main Nirakhat Hoon", "name_hi": "जित-जित मैं निरखत हूँ", "desc": "पंडित बिरजू महाराज का साक्षात्कार (रश्मि वाजपेयी द्वारा); कथक नृत्य, लखनऊ घराना, अच्छन महाराज (पिता), शंभू महाराज (चाचा), घुंघरू, साधना, कला अकादमी"},
                {"number": "9", "name_en": "Aavinyon", "name_hi": "आविन्यों", "desc": "अशोक वाजपेयी का यात्रा-संस्मरण; दक्षिणी फ्रांस का रोन नदी किनारे पुराना शहर आविन्यों, ला सत्रूज ईसाई मठ, विलनव्य ला आविन्यों, रंगमंच और कविता लेखन"},
                {"number": "10", "name_en": "Machhli", "name_hi": "मछली", "desc": "विनोद कुमार शुक्ल की कहानी; बारिश के दिन बाजार से तीन मछलियाँ लाना, संतू और नरेन, कुएँ में मछली पालने की इच्छा, दीदी, भक्कू नौकर, पिताजी का गुस्सा"},
                {"number": "11", "name_en": "Naubatkhane mein Ibadat", "name_hi": "नौबतखाने में इबादत", "desc": "यतींद्र मिश्र का व्यक्तिचित्र; शहनाई के उस्ताद भारत रत्न बिस्मिल्ला खाँ (अमीरुद्दीन), डुमराँव, काशी विश्वनाथ और बालाजी मंदिर, शहनाई की रियाज, गंगा-जमुनी संस्कृति"},
                {"number": "12", "name_en": "Shiksha aur Sanskriti", "name_hi": "शिक्षा और संस्कृति", "desc": "महात्मा गांधी का शिक्षा दर्शन; बुनियादी शिक्षा (वर्धा शिक्षा योजना), चरित्र निर्माण, हाथ का काम सीखना, अहिंसक प्रतिरोध, सभी संस्कृतियों के लिए खुली खिड़कियाँ"},
                {"number": "13", "name_en": "Ram Binu Birthe Jagi Janma", "name_hi": "राम बिनु बिरथे जगि जनमा", "desc": "सिख धर्म के प्रवर्तक गुरु नानक देव के पद; बाह्य आडंबरों और पूजा-पाठ का विरोध, राम नाम की सच्ची महिमा, 'जो नर दुख में दुख नहिं मानै'"},
                {"number": "14", "name_en": "Prem Ayani Shri Radhika", "name_hi": "प्रेम अयनि श्री राधिका", "desc": "रसखान के सवैये; राधा-कृष्ण का प्रेम वाटिका के माली-मालिन के रूप में वर्णन, ब्रजभूमि के कुंज, करील के कुंजन ऊपर वारौं, कृष्ण रूप माधुरी"},
                {"number": "15", "name_en": "Ati Sudho Sneh ko Marag Hai", "name_hi": "अति सूधो सनेह को मारग है", "desc": "रीतिकाल के स्वच्छंद कवि घनानंद के कवित्त; प्रेम का मार्ग सीधा और सरल है, प्रेमिका सुजान, बादल के माध्यम से अपनी विरह वेदना सुजान के आँगन में बरसाना"},
                {"number": "16", "name_en": "Swadeshi", "name_hi": "स्वदेशी", "desc": "बदरीनारायण चौधरी 'प्रेमघन' के दोहे; भारत में विदेशी वस्तुओं, वेषभूषा और रीति-रिवाजों का बढ़ता प्रभाव, स्वदेशी भावना और भारतीयता का लुप्त होना, डफली बजाना"},
                {"number": "17", "name_en": "Bharat Mata", "name_hi": "भारतमाता", "desc": "प्रकृति के सुकुमार कवि सुमित्रानंदन पंत की कविता; ग्रामवासिनी भारतमाता, खेतों में फैला श्यामल धूल भरा आँचल, तीस कोटि संतान दरिद्र और शोषित, गीता प्रकाशिनी"},
                {"number": "18", "name_en": "Janatantra ka Janm", "name_hi": "जनतंत्र का जन्म", "desc": "राष्ट्रकवि रामधारी सिंह 'दिनकर' की ओजस्वी कविता; सदियों की ठंडी-बुझी राख में चिंगारी सुलग उठी, 'सिंहासन खाली करो कि जनता आती है', फावड़े और हल राजदंड बनने को हैं"},
                {"number": "19", "name_en": "Hiroshima", "name_hi": "हिरोशिमा", "desc": "सच्चिदानंद हीरानंद वात्स्यायन 'अज्ञेय' की कविता; दोपहर में सूरज का अचानक निकलना, परमाणु बम का विस्फोट, मानव द्वारा बनाया गया सूरज मानव को ही भाप बनाकर सोख गया"},
                {"number": "20", "name_en": "Ek Vriksha ki Hatya", "name_hi": "एक वृक्ष की हत्या", "desc": "कुँवर नारायण की कविता; घर के दरवाजे पर तैनात बूढ़ा चौकीदार वृक्ष, खाकी वर्दी, सूखी डाल, पर्यावरण संरक्षण और प्रकृति का संहार, शहरों को नदियों को बचाना"},
                {"number": "21", "name_en": "Hamari Neend", "name_hi": "हमारी नींद", "desc": "वीरेन डंगवाल की कविता; हमारे सोते रहने के दौरान भी जीवन-चक्र चलता रहता है, पेड़ का बढ़ना, मक्खी का जीवन-क्रम पूरा होना, अत्याचारियों का लगातार साधन जुटाना"},
                {"number": "22", "name_en": "Akshar-Gyan", "name_hi": "अक्षर-ज्ञान", "desc": "कवयित्री अनामिका की कविता; बच्चे द्वारा क, ख, ग, घ, ङ लिखना सीखने की प्रक्रिया, क कबूतर, ख खरगोश, ग गमला, घ घड़ा, ङ को माँ और बिंदी को गोद में बैठा बेटा समझना"},
                {"number": "23", "name_en": "Lautkar Aaunga Phir", "name_hi": "लौटकर आऊँगा फिर", "desc": "बांग्ला कवि जीवनानंद दास की कविता (अनुवाद प्रयाग शुक्ल); बंगाल की हरी-भरी धरती से गहरा प्रेम, धान के खेत, कलकल करती नदियाँ, हंस, कौआ या पक्षी बनकर पुनः जन्म लेने की चाह"},
                {"number": "24", "name_en": "Mere Bina Tum Prabhu", "name_hi": "मेरे बिना तुम प्रभु", "desc": "जर्मन कवि रेनर मारिया रिल्के की कविता (अनुवाद धर्मवीर भारती); भक्त और भगवान का अटूट संबंध, भक्त के बिना भगवान निराश्रय हो जाएंगे, भक्त ही भगवान का जलपात्र और मदिरा है"}
            ],
            "Vyakaran": [
                {"number": "1", "name_en": "Alphabet and Phonetics", "name_hi": "वर्ण विचार और उच्चारण", "desc": "स्वर वर्ण, व्यंजन वर्ण, स्पर्श, अंतःस्थ, ऊष्म, संयुक्त व्यंजन, कंठ्य, तालव्य, मूर्धन्य, दंत्य, ओष्ठ्य उच्चारण स्थान, अल्पप्राण, महाप्राण, घोष, अघोष"},
                {"number": "2", "name_en": "Word Analysis (Tatsam, Tadbhav, Deshaj, Videshi)", "name_hi": "शब्द विचार (तत्सम, तद्भव, देशज, विदेशी)", "desc": "तत्सम शब्द (संस्कृत के मूल शब्द), तद्भव शब्द, देशज शब्द (खिड़की, लोटा, पगड़ी), विदेशी शब्द, रूढ़, यौगिक, योगरूढ़ शब्द"},
                {"number": "3", "name_en": "Sandhi", "name_hi": "संधि", "desc": "स्वर संधि (दीर्घ, गुण, वृद्धि, यण, अयादि), व्यंजन संधि, विसर्ग संधि, संधि विच्छेद और संधि युक्त शब्द"},
                {"number": "4", "name_en": "Samas", "name_hi": "समास", "desc": "अव्ययीभाव, तत्पुरुष, कर्मधारय, द्विगु, द्वंद्व, बहुव्रीहि समास के नियम और सामासिक पदों का विग्रह"},
                {"number": "5", "name_en": "Prefix and Suffix", "name_hi": "उपसर्ग और प्रत्यय", "desc": "उपसर्ग (शब्द के आगे जुड़ने वाले शब्दांश: प्र, अनु, अप, उप) और प्रत्यय (कृत प्रत्यय, तद्धित प्रत्यय, ईय, ता, इक)"},
                {"number": "6", "name_en": "Noun", "name_hi": "संज्ञा", "desc": "व्यक्तिवाचक, जातिवाचक, भाववाचक, समूहवाचक, द्रव्यवाचक संज्ञा और भाववाचक संज्ञा का निर्माण"},
                {"number": "7", "name_en": "Pronoun", "name_hi": "सर्वनाम", "desc": "पुरुषवाचक, निजवाचक, निश्चयवाचक, अनिश्चयवाचक, संबंधवाचक, प्रश्नवाचक सर्वनाम"},
                {"number": "8", "name_en": "Adjective", "name_hi": "विशेषण", "desc": "गुणवाचक, संख्यावाचक, परिमाणवाचक, सार्वनामिक विशेषण और प्रविशेषण"},
                {"number": "9", "name_en": "Verb", "name_hi": "क्रिया", "desc": "सकर्मक क्रिया, अकर्मक क्रिया, प्रेरणार्थक क्रिया, संयुक्त क्रिया, नामधातु क्रिया, पूर्वकालिक क्रिया"},
                {"number": "10", "name_en": "Indeclinable (Avyay)", "name_hi": "अव्यय", "desc": "क्रिया-विशेषण, संबंधबोधक, समुच्चयबोधक (और, लेकिन, किंतु), विस्मयादिबोधक अव्यय, निपात (भी, ही, तो)"},
                {"number": "11", "name_en": "Gender, Number and Case", "name_hi": "लिंग, वचन और कारक", "desc": "पुल्लिंग, स्त्रीलिंग; एकवचन, बहुवचन; कर्ता ने, कर्म को, करण से, संप्रदान को/के लिए, अपादान से, संबंध का/की/के, अधिकरण में/पर, संबोधन हे/अरे कारक चिह्न"},
                {"number": "12", "name_en": "Tense and Voice", "name_hi": "काल और वाच्य", "desc": "भूतकाल, वर्तमानकाल, भविष्यतकाल के भेद; कर्तृवाच्य, कर्मवाच्य, भाववाच्य और उनका रूपांतरण"},
                {"number": "13", "name_en": "Sentence and Structure", "name_hi": "वाक्य विचार और संरचना", "desc": "उद्देश्य और विधेय, रचना की दृष्टि से सरल, संयुक्त, मिश्र वाक्य, अर्थ की दृष्टि से विधानवाचक, निषेधवाचक, आज्ञावाचक, प्रश्नवाचक वाक्य"},
                {"number": "14", "name_en": "Punctuation", "name_hi": "विराम चिह्न", "desc": "पूर्ण विराम, अल्प विराम, अर्ध विराम, प्रश्नवाचक चिह्न, विस्मयसूचक चिह्न, उद्धरण चिह्न, योजक चिह्न"},
                {"number": "15", "name_en": "Vocabulary (Synonyms, Antonyms, etc.)", "name_hi": "शब्द भंडार (पर्यायवाची, विलोम, आदि)", "desc": "समानार्थी / पर्यायवाची शब्द (सूर्य, चंद्रमा, अग्नि, जल, आकाश) और विपरीतार्थक / विलोम शब्द"},
                {"number": "16", "name_en": "One Word Substitution", "name_hi": "अनेक शब्दों के लिए एक शब्द", "desc": "वाक्यांश के लिए एक शब्द (जैसे जो सब कुछ जानता हो = सर्वज्ञ, जो कभी न मरे = अमर, जिसका कोई शत्रु न जन्मा हो = अजातशत्रु)"},
                {"number": "17", "name_en": "Idioms and Proverbs", "name_hi": "मुहावरे और लोकोक्तियाँ", "desc": "हिंदी मुहावरे (अंगूठा दिखाना, आँख का तारा, ईद का चाँद होना, नौ दो ग्यारह होना) और लोकोक्तियाँ/कहावतें"},
                {"number": "18", "name_en": "Sentence Correction", "name_hi": "वाक्य शुद्धि", "desc": "अशुद्ध वाक्यों को शुद्ध करना, वर्तनी, लिंग, वचन, कारक संबंधी अशुद्धियों का संशोधन"},
                {"number": "19", "name_en": "Poetic Elements (Introduction)", "name_hi": "काव्य-तत्त्व (सामान्य परिचय)", "desc": "काव्य की परिभाषा, शब्द शक्ति (अभिधा, लक्षणा, व्यंजना), काव्य गुण (माधुर्य, ओज, प्रसाद)"},
                {"number": "20", "name_en": "Essay Writing", "name_hi": "निबंध लेखन", "desc": "समसामयिक, सामाजिक, राष्ट्रीय विषयों पर निबंध (होली, पर्यावरण प्रदूषण, दहेज प्रथा, अनुशासन, इंटरनेट, पुस्तकालय)"},
                {"number": "21", "name_en": "Letter and Application Writing", "name_hi": "पत्र और आवेदन लेखन", "desc": "प्रधानाध्यापक को शुल्क माफी / छुट्टी हेतु आवेदन पत्र, पिता या मित्र को पत्र, संवाद लेखन"},
                {"number": "22", "name_en": "Adverbs", "name_hi": "क्रिया-विशेषण", "desc": "रीतिवाचक, कालवाचक, स्थानवाचक, परिमाणवाचक क्रिया-विशेषण के उदाहरण और पहचान"},
                {"number": "23", "name_en": "Ras", "name_hi": "रस", "desc": "रस के चार अंग (स्थायी भाव, विभाव, अनुभाव, संचारी भाव), प्रमुख रस: श्रृंगार, हास्य, करुण, वीर, शांत, रौद्र रस"},
                {"number": "24", "name_en": "Chhand", "name_hi": "छंद", "desc": "मात्रिक और वर्णिक छंद, दोहा, चौपाई, सोरठा, रोला छंद के लक्षण और मात्रा गणना"},
                {"number": "25", "name_en": "Alankar", "name_hi": "अलंकार", "desc": "शब्दालंकार (अनुप्रास, यमक, श्लेष) और अर्थालंकार (उपमा, रूपक, उत्प्रेक्षा, अतिशयोक्ति, मानवीकरण) की पहचान"}
            ]
        }
    },
    "sanskrit": {
        "is_multi_section": True,
        "sections": {
            "Piyusham": [
                {"number": "1", "name_en": "Mangalam", "name_hi": "मङ्गलम्", "desc": "उपनिषदों (ईशावास्य, कठ, मुण्डक, श्वेताश्वतर) से संकलित पाँच पद्य; सत्य का मुख स्वर्णपात्र से ढँका है, सत्यमेव जयते, आत्मा अणु से भी सूक्ष्म और महान से भी महान है"},
                {"number": "2", "name_en": "Patliputra-vaibhavam", "name_hi": "पाटलिपुत्रवैभवम्", "desc": "बिहार की राजधानी पटना का ऐतिहासिक और सांस्कृतिक वैभव; मेगास्थनीज, फाह्यान, ह्वेनसांग के यात्रा वृत्तांत, चंद्रगुप्त मौर्य और अशोक, कौमुदी महोत्सव, गोलघर, जैविक उद्यान, सिख गुरु गोविंद सिंह जन्मस्थान तख्त हरमंदिर साहिब"},
                {"number": "3", "name_en": "Alasa-katha", "name_hi": "अलसकथा", "desc": "विद्यापति रचित पुरुषपरीक्षा कथा-ग्रंथ; मिथिला के मंत्री वीरेश्वर का दानशील स्वभाव, अलसियों की परीक्षा हेतु अलसशाला में आग लगाना, चार सच्चे आलसियों की वार्तालाप, आलसियों की रक्षा केवल दयावान करते हैं"},
                {"number": "4", "name_en": "Sanskrit-sahitye Lekhika:", "name_hi": "संस्कृतसाहित्ये लेखिकाः", "desc": "संस्कृत साहित्य में विदुषी स्त्रियों का योगदान; वैदिक काल की गार्गी, मैत्रेयी, अपाला, विजयाङ्का (श्याम वर्ण), दक्षिण भारत की शीलाभट्टारिका, रामभद्राम्बा, तिरुमलाम्बा, आधुनिक काल की पंडिता क्षमाराव, मिथिला कुमारी मिश्र"},
                {"number": "5", "name_en": "Bharat-mahima", "name_hi": "भारतमहिमा", "desc": "विष्णु पुराण और भागवत पुराण के श्लोक; भारतभूमि स्वर्ग से भी बढ़कर है, देवता भी भारत में जन्म लेने के लिए लालायित रहते हैं, यहाँ की नदियाँ, पर्वत, सागर और देशभक्ति की भावना"},
                {"number": "6", "name_en": "Bharatiya-samskarah", "name_hi": "भारतीयसंस्काराः", "desc": "भारतीय जीवन दर्शन में कुल 16 संस्कार; जन्मपूर्व 3 संस्कार (गर्भाधान, पुंसवन, सीमन्तोन्नयन), शैशव 6 संस्कार, शैक्षणिक 5 संस्कार (उपनयन, वेदारम्भ, केशान्त/गोदान, समावर्तन), विवाह संस्कार, अन्त्येष्टि/मरणोपरांत संस्कार"},
                {"number": "7", "name_en": "Niti-shlokaha", "name_hi": "नीतिश्लोकाः", "desc": "महाभारत उद्योग पर्व अंतर्गत महात्मा विदुर और धृतराष्ट्र का संवाद (विदुरनीति); पंडित के लक्षण, नरक के तीन द्वार (काम, क्रोध, लोभ), षड् दोषाः (निद्रा, तन्द्रा, भय, क्रोध, आलस्य, दीर्घसूत्रता), धर्म और अहिंसा"},
                {"number": "8", "name_en": "Karmaveer-katha", "name_hi": "कर्मवीर कथाः", "desc": "बिहार के भीखनटोला गाँव के दलित बालक रामप्रवेश राम की प्रेरणादायक कथा; शिक्षक की प्रेरणा से प्राथमिक विद्यालय से उच्च शिक्षा प्राप्त कर केंद्रीय लोक सेवा आयोग (UPSC) परीक्षा में सर्वोच्च स्थान प्राप्त करना"},
                {"number": "9", "name_en": "Swami-Dayanandah", "name_hi": "स्वामी दयानन्दः", "desc": "19वीं सदी के महान समाज सुधारक स्वामी दयानंद सरस्वती; गुजरात के टंकारा में जन्म, मूलशंकर नाम, शिवरात्रि की रात चूहे द्वारा शिवलिंग पर प्रसाद खाना, वैराग्य, गुरु विरजानंद, आर्य समाज की स्थापना 1875 मुंबई, सत्यार्थ प्रकाश ग्रंथ, डीएवी विद्यालयों की श्रृंखला"},
                {"number": "10", "name_en": "Mandakini-varnanam", "name_hi": "मन्दाकिनीवर्णनम्", "desc": "वाल्मीकि रामायण के अयोध्या काण्ड का सर्ग 95; वनवास काल में चित्रकूट के निकट मन्दाकिनी नदी की प्राकृतिक सुंदरता का श्रीराम द्वारा सीता को दर्शन कराना, हंस-सारस, मुनि, विशालाक्षी"},
                {"number": "11", "name_en": "Vyaghra-pathika-katha", "name_hi": "व्याघ्रपथिककथाः", "desc": "नारायण पंडित रचित हितोपदेश के मित्रलाभ खंड की कथा; वृद्ध और दंतहीन बाघ हाथ में सोने का कंगन लेकर पथिक को लालच देना, लोभ के कारण दलदल में फँसकर मारा जाना, 'लोभः पापस्य कारणम्'"},
                {"number": "12", "name_en": "Karnasya-danavirata", "name_hi": "कर्णस्य दानवीरता", "desc": "भास रचित नाटक कर्णभार; दानवीर कर्ण द्वारा ब्राह्मण रूपी इंद्र (शक्र) को अपना जन्मजात रक्षा कवच और कुंडल सहर्ष दान कर देना, गाय, घोड़े, हाथी, भूमि का दान प्रस्ताव"},
                {"number": "13", "name_en": "Vishwa-shantih", "name_hi": "विश्वशांतिः", "desc": "विश्व में अशांति, ईर्ष्या, असहिष्णुता और युद्ध के संकट; विनाशकारी अस्त्र-शस्त्र, अशांति का निवारण परोपकार, शांति, बंधुत्व, 'अयं निजः परो वेति गणना लघुचेतसाम्, उदारचरितानां तु वसुधैव कुटुम्बकम्'"},
                {"number": "14", "name_en": "Shastrakarah", "name_hi": "शास्त्रकाराः", "desc": "संस्कृत शास्त्रों और ऋषियों का परिचय; 6 वेदांग: शिक्षा (पाणिनी), कल्प (बौधायन/भारद्वाज), व्याकरण (पाणिनी), निरुक्त (यास्क), छंद (पिंगल), ज्योतिष (लगध); 6 दर्शन: सांख्य (कपिल), योग (पतंजलि), न्याय (गौतम), वैशेषिक (कणाद), मीमांसा (जैमिनी), वेदांत (बादरायण); आयुर्वेद (चरक, सुश्रुत), खगोल (आर्यभट्ट)"}
            ],
            "Vyakaran": [
                {"number": "1", "name_en": "Letters and Pronunciation", "name_hi": "वर्ण-विचार एवं उच्चारण", "desc": "संस्कृत वर्णमाला, माहेश्वर सूत्राणि, स्वर (अच्), व्यंजन (हल्), उच्चारण स्थानानि (अकुहविसर्जनीयानां कण्ठः, इचुयशानां तालु, ऋटुरषाणां मूर्धा, उपूपध्मानीयानाम् ओष्ठौ)"},
                {"number": "2", "name_en": "Sandhi (Joining of Sounds)", "name_hi": "संधि", "desc": "अच् संधि / स्वर संधि (दीर्घ, गुण, वृद्धि, यण, अयादि, पूर्वरूप), हल् संधि / व्यंजन संधि (श्चुत्व, ष्टुत्व, जश्त्व), विसर्ग संधि (सत्व, उत्व, रुत्व, लोप)"},
                {"number": "3", "name_en": "Shabda Rupa (Noun Forms)", "name_hi": "शब्द-रूपाणि", "desc": "अकारांत बालक/राम, आकारांत लता, इकारांत मुनि/हरि, ईकारांत नदी, उकारांत साधु/गुरु, पितृ, मातृ, असमद् (अहम्/माम्), युष्मद् (त्वम्/त्वाम्), तद् (सः/तौ/ते) शब्द रूप सातों विभक्तियों में"},
                {"number": "4", "name_en": "Dhatu Rupa (Verb Forms)", "name_hi": "धातु-रूपाणि", "desc": "पठ्, गम्/गच्छ्, भू/भव्, कृ, दृश्/पश्य् धातुओं के रूप 5 लकारों में: लट् लकार (वर्तमान), लोट् लकार (आज्ञार्थक), लङ् लकार (भूतकाल), विधिलिङ् लकार (चाहिए), लृट् लकार (भविष्यत्)"},
                {"number": "5", "name_en": "Samas (Compound Words)", "name_hi": "समास", "desc": "अव्ययीभाव (यथाशक्ति, उपगङ्गम्), तत्पुरुष (राजपुरुषः), कर्मधारय (नीलोत्पलम्, महापुरुषः), द्विगु (त्रिभुवनम्, पंचवटी), द्वंद्व (रामलक्ष्मणौ), बहुव्रीहि (पीताम्बरः, दशाननः)"},
                {"number": "6", "name_en": "Karak and Vibhakti", "name_hi": "कारक एवं विभक्ति", "desc": "कारक सूत्र: कर्तृकारक प्रथमा, कर्मणि द्वितीया (अभितः परितः समय निकषा प्रति योगेऽपि), साधकतमं करणम् तृतीया (येनाङ्गविकारः, सहयुक्तेऽप्रधाने), दाणार्थे चतुर्थी, अपादाने पंचमी (भीत्रार्थानां भयहेतुः), षष्ठी शेषे, यतश्च निर्धारणम् सप्तमी"},
                {"number": "7", "name_en": "Pratyaya (Suffixes)", "name_hi": "प्रत्यय", "desc": "कृत् प्रत्यय: क्त्वा (पठित्वा, गत्वा), ल्यप् (आगत्य, प्रणम्य), तुमुन् (पठितुम्, गन्तुम्), क्त, क्तवतु, शतृ, शानच्; तद्धित प्रत्यय: मतुप्, अण्, तल्, त्व; स्त्री प्रत्यय: टाप् (अजा, बाला), ङीप् (नदी, किशोरी)"},
                {"number": "8", "name_en": "Vachya Parivartan (Voice Change)", "name_hi": "वाच्य परिवर्तनम्", "desc": "कर्तृवाच्य (सः पुस्तकं पठति), कर्मवाच्य (तेन पुस्तकं पठ्यते), भाववाच्य (तेन गम्यते) का परस्पर परिवर्तन"},
                {"number": "9", "name_en": "Upasarga and Avyaya", "name_hi": "उपसर्ग एवं अव्यय", "desc": "22 प्रादयः उपसर्गाः (प्र, परा, अप, सम्, अनु, अव, निर्, दुर्, वि, आङ्, नि, अधि, अपि, अति, सु, उत्, अभि, प्रति, परि, उप); अव्ययानि (अत्र, तत्र, कुत्र, यदा, कदा, सर्वदा, च, अपि, विना, सह)"},
                {"number": "10", "name_en": "Sentence Correction and Transformation", "name_hi": "वाक्य-शुद्धि एवं परिवर्तन", "desc": "संस्कृत वाक्यों में कर्ता-क्रिया, लिंग, वचन, पुरुष और विभक्ति संबंधी त्रुटियों का निवारण"},
                {"number": "11", "name_en": "Translation (Sanskrit to Hindi/English)", "name_hi": "अनुवाद", "desc": "हिंदी या अंग्रेजी से संस्कृत में अनुवाद (जैसे: गंगा हिमालय से निकलती है = गङ्गा हिमालयात् प्रभवति; वह आँख से काना है = सः अक्षा काणः अस्ति)"},
                {"number": "12", "name_en": "Letter Writing", "name_hi": "पत्र-लेखनम्", "desc": "प्राचार्य को अवकाश हेतु आवेदन पत्र, पिता को परीक्षा परिणाम संबंधी पत्र संस्कृत में लिखना"},
                {"number": "13", "name_en": "Unseen Passage", "name_hi": "अपठित-अवबोधनम्", "desc": "अपठित संस्कृत गद्यांश को पढ़कर एकपदेन उत्तरत, पूर्णवाक्येन उत्तरत और समुचित शीर्षक लिखना"},
                {"number": "14", "name_en": "Paragraph and Picture Description", "name_hi": "अनुच्छेद एवं चित्र-वर्णनम्", "desc": "दिए गए विषय (मम विद्यालयः, अस्माकं देशः, होलीकोत्सवः, गङ्गा नदी) पर 7 वाक्यों का संस्कृत अनुच्छेद अथवा चित्र आधारित वाक्य रचना"}
            ]
        }
    }
}

def get_all_chapter_options(subject: str):
    """Returns a list of dicts: [{'key': '...', 'label': '...', 'section': '...', 'number': '...', 'desc': '...'}]"""
    subj_data = CHAPTERS.get(subject, {})
    options = []
    is_multi = subj_data.get("is_multi_section", False)
    for section_name, ch_list in subj_data.get("sections", {}).items():
        for ch in ch_list:
            label = f"{section_name} - {ch['number']}. {ch['name_en']} ({ch['name_hi']})" if is_multi else f"{ch['number']}. {ch['name_en']} ({ch['name_hi']})"
            key = f"{section_name}::{ch['number']}" if is_multi else ch['number']
            options.append({
                "key": key,
                "label": label,
                "section": section_name if is_multi else "",
                "number": ch["number"],
                "name_en": ch["name_en"],
                "name_hi": ch["name_hi"],
                "desc": ch.get("desc", f"Topics related to {ch['name_en']}")
            })
    return options
