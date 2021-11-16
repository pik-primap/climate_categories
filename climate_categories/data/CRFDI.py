spec = {
    "name": "CRFDI",
    "title": "CRF GHG emission categories (DI query interface)",
    "comment": "Common Reporting Format categories of GHG emissions and removals and some other quantities as obtained from the di.unfccc.int flexible query interface",
    "references": "https://unfccc.int/process-and-meetings/transparency-and-reporting/greenhouse-gas-data/data-interface-help#eq-7",
    "institution": "UNFCCC",
    "hierarchical": True,
    "last_update": "2021-11-05",
    "total_sum": True,
    "canonical_top_level_category": "8677",
    "categories": {
        "8270": {
            "title": "CO₂ Emissions from Biomass",
            "info": {"numerical_ids": ["8270"]},
        },
        "8564": {
            "title": "International Bunkers",
            "info": {"numerical_ids": ["8564"]},
            "children": [["10357", "8828"]],
        },
        "8677": {
            "title": "Total GHG emissions with LULUCF",
            "info": {"numerical_ids": ["8677"]},
            "children": [["1", "2", "3", "4", "5", "6"]],
        },
        "8828": {
            "title": "International Navigation",
            "info": {"numerical_ids": ["8828"]},
        },
        "8869": {
            "title": "Memo Items",
            "info": {"numerical_ids": ["8869"]},
            "children": [["8270", "8564", "8987"]],
        },
        "8987": {
            "title": "Multilateral Operations",
            "info": {"numerical_ids": ["8987"]},
        },
        "10357": {
            "title": "International Aviation",
            "info": {"numerical_ids": ["10357"]},
        },
        "10464": {
            "title": "Total GHG emissions without LULUCF",
            "info": {"numerical_ids": ["10464"]},
            "children": [["1", "2", "3", "5", "6"]],
        },
        "10479": {
            "title": "Total GHG emissions without LULUCF including indirect CO₂",
            "info": {"numerical_ids": ["10479"]},
        },
        "10480": {
            "title": "Total GHG emissions with LULUCF including indirect CO₂",
            "info": {"numerical_ids": ["10480"]},
        },
        "10502": {"title": "Total land area", "info": {"numerical_ids": ["10502"]}},
        "10503": {"title": "GDP", "info": {"numerical_ids": ["10503"]}},
        "10504": {"title": "Total population", "info": {"numerical_ids": ["10504"]}},
        "11022": {
            "title": "Memo Items",
            "info": {"numerical_ids": ["11022"]},
            "children": [["11023", "11024", "11025"]],
        },
        "11023": {
            "title": "Long-term Storage of C in Waste Disposal Sites",
            "info": {"numerical_ids": ["11023"]},
        },
        "11024": {
            "title": "Annual Change in Total Long-term C Storage",
            "info": {"numerical_ids": ["11024"]},
        },
        "11025": {
            "title": "Annual Change in Total Long-term C Storage in HWP Waste",
            "info": {"numerical_ids": ["11025"]},
        },
        "11026": {
            "title": "Information Item",
            "info": {"numerical_ids": ["11026"]},
            "children": [["11027", "11028"]],
        },
        "11027": {
            "title": "Waste Incineration with Energy Recovery included as Biomass",
            "info": {"numerical_ids": ["11027"]},
        },
        "11028": {
            "title": "Waste Incineration with Energy Recovery included as Fossil Fuels",
            "info": {"numerical_ids": ["11028"]},
        },
        "11029": {
            "title": "Information Item",
            "info": {"numerical_ids": ["11029"]},
            "children": [["11030", "11031", "11032", "11033", "11034"]],
        },
        "11030": {
            "title": "Total Amount Captured for Storage",
            "info": {"numerical_ids": ["11030"]},
        },
        "11031": {
            "title": "Total Amount of Imports for Storage",
            "info": {"numerical_ids": ["11031"]},
        },
        "11032": {
            "title": "Total Amount of Exports for Storage",
            "info": {"numerical_ids": ["11032"]},
        },
        "11033": {
            "title": "Total Amount of CO₂ Injected at Storage Sites",
            "info": {"numerical_ids": ["11033"]},
        },
        "11034": {
            "title": "Total Leakage from Transport, Injection and Storage",
            "info": {"numerical_ids": ["11034"]},
        },
        "11035": {
            "title": "Information Item",
            "info": {"numerical_ids": ["11035"]},
            "children": [["11036"]],
        },
        "11036": {"title": "HWP in SWDS", "info": {"numerical_ids": ["11036"]}},
        "1": {
            "title": "Energy",
            "alternative_codes": ["1.", "10481", "8819"],
            "info": {"numerical_ids": ["10481", "8819"]},
            "children": [["1.AA", "1.AB", "1.AD", "1.B", "1.C", "8869"]],
        },
        "1.A.1": {
            "title": "Energy Industries",
            "alternative_codes": ["10402", "1A1", "1 A 1"],
            "info": {"numerical_ids": ["10402"]},
            "children": [["1.A.1.a", "1.A.1.b", "1.A.1.c"]],
        },
        "1.A.1.a": {
            "title": "Public Electricity and Heat Production",
            "alternative_codes": ["9422", "1A1a", "1 A 1 a"],
            "info": {"numerical_ids": ["9422"]},
            "children": [["1.A.1.a.i", "1.A.1.a.ii", "1.A.1.a.iii", "1.A.1.a.iv"]],
        },
        "1.A.1.a.i": {
            "title": "Electricity Generation",
            "alternative_codes": ["8616", "1A1ai", "1 A 1 a i"],
            "info": {"numerical_ids": ["8616"]},
        },
        "1.A.1.a.ii": {
            "title": "Combined Heat and Power Generation",
            "alternative_codes": ["9614", "1A1aii", "1 A 1 a ii"],
            "info": {"numerical_ids": ["9614"]},
        },
        "1.A.1.a.iii": {
            "title": "Heat Plants",
            "alternative_codes": ["9971", "1A1aiii", "1 A 1 a iii"],
            "info": {"numerical_ids": ["9971"]},
        },
        "1.A.1.a.iv": {
            "title": "Other",
            "alternative_codes": ["8368", "1A1aiv", "1 A 1 a iv"],
            "info": {"numerical_ids": ["8368"]},
        },
        "1.A.1.b": {
            "title": "Petroleum Refining",
            "alternative_codes": ["9771", "1A1b", "1 A 1 b"],
            "info": {"numerical_ids": ["9771"]},
        },
        "1.A.1.c": {
            "title": "Manufacture of Solid Fuels and Other Energy Industries",
            "alternative_codes": ["9004", "1A1c", "1 A 1 c"],
            "info": {"numerical_ids": ["9004"]},
            "children": [["1.A.1.c.i", "1.A.1.c.ii", "1.A.1.c.iii", "1.A.1.c.iv"]],
        },
        "1.A.1.c.i": {
            "title": "Manufacture of Solid Fuels",
            "alternative_codes": ["10306", "1A1ci", "1 A 1 c i"],
            "info": {"numerical_ids": ["10306"]},
        },
        "1.A.1.c.ii": {
            "title": "Oil and Gas Extraction",
            "alternative_codes": ["10425", "1A1cii", "1 A 1 c ii"],
            "info": {"numerical_ids": ["10425"]},
        },
        "1.A.1.c.iii": {
            "title": "Other Energy Industries",
            "alternative_codes": ["8335", "1A1ciii", "1 A 1 c iii"],
            "info": {"numerical_ids": ["8335"]},
        },
        "1.A.1.c.iv": {
            "title": "Other",
            "alternative_codes": ["8656", "1A1civ", "1 A 1 c iv"],
            "info": {"numerical_ids": ["8656"]},
        },
        "1.A.2": {
            "title": "Manufacturing Industries and Construction",
            "alternative_codes": ["8556", "1A2", "1 A 2"],
            "info": {"numerical_ids": ["8556"]},
            "children": [
                [
                    "1.A.2.a",
                    "1.A.2.b",
                    "1.A.2.c",
                    "1.A.2.d",
                    "1.A.2.e",
                    "1.A.2.f",
                    "1.A.2.g",
                ]
            ],
        },
        "1.A.2.a": {
            "title": "Iron and Steel",
            "alternative_codes": ["10329", "1A2a", "1 A 2 a"],
            "info": {"numerical_ids": ["10329"]},
        },
        "1.A.2.b": {
            "title": "Non-Ferrous Metals",
            "alternative_codes": ["9859", "1A2b", "1 A 2 b"],
            "info": {"numerical_ids": ["9859"]},
        },
        "1.A.2.c": {
            "title": "Chemicals",
            "alternative_codes": ["9369", "1A2c", "1 A 2 c"],
            "info": {"numerical_ids": ["9369"]},
        },
        "1.A.2.d": {
            "title": "Pulp, Paper and Print",
            "alternative_codes": ["10119", "1A2d", "1 A 2 d"],
            "info": {"numerical_ids": ["10119"]},
        },
        "1.A.2.e": {
            "title": "Food Processing, Beverages and Tobacco",
            "alternative_codes": ["8321", "1A2e", "1 A 2 e"],
            "info": {"numerical_ids": ["8321"]},
        },
        "1.A.2.f": {
            "title": "Non-metallic Minerals",
            "alternative_codes": ["8876", "1A2f", "1 A 2 f"],
            "info": {"numerical_ids": ["8876"]},
        },
        "1.A.2.g": {
            "title": "Other",
            "alternative_codes": ["9832", "1A2g", "1 A 2 g"],
            "info": {"numerical_ids": ["9832"]},
            "children": [
                [
                    "1.A.2.g.i",
                    "1.A.2.g.ii",
                    "1.A.2.g.iii",
                    "1.A.2.g.iv",
                    "1.A.2.g.v",
                    "1.A.2.g.vi",
                    "1.A.2.g.vii",
                    "1.A.2.g.viii",
                ]
            ],
        },
        "1.A.2.g.i": {
            "title": "Manufacturing of Machinery",
            "alternative_codes": ["10308", "1A2gi", "1 A 2 g i"],
            "info": {"numerical_ids": ["10308"]},
        },
        "1.A.2.g.ii": {
            "title": "Manufacturing of Transport Equipment",
            "alternative_codes": ["10150", "1A2gii", "1 A 2 g ii"],
            "info": {"numerical_ids": ["10150"]},
        },
        "1.A.2.g.iii": {
            "title": "Mining (Excluding Fuels) and Quarrying",
            "alternative_codes": ["8527", "1A2giii", "1 A 2 g iii"],
            "info": {"numerical_ids": ["8527"]},
        },
        "1.A.2.g.iv": {
            "title": "Wood and Wood Products",
            "alternative_codes": ["8424", "1A2giv", "1 A 2 g iv"],
            "info": {"numerical_ids": ["8424"]},
        },
        "1.A.2.g.v": {
            "title": "Construction",
            "alternative_codes": ["10287", "1A2gv", "1 A 2 g v"],
            "info": {"numerical_ids": ["10287"]},
        },
        "1.A.2.g.vi": {
            "title": "Textile and Leather",
            "alternative_codes": ["8721", "1A2gvi", "1 A 2 g vi"],
            "info": {"numerical_ids": ["8721"]},
        },
        "1.A.2.g.vii": {
            "title": "Off-road Vehicles and Other Machinery",
            "alternative_codes": ["8587", "1A2gvii", "1 A 2 g vii"],
            "info": {"numerical_ids": ["8587"]},
        },
        "1.A.2.g.viii": {
            "title": "Other",
            "alternative_codes": ["8794", "1A2gviii", "1 A 2 g viii"],
            "info": {"numerical_ids": ["8794"]},
        },
        "1.A.3": {
            "title": "Transport",
            "alternative_codes": ["8322", "1A3", "1 A 3"],
            "info": {"numerical_ids": ["8322"]},
            "children": [["1.A.3.a", "1.A.3.b", "1.A.3.c", "1.A.3.d", "1.A.3.e"]],
        },
        "1.A.3.a": {
            "title": "Domestic Aviation",
            "alternative_codes": ["10419", "1A3a", "1 A 3 a"],
            "info": {"numerical_ids": ["10419"]},
        },
        "1.A.3.b": {
            "title": "Road Transportation",
            "alternative_codes": ["9607", "1A3b", "1 A 3 b"],
            "info": {"numerical_ids": ["9607"]},
            "children": [
                ["1.A.3.b.i", "1.A.3.b.ii", "1.A.3.b.iii", "1.A.3.b.iv", "1.A.3.b.v"]
            ],
        },
        "1.A.3.b.i": {
            "title": "Cars",
            "alternative_codes": ["9279", "1A3bi", "1 A 3 b i"],
            "info": {"numerical_ids": ["9279"]},
        },
        "1.A.3.b.ii": {
            "title": "Light Duty Trucks",
            "alternative_codes": ["9702", "1A3bii", "1 A 3 b ii"],
            "info": {"numerical_ids": ["9702"]},
        },
        "1.A.3.b.iii": {
            "title": "Heavy Duty Trucks and Buses",
            "alternative_codes": ["8358", "1A3biii", "1 A 3 b iii"],
            "info": {"numerical_ids": ["8358"]},
        },
        "1.A.3.b.iv": {
            "title": "Motorcycles",
            "alternative_codes": ["9622", "1A3biv", "1 A 3 b iv"],
            "info": {"numerical_ids": ["9622"]},
        },
        "1.A.3.b.v": {
            "title": "Other",
            "alternative_codes": ["9083", "1A3bv", "1 A 3 b v"],
            "info": {"numerical_ids": ["9083"]},
        },
        "1.A.3.c": {
            "title": "Railways",
            "alternative_codes": ["8924", "1A3c", "1 A 3 c"],
            "info": {"numerical_ids": ["8924"]},
        },
        "1.A.3.d": {
            "title": "Domestic Navigation",
            "alternative_codes": ["9670", "1A3d", "1 A 3 d"],
            "info": {"numerical_ids": ["9670"]},
        },
        "1.A.3.e": {
            "title": "Other Transportation",
            "alternative_codes": ["8456", "1A3e", "1 A 3 e"],
            "info": {"numerical_ids": ["8456"]},
            "children": [["1.A.3.e.i", "1.A.3.e.ii"]],
        },
        "1.A.3.e.i": {
            "title": "Pipeline Transport",
            "alternative_codes": ["9504", "1A3ei", "1 A 3 e i"],
            "info": {"numerical_ids": ["9504"]},
        },
        "1.A.3.e.ii": {
            "title": "Other",
            "alternative_codes": ["9935", "1A3eii", "1 A 3 e ii"],
            "info": {"numerical_ids": ["9935"]},
        },
        "1.A.4": {
            "title": "Other Sectors",
            "alternative_codes": ["9815", "1A4", "1 A 4"],
            "info": {"numerical_ids": ["9815"]},
            "children": [["1.A.4.a", "1.A.4.b", "1.A.4.c"]],
        },
        "1.A.4.a": {
            "title": "Commercial/Institutional",
            "alternative_codes": ["8597", "1A4a", "1 A 4 a"],
            "info": {"numerical_ids": ["8597"]},
            "children": [["1.A.4.a.i", "1.A.4.a.ii", "1.A.4.a.iii"]],
        },
        "1.A.4.a.i": {
            "title": "Stationary Combustion",
            "alternative_codes": ["8216", "1A4ai", "1 A 4 a i"],
            "info": {"numerical_ids": ["8216"]},
        },
        "1.A.4.a.ii": {
            "title": "Off-road Vehicles and Other Machinery",
            "alternative_codes": ["8251", "1A4aii", "1 A 4 a ii"],
            "info": {"numerical_ids": ["8251"]},
        },
        "1.A.4.a.iii": {
            "title": "Other",
            "alternative_codes": ["8223", "1A4aiii", "1 A 4 a iii"],
            "info": {"numerical_ids": ["8223"]},
        },
        "1.A.4.b": {
            "title": "Residential",
            "alternative_codes": ["9823", "1A4b", "1 A 4 b"],
            "info": {"numerical_ids": ["9823"]},
            "children": [["1.A.4.b.i", "1.A.4.b.ii", "1.A.4.b.iii"]],
        },
        "1.A.4.b.i": {
            "title": "Stationary Combustion",
            "alternative_codes": ["8609", "1A4bi", "1 A 4 b i"],
            "info": {"numerical_ids": ["8609"]},
        },
        "1.A.4.b.ii": {
            "title": "Off-road Vehicles and Other Machinery",
            "alternative_codes": ["10435", "1A4bii", "1 A 4 b ii"],
            "info": {"numerical_ids": ["10435"]},
        },
        "1.A.4.b.iii": {
            "title": "Other",
            "alternative_codes": ["8632", "1A4biii", "1 A 4 b iii"],
            "info": {"numerical_ids": ["8632"]},
        },
        "1.A.4.c": {
            "title": "Agriculture/Forestry/Fishing",
            "alternative_codes": ["8554", "1A4c", "1 A 4 c"],
            "info": {"numerical_ids": ["8554"]},
            "children": [["1.A.4.c.i", "1.A.4.c.ii", "1.A.4.c.iii"]],
        },
        "1.A.4.c.i": {
            "title": "Stationary",
            "alternative_codes": ["8364", "1A4ci", "1 A 4 c i"],
            "info": {"numerical_ids": ["8364"]},
        },
        "1.A.4.c.ii": {
            "title": "Off-road Vehicles and Other Machinery",
            "alternative_codes": ["10080", "1A4cii", "1 A 4 c ii"],
            "info": {"numerical_ids": ["10080"]},
        },
        "1.A.4.c.iii": {
            "title": "Fishing",
            "alternative_codes": ["9812", "1A4ciii", "1 A 4 c iii"],
            "info": {"numerical_ids": ["9812"]},
        },
        "1.A.5": {
            "title": "Other (Not specified elsewhere)",
            "alternative_codes": ["10273", "1A5", "1 A 5"],
            "info": {"numerical_ids": ["10273"]},
            "children": [["1.A.5.a", "1.A.5.b"]],
        },
        "1.A.5.a": {
            "title": "Stationary",
            "alternative_codes": ["9861", "1A5a", "1 A 5 a"],
            "info": {"numerical_ids": ["9861"]},
        },
        "1.A.5.b": {
            "title": "Mobile",
            "alternative_codes": ["9101", "1A5b", "1 A 5 b"],
            "info": {"numerical_ids": ["9101"]},
        },
        "1.AA": {
            "title": "Fuel Combustion - Sectoral approach",
            "alternative_codes": ["9089", "1.A", "1A", "1 A", "1AA", "1 AA"],
            "info": {"numerical_ids": ["9089"]},
            "children": [["1.A.1", "1.A.2", "1.A.3", "1.A.4", "1.A.5", "11026"]],
        },
        "1.AB": {
            "title": "Fuel Combustion - Reference Approach",
            "alternative_codes": ["8533", "1AB", "1 AB"],
            "info": {"numerical_ids": ["8533"]},
        },
        "1.AD": {
            "title": "Feedstocks, Reductants and Other Non-energy Use of Fuels",
            "alternative_codes": ["8731", "1AD", "1 AD"],
            "info": {"numerical_ids": ["8731"]},
        },
        "1.B": {
            "title": "Fugitive Emissions from Fuels",
            "alternative_codes": ["9374", "1B", "1 B"],
            "info": {"numerical_ids": ["9374"]},
            "children": [["1.B.1", "1.B.2"]],
        },
        "1.B.1": {
            "title": "Solid Fuels",
            "alternative_codes": ["9455", "1B1", "1 B 1"],
            "info": {"numerical_ids": ["9455"]},
            "children": [["1.B.1.a", "1.B.1.b", "1.B.1.c"]],
        },
        "1.B.1.a": {
            "title": "Coal Mining and Handling",
            "alternative_codes": ["9835", "1B1a", "1 B 1 a"],
            "info": {"numerical_ids": ["9835"]},
            "children": [["1.B.1.a.i", "1.B.1.a.ii"]],
        },
        "1.B.1.a.i": {
            "title": "Underground Mines",
            "alternative_codes": ["9116", "1B1ai", "1 B 1 a i"],
            "info": {"numerical_ids": ["9116"]},
            "children": [["1.B.1.a.i.1", "1.B.1.a.i.2", "1.B.1.a.i.3"]],
        },
        "1.B.1.a.i.1": {
            "title": "Mining Activities",
            "alternative_codes": ["9933", "1B1ai1", "1 B 1 a i 1"],
            "info": {"numerical_ids": ["9933"]},
        },
        "1.B.1.a.i.2": {
            "title": "Post-Mining Activities",
            "alternative_codes": ["9427", "1B1ai2", "1 B 1 a i 2"],
            "info": {"numerical_ids": ["9427"]},
        },
        "1.B.1.a.i.3": {
            "title": "Abandoned Underground Mines",
            "alternative_codes": ["8211", "1B1ai3", "1 B 1 a i 3"],
            "info": {"numerical_ids": ["8211"]},
        },
        "1.B.1.a.ii": {
            "title": "Surface Mines",
            "alternative_codes": ["8573", "1B1aii", "1 B 1 a ii"],
            "info": {"numerical_ids": ["8573"]},
            "children": [["1.B.1.a.ii.1", "1.B.1.a.ii.2"]],
        },
        "1.B.1.a.ii.1": {
            "title": "Mining Activities",
            "alternative_codes": ["10282", "1B1aii1", "1 B 1 a ii 1"],
            "info": {"numerical_ids": ["10282"]},
        },
        "1.B.1.a.ii.2": {
            "title": "Post-Mining Activities",
            "alternative_codes": ["9601", "1B1aii2", "1 B 1 a ii 2"],
            "info": {"numerical_ids": ["9601"]},
        },
        "1.B.1.b": {
            "title": "Solid Fuel Transformation",
            "alternative_codes": ["8300", "1B1b", "1 B 1 b"],
            "info": {"numerical_ids": ["8300"]},
        },
        "1.B.1.c": {
            "title": "Other",
            "alternative_codes": ["8964", "1B1c", "1 B 1 c"],
            "info": {"numerical_ids": ["8964"]},
        },
        "1.B.2": {
            "title": "Oil and Natural Gas and Other Emissions from Energy Production",
            "alternative_codes": ["8806", "1B2", "1 B 2"],
            "info": {"numerical_ids": ["8806"]},
            "children": [["1.B.2.a", "1.B.2.b", "1.B.2.c", "1.B.2.d"]],
        },
        "1.B.2.a": {
            "title": "Oil",
            "alternative_codes": ["9822", "1B2a", "1 B 2 a"],
            "info": {"numerical_ids": ["9822"]},
            "children": [
                [
                    "1.B.2.a.i",
                    "1.B.2.a.ii",
                    "1.B.2.a.iii",
                    "1.B.2.a.iv",
                    "1.B.2.a.v",
                    "1.B.2.a.vi",
                ]
            ],
        },
        "1.B.2.a.i": {
            "title": "Exploration",
            "alternative_codes": ["8165", "1B2ai", "1 B 2 a i"],
            "info": {"numerical_ids": ["8165"]},
        },
        "1.B.2.a.ii": {
            "title": "Production",
            "alternative_codes": ["10078", "1B2aii", "1 B 2 a ii"],
            "info": {"numerical_ids": ["10078"]},
        },
        "1.B.2.a.iii": {
            "title": "Transport",
            "alternative_codes": ["9550", "1B2aiii", "1 B 2 a iii"],
            "info": {"numerical_ids": ["9550"]},
        },
        "1.B.2.a.iv": {
            "title": "Refining / Storage",
            "alternative_codes": ["9891", "1B2aiv", "1 B 2 a iv"],
            "info": {"numerical_ids": ["9891"]},
        },
        "1.B.2.a.v": {
            "title": "Distribution of Oil Products",
            "alternative_codes": ["8371", "1B2av", "1 B 2 a v"],
            "info": {"numerical_ids": ["8371"]},
        },
        "1.B.2.a.vi": {
            "title": "Other",
            "alternative_codes": ["8228", "1B2avi", "1 B 2 a vi"],
            "info": {"numerical_ids": ["8228"]},
        },
        "1.B.2.b": {
            "title": "Natural Gas",
            "alternative_codes": ["8493", "1B2b", "1 B 2 b"],
            "info": {"numerical_ids": ["8493"]},
            "children": [
                [
                    "1.B.2.b.i",
                    "1.B.2.b.ii",
                    "1.B.2.b.iii",
                    "1.B.2.b.iv",
                    "1.B.2.b.v",
                    "1.B.2.b.vi",
                ]
            ],
        },
        "1.B.2.b.i": {
            "title": "Exploration",
            "alternative_codes": ["9314", "1B2bi", "1 B 2 b i"],
            "info": {"numerical_ids": ["9314"]},
        },
        "1.B.2.b.ii": {
            "title": "Production",
            "alternative_codes": ["8474", "1B2bii", "1 B 2 b ii"],
            "info": {"numerical_ids": ["8474"]},
        },
        "1.B.2.b.iii": {
            "title": "Processing",
            "alternative_codes": ["9999", "1B2biii", "1 B 2 b iii"],
            "info": {"numerical_ids": ["9999"]},
        },
        "1.B.2.b.iv": {
            "title": "Transmission and Storage",
            "alternative_codes": ["9902", "1B2biv", "1 B 2 b iv"],
            "info": {"numerical_ids": ["9902"]},
        },
        "1.B.2.b.v": {
            "title": "Distribution",
            "alternative_codes": ["9728", "1B2bv", "1 B 2 b v"],
            "info": {"numerical_ids": ["9728"]},
        },
        "1.B.2.b.vi": {
            "title": "Other",
            "alternative_codes": ["9974", "1B2bvi", "1 B 2 b vi"],
            "info": {"numerical_ids": ["9974"]},
        },
        "1.B.2.c": {
            "title": "Venting and Flaring",
            "alternative_codes": ["8333", "1B2c", "1 B 2 c"],
            "info": {"numerical_ids": ["8333"]},
            "children": [["1.B.2.c.i", "1.B.2.c.ii"]],
        },
        "1.B.2.c.i": {
            "title": "Venting",
            "alternative_codes": ["10303", "1B2ci", "1 B 2 c i"],
            "info": {"numerical_ids": ["10303"]},
            "children": [["1.B.2.c.i.1", "1.B.2.c.i.2", "1.B.2.c.i.3"]],
        },
        "1.B.2.c.i.1": {
            "title": "Oil",
            "alternative_codes": ["9827", "1B2ci1", "1 B 2 c i 1"],
            "info": {"numerical_ids": ["9827"]},
        },
        "1.B.2.c.i.2": {
            "title": "Gas",
            "alternative_codes": ["10239", "1B2ci2", "1 B 2 c i 2"],
            "info": {"numerical_ids": ["10239"]},
        },
        "1.B.2.c.i.3": {
            "title": "Combined",
            "alternative_codes": ["8576", "1B2ci3", "1 B 2 c i 3"],
            "info": {"numerical_ids": ["8576"]},
        },
        "1.B.2.c.ii": {
            "title": "Flaring",
            "alternative_codes": ["10392", "1B2cii", "1 B 2 c ii"],
            "info": {"numerical_ids": ["10392"]},
            "children": [["1.B.2.c.ii.1", "1.B.2.c.ii.2", "1.B.2.c.ii.3"]],
        },
        "1.B.2.c.ii.1": {
            "title": "Oil",
            "alternative_codes": ["9210", "1B2cii1", "1 B 2 c ii 1"],
            "info": {"numerical_ids": ["9210"]},
        },
        "1.B.2.c.ii.2": {
            "title": "Gas",
            "alternative_codes": ["8904", "1B2cii2", "1 B 2 c ii 2"],
            "info": {"numerical_ids": ["8904"]},
        },
        "1.B.2.c.ii.3": {
            "title": "Combined",
            "alternative_codes": ["9824", "1B2cii3", "1 B 2 c ii 3"],
            "info": {"numerical_ids": ["9824"]},
        },
        "1.B.2.d": {
            "title": "Other",
            "alternative_codes": ["9077", "1B2d", "1 B 2 d"],
            "info": {"numerical_ids": ["9077"]},
        },
        "1.C": {
            "title": "CO₂ Transport and Storage",
            "alternative_codes": ["9070", "1C", "1 C"],
            "info": {"numerical_ids": ["9070"]},
            "children": [["1.C.1", "1.C.2", "1.C.3", "11029"]],
        },
        "1.C.1": {
            "title": "Transport of CO₂",
            "alternative_codes": ["9365", "1C1", "1 C 1"],
            "info": {"numerical_ids": ["9365"]},
            "children": [["1.C.1.a", "1.C.1.b", "1.C.1.c"]],
        },
        "1.C.1.a": {
            "title": "Pipelines",
            "alternative_codes": ["9769", "1C1a", "1 C 1 a"],
            "info": {"numerical_ids": ["9769"]},
        },
        "1.C.1.b": {
            "title": "Ships",
            "alternative_codes": ["10197", "1C1b", "1 C 1 b"],
            "info": {"numerical_ids": ["10197"]},
        },
        "1.C.1.c": {
            "title": "Other",
            "alternative_codes": ["9366", "1C1c", "1 C 1 c"],
            "info": {"numerical_ids": ["9366"]},
        },
        "1.C.2": {
            "title": "Injection and Storage",
            "alternative_codes": ["9474", "1C2", "1 C 2"],
            "info": {"numerical_ids": ["9474"]},
            "children": [["1.C.2.a", "1.C.2.b"]],
        },
        "1.C.2.a": {
            "title": "Injection",
            "alternative_codes": ["8741", "1C2a", "1 C 2 a"],
            "info": {"numerical_ids": ["8741"]},
        },
        "1.C.2.b": {
            "title": "Storage",
            "alternative_codes": ["10333", "1C2b", "1 C 2 b"],
            "info": {"numerical_ids": ["10333"]},
        },
        "1.C.3": {
            "title": "Other",
            "alternative_codes": ["9330", "1C3", "1 C 3"],
            "info": {"numerical_ids": ["9330"]},
        },
        "2": {
            "title": "Industrial Processes and Product Use",
            "alternative_codes": ["2.", "10393", "10482"],
            "info": {"numerical_ids": ["10393", "10482"]},
            "children": [["2.A", "2.B", "2.C", "2.D", "2.E", "2.F", "2.G", "2.H"]],
        },
        "2.A": {
            "title": "Mineral Industry",
            "alternative_codes": ["8452", "2A", "2 A"],
            "info": {"numerical_ids": ["8452"]},
            "children": [["2.A.1", "2.A.2", "2.A.3", "2.A.4"]],
        },
        "2.A.1": {
            "title": "Cement Production",
            "alternative_codes": ["8787", "2A1", "2 A 1"],
            "info": {"numerical_ids": ["8787"]},
        },
        "2.A.2": {
            "title": "Lime Production",
            "alternative_codes": ["8702", "2A2", "2 A 2"],
            "info": {"numerical_ids": ["8702"]},
        },
        "2.A.3": {
            "title": "Glass production",
            "alternative_codes": ["8579", "2A3", "2 A 3"],
            "info": {"numerical_ids": ["8579"]},
        },
        "2.A.4": {
            "title": "Other Process Uses of Carbonates",
            "alternative_codes": ["9731", "2A4", "2 A 4"],
            "info": {"numerical_ids": ["9731"]},
            "children": [["2.A.4.a", "2.A.4.b", "2.A.4.c", "2.A.4.d"]],
        },
        "2.A.4.a": {
            "title": "Ceramics",
            "alternative_codes": ["8539", "2A4a", "2 A 4 a"],
            "info": {"numerical_ids": ["8539"]},
        },
        "2.A.4.b": {
            "title": "Other Uses of Soda Ash",
            "alternative_codes": ["9452", "2A4b", "2 A 4 b"],
            "info": {"numerical_ids": ["9452"]},
        },
        "2.A.4.c": {
            "title": "Non-metallurgical Magnesium Production",
            "alternative_codes": ["10101", "2A4c", "2 A 4 c"],
            "info": {"numerical_ids": ["10101"]},
        },
        "2.A.4.d": {
            "title": "Other",
            "alternative_codes": ["9342", "2A4d", "2 A 4 d"],
            "info": {"numerical_ids": ["9342"]},
        },
        "2.B": {
            "title": "Chemical Industry",
            "alternative_codes": ["9304", "2B", "2 B"],
            "info": {"numerical_ids": ["9304"]},
            "children": [
                [
                    "2.B.1",
                    "2.B.10",
                    "2.B.2",
                    "2.B.3",
                    "2.B.4",
                    "2.B.5",
                    "2.B.6",
                    "2.B.7",
                    "2.B.8",
                    "2.B.9",
                ]
            ],
        },
        "2.B.1": {
            "title": "Ammonia Production",
            "alternative_codes": ["9658", "2B1", "2 B 1"],
            "info": {"numerical_ids": ["9658"]},
        },
        "2.B.2": {
            "title": "Nitric Acid Production",
            "alternative_codes": ["9410", "2B2", "2 B 2"],
            "info": {"numerical_ids": ["9410"]},
        },
        "2.B.3": {
            "title": "Adipic Acid Production",
            "alternative_codes": ["8468", "2B3", "2 B 3"],
            "info": {"numerical_ids": ["8468"]},
        },
        "2.B.4": {
            "title": "Caprolactam, Glyoxal and Glyoxylic Acid Production",
            "alternative_codes": ["8544", "2B4", "2 B 4"],
            "info": {"numerical_ids": ["8544"]},
            "children": [["2.B.4.a", "2.B.4.b", "2.B.4.c"]],
        },
        "2.B.4.a": {
            "title": "Caprolactam",
            "alternative_codes": ["9515", "2B4a", "2 B 4 a"],
            "info": {"numerical_ids": ["9515"]},
        },
        "2.B.4.b": {
            "title": "Glyoxal",
            "alternative_codes": ["9564", "2B4b", "2 B 4 b"],
            "info": {"numerical_ids": ["9564"]},
        },
        "2.B.4.c": {
            "title": "Glyoxylic Acid",
            "alternative_codes": ["8789", "2B4c", "2 B 4 c"],
            "info": {"numerical_ids": ["8789"]},
        },
        "2.B.5": {
            "title": "Carbide Production",
            "alternative_codes": ["9531", "2B5", "2 B 5"],
            "info": {"numerical_ids": ["9531"]},
            "children": [["2.B.5.a", "2.B.5.b"]],
        },
        "2.B.5.a": {
            "title": "Silicon Carbide",
            "alternative_codes": ["9683", "2B5a", "2 B 5 a"],
            "info": {"numerical_ids": ["9683"]},
        },
        "2.B.5.b": {
            "title": "Calcium Carbide",
            "alternative_codes": ["9206", "2B5b", "2 B 5 b"],
            "info": {"numerical_ids": ["9206"]},
        },
        "2.B.6": {
            "title": "Titanium Dioxide Production",
            "alternative_codes": ["9917", "2B6", "2 B 6"],
            "info": {"numerical_ids": ["9917"]},
        },
        "2.B.7": {
            "title": "Soda Ash Production",
            "alternative_codes": ["8530", "2B7", "2 B 7"],
            "info": {"numerical_ids": ["8530"]},
        },
        "2.B.8": {
            "title": "Petrochemical and Carbon Black Production",
            "alternative_codes": ["9000", "2B8", "2 B 8"],
            "info": {"numerical_ids": ["9000"]},
            "children": [
                [
                    "2.B.8.a",
                    "2.B.8.b",
                    "2.B.8.c",
                    "2.B.8.d",
                    "2.B.8.e",
                    "2.B.8.f",
                    "2.B.8.g",
                ]
            ],
        },
        "2.B.8.a": {
            "title": "Methanol",
            "alternative_codes": ["8934", "2B8a", "2 B 8 a"],
            "info": {"numerical_ids": ["8934"]},
        },
        "2.B.8.b": {
            "title": "Ethylene",
            "alternative_codes": ["9146", "2B8b", "2 B 8 b"],
            "info": {"numerical_ids": ["9146"]},
        },
        "2.B.8.c": {
            "title": "Ethylene Dichloride and Vinyl Chloride Monomer",
            "alternative_codes": ["8686", "2B8c", "2 B 8 c"],
            "info": {"numerical_ids": ["8686"]},
        },
        "2.B.8.d": {
            "title": "Ethylene Oxide",
            "alternative_codes": ["9468", "2B8d", "2 B 8 d"],
            "info": {"numerical_ids": ["9468"]},
        },
        "2.B.8.e": {
            "title": "Acrylonitrile",
            "alternative_codes": ["9784", "2B8e", "2 B 8 e"],
            "info": {"numerical_ids": ["9784"]},
        },
        "2.B.8.f": {
            "title": "Carbon Black",
            "alternative_codes": ["8864", "2B8f", "2 B 8 f"],
            "info": {"numerical_ids": ["8864"]},
        },
        "2.B.8.g": {
            "title": "Other",
            "alternative_codes": ["9384", "2B8g", "2 B 8 g"],
            "info": {"numerical_ids": ["9384"]},
            "children": [["2.B.8.g.i", "2.B.8.g.ii"]],
        },
        "2.B.8.g.i": {
            "title": "Styrene",
            "alternative_codes": ["9941", "2B8gi", "2 B 8 g i"],
            "info": {"numerical_ids": ["9941"]},
        },
        "2.B.8.g.ii": {
            "title": "Other",
            "alternative_codes": ["8276", "2B8gii", "2 B 8 g ii"],
            "info": {"numerical_ids": ["8276"]},
        },
        "2.B.9": {
            "title": "Fluorochemical Production",
            "alternative_codes": ["8884", "2B9", "2 B 9"],
            "info": {"numerical_ids": ["8884"]},
            "children": [["2.B.9.a", "2.B.9.b"]],
        },
        "2.B.9.a": {
            "title": "By-Product Emissions",
            "alternative_codes": ["9517", "2B9a", "2 B 9 a"],
            "info": {"numerical_ids": ["9517"]},
            "children": [["2.B.9.a.i", "2.B.9.a.ii"]],
        },
        "2.B.9.a.i": {
            "title": "Production of HCFC-22",
            "alternative_codes": ["9992", "2B9ai", "2 B 9 a i"],
            "info": {"numerical_ids": ["9992"]},
        },
        "2.B.9.a.ii": {
            "title": "Other",
            "alternative_codes": ["8782", "2B9aii", "2 B 9 a ii"],
            "info": {"numerical_ids": ["8782"]},
        },
        "2.B.9.b": {
            "title": "Fugitive Emissions",
            "alternative_codes": ["9938", "2B9b", "2 B 9 b"],
            "info": {"numerical_ids": ["9938"]},
            "children": [["2.B.9.b.i", "2.B.9.b.ii", "2.B.9.b.iii"]],
        },
        "2.B.9.b.i": {
            "title": "Production of HFC-134a",
            "alternative_codes": ["8427", "2B9bi", "2 B 9 b i"],
            "info": {"numerical_ids": ["8427"]},
        },
        "2.B.9.b.ii": {
            "title": "Production of SF₆",
            "alternative_codes": ["8150", "2B9bii", "2 B 9 b ii"],
            "info": {"numerical_ids": ["8150"]},
        },
        "2.B.9.b.iii": {
            "title": "Other",
            "alternative_codes": ["8419", "2B9biii", "2 B 9 b iii"],
            "info": {"numerical_ids": ["8419"]},
        },
        "2.B.10": {
            "title": "Other",
            "alternative_codes": ["9953", "2B10", "2 B 10"],
            "info": {"numerical_ids": ["9953"]},
        },
        "2.C": {
            "title": "Metal Industry",
            "alternative_codes": ["9064", "2C", "2 C"],
            "info": {"numerical_ids": ["9064"]},
            "children": [
                ["2.C.1", "2.C.2", "2.C.3", "2.C.4", "2.C.5", "2.C.6", "2.C.7"]
            ],
        },
        "2.C.1": {
            "title": "Iron and Steel Production",
            "alternative_codes": ["8229", "2C1", "2 C 1"],
            "info": {"numerical_ids": ["8229"]},
            "children": [
                ["2.C.1.a", "2.C.1.b", "2.C.1.c", "2.C.1.d", "2.C.1.e", "2.C.1.f"]
            ],
        },
        "2.C.1.a": {
            "title": "Steel",
            "alternative_codes": ["9540", "2C1a", "2 C 1 a"],
            "info": {"numerical_ids": ["9540"]},
        },
        "2.C.1.b": {
            "title": "Pig Iron",
            "alternative_codes": ["9567", "2C1b", "2 C 1 b"],
            "info": {"numerical_ids": ["9567"]},
        },
        "2.C.1.c": {
            "title": "Direct Reduced Iron",
            "alternative_codes": ["9679", "2C1c", "2 C 1 c"],
            "info": {"numerical_ids": ["9679"]},
        },
        "2.C.1.d": {
            "title": "Sinter",
            "alternative_codes": ["8962", "2C1d", "2 C 1 d"],
            "info": {"numerical_ids": ["8962"]},
        },
        "2.C.1.e": {
            "title": "Pellet",
            "alternative_codes": ["9387", "2C1e", "2 C 1 e"],
            "info": {"numerical_ids": ["9387"]},
        },
        "2.C.1.f": {
            "title": "Other",
            "alternative_codes": ["10223", "2C1f", "2 C 1 f"],
            "info": {"numerical_ids": ["10223"]},
        },
        "2.C.2": {
            "title": "Ferroalloys Production",
            "alternative_codes": ["10390", "2C2", "2 C 2"],
            "info": {"numerical_ids": ["10390"]},
        },
        "2.C.3": {
            "title": "Aluminium Production",
            "alternative_codes": ["10068", "2C3", "2 C 3"],
            "info": {"numerical_ids": ["10068"]},
            "children": [["2.C.3.a", "2.C.3.b", "2.C.3.c"]],
        },
        "2.C.3.a": {
            "title": "CO₂ Emissions",
            "alternative_codes": ["9079", "2C3a", "2 C 3 a"],
            "info": {"numerical_ids": ["9079"]},
        },
        "2.C.3.b": {
            "title": "By-Product Emissions",
            "alternative_codes": ["9445", "2C3b", "2 C 3 b"],
            "info": {"numerical_ids": ["9445"]},
        },
        "2.C.3.c": {
            "title": "F-gases Used in Foundries",
            "alternative_codes": ["9072", "2C3c", "2 C 3 c"],
            "info": {"numerical_ids": ["9072"]},
        },
        "2.C.4": {
            "title": "Magnesium Production",
            "alternative_codes": ["9635", "2C4", "2 C 4"],
            "info": {"numerical_ids": ["9635"]},
        },
        "2.C.5": {
            "title": "Lead Production",
            "alternative_codes": ["10210", "2C5", "2 C 5"],
            "info": {"numerical_ids": ["10210"]},
        },
        "2.C.6": {
            "title": "Zinc Production",
            "alternative_codes": ["9667", "2C6", "2 C 6"],
            "info": {"numerical_ids": ["9667"]},
        },
        "2.C.7": {
            "title": "Other",
            "alternative_codes": ["10447", "2C7", "2 C 7"],
            "info": {"numerical_ids": ["10447"]},
        },
        "2.D": {
            "title": "Non-energy Products from Fuels and Solvent Use",
            "alternative_codes": ["10094", "2D", "2 D"],
            "info": {"numerical_ids": ["10094"]},
            "children": [["2.D.1", "2.D.2", "2.D.3"]],
        },
        "2.D.1": {
            "title": "Lubricant Use",
            "alternative_codes": ["8852", "2D1", "2 D 1"],
            "info": {"numerical_ids": ["8852"]},
        },
        "2.D.2": {
            "title": "Paraffin Wax Use",
            "alternative_codes": ["8925", "2D2", "2 D 2"],
            "info": {"numerical_ids": ["8925"]},
        },
        "2.D.3": {
            "title": "Other",
            "alternative_codes": ["8811", "2D3", "2 D 3"],
            "info": {"numerical_ids": ["8811"]},
            "children": [["2.D.3.a", "2.D.3.b", "2.D.3.c", "2.D.3.d"]],
        },
        "2.D.3.a": {
            "title": "Solvent Use",
            "alternative_codes": ["10214", "2D3a", "2 D 3 a"],
            "info": {"numerical_ids": ["10214"]},
        },
        "2.D.3.b": {
            "title": "Road Paving with Asphalt",
            "alternative_codes": ["10044", "2D3b", "2 D 3 b"],
            "info": {"numerical_ids": ["10044"]},
        },
        "2.D.3.c": {
            "title": "Asphalt Roofing",
            "alternative_codes": ["8822", "2D3c", "2 D 3 c"],
            "info": {"numerical_ids": ["8822"]},
        },
        "2.D.3.d": {
            "title": "Other",
            "alternative_codes": ["8212", "2D3d", "2 D 3 d"],
            "info": {"numerical_ids": ["8212"]},
        },
        "2.E": {
            "title": "Electronics Industry",
            "alternative_codes": ["8938", "2E", "2 E"],
            "info": {"numerical_ids": ["8938"]},
            "children": [["2.E.1", "2.E.2", "2.E.3", "2.E.4", "2.E.5"]],
        },
        "2.E.1": {
            "title": "Integrated Circuit or Semiconductor",
            "alternative_codes": ["10075", "2E1", "2 E 1"],
            "info": {"numerical_ids": ["10075"]},
        },
        "2.E.2": {
            "title": "TFT Flat Panel Display",
            "alternative_codes": ["10442", "2E2", "2 E 2"],
            "info": {"numerical_ids": ["10442"]},
        },
        "2.E.3": {
            "title": "Photovoltaics",
            "alternative_codes": ["8601", "2E3", "2 E 3"],
            "info": {"numerical_ids": ["8601"]},
        },
        "2.E.4": {
            "title": "Heat Transfer Fluid",
            "alternative_codes": ["9911", "2E4", "2 E 4"],
            "info": {"numerical_ids": ["9911"]},
        },
        "2.E.5": {
            "title": "Other",
            "alternative_codes": ["8434", "2E5", "2 E 5"],
            "info": {"numerical_ids": ["8434"]},
        },
        "2.F": {
            "title": "Product Uses as Substitutes for ODS",
            "alternative_codes": ["8262", "2F", "2 F"],
            "info": {"numerical_ids": ["8262"]},
            "children": [["2.F.1", "2.F.2", "2.F.3", "2.F.4", "2.F.5", "2.F.6"]],
        },
        "2.F.1": {
            "title": "Refrigeration and Air-conditioning",
            "alternative_codes": ["9207", "2F1", "2 F 1"],
            "info": {"numerical_ids": ["9207"]},
            "children": [
                ["2.F.1.a", "2.F.1.b", "2.F.1.c", "2.F.1.d", "2.F.1.e", "2.F.1.f"]
            ],
        },
        "2.F.1.a": {
            "title": "Commercial Refrigeration",
            "alternative_codes": ["9129", "2F1a", "2 F 1 a"],
            "info": {"numerical_ids": ["9129"]},
        },
        "2.F.1.b": {
            "title": "Domestic Refrigeration",
            "alternative_codes": ["9780", "2F1b", "2 F 1 b"],
            "info": {"numerical_ids": ["9780"]},
        },
        "2.F.1.c": {
            "title": "Industrial Refrigeration",
            "alternative_codes": ["10252", "2F1c", "2 F 1 c"],
            "info": {"numerical_ids": ["10252"]},
        },
        "2.F.1.d": {
            "title": "Transport Refrigeration",
            "alternative_codes": ["9634", "2F1d", "2 F 1 d"],
            "info": {"numerical_ids": ["9634"]},
        },
        "2.F.1.e": {
            "title": "Mobile Air-conditioning",
            "alternative_codes": ["10244", "2F1e", "2 F 1 e"],
            "info": {"numerical_ids": ["10244"]},
        },
        "2.F.1.f": {
            "title": "Stationary Air-conditioning",
            "alternative_codes": ["10298", "2F1f", "2 F 1 f"],
            "info": {"numerical_ids": ["10298"]},
        },
        "2.F.2": {
            "title": "Foam Blowing Agents",
            "alternative_codes": ["9352", "2F2", "2 F 2"],
            "info": {"numerical_ids": ["9352"]},
            "children": [["2.F.2.a", "2.F.2.b"]],
        },
        "2.F.2.a": {
            "title": "Closed Cells",
            "alternative_codes": ["8642", "2F2a", "2 F 2 a"],
            "info": {"numerical_ids": ["8642"]},
        },
        "2.F.2.b": {
            "title": "Open Cells",
            "alternative_codes": ["9224", "2F2b", "2 F 2 b"],
            "info": {"numerical_ids": ["9224"]},
        },
        "2.F.3": {
            "title": "Fire Protection",
            "alternative_codes": ["9296", "2F3", "2 F 3"],
            "info": {"numerical_ids": ["9296"]},
        },
        "2.F.4": {
            "title": "Aerosols",
            "alternative_codes": ["10383", "2F4", "2 F 4"],
            "info": {"numerical_ids": ["10383"]},
            "children": [["2.F.4.a", "2.F.4.b"]],
        },
        "2.F.4.a": {
            "title": "Metered Dose Inhalers",
            "alternative_codes": ["8519", "2F4a", "2 F 4 a"],
            "info": {"numerical_ids": ["8519"]},
        },
        "2.F.4.b": {
            "title": "Other",
            "alternative_codes": ["8379", "2F4b", "2 F 4 b"],
            "info": {"numerical_ids": ["8379"]},
        },
        "2.F.5": {
            "title": "Solvents",
            "alternative_codes": ["8316", "2F5", "2 F 5"],
            "info": {"numerical_ids": ["8316"]},
        },
        "2.F.6": {
            "title": "Other Applications",
            "alternative_codes": ["8607", "2F6", "2 F 6"],
            "info": {"numerical_ids": ["8607"]},
            "children": [["2.F.6.a", "2.F.6.b"]],
        },
        "2.F.6.a": {
            "title": "Emissive",
            "alternative_codes": ["10246", "2F6a", "2 F 6 a"],
            "info": {"numerical_ids": ["10246"]},
        },
        "2.F.6.b": {
            "title": "Contained",
            "alternative_codes": ["10042", "2F6b", "2 F 6 b"],
            "info": {"numerical_ids": ["10042"]},
        },
        "2.G": {
            "title": "Other Product Manufacture and Use",
            "alternative_codes": ["8201", "2G", "2 G"],
            "info": {"numerical_ids": ["8201"]},
            "children": [["2.G.1", "2.G.2", "2.G.3", "2.G.4"]],
        },
        "2.G.1": {
            "title": "Electrical Equipment",
            "alternative_codes": ["9490", "2G1", "2 G 1"],
            "info": {"numerical_ids": ["9490"]},
        },
        "2.G.2": {
            "title": "SF₆ and PFCs from Other Product Use",
            "alternative_codes": ["10301", "2G2", "2 G 2"],
            "info": {"numerical_ids": ["10301"]},
            "children": [["2.G.2.a", "2.G.2.b", "2.G.2.c", "2.G.2.d", "2.G.2.e"]],
        },
        "2.G.2.a": {
            "title": "Military Applications",
            "alternative_codes": ["9055", "2G2a", "2 G 2 a"],
            "info": {"numerical_ids": ["9055"]},
        },
        "2.G.2.b": {
            "title": "Accelerators",
            "alternative_codes": ["9925", "2G2b", "2 G 2 b"],
            "info": {"numerical_ids": ["9925"]},
        },
        "2.G.2.c": {
            "title": "Soundproof Windows",
            "alternative_codes": ["9789", "2G2c", "2 G 2 c"],
            "info": {"numerical_ids": ["9789"]},
        },
        "2.G.2.d": {
            "title": "Adiabatic Properties: Shoes and Tyres",
            "alternative_codes": ["9610", "2G2d", "2 G 2 d"],
            "info": {"numerical_ids": ["9610"]},
        },
        "2.G.2.e": {
            "title": "Other",
            "alternative_codes": ["8978", "2G2e", "2 G 2 e"],
            "info": {"numerical_ids": ["8978"]},
        },
        "2.G.3": {
            "title": "N₂O from Product Uses",
            "alternative_codes": ["10433", "2G3", "2 G 3"],
            "info": {"numerical_ids": ["10433"]},
            "children": [["2.G.3.a", "2.G.3.b"]],
        },
        "2.G.3.a": {
            "title": "Medical Applications",
            "alternative_codes": ["8737", "2G3a", "2 G 3 a"],
            "info": {"numerical_ids": ["8737"]},
        },
        "2.G.3.b": {
            "title": "Other",
            "alternative_codes": ["9014", "2G3b", "2 G 3 b"],
            "info": {"numerical_ids": ["9014"]},
            "children": [["2.G.3.b.i", "2.G.3.b.ii"]],
        },
        "2.G.3.b.i": {
            "title": "Propellant for Pressure and Aerosol Products",
            "alternative_codes": ["9201", "2G3bi", "2 G 3 b i"],
            "info": {"numerical_ids": ["9201"]},
        },
        "2.G.3.b.ii": {
            "title": "Other",
            "alternative_codes": ["8566", "2G3bii", "2 G 3 b ii"],
            "info": {"numerical_ids": ["8566"]},
        },
        "2.G.4": {
            "title": "Other",
            "alternative_codes": ["8534", "2G4", "2 G 4"],
            "info": {"numerical_ids": ["8534"]},
        },
        "2.H": {
            "title": "Other",
            "alternative_codes": ["9899", "2H", "2 H"],
            "info": {"numerical_ids": ["9899"]},
            "children": [["2.H.1", "2.H.2", "2.H.3"]],
        },
        "2.H.1": {
            "title": "Pulp and Paper",
            "alternative_codes": ["8644", "2H1", "2 H 1"],
            "info": {"numerical_ids": ["8644"]},
        },
        "2.H.2": {
            "title": "Food and Beverages Industry",
            "alternative_codes": ["8797", "2H2", "2 H 2"],
            "info": {"numerical_ids": ["8797"]},
        },
        "2.H.3": {
            "title": "Other",
            "alternative_codes": ["8883", "2H3", "2 H 3"],
            "info": {"numerical_ids": ["8883"]},
        },
        "3": {
            "title": "Agriculture",
            "alternative_codes": ["3.", "10483", "10096"],
            "info": {"numerical_ids": ["10483", "10096"]},
            "children": [
                ["3.A", "3.B", "3.C", "3.D", "3.E", "3.F", "3.G", "3.H", "3.I", "3.J"]
            ],
        },
        "3.A": {
            "title": "Enteric Fermentation",
            "alternative_codes": ["9559", "3A", "3 A"],
            "info": {"numerical_ids": ["9559"]},
        },
        "3.B": {
            "title": "Manure Management",
            "alternative_codes": ["9608", "3B", "3 B"],
            "info": {"numerical_ids": ["9608"]},
        },
        "3.C": {
            "title": "Rice Cultivation",
            "alternative_codes": ["10228", "3C", "3 C"],
            "info": {"numerical_ids": ["10228"]},
            "children": [["3.C.1", "3.C.2", "3.C.3", "3.C.4"]],
        },
        "3.C.1": {
            "title": "Irrigated",
            "alternative_codes": ["9960", "3C1", "3 C 1"],
            "info": {"numerical_ids": ["9960"]},
            "children": [["3.C.1.a", "3.C.1.b"]],
        },
        "3.C.1.a": {
            "title": "Continuously Flooded",
            "alternative_codes": ["10315", "3C1a", "3 C 1 a"],
            "info": {"numerical_ids": ["10315"]},
        },
        "3.C.1.b": {
            "title": "Intermittently Flooded",
            "alternative_codes": ["8915", "3C1b", "3 C 1 b"],
            "info": {"numerical_ids": ["8915"]},
            "children": [["3.C.1.b.i", "3.C.1.b.ii"]],
        },
        "3.C.1.b.i": {
            "title": "Single Aeration",
            "alternative_codes": ["9184", "3C1bi", "3 C 1 b i"],
            "info": {"numerical_ids": ["9184"]},
        },
        "3.C.1.b.ii": {
            "title": "Multiple Aeration",
            "alternative_codes": ["10065", "3C1bii", "3 C 1 b ii"],
            "info": {"numerical_ids": ["10065"]},
        },
        "3.C.2": {
            "title": "Rainfed",
            "alternative_codes": ["8984", "3C2", "3 C 2"],
            "info": {"numerical_ids": ["8984"]},
            "children": [["3.C.2.a", "3.C.2.b"]],
        },
        "3.C.2.a": {
            "title": "Flood Prone",
            "alternative_codes": ["9942", "3C2a", "3 C 2 a"],
            "info": {"numerical_ids": ["9942"]},
        },
        "3.C.2.b": {
            "title": "Drought Prone",
            "alternative_codes": ["8941", "3C2b", "3 C 2 b"],
            "info": {"numerical_ids": ["8941"]},
        },
        "3.C.3": {
            "title": "Deep Water",
            "alternative_codes": ["9094", "3C3", "3 C 3"],
            "info": {"numerical_ids": ["9094"]},
            "children": [["3.C.3.a", "3.C.3.b"]],
        },
        "3.C.3.a": {
            "title": "Water Depth 50-100 cm",
            "alternative_codes": ["8995", "3C3a", "3 C 3 a"],
            "info": {"numerical_ids": ["8995"]},
        },
        "3.C.3.b": {
            "title": "Water Depth > 100 cm",
            "alternative_codes": ["8373", "3C3b", "3 C 3 b"],
            "info": {"numerical_ids": ["8373"]},
        },
        "3.C.4": {
            "title": "Other",
            "alternative_codes": ["8747", "3C4", "3 C 4"],
            "info": {"numerical_ids": ["8747"]},
        },
        "3.D": {
            "title": "Agricultural Soils",
            "alternative_codes": ["9678", "3D", "3 D"],
            "info": {"numerical_ids": ["9678"]},
            "children": [["3.D.1", "3.D.2"]],
        },
        "3.D.1": {
            "title": "Direct N₂O Emissions From Managed Soils",
            "alternative_codes": ["9087", "3D1", "3 D 1"],
            "info": {"numerical_ids": ["9087"]},
            "children": [
                [
                    "3.D.1.a",
                    "3.D.1.b",
                    "3.D.1.c",
                    "3.D.1.d",
                    "3.D.1.e",
                    "3.D.1.f",
                    "3.D.1.g",
                ]
            ],
        },
        "3.D.1.a": {
            "title": "Inorganic N Fertilizers",
            "alternative_codes": ["9566", "3D1a", "3 D 1 a"],
            "info": {"numerical_ids": ["9566"]},
        },
        "3.D.1.b": {
            "title": "Organic N Fertilizers",
            "alternative_codes": ["9523", "3D1b", "3 D 1 b"],
            "info": {"numerical_ids": ["9523"]},
            "children": [["3.D.1.b.i", "3.D.1.b.ii", "3.D.1.b.iii"]],
        },
        "3.D.1.b.i": {
            "title": "Animal Manure Applied to Soils",
            "alternative_codes": ["8365", "3D1bi", "3 D 1 b i"],
            "info": {"numerical_ids": ["8365"]},
        },
        "3.D.1.b.ii": {
            "title": "Sewage Sludge Applied to Soils",
            "alternative_codes": ["8482", "3D1bii", "3 D 1 b ii"],
            "info": {"numerical_ids": ["8482"]},
        },
        "3.D.1.b.iii": {
            "title": "Other Organic Fertilizers Applied to Soils",
            "alternative_codes": ["8218", "3D1biii", "3 D 1 b iii"],
            "info": {"numerical_ids": ["8218"]},
        },
        "3.D.1.c": {
            "title": "Urine and Dung Deposited by Grazing Animals",
            "alternative_codes": ["9041", "3D1c", "3 D 1 c"],
            "info": {"numerical_ids": ["9041"]},
        },
        "3.D.1.d": {
            "title": "Crop Residues",
            "alternative_codes": ["10142", "3D1d", "3 D 1 d"],
            "info": {"numerical_ids": ["10142"]},
        },
        "3.D.1.e": {
            "title": "Mineralization/Immobilization Associated with Loss/Gain of Soil Organic Matter",
            "alternative_codes": ["9302", "3D1e", "3 D 1 e"],
            "info": {"numerical_ids": ["9302"]},
        },
        "3.D.1.f": {
            "title": "Cultivation of Organic Soils",
            "alternative_codes": ["10437", "3D1f", "3 D 1 f"],
            "info": {"numerical_ids": ["10437"]},
        },
        "3.D.1.g": {
            "title": "Other",
            "alternative_codes": ["8502", "3D1g", "3 D 1 g"],
            "info": {"numerical_ids": ["8502"]},
        },
        "3.D.2": {
            "title": "Indirect N₂O Emissions From Managed Soils",
            "alternative_codes": ["8920", "3D2", "3 D 2"],
            "info": {"numerical_ids": ["8920"]},
            "children": [["3.D.2.a", "3.D.2.b"]],
        },
        "3.D.2.a": {
            "title": "Atmospheric Deposition",
            "alternative_codes": ["9821", "3D2a", "3 D 2 a"],
            "info": {"numerical_ids": ["9821"]},
        },
        "3.D.2.b": {
            "title": "Nitrogen Leaching and Run-off",
            "alternative_codes": ["9875", "3D2b", "3 D 2 b"],
            "info": {"numerical_ids": ["9875"]},
        },
        "3.E": {
            "title": "Prescribed Burning of Savannas",
            "alternative_codes": ["10322", "3E", "3 E"],
            "info": {"numerical_ids": ["10322"]},
            "children": [["3.E.1", "3.E.2"]],
        },
        "3.E.1": {
            "title": "Forest Land",
            "alternative_codes": ["9488", "3E1", "3 E 1"],
            "info": {"numerical_ids": ["9488"]},
        },
        "3.E.2": {
            "title": "Grassland",
            "alternative_codes": ["9970", "3E2", "3 E 2"],
            "info": {"numerical_ids": ["9970"]},
        },
        "3.F": {
            "title": "Field Burning of Agricultural Residues",
            "alternative_codes": ["8783", "3F", "3 F"],
            "info": {"numerical_ids": ["8783"]},
            "children": [["3.F.1", "3.F.2", "3.F.3", "3.F.4", "3.F.5"]],
        },
        "3.F.1": {
            "title": "Cereals",
            "alternative_codes": ["10305", "3F1", "3 F 1"],
            "info": {"numerical_ids": ["10305"]},
            "children": [["3.F.1.a", "3.F.1.b", "3.F.1.c", "3.F.1.d"]],
        },
        "3.F.1.a": {
            "title": "Wheat",
            "alternative_codes": ["8669", "3F1a", "3 F 1 a"],
            "info": {"numerical_ids": ["8669"]},
        },
        "3.F.1.b": {
            "title": "Barley",
            "alternative_codes": ["10193", "3F1b", "3 F 1 b"],
            "info": {"numerical_ids": ["10193"]},
        },
        "3.F.1.c": {
            "title": "Maize",
            "alternative_codes": ["8990", "3F1c", "3 F 1 c"],
            "info": {"numerical_ids": ["8990"]},
        },
        "3.F.1.d": {
            "title": "Other",
            "alternative_codes": ["9507", "3F1d", "3 F 1 d"],
            "info": {"numerical_ids": ["9507"]},
        },
        "3.F.2": {
            "title": "Pulses",
            "alternative_codes": ["9749", "3F2", "3 F 2"],
            "info": {"numerical_ids": ["9749"]},
        },
        "3.F.3": {
            "title": "Tubers and Roots",
            "alternative_codes": ["9142", "3F3", "3 F 3"],
            "info": {"numerical_ids": ["9142"]},
        },
        "3.F.4": {
            "title": "Sugar Cane",
            "alternative_codes": ["10387", "3F4", "3 F 4"],
            "info": {"numerical_ids": ["10387"]},
        },
        "3.F.5": {
            "title": "Other",
            "alternative_codes": ["10336", "3F5", "3 F 5"],
            "info": {"numerical_ids": ["10336"]},
        },
        "3.G": {
            "title": "Liming",
            "alternative_codes": ["8278", "3G", "3 G"],
            "info": {"numerical_ids": ["8278"]},
            "children": [["3.G.1", "3.G.2"]],
        },
        "3.G.1": {
            "title": "Limestone CaCO₃",
            "alternative_codes": ["8504", "3G1", "3 G 1"],
            "info": {"numerical_ids": ["8504"]},
        },
        "3.G.2": {
            "title": "Dolomite CaMg(CO₃)₂",
            "alternative_codes": ["8267", "3G2", "3 G 2"],
            "info": {"numerical_ids": ["8267"]},
        },
        "3.H": {
            "title": "Urea Application",
            "alternative_codes": ["9927", "3H", "3 H"],
            "info": {"numerical_ids": ["9927"]},
        },
        "3.I": {
            "title": "Other Carbon-containing Fertilizers",
            "alternative_codes": ["8417", "3I", "3 I"],
            "info": {"numerical_ids": ["8417"]},
        },
        "3.J": {
            "title": "Other",
            "alternative_codes": ["10025", "3J", "3 J"],
            "info": {"numerical_ids": ["10025"]},
        },
        "4": {
            "title": "Land Use, Land-Use Change and Forestry",
            "alternative_codes": ["4.", "9411"],
            "info": {"numerical_ids": ["9411"]},
            "children": [["4.A", "4.B", "4.C", "4.D", "4.E", "4.F", "4.G", "4.H"]],
        },
        "4.A": {
            "title": "Forest Land",
            "alternative_codes": ["10121", "4A", "4 A"],
            "info": {"numerical_ids": ["10121"]},
            "children": [["4.A.1", "4.A.2"]],
        },
        "4.A.1": {
            "title": "Forest Land Remaining Forest Land",
            "alternative_codes": ["8348", "4A1", "4 A 1"],
            "info": {"numerical_ids": ["8348"]},
        },
        "4.A.2": {
            "title": "Land Converted to Forest Land",
            "alternative_codes": ["8416", "4A2", "4 A 2"],
            "info": {"numerical_ids": ["8416"]},
            "children": [["4.A.2.a", "4.A.2.b", "4.A.2.c", "4.A.2.d", "4.A.2.e"]],
        },
        "4.A.2.a": {
            "title": "Cropland Converted to Forest Land",
            "alternative_codes": ["9741", "4A2a", "4 A 2 a"],
            "info": {"numerical_ids": ["9741"]},
        },
        "4.A.2.b": {
            "title": "Grassland Converted to Forest Land",
            "alternative_codes": ["9851", "4A2b", "4 A 2 b"],
            "info": {"numerical_ids": ["9851"]},
        },
        "4.A.2.c": {
            "title": "Wetlands Converted to Forest Land",
            "alternative_codes": ["9306", "4A2c", "4 A 2 c"],
            "info": {"numerical_ids": ["9306"]},
        },
        "4.A.2.d": {
            "title": "Settlements Converted to Forest Land",
            "alternative_codes": ["10297", "4A2d", "4 A 2 d"],
            "info": {"numerical_ids": ["10297"]},
        },
        "4.A.2.e": {
            "title": "Other Land Converted to Forest Land",
            "alternative_codes": ["8735", "4A2e", "4 A 2 e"],
            "info": {"numerical_ids": ["8735"]},
        },
        "4.B": {
            "title": "Cropland",
            "alternative_codes": ["9805", "4B", "4 B"],
            "info": {"numerical_ids": ["9805"]},
            "children": [["4.B.1", "4.B.2"]],
        },
        "4.B.1": {
            "title": "Cropland Remaining Cropland",
            "alternative_codes": ["10430", "4B1", "4 B 1"],
            "info": {"numerical_ids": ["10430"]},
        },
        "4.B.2": {
            "title": "Land Converted to Cropland",
            "alternative_codes": ["8678", "4B2", "4 B 2"],
            "info": {"numerical_ids": ["8678"]},
            "children": [["4.B.2.a", "4.B.2.b", "4.B.2.c", "4.B.2.d", "4.B.2.e"]],
        },
        "4.B.2.a": {
            "title": "Forest Land Converted to Cropland",
            "alternative_codes": ["9799", "4B2a", "4 B 2 a"],
            "info": {"numerical_ids": ["9799"]},
        },
        "4.B.2.b": {
            "title": "Grassland Converted to Cropland",
            "alternative_codes": ["9491", "4B2b", "4 B 2 b"],
            "info": {"numerical_ids": ["9491"]},
        },
        "4.B.2.c": {
            "title": "Wetlands Converted to Cropland",
            "alternative_codes": ["10450", "4B2c", "4 B 2 c"],
            "info": {"numerical_ids": ["10450"]},
        },
        "4.B.2.d": {
            "title": "Settlements Converted to Cropland",
            "alternative_codes": ["8709", "4B2d", "4 B 2 d"],
            "info": {"numerical_ids": ["8709"]},
        },
        "4.B.2.e": {
            "title": "Other Land Converted to Cropland",
            "alternative_codes": ["9560", "4B2e", "4 B 2 e"],
            "info": {"numerical_ids": ["9560"]},
        },
        "4.C": {
            "title": "Grassland",
            "alternative_codes": ["8849", "4C", "4 C"],
            "info": {"numerical_ids": ["8849"]},
            "children": [["4.C.1", "4.C.2"]],
        },
        "4.C.1": {
            "title": "Grassland Remaining Grassland",
            "alternative_codes": ["9360", "4C1", "4 C 1"],
            "info": {"numerical_ids": ["9360"]},
        },
        "4.C.2": {
            "title": "Land Converted to Grassland",
            "alternative_codes": ["8259", "4C2", "4 C 2"],
            "info": {"numerical_ids": ["8259"]},
            "children": [["4.C.2.a", "4.C.2.b", "4.C.2.c", "4.C.2.d", "4.C.2.e"]],
        },
        "4.C.2.a": {
            "title": "Forest Land Converted to Grassland",
            "alternative_codes": ["9405", "4C2a", "4 C 2 a"],
            "info": {"numerical_ids": ["9405"]},
        },
        "4.C.2.b": {
            "title": "Cropland Converted to Grassland",
            "alternative_codes": ["9966", "4C2b", "4 C 2 b"],
            "info": {"numerical_ids": ["9966"]},
        },
        "4.C.2.c": {
            "title": "Wetlands Converted to Grassland",
            "alternative_codes": ["10323", "4C2c", "4 C 2 c"],
            "info": {"numerical_ids": ["10323"]},
        },
        "4.C.2.d": {
            "title": "Settlements Converted to Grassland",
            "alternative_codes": ["9444", "4C2d", "4 C 2 d"],
            "info": {"numerical_ids": ["9444"]},
        },
        "4.C.2.e": {
            "title": "Other Land Converted to Grassland",
            "alternative_codes": ["10189", "4C2e", "4 C 2 e"],
            "info": {"numerical_ids": ["10189"]},
        },
        "4.D": {
            "title": "Wetlands",
            "alternative_codes": ["9897", "4D", "4 D"],
            "info": {"numerical_ids": ["9897"]},
            "children": [["4.D.1", "4.D.2"]],
        },
        "4.D.1": {
            "title": "Wetlands Remaining Wetlands",
            "alternative_codes": ["9154", "4D1", "4 D 1"],
            "info": {"numerical_ids": ["9154"]},
            "children": [["4.D.1.a", "4.D.1.b", "4.D.1.c"]],
        },
        "4.D.1.a": {
            "title": "Peat Extraction Remaining Peat Extraction",
            "alternative_codes": ["10156", "4D1a", "4 D 1 a"],
            "info": {"numerical_ids": ["10156"]},
        },
        "4.D.1.b": {
            "title": "Flooded Land Remaining Flooded Land",
            "alternative_codes": ["9151", "4D1b", "4 D 1 b"],
            "info": {"numerical_ids": ["9151"]},
        },
        "4.D.1.c": {
            "title": "Other Wetlands Remaining Other Wetlands",
            "alternative_codes": ["8307", "4D1c", "4 D 1 c"],
            "info": {"numerical_ids": ["8307"]},
        },
        "4.D.2": {
            "title": "Land Converted to Wetlands",
            "alternative_codes": ["8232", "4D2", "4 D 2"],
            "info": {"numerical_ids": ["8232"]},
            "children": [["4.D.2.a", "4.D.2.b", "4.D.2.c"]],
        },
        "4.D.2.a": {
            "title": "Land Converted to Peat Extraction",
            "alternative_codes": ["11002", "4D2a", "4 D 2 a"],
            "info": {"numerical_ids": ["11002"]},
        },
        "4.D.2.b": {
            "title": "Land Converted to Flooded Land",
            "alternative_codes": ["11003", "4D2b", "4 D 2 b"],
            "info": {"numerical_ids": ["11003"]},
            "children": [
                ["4.D.2.b.i", "4.D.2.b.ii", "4.D.2.b.iii", "4.D.2.b.iv", "4.D.2.b.v"]
            ],
        },
        "4.D.2.b.i": {
            "title": "Forest Land Converted to Flooded Land",
            "alternative_codes": ["11004", "4D2bi", "4 D 2 b i"],
            "info": {"numerical_ids": ["11004"]},
        },
        "4.D.2.b.ii": {
            "title": "Cropland Converted to Flooded Land",
            "alternative_codes": ["11005", "4D2bii", "4 D 2 b ii"],
            "info": {"numerical_ids": ["11005"]},
        },
        "4.D.2.b.iii": {
            "title": "Grassland Converted to Flooded Land",
            "alternative_codes": ["11006", "4D2biii", "4 D 2 b iii"],
            "info": {"numerical_ids": ["11006"]},
        },
        "4.D.2.b.iv": {
            "title": "Settlements Converted to Flooded Land",
            "alternative_codes": ["11007", "4D2biv", "4 D 2 b iv"],
            "info": {"numerical_ids": ["11007"]},
        },
        "4.D.2.b.v": {
            "title": "Other Land Converted to Flooded Land",
            "alternative_codes": ["11008", "4D2bv", "4 D 2 b v"],
            "info": {"numerical_ids": ["11008"]},
        },
        "4.D.2.c": {
            "title": "Land Converted to Other Wetlands",
            "alternative_codes": ["11009", "4D2c", "4 D 2 c"],
            "info": {"numerical_ids": ["11009"]},
            "children": [
                ["4.D.2.c.i", "4.D.2.c.ii", "4.D.2.c.iii", "4.D.2.c.iv", "4.D.2.c.v"]
            ],
        },
        "4.D.2.c.i": {
            "title": "Forest Land Converted to Other Wetlands",
            "alternative_codes": ["11010", "4D2ci", "4 D 2 c i"],
            "info": {"numerical_ids": ["11010"]},
        },
        "4.D.2.c.ii": {
            "title": "Cropland Converted to Other Wetlands",
            "alternative_codes": ["11011", "4D2cii", "4 D 2 c ii"],
            "info": {"numerical_ids": ["11011"]},
        },
        "4.D.2.c.iii": {
            "title": "Grassland Converted to Other Wetlands",
            "alternative_codes": ["11012", "4D2ciii", "4 D 2 c iii"],
            "info": {"numerical_ids": ["11012"]},
        },
        "4.D.2.c.iv": {
            "title": "Settlements Converted to Other Wetlands",
            "alternative_codes": ["11013", "4D2civ", "4 D 2 c iv"],
            "info": {"numerical_ids": ["11013"]},
        },
        "4.D.2.c.v": {
            "title": "Other Land Converted to Other Wetlands",
            "alternative_codes": ["11014", "4D2cv", "4 D 2 c v"],
            "info": {"numerical_ids": ["11014"]},
        },
        "4.E": {
            "title": "Settlements",
            "alternative_codes": ["10314", "4E", "4 E"],
            "info": {"numerical_ids": ["10314"]},
            "children": [["4.E.1", "4.E.2"]],
        },
        "4.E.1": {
            "title": "Settlements Remaining Settlements",
            "alternative_codes": ["10132", "4E1", "4 E 1"],
            "info": {"numerical_ids": ["10132"]},
        },
        "4.E.2": {
            "title": "Land Converted to Settlements",
            "alternative_codes": ["9506", "4E2", "4 E 2"],
            "info": {"numerical_ids": ["9506"]},
            "children": [["4.E.2.a", "4.E.2.b", "4.E.2.c", "4.E.2.d", "4.E.2.e"]],
        },
        "4.E.2.a": {
            "title": "Forest Land Converted to Settlements",
            "alternative_codes": ["10183", "4E2a", "4 E 2 a"],
            "info": {"numerical_ids": ["10183"]},
        },
        "4.E.2.b": {
            "title": "Cropland Converted to Settlements",
            "alternative_codes": ["9914", "4E2b", "4 E 2 b"],
            "info": {"numerical_ids": ["9914"]},
        },
        "4.E.2.c": {
            "title": "Grassland Converted to Settlements",
            "alternative_codes": ["10026", "4E2c", "4 E 2 c"],
            "info": {"numerical_ids": ["10026"]},
        },
        "4.E.2.d": {
            "title": "Wetlands Converted to Settlements",
            "alternative_codes": ["8465", "4E2d", "4 E 2 d"],
            "info": {"numerical_ids": ["8465"]},
        },
        "4.E.2.e": {
            "title": "Other Land Converted to Settlements",
            "alternative_codes": ["9857", "4E2e", "4 E 2 e"],
            "info": {"numerical_ids": ["9857"]},
        },
        "4.F": {
            "title": "Other Land",
            "alternative_codes": ["8288", "4F", "4 F"],
            "info": {"numerical_ids": ["8288"]},
            "children": [["4.F.1", "4.F.2"]],
        },
        "4.F.1": {
            "title": "Other Land Remaining Other Land",
            "alternative_codes": ["11015", "4F1", "4 F 1"],
            "info": {"numerical_ids": ["11015"]},
        },
        "4.F.2": {
            "title": "Land Converted to Other Land",
            "alternative_codes": ["8343", "4F2", "4 F 2"],
            "info": {"numerical_ids": ["8343"]},
            "children": [["4.F.2.a", "4.F.2.b", "4.F.2.c", "4.F.2.d", "4.F.2.e"]],
        },
        "4.F.2.a": {
            "title": "Forest Land Converted to Other Land",
            "alternative_codes": ["8488", "4F2a", "4 F 2 a"],
            "info": {"numerical_ids": ["8488"]},
        },
        "4.F.2.b": {
            "title": "Cropland Converted to Other Land",
            "alternative_codes": ["8234", "4F2b", "4 F 2 b"],
            "info": {"numerical_ids": ["8234"]},
        },
        "4.F.2.c": {
            "title": "Grassland Converted  to Other Land",
            "alternative_codes": ["8574", "4F2c", "4 F 2 c"],
            "info": {"numerical_ids": ["8574"]},
        },
        "4.F.2.d": {
            "title": "Wetlands Converted to Other Land",
            "alternative_codes": ["10371", "4F2d", "4 F 2 d"],
            "info": {"numerical_ids": ["10371"]},
        },
        "4.F.2.e": {
            "title": "Settlements Converted to Other Land",
            "alternative_codes": ["9019", "4F2e", "4 F 2 e"],
            "info": {"numerical_ids": ["9019"]},
        },
        "4.G": {
            "title": "Harvested Wood Products",
            "alternative_codes": ["9133", "4G", "4 G"],
            "info": {"numerical_ids": ["9133"]},
            "children": [["11035", "4.G.1", "4.G.2", "4.G.3"]],
        },
        "4.G.1": {
            "title": "Solid Wood",
            "alternative_codes": ["11016", "4G1", "4 G 1"],
            "info": {"numerical_ids": ["11016"]},
            "children": [["4.G.1.a", "4.G.1.b", "4.G.1.c"]],
        },
        "4.G.1.a": {
            "title": "Sawnwood",
            "alternative_codes": ["11017", "4G1a", "4 G 1 a"],
            "info": {"numerical_ids": ["11017"]},
        },
        "4.G.1.b": {
            "title": "Wood Panels",
            "alternative_codes": ["11018", "4G1b", "4 G 1 b"],
            "info": {"numerical_ids": ["11018"]},
        },
        "4.G.1.c": {
            "title": "Other Solid Wood Products",
            "alternative_codes": ["11019", "4G1c", "4 G 1 c"],
            "info": {"numerical_ids": ["11019"]},
        },
        "4.G.2": {
            "title": "Paper and Paperboard",
            "alternative_codes": ["11020", "4G2", "4 G 2"],
            "info": {"numerical_ids": ["11020"]},
        },
        "4.G.3": {
            "title": "Other",
            "alternative_codes": ["11021", "4G3", "4 G 3"],
            "info": {"numerical_ids": ["11021"]},
        },
        "4.H": {
            "title": "Other",
            "alternative_codes": ["9158", "4H", "4 H"],
            "info": {"numerical_ids": ["9158"]},
        },
        "5": {
            "title": "Waste",
            "alternative_codes": ["5.", "10484", "10159"],
            "info": {"numerical_ids": ["10484", "10159"]},
            "children": [["11022", "5.A", "5.B", "5.C", "5.D", "5.E"]],
        },
        "5.A": {
            "title": "Solid Waste Disposal",
            "alternative_codes": ["9284", "5A", "5 A"],
            "info": {"numerical_ids": ["9284"]},
            "children": [["5.A.1", "5.A.2", "5.A.3"]],
        },
        "5.A.1": {
            "title": "Managed Waste Disposal Sites",
            "alternative_codes": ["8477", "5A1", "5 A 1"],
            "info": {"numerical_ids": ["8477"]},
            "children": [["5.A.1.a", "5.A.1.b"]],
        },
        "5.A.1.a": {
            "title": "Anaerobic",
            "alternative_codes": ["9839", "5A1a", "5 A 1 a"],
            "info": {"numerical_ids": ["9839"]},
        },
        "5.A.1.b": {
            "title": "Semi-aerobic",
            "alternative_codes": ["9144", "5A1b", "5 A 1 b"],
            "info": {"numerical_ids": ["9144"]},
        },
        "5.A.2": {
            "title": "Unmanaged Waste Disposal Sites",
            "alternative_codes": ["10235", "5A2", "5 A 2"],
            "info": {"numerical_ids": ["10235"]},
        },
        "5.A.3": {
            "title": "Uncategorized Waste Disposal Sites",
            "alternative_codes": ["8652", "5A3", "5 A 3"],
            "info": {"numerical_ids": ["8652"]},
        },
        "5.B": {
            "title": "Biological Treatment of Solid Waste",
            "alternative_codes": ["9245", "5B", "5 B"],
            "info": {"numerical_ids": ["9245"]},
            "children": [["5.B.1", "5.B.2"]],
        },
        "5.B.1": {
            "title": "Composting",
            "alternative_codes": ["8701", "5B1", "5 B 1"],
            "info": {"numerical_ids": ["8701"]},
            "children": [["5.B.1.a", "5.B.1.b"]],
        },
        "5.B.1.a": {
            "title": "Municipal Solid Waste",
            "alternative_codes": ["9682", "5B1a", "5 B 1 a"],
            "info": {"numerical_ids": ["9682"]},
        },
        "5.B.1.b": {
            "title": "Other",
            "alternative_codes": ["8640", "5B1b", "5 B 1 b"],
            "info": {"numerical_ids": ["8640"]},
        },
        "5.B.2": {
            "title": "Anaerobic Digestion at Biogas Facilities",
            "alternative_codes": ["8225", "5B2", "5 B 2"],
            "info": {"numerical_ids": ["8225"]},
            "children": [["5.B.2.a", "5.B.2.b"]],
        },
        "5.B.2.a": {
            "title": "Municipal Solid Waste",
            "alternative_codes": ["9290", "5B2a", "5 B 2 a"],
            "info": {"numerical_ids": ["9290"]},
        },
        "5.B.2.b": {
            "title": "Other",
            "alternative_codes": ["9639", "5B2b", "5 B 2 b"],
            "info": {"numerical_ids": ["9639"]},
        },
        "5.C": {
            "title": "Incineration and Open Burning of Waste",
            "alternative_codes": ["8227", "5C", "5 C"],
            "info": {"numerical_ids": ["8227"]},
            "children": [["5.C.1", "5.C.2"]],
        },
        "5.C.1": {
            "title": "Waste Incineration",
            "alternative_codes": ["10408", "5C1", "5 C 1"],
            "info": {"numerical_ids": ["10408"]},
            "children": [["5.C.1.a", "5.C.1.b"]],
        },
        "5.C.1.a": {
            "title": "Biogenic",
            "alternative_codes": ["8776", "5C1a", "5 C 1 a"],
            "info": {"numerical_ids": ["8776"]},
            "children": [["5.C.1.a.i", "5.C.1.a.ii"]],
        },
        "5.C.1.a.i": {
            "title": "Municipal Solid Waste",
            "alternative_codes": ["9069", "5C1ai", "5 C 1 a i"],
            "info": {"numerical_ids": ["9069"]},
        },
        "5.C.1.a.ii": {
            "title": "Other",
            "alternative_codes": ["8401", "5C1aii", "5 C 1 a ii"],
            "info": {"numerical_ids": ["8401"]},
            "children": [
                [
                    "5.C.1.a.ii.1",
                    "5.C.1.a.ii.2",
                    "5.C.1.a.ii.3",
                    "5.C.1.a.ii.4",
                    "5.C.1.a.ii.5",
                ]
            ],
        },
        "5.C.1.a.ii.1": {
            "title": "Industrial Solid Wastes",
            "alternative_codes": ["8260", "5C1aii1", "5 C 1 a ii 1"],
            "info": {"numerical_ids": ["8260"]},
        },
        "5.C.1.a.ii.2": {
            "title": "Hazardous Waste",
            "alternative_codes": ["9329", "5C1aii2", "5 C 1 a ii 2"],
            "info": {"numerical_ids": ["9329"]},
        },
        "5.C.1.a.ii.3": {
            "title": "Clinical Waste",
            "alternative_codes": ["9141", "5C1aii3", "5 C 1 a ii 3"],
            "info": {"numerical_ids": ["9141"]},
        },
        "5.C.1.a.ii.4": {
            "title": "Sewage Sludge",
            "alternative_codes": ["9538", "5C1aii4", "5 C 1 a ii 4"],
            "info": {"numerical_ids": ["9538"]},
        },
        "5.C.1.a.ii.5": {
            "title": "Other",
            "alternative_codes": ["9218", "5C1aii5", "5 C 1 a ii 5"],
            "info": {"numerical_ids": ["9218"]},
        },
        "5.C.1.b": {
            "title": "Non-biogenic",
            "alternative_codes": ["9979", "5C1b", "5 C 1 b"],
            "info": {"numerical_ids": ["9979"]},
            "children": [["5.C.1.b.i", "5.C.1.b.ii"]],
        },
        "5.C.1.b.i": {
            "title": "Municipal Solid Waste",
            "alternative_codes": ["10302", "5C1bi", "5 C 1 b i"],
            "info": {"numerical_ids": ["10302"]},
        },
        "5.C.1.b.ii": {
            "title": "Other",
            "alternative_codes": ["9696", "5C1bii", "5 C 1 b ii"],
            "info": {"numerical_ids": ["9696"]},
            "children": [
                [
                    "5.C.1.b.ii.1",
                    "5.C.1.b.ii.2",
                    "5.C.1.b.ii.3",
                    "5.C.1.b.ii.4",
                    "5.C.1.b.ii.5",
                    "5.C.1.b.ii.6",
                ]
            ],
        },
        "5.C.1.b.ii.1": {
            "title": "Industrial Solid Wastes",
            "alternative_codes": ["8158", "5C1bii1", "5 C 1 b ii 1"],
            "info": {"numerical_ids": ["8158"]},
        },
        "5.C.1.b.ii.2": {
            "title": "Hazardous Waste",
            "alternative_codes": ["9250", "5C1bii2", "5 C 1 b ii 2"],
            "info": {"numerical_ids": ["9250"]},
        },
        "5.C.1.b.ii.3": {
            "title": "Clinical Waste",
            "alternative_codes": ["10050", "5C1bii3", "5 C 1 b ii 3"],
            "info": {"numerical_ids": ["10050"]},
        },
        "5.C.1.b.ii.4": {
            "title": "Sewage Sludge",
            "alternative_codes": ["8619", "5C1bii4", "5 C 1 b ii 4"],
            "info": {"numerical_ids": ["8619"]},
        },
        "5.C.1.b.ii.5": {
            "title": "Fossil Liquid Waste",
            "alternative_codes": ["9730", "5C1bii5", "5 C 1 b ii 5"],
            "info": {"numerical_ids": ["9730"]},
        },
        "5.C.1.b.ii.6": {
            "title": "Other",
            "alternative_codes": ["9649", "5C1bii6", "5 C 1 b ii 6"],
            "info": {"numerical_ids": ["9649"]},
        },
        "5.C.2": {
            "title": "Open Burning of Waste",
            "alternative_codes": ["8943", "5C2", "5 C 2"],
            "info": {"numerical_ids": ["8943"]},
            "children": [["5.C.2.a", "5.C.2.b"]],
        },
        "5.C.2.a": {
            "title": "Biogenic",
            "alternative_codes": ["8825", "5C2a", "5 C 2 a"],
            "info": {"numerical_ids": ["8825"]},
            "children": [["5.C.2.a.i", "5.C.2.a.ii"]],
        },
        "5.C.2.a.i": {
            "title": "Municipal Solid Waste",
            "alternative_codes": ["10182", "5C2ai", "5 C 2 a i"],
            "info": {"numerical_ids": ["10182"]},
        },
        "5.C.2.a.ii": {
            "title": "Other",
            "alternative_codes": ["8772", "5C2aii", "5 C 2 a ii"],
            "info": {"numerical_ids": ["8772"]},
        },
        "5.C.2.b": {
            "title": "Non-biogenic",
            "alternative_codes": ["8910", "5C2b", "5 C 2 b"],
            "info": {"numerical_ids": ["8910"]},
            "children": [["5.C.2.b.i", "5.C.2.b.ii"]],
        },
        "5.C.2.b.i": {
            "title": "Municipal Solid Waste",
            "alternative_codes": ["8768", "5C2bi", "5 C 2 b i"],
            "info": {"numerical_ids": ["8768"]},
        },
        "5.C.2.b.ii": {
            "title": "Other",
            "alternative_codes": ["9181", "5C2bii", "5 C 2 b ii"],
            "info": {"numerical_ids": ["9181"]},
        },
        "5.D": {
            "title": "Wastewater Treatment and Discharge",
            "alternative_codes": ["8423", "5D", "5 D"],
            "info": {"numerical_ids": ["8423"]},
            "children": [["5.D.1", "5.D.2", "5.D.3"]],
        },
        "5.D.1": {
            "title": "Domestic Wastewater",
            "alternative_codes": ["10391", "5D1", "5 D 1"],
            "info": {"numerical_ids": ["10391"]},
        },
        "5.D.2": {
            "title": "Industrial Wastewater",
            "alternative_codes": ["9831", "5D2", "5 D 2"],
            "info": {"numerical_ids": ["9831"]},
        },
        "5.D.3": {
            "title": "Other",
            "alternative_codes": ["8153", "5D3", "5 D 3"],
            "info": {"numerical_ids": ["8153"]},
        },
        "5.E": {
            "title": "Other",
            "alternative_codes": ["8284", "5E", "5 E"],
            "info": {"numerical_ids": ["8284"]},
        },
        "6": {
            "title": "Other",
            "alternative_codes": ["6.", "10476", "10485"],
            "info": {"numerical_ids": ["10476", "10485"]},
        },
    },
}