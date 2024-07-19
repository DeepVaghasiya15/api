from pymongo import MongoClient
from config import MONGO_URI

properties = [
    {
        "index": 0,
        "imageAssetPath": "assets/images/PropertyCard/land1.jpg",
        "type": "Agriculture Land",
        "title": "My Land",
        "address": "15875 FM 529, Houston, TX 77084, United States",
        "builtUpArea": "217,800 sqft",
        "lotSize": "10 Acres",
        "auctionStatus": "Auction Coming Soon",
        "currentBid": "",
        "category": "Land",
        "id": "PROP240611280",
        "imagePaths": [
            "assets/images/MyLand/land.jpg",
            "assets/images/MyLand/land2.webp",
            "assets/images/MyLand/land3.jpg",
        ],
        "listedBy": "Owner",
        "startingBid": "$500,000",
        "lotSize2": "5",
        "propertyType": "Agricultural Land",
        "BuilderName": "NA",
        "totalFloor": "NA",
        "propertyFloor": "NA",
        "PossesionTime": "NA",
        "AcceptBuyersTitle": "Yes",
        "PropertyBuiltYear": "NA",
        "ArchitextName": "NA",
        "BuiltupArea": "NA",
        "CarParking": "NA",
        "PropertyTaxID": "551111151",
        "AssetType": "Land",
        "Rentable": "NA",
        "InteriorAccess": "NA",
        "Ownership": "Community Property",
        "latitude": "29.8775805",
        "longitude": "-95.6514305",
        "description": "Agribusiness covers the production, processing, and distribution of farm-based goods.",
        "title4FC": "Land Inspection",
        "subtitleFC": "Winner will not be charged fee for this property.",
        "subtitle2FC": "As per the terms of the Listing Agreement, the Seller will provide a commission/fee to any appropriately registered Broker whose client not only emerges as the successful Buyer at the Auction but also completes the purchase of the Property.",
        "subtitle3FC": "Indicates that the seller is willing to share 5 % of the closing costs with the buyer.",
        "subtitle4FC": "Please contact +1 832 679 2176 for details or Click Here to request a tour.",
        "trailingFC": "Not Applicable",
        "trailing2FC": "5% Available",
        "trailing3FC": "5% Available",
        "trailing4FC": "Yes",
    },
    {
        "index": 1,
        "imageAssetPath": "assets/images/PropertyCard/perfectPlaza.webp",
        "type": "Commercial Plaza",
        "title": "Perfect Plaza",
        "address": "New York St, New York, NY 10001, United States",
        "builtUpArea": "25,000 sqft",
        "lotSize": "0.5 Acres",
        "auctionStatus": "Auction Coming Soon",
        "currentBid": "",
        "category": "Commercial",
        "id": "PROP240611285",
        "imagePaths": [
            "assets/images/PerfectPlaza/perfectPlaza.webp",
        ],
        "listedBy": "Owner",
        "startingBid": "\$500,000",
        "lotSize2": "3",
        "propertyType": "Commercial Plaza",
        "BuilderName": "Sakar",
        "totalFloor": "15",
        "propertyFloor": "12",
        "PossesionTime": "4",
        "AcceptBuyersTitle": "Yes",
        "PropertyBuiltYear": "1996",
        "ArchitextName": "Mohan",
        "BuiltupArea": "25,000",
        "CarParking": "Reserved",
        "PropertyTaxID": "346",
        "AssetType": "Commercial",
        "Rentable": "12",
        "InteriorAccess": "Yes",
        "Ownership": "Sole Ownership",
        "latitude": "40.7858896",
        "longitude": "-74.0112249",
        "description": "Big Plaza",
        "title4FC": "Interior Access",
        "subtitleFC": "Winner will not be charged fee for this property.",
        "subtitle2FC": "As per the terms of the Listing Agreement, the Seller will provide a commission/fee to any appropriately registered Broker whose client not only emerges as the successful Buyer at the Auction but also completes the purchase of the Property.",
        "subtitle3FC": "Closing cost will not share with buyer.",
        "subtitle4FC": "Please contact +1 832 679 2176 for details or Click Here to request a tour.",
        "trailingFC": "Not Applicable",
        "trailing2FC": "2% Available",
        "trailing3FC": "Not Offered",
        "trailing4FC": "Yes",
    },
    {
        "index": 2,
        "imageAssetPath": "assets/images/PropertyCard/myPlaza.jpg",
        "type": "Commercial Plaza",
        "title": "My Plaza",
        "address": "Florida A1A, Miami, FL 33125, United States",
        "builtUpArea": "10,000 sqft",
        "lotSize": "0.2 Acres",
        "auctionStatus": "Auction Coming Soon",
        "currentBid": "",
        "category": "Commercial",
        "id": "PROP240611281",
        "imagePaths": [
            "assets/images/MyPlaza/myPlaza.jpg",
        ],
        "listedBy": "Owner",
        "startingBid": "\$25,000",
        "lotSize2": "2",
        "propertyType": "Commercial Plaza",
        "BuilderName": "Agam Enterprises",
        "totalFloor": "20",
        "propertyFloor": "1",
        "PossesionTime": "60",
        "AcceptBuyersTitle": "No",
        "PropertyBuiltYear": "2015",
        "ArchitextName": "Agham Rao",
        "BuiltupArea": "10,000",
        "CarParking": "Reserved (200)",
        "PropertyTaxID": "316546661",
        "AssetType": "Commercial",
        "Rentable": "12",
        "InteriorAccess": "Yes",
        "Ownership": "Joint Tenancy",
        "latitude": "27.8130567",
        "longitude": "-80.427826",
        "description": "you can use for business activities.",
        "title4FC": "Interior Access",
        "subtitleFC": "Winner will not be charged fee for this property.",
        "subtitle2FC": "As per the terms of the Listing Agreement, the Seller will provide a commission/fee to any appropriately registered Broker whose client not only emerges as the successful Buyer at the Auction but also completes the purchase of the Property.",
        "subtitle3FC": "Indicates that the seller is willing to share 2% of the closing costs with the buyer.",
        "subtitle4FC": "Please contact +1 832 679 2176 for details or Click Here to request a tour.",
        "trailingFC": "Not Applicable",
        "trailing2FC": "3% Available",
        "trailing3FC": "2% Available",
        "trailing4FC": "Yes",
    },
    {
        "index": 3,
        "imageAssetPath": "assets/images/PropertyCard/megma.webp",
        "type": "Hotel",
        "title": "Megma",
        "address": "Indira Gandhi Int'l T3 Rd, Delhi, DL 110037, India",
        "builtUpArea": "150,000 sqft",
        "lotSize": "3.44 Acres",
        "auctionStatus": "Auction Coming Soon",
        "currentBid": "",
        "category": "Commercial",
        "id": "PROP240703311",
        "imagePaths": [
            "assets/images/Megma/megma.webp",
        ],
        "listedBy": "Owner",
        "startingBid": "\₹15,00,000",
        "lotSize2": "3.44",
        "propertyType": "Hotel",
        "BuilderName": "NA",
        "totalFloor": "NA",
        "propertyFloor": "NA",
        "PossesionTime": "NA",
        "AcceptBuyersTitle": "No",
        "PropertyBuiltYear": "2018",
        "ArchitextName": "NA",
        "BuiltupArea": "150,000",
        "CarParking": "Available",
        "PropertyTaxID": "NA",
        "AssetType": "Commercial",
        "Rentable": "NA",
        "InteriorAccess": "No",
        "Ownership": "Sole Ownership",
        "latitude": "28.5544158",
        "longitude": "77.0945783",
        "description": "Indulge your palate at the on-site gourmet restaurant, where culinary mastery meets sensory delight. Elevate your spirits at the rooftop bar, offering panoramic city views and handcrafted libations. Rejuvenate your body and mind at the state-of-the-art fitness center and tranquil spa oasis. Host memorable events and conferences in sophisticated venues designed to inspire and impress. \n\nLocation Advantage:\n\n Ideally situated in the heart of a dynamic cityscape, the hotel enjoys privileged proximity to renowned attractions, entertainment venues, and corporate hubs. Whether for business or leisure, guests are seamlessly connected to the pulse of urban life, ensuring a memorable and convenient stay.",
        "title4FC": "Interior Access",
        "subtitleFC": "Winner will not be charged fee for this property.",
        "subtitle2FC": "Broker Co-op is not Offered.",
        "subtitle3FC": "Closing cost will not share with buyer.",
        "subtitle4FC": "Please contact +1 832 679 2176 for details or Click Here to request a tour.",
        "trailingFC": "Not Applicable",
        "trailing2FC": "Not Offered",
        "trailing3FC": "Not Offered",
        "trailing4FC": "No",
    },
    {
        "index": 4,
        "imageAssetPath": "assets/images/PropertyCard/LuxuriousBoutiqueRetreat.jpg",
        "type": "Condo",
        "title": "Luxurious Boutique Retreat",
        "address": "Noida-Greater Noida Expy, Noida, UP, India",
        "builtUpArea": "5000 sqft",
        "lotSize": "0.1 Acre",
        "auctionStatus": "Auction is live",
        "currentBid": "₹ 10,00,01,35,00,000",
        "category": "Residential",
        "id": "PROP240611285",
        "imagePaths": [
            "assets/images/LuxuriousBoutiqueRetreat/LuxuriousBoutiqueRetreat.jpg",
        ],
        "listedBy": "Owner",
        "startingBid": "\₹60,00,000",
        "lotSize2": "1.50",
        "propertyType": "Condo",
        "BuilderName": "NA",
        "totalFloor": "NA",
        "propertyFloor": "NA",
        "PossesionTime": "NA",
        "AcceptBuyersTitle": "No",
        "PropertyBuiltYear": "2015",
        "ArchitextName": "NA",
        "BuiltupArea": "5,000",
        "CarParking": "Available",
        "PropertyTaxID": "NA",
        "AssetType": "Residential",
        "Rentable": "NA",
        "InteriorAccess": "No",
        "Ownership": "Sole Ownership",
        "latitude": "28.5003977",
        "longitude": "77.4045406",
        "description": "Hotel Highlights \n\n- Step into a realm of refined opulence, where every detail is meticulously curated to exceed the expectations of the discerning traveler. \n\n- From the exquisite architecture to the personalized service, this boutique hotel sets the standard for luxury accommodations and bespoke experiences.",
        "title4FC": "Interior Access",
        "subtitleFC": "Winner will not be charged fee for this property.",
        "subtitle2FC": "Broker Co-op is not Offered.",
        "subtitle3FC": "Closing cost will not share with buyer.",
        "subtitle4FC": "Please contact +1 832 679 2176 for details or Click Here to request a tour.",
        "trailingFC": "Not Applicable",
        "trailing2FC": "Not Offered",
        "trailing3FC": "Not Offered",
        "trailing4FC": "No",
    },
    {
        "index": 5,
        "imageAssetPath": "assets/images/PropertyCard/exquisiteEstate.jpg",
        "type": "Single Family",
        "title": "Exquisite Estate",
        "address": "Kochi - Salem Hwy, Ernakulam, KL, India",
        "builtUpArea": "2500 sqft",
        "lotSize": "0.05 Acre",
        "auctionStatus": "Auction is live",
        "currentBid": "₹ 2,00,000",
        "category": "Residential",
        "id": "PROP240611256",
        "imagePaths": [
            "assets/images/ExquisiteEstate/exquisiteEstate.jpg",
        ],
        "listedBy": "Owner",
        "startingBid": "\₹1,00,000",
        "lotSize2": "0.5",
        "propertyType": "Commercial Plaza",
        "BuilderName": "NA",
        "totalFloor": "NA",
        "propertyFloor": "NA",
        "PossesionTime": "NA",
        "AcceptBuyersTitle": "No",
        "PropertyBuiltYear": "2020",
        "ArchitextName": "NA",
        "BuiltupArea": "2,500",
        "CarParking": "Available",
        "PropertyTaxID": "NA",
        "AssetType": "Residential",
        "Rentable": "NA",
        "InteriorAccess": "Yes",
        "Ownership": "Joint Tenancy",
        "latitude": "10.3471077",
        "longitude": "76.3186012",
        "description": "Interior Features: \n\nAs you enter, you're greeted by a grand foyer, where gleaming hardwood floors lead you through the open-concept layout. The living room, adorned with a statement fireplace, invites cozy evenings, while the adjacent dining area is perfect for hosting gatherings.",
        "title4FC": "Interior Access",
        "subtitleFC": "Winner will not be charged fee for this property.",
        "subtitle2FC": "Broker Co-op is not Offered.",
        "subtitle3FC": "Closing cost will not share with buyer.",
        "subtitle4FC": "Please contact +1 832 679 2176 for details or Click Here to request a tour.",
        "trailingFC": "Not Applicable",
        "trailing2FC": "Not Offered",
        "trailing3FC": "Not Offered",
        "trailing4FC": "Yes",
    },
    {
        "index": 6,
        "imageAssetPath": "assets/images/PropertyCard/sunshinevilla.webp",
        "type": "Single Family",
        "title": "Sunshine Villa",
        "address": "2150 Town Square Place, Sugar Land, TX 77478, United States",
        "builtUpArea": "3500 sqft",
        "lotSize": "0.08 Acre",
        "auctionStatus": "Auction Coming Soon",
        "currentBid": "",
        "category": "Residential",
        "id": "PROP240611283",
        "imagePaths": [
            "assets/images/SunshineVilla/sunshinevilla.webp",
        ],
        "listedBy": "Owner",
        "startingBid": "\$50,000",
        "lotSize2": "2.10",
        "propertyType": "Single Family",
        "BuilderName": "K.SJ Associates",
        "totalFloor": "2",
        "propertyFloor": "1",
        "PossesionTime": "NA",
        "AcceptBuyersTitle": "Yes",
        "PropertyBuiltYear": "2014",
        "ArchitextName": "Keshavraj",
        "BuiltupArea": "3,500",
        "CarParking": "Reserved",
        "PropertyTaxID": "NA",
        "AssetType": "Residential",
        "Rentable": "NA",
        "InteriorAccess": "Yes",
        "Ownership": "Sole Ownership",
        "latitude": "29.596039",
        "longitude": "-95.6256584",
        "description": "Single Family Villa",
        "title4FC": "Interior Access",
        "subtitleFC": "Winner will not be charged fee for this property.",
        "subtitle2FC": "As per the terms of the Listing Agreement, the Seller will provide a commission/fee to any appropriately registered Broker whose client not only emerges as the successful Buyer at the Auction but also completes the purchase of the Property.",
        "subtitle3FC": "Closing cost will not share with buyer.",
        "subtitle4FC": "Please contact +1 832 679 2176 for details or Click Here to request a tour.",
        "trailingFC": "Not Applicable",
        "trailing2FC": "5% Available",
        "trailing3FC": "Not Offered",
        "trailing4FC": "Yes",
    },
    {
        "index": 7,
        "imageAssetPath": "assets/images/PropertyCard/home.jpg",
        "type": "Single Family",
        "title": "House",
        "address": "3737Branford Pl, Sugar Land, sugar land, Texas 77479, United States",
        "builtUpArea": "4000 sqft",
        "lotSize": "0.09 Acre",
        "auctionStatus": "Auction Coming Soon",
        "currentBid": "",
        "category": "Residential",
        "id": "PROP240611284",
        "imagePaths": [
            "assets/images/House/home.jpg",
        ],
        "listedBy": "Owner",
        "startingBid": "\$100,000",
        "lotSize2": "3",
        "propertyType": "Single Family",
        "BuilderName": "Atif",
        "totalFloor": "2",
        "propertyFloor": "1",
        "PossesionTime": "4",
        "AcceptBuyersTitle": "Yes",
        "PropertyBuiltYear": "1995",
        "ArchitextName": "Trusa",
        "BuiltupArea": "4,000",
        "CarParking": "Common",
        "PropertyTaxID": "3756",
        "AssetType": "Residential",
        "Rentable": "4000",
        "InteriorAccess": "Yes",
        "Ownership": "Owned By Entity",
        "latitude": "29.5409594",
        "longitude": "-95.6054144",
        "description": "Good property , not damaged",
        "title4FC": "Interior Access",
        "subtitleFC": "Winner will not be charged fee for this property.",
        "subtitle2FC": "Broker Co-op is not Offered.",
        "subtitle3FC": "Closing cost will not share with buyer.",
        "subtitle4FC": "Please contact +1 832 679 2176 for details or Click Here to request a tour.",
        "trailingFC": "Not Applicable",
        "trailing2FC": "Not Offered",
        "trailing3FC": "Not Offered",
        "trailing4FC": "Yes",
    },
    {
        "index": 8,
        "imageAssetPath": "assets/images/PropertyCard/GasStation.webp",
        "type": "Single Family",
        "title": "Gas Station",
        "address": "3737Branford Pl, Sugar Land, sugar land, Texas 77479, United States",
        "builtUpArea": "4000 sqft",
        "lotSize": "0.09 Acre",
        "auctionStatus": "Auction Coming Soon",
        "currentBid": "",
        "category": "Residential",
        "id": "PROP240611284",
        "imagePaths": [
            "assets/images/House/home.jpg",
        ],
        "listedBy": "Owner",
        "startingBid": "\$100,000",
        "lotSize2": "3",
        "propertyType": "Gas Station",
        "BuilderName": "Atif",
        "totalFloor": "2",
        "propertyFloor": "1",
        "PossesionTime": "50",
        "AcceptBuyersTitle": "No",
        "PropertyBuiltYear": "2000",
        "ArchitextName": "Trusa",
        "BuiltupArea": "5,000",
        "CarParking": "Common",
        "PropertyTaxID": "3756",
        "AssetType": "Residential",
        "Rentable": "4000",
        "InteriorAccess": "No",
        "Ownership": "Community Property",
        "latitude": "29.5409594",
        "longitude": "-95.6054144",
        "description": "Good property , not damaged",
        "title4FC": "Interior Access",
        "subtitleFC": "Winner will not be charged fee for this property.",
        "subtitle2FC": "Broker Co-op is not Offered.",
        "subtitle3FC": "Closing cost will not share with buyer.",
        "subtitle4FC": "Please contact +1 832 679 2176 for details or Click Here to request a tour.",
        "trailingFC": "Not Applicable",
        "trailing2FC": "Not Offered",
        "trailing3FC": "Not Offered",
        "trailing4FC": "Yes",
    },
]

client = MongoClient(MONGO_URI)
db = client.get_database()
property_collection = db.properties
property_collection.insert_many(properties)
print("Data inserted successfully.")
client.close()
