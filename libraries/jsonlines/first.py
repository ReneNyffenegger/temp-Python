import sys
import jsonlines

with jsonlines.open('/home/rene/github/Bible-Geocoding-Data/data/ancient.jsonl') as reader:
    for obj in reader:
        print(obj['friendly_id'])
        print(obj['geojson_file'])
        print(len(obj['identifications']))

        if 'verses' in obj:
           print(len(obj['verses']))
           print(' - '.join([ verse['usx'     ] for verse in obj['verses'] ] ))
           print(' - '.join([ verse['osis'    ] for verse in obj['verses'] ] ))
           print(' - '.join([ verse['readable'] for verse in obj['verses'] ] ))
        else:
           print('no verses')
#          sys.exit(1)
           

        print('')


"""
{
  "extra": "{\"associations\":[{\"url_slug\":\"barada-river\",\"thumbnail\":{\"credit_url\":\"https://commons.wikimedia.org/wiki/File:Barada_river.Damascus.jpg\",\"file\":\"m39ac0b.ia3a355.jpg\",\"image_id\":\"ia3a355\",\"description\":\"closeup of the <modern id=\\\"m39ac0b\\\">Barada River</modern>\",\"credit\":\"Arch rim\",\"placeholder\":\"#a5a692,#6c6d5a,#6b8192\"},\"identification_ids\":[[0,0]],\"score\":1000,\"modern_id\":\"m39ac0b\",\"name\":\"Barada River\"}],\"osises\":[\"2Kgs.5.12\"],\"identifications\":[\"Barada River\"]}",
  "friendly_id": "Abana",
  "geojson_file": "aea17b7.geojson",
  "geometry_credit": "osm",
  "id": "aea17b7",
  "identifications": [
    {
      "class": "natural",
      "description": "<modern id=\"m39ac0b\">Barada River</modern>",
      "id": "m39ac0b",
      "id_source": "modern",
      "media": {
        "thumbnail": {
          "credit": "Arch rim",
          "credit_url": "https://commons.wikimedia.org/wiki/File:Barada_river.Damascus.jpg",
          "description": "closeup of the <modern id=\"m39ac0b\">Barada River</modern>",
          "file": "m39ac0b.ia3a355.jpg",
          "image_id": "ia3a355",
          "placeholder": "#a5a692,#6c6d5a,#6b8192"
        }
      },
      "resolutions": [
        {
          "ancient_geometry": "path",
          "best_path_score": 500,
          "class": "natural",
          "description": "<modern id=\"m39ac0b\">Barada River</modern>",
          "geojson_roles": {
            "precise": {
              "description": "Barada River",
              "geometry_credit": "osm",
              "id": "g3513e7.geometry"
            },
            "representative_point": {
              "description": "representative point for the <modern id=\"m39ac0b\">Barada River</modern>",
              "id": "m39ac0b.point"
            },
            "simplified_precise": {
              "description": "Barada River",
              "geometry_credit": "osm",
              "id": "g3513e7.simplified"
            }
          },
          "land_or_water": "water",
          "lonlat": "36.305000,33.513542",
          "lonlat_type": "representative point",
          "modern_basis_id": "m39ac0b",
          "paths": [
            [
              {
                "ancient_id": "aea17b7",
                "identification_i": 0
              },
              {
                "modern_id": "m39ac0b"
              }
            ]
          ],
          "precise_geometry_id": "g3513e7",
          "type": "river"
        }
      ],
      "score": {
        "time_best_fits": [],
        "time_intercept": 1000,
        "time_r_squared": 0,
        "time_slope": 0,
        "time_total": 1000,
        "time_values": [],
        "vote_average": 500,
        "vote_count": 1,
        "vote_total": 500
      },
      "types": [
        "river"
      ]
    }
  ],
  "kml_file": "aea17b7.kml",
  "linked_data": {
    "s294e03": {
      "id": "Abana"
    },
    "s3b25cf": {
      "id": "Abana@2Ki.5.12"
    },
    "s7cc8b2": {
      "id": "Q765106"
    },
    "s7f5356": {
      "name": "Abana",
      "review": "automatic",
      "url": "https://biblia.com/factbook/Abana"
    },
    "s85af0b": {
      "biblemapper_locids_parameters": [
        1015
      ]
    }
  },
  "media": {
    "thumbnail": {
      "credit": "Arch rim",
      "credit_url": "https://commons.wikimedia.org/wiki/File:Barada_river.Damascus.jpg",
      "description": "closeup of the <modern id=\"m39ac0b\">Barada River</modern>",
      "file": "m39ac0b.ia3a355.jpg",
      "image_id": "ia3a355",
      "placeholder": "#a5a692,#6c6d5a,#6b8192"
    }
  },
  "modern_associations": {
    "m39ac0b": {
      "identification_ids": [
        [
          0,
          0
        ]
      ],
      "name": "Barada River",
      "score": 1000,
      "url_slug": "barada-river"
    }
  },
  "preceding_article": "the",
  "translation_name_counts": {
    "Abana": 8,
    "Abanah": 2
  },
  "types": [
    "river"
  ],
  "url_slug": "abana",
  "verses": [
    {
      "instance_types": {
        "name": 10
      },
      "osis": "2Kgs.5.12",
      "readable": "2 Kgs 5:12",
      "sort": "12005012",
      "translations": [
        "csb",
        "esv",
        "kjv",
        "leb",
        "nasb",
        "net",
        "niv",
        "nkjv",
        "nlt",
        "nrsv"
      ],
      "usx": "2KI 5:12"
    }
  ]
}
"""
