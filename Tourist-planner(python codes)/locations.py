graph = {
    "Charminar": {
        "Salar Jung Museum": 3,
        "Birla Mandir": 6
    },
    "Salar Jung Museum": {
        "Charminar": 3,
        "Golconda Fort": 10,
        "Hussain Sagar": 5
    },
    "Birla Mandir": {
        "Charminar": 6,
        "Hussain Sagar": 4
    },
    "Hussain Sagar": {
        "Birla Mandir": 4,
        "Salar Jung Museum": 5,
        "Golconda Fort": 12
    },
    "Golconda Fort": {
        "Salar Jung Museum": 10,
        "Hussain Sagar": 12
    }
}

place_type = {
    "Charminar": "Historical",
    "Salar Jung Museum": "Museum",
    "Birla Mandir": "Temple",
    "Hussain Sagar": "Nature",
    "Golconda Fort": "Historical"
}