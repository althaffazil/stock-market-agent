COMPETITORS = {
    "Nvidia": [
        "AMD",
        "Intel"
    ],

    "Microsoft": [
        "Google",
        "Amazon"
    ],

    "Apple": [
        "Samsung",
        "Google"
    ],

    "Amazon": [
        "Walmart",
        "Alibaba"
    ],

    "Tesla": [
        "BYD",
        "Ford"
    ],

    "Meta": [
        "TikTok",
        "Snap"
    ]
}


def get_competitors(company: str):
    return COMPETITORS.get(
        company.title(),
        []
    )