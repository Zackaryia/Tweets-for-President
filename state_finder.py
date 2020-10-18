states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",  "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina","North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

state_2_letter = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"] 

state_data = {
	"AL": {"sentamint": 0, "mentions": 0},
	"AK": {"sentamint": 0, "mentions": 0},
	"AZ": {"sentamint": 0, "mentions": 0},
	"AR": {"sentamint": 0, "mentions": 0},
	"CA": {"sentamint": 0, "mentions": 0},
	"CO": {"sentamint": 0, "mentions": 0},
	"CT": {"sentamint": 0, "mentions": 0},
	"DE": {"sentamint": 0, "mentions": 0},
	"FL": {"sentamint": 0, "mentions": 0},
	"GA": {"sentamint": 0, "mentions": 0},
	"HI": {"sentamint": 0, "mentions": 0},
	"ID": {"sentamint": 0, "mentions": 0},
	"IL": {"sentamint": 0, "mentions": 0},
	"IN": {"sentamint": 0, "mentions": 0},
	"IA": {"sentamint": 0, "mentions": 0},
	"KS": {"sentamint": 0, "mentions": 0},
	"KY": {"sentamint": 0, "mentions": 0},
	"LA": {"sentamint": 0, "mentions": 0},
	"ME": {"sentamint": 0, "mentions": 0},
	"MD": {"sentamint": 0, "mentions": 0},
	"MA": {"sentamint": 0, "mentions": 0},
	"MI": {"sentamint": 0, "mentions": 0},
	"MN": {"sentamint": 0, "mentions": 0},
	"MS": {"sentamint": 0, "mentions": 0},
	"MO": {"sentamint": 0, "mentions": 0},
	"MT": {"sentamint": 0, "mentions": 0},
	"NE": {"sentamint": 0, "mentions": 0},
	"NV": {"sentamint": 0, "mentions": 0},
	"NH": {"sentamint": 0, "mentions": 0},
	"NJ": {"sentamint": 0, "mentions": 0},
	"NM": {"sentamint": 0, "mentions": 0},
	"NY": {"sentamint": 0, "mentions": 0},
	"NC": {"sentamint": 0, "mentions": 0},
	"ND": {"sentamint": 0, "mentions": 0},
	"OH": {"sentamint": 0, "mentions": 0},
	"OK": {"sentamint": 0, "mentions": 0},
	"OR": {"sentamint": 0, "mentions": 0},
	"PA": {"sentamint": 0, "mentions": 0},
	"RI": {"sentamint": 0, "mentions": 0},
	"SC": {"sentamint": 0, "mentions": 0},
	"SD": {"sentamint": 0, "mentions": 0},
	"TN": {"sentamint": 0, "mentions": 0},
	"TX": {"sentamint": 0, "mentions": 0},
	"UT": {"sentamint": 0, "mentions": 0},
	"VT": {"sentamint": 0, "mentions": 0},
	"VA": {"sentamint": 0, "mentions": 0},
	"WA": {"sentamint": 0, "mentions": 0},
	"WV": {"sentamint": 0, "mentions": 0},
	"WI": {"sentamint": 0, "mentions": 0},
	"WY": {"sentamint": 0, "mentions": 0}
}

def statefinder(place):
	if place == None:
		return None
	if "," in place:
		place_split = place.split(',')
		if place_split[1].strip() == "USA":
			if place_split[0].strip() in states:
				return state_2_letter[states.index(place_split[0].strip())]
		elif place_split[1].strip() in state_2_letter:
			return place_split[1].strip()
		elif place_split[1].strip() in states:
			return state_2_letter[states.index(place_split[1].strip())]

	return None

if __name__ == "__main__":
	

	places = [
		"Mountainous Nevada",
		"Miami, FL",
		"Miami, FL",
		"South Carolina, USA",
		"Europa, Jupiter",
		"Moreno Valley, CA",
		"California, USA",
		"Paraguaipoa, Venezuela",
		"South Bay Area, CA/So Florida",
		"NY",
		"CA",
		"St Joseph, MI",
		"Colorado, USA",
		"United States",
		"Frisco, TX",
		"Los Altos Hills, CA",
		"São Paulo, Brasil",
		"Nj",
		"Ponca City, Oklahoma",
		"N. Carolina USA",
		"U.K.",
		"Everywhere",
		"Texas & I don't do TrueTwit😜",
		"@URAnonymous1 (backup acct)"
	]

	for place in places:
		print(place)
		print(statefinder(place))
