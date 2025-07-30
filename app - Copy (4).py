import streamlit as st
import random
import base64
from PIL import Image
import io
import requests

# Country data with flags and facts
COUNTRIES_DATA = {
    "Afghanistan": {
        "flag": "🇦🇫",
        "fact": "Afghanistan is known as the 'Graveyard of Empires' due to its history of resisting foreign invasions.",
        "hint": "This country's flag has black, red, and green stripes with a central emblem."
    },
    "Albania": {
        "flag": "🇦🇱",
        "fact": "Albania has the world's largest number of bunkers per capita, built during the communist era.",
        "hint": "This flag features a black double-headed eagle on a red background."
    },
    "Algeria": {
        "flag": "🇩🇿",
        "fact": "Algeria is the largest country in Africa by land area."
    },
    "Andorra": {
        "flag": "🇦🇩",
        "fact": "Andorra is one of the smallest countries in Europe, located in the Pyrenees mountains."
    },
    "Angola": {
        "flag": "🇦🇴",
        "fact": "Angola is one of the world's largest producers of diamonds."
    },
    "Antigua and Barbuda": {
        "flag": "🇦🇬",
        "fact": "Antigua and Barbuda has 365 beaches, one for each day of the year."
    },
    "Argentina": {
        "flag": "🇦🇷",
        "fact": "Argentina is the world's largest Spanish-speaking country by land area."
    },
    "Armenia": {
        "flag": "🇦🇲",
        "fact": "Armenia was the first country to officially adopt Christianity as its state religion in 301 AD."
    },
    "Australia": {
        "flag": "🇦🇺",
        "fact": "Australia is home to the world's largest coral reef system, the Great Barrier Reef."
    },
    "Austria": {
        "flag": "🇦🇹",
        "fact": "Austria is the birthplace of many famous composers including Mozart, Beethoven, and Strauss."
    },
    "Azerbaijan": {
        "flag": "🇦🇿",
        "fact": "Azerbaijan is known as the 'Land of Fire' due to its natural gas reserves."
    },
    "Bahamas": {
        "flag": "🇧🇸",
        "fact": "The Bahamas consists of over 700 islands, cays, and islets."
    },
    "Bahrain": {
        "flag": "🇧🇭",
        "fact": "Bahrain is an archipelago of 33 islands in the Persian Gulf."
    },
    "Bangladesh": {
        "flag": "🇧🇩",
        "fact": "Bangladesh has the world's largest river delta, formed by the Ganges, Brahmaputra, and Meghna rivers."
    },
    "Barbados": {
        "flag": "🇧🇧",
        "fact": "Barbados is known as the 'Land of the Flying Fish' and has the third oldest parliament in the world."
    },
    "Belarus": {
        "flag": "🇧🇾",
        "fact": "Belarus is known as the 'Lungs of Europe' due to its extensive forests."
    },
    "Belgium": {
        "flag": "🇧🇪",
        "fact": "Belgium produces over 800 varieties of beer and is famous for its chocolate."
    },
    "Belize": {
        "flag": "🇧🇿",
        "fact": "Belize has the world's second-largest barrier reef system."
    },
    "Benin": {
        "flag": "🇧🇯",
        "fact": "Benin was once the center of the powerful Kingdom of Dahomey."
    },
    "Bhutan": {
        "flag": "🇧🇹",
        "fact": "Bhutan is the only country in the world that measures Gross National Happiness instead of GDP."
    },
    "Bolivia": {
        "flag": "🇧🇴",
        "fact": "Bolivia has the world's highest navigable lake, Lake Titicaca."
    },
    "Bosnia and Herzegovina": {
        "flag": "🇧🇦",
        "fact": "Bosnia and Herzegovina has one of the most diverse religious populations in Europe."
    },
    "Botswana": {
        "flag": "🇧🇼",
        "fact": "Botswana is one of the world's largest producers of diamonds and has the world's largest elephant population."
    },
    "Brazil": {
        "flag": "🇧🇷",
        "fact": "Brazil is home to the Amazon Rainforest, which produces 20% of the world's oxygen."
    },
    "Brunei": {
        "flag": "🇧🇳",
        "fact": "Brunei has one of the highest standards of living in Asia due to its oil and gas wealth."
    },
    "Bulgaria": {
        "flag": "🇧🇬",
        "fact": "Bulgaria is the world's largest producer of rose oil, used in perfumes."
    },
    "Burkina Faso": {
        "flag": "🇧🇫",
        "fact": "Burkina Faso means 'Land of Honest People' in the local language."
    },
    "Burundi": {
        "flag": "🇧🇮",
        "fact": "Burundi is one of the poorest countries in the world but has a rich cultural heritage."
    },
    "Cambodia": {
        "flag": "🇰🇭",
        "fact": "Cambodia is home to Angkor Wat, the largest religious monument in the world."
    },
    "Cameroon": {
        "flag": "🇨🇲",
        "fact": "Cameroon is known as 'Africa in Miniature' due to its diverse geography and culture."
    },
    "Canada": {
        "flag": "🇨🇦",
        "fact": "Canada has the world's longest coastline, stretching over 202,080 kilometers."
    },
    "Cape Verde": {
        "flag": "🇨🇻",
        "fact": "Cape Verde is an archipelago of 10 volcanic islands off the coast of West Africa."
    },
    "Central African Republic": {
        "flag": "🇨🇫",
        "fact": "The Central African Republic is rich in natural resources including diamonds, gold, and uranium."
    },
    "Chad": {
        "flag": "🇹🇩",
        "fact": "Chad is named after Lake Chad, which was once one of the largest lakes in Africa."
    },
    "Chile": {
        "flag": "🇨🇱",
        "fact": "Chile is the world's longest country from north to south, stretching over 4,300 km."
    },
    "China": {
        "flag": "🇨🇳",
        "fact": "China is home to the Great Wall, which is over 13,000 miles long."
    },
    "Colombia": {
        "flag": "🇨🇴",
        "fact": "Colombia is the world's largest producer of emeralds and second-largest producer of coffee."
    },
    "Comoros": {
        "flag": "🇰🇲",
        "fact": "Comoros is an archipelago of four islands in the Indian Ocean."
    },
    "Congo": {
        "flag": "🇨🇬",
        "fact": "The Republic of Congo is home to the world's second-largest rainforest."
    },
    "Costa Rica": {
        "flag": "🇨🇷",
        "fact": "Costa Rica has no army and is known for its commitment to environmental protection."
    },
    "Croatia": {
        "flag": "🇭🇷",
        "fact": "Croatia has over 1,000 islands along its Adriatic coast."
    },
    "Cuba": {
        "flag": "🇨🇺",
        "fact": "Cuba has one of the world's best healthcare systems and highest doctor-to-patient ratios."
    },
    "Cyprus": {
        "flag": "🇨🇾",
        "fact": "Cyprus is the birthplace of Aphrodite, the Greek goddess of love and beauty."
    },
    "Czech Republic": {
        "flag": "🇨🇿",
        "fact": "The Czech Republic has the highest beer consumption per capita in the world."
    },
    "Denmark": {
        "flag": "🇩🇰",
        "fact": "Denmark is home to the world's oldest monarchy, dating back over 1,000 years."
    },
    "Djibouti": {
        "flag": "🇩🇯",
        "fact": "Djibouti is located at the strategic entrance to the Red Sea."
    },
    "Dominica": {
        "flag": "🇩🇲",
        "fact": "Dominica is known as the 'Nature Island' due to its lush rainforests and natural hot springs."
    },
    "Dominican Republic": {
        "flag": "🇩🇴",
        "fact": "The Dominican Republic shares the island of Hispaniola with Haiti."
    },
    "East Timor": {
        "flag": "🇹🇱",
        "fact": "East Timor is one of the youngest countries in the world, gaining independence in 2002."
    },
    "Ecuador": {
        "flag": "🇪🇨",
        "fact": "Ecuador is home to the Galapagos Islands, which inspired Charles Darwin's theory of evolution."
    },
    "Egypt": {
        "flag": "🇪🇬",
        "fact": "Egypt is home to the Great Pyramid of Giza, one of the Seven Wonders of the Ancient World."
    },
    "El Salvador": {
        "flag": "🇸🇻",
        "fact": "El Salvador is the smallest and most densely populated country in Central America."
    },
    "Equatorial Guinea": {
        "flag": "🇬🇶",
        "fact": "Equatorial Guinea is the only African country where Spanish is an official language."
    },
    "Eritrea": {
        "flag": "🇪🇷",
        "fact": "Eritrea has a coastline along the Red Sea and is known for its ancient port cities."
    },
    "Estonia": {
        "flag": "🇪🇪",
        "fact": "Estonia is one of the most digitally advanced countries in the world."
    },
    "Eswatini": {
        "flag": "🇸🇿",
        "fact": "Eswatini (formerly Swaziland) is Africa's last absolute monarchy."
    },
    "Ethiopia": {
        "flag": "🇪🇹",
        "fact": "Ethiopia is the only African country that was never colonized by Europeans."
    },
    "Fiji": {
        "flag": "🇫🇯",
        "fact": "Fiji consists of over 300 islands and is known for its pristine beaches and coral reefs."
    },
    "Finland": {
        "flag": "🇫🇮",
        "fact": "Finland is known as the 'Land of a Thousand Lakes' and has the world's best education system."
    },
    "France": {
        "flag": "🇫🇷",
        "fact": "France is the world's most visited country and home to the Eiffel Tower."
    },
    "Gabon": {
        "flag": "🇬🇦",
        "fact": "Gabon has one of the highest forest coverages in the world, with 85% of its land covered in forests."
    },
    "Gambia": {
        "flag": "🇬🇲",
        "fact": "The Gambia is the smallest country in mainland Africa."
    },
    "Georgia": {
        "flag": "🇬🇪",
        "fact": "Georgia is considered the birthplace of wine, with evidence of winemaking dating back 8,000 years."
    },
    "Germany": {
        "flag": "🇩🇪",
        "fact": "Germany is home to the world's largest beer festival, Oktoberfest."
    },
    "Ghana": {
        "flag": "🇬🇭",
        "fact": "Ghana was the first African country to gain independence from colonial rule in 1957."
    },
    "Greece": {
        "flag": "🇬🇷",
        "fact": "Greece is the birthplace of democracy, philosophy, and the Olympic Games."
    },
    "Grenada": {
        "flag": "🇬🇩",
        "fact": "Grenada is known as the 'Spice Isle' and is the world's second-largest producer of nutmeg."
    },
    "Guatemala": {
        "flag": "🇬🇹",
        "fact": "Guatemala is home to the ancient Mayan city of Tikal and has the largest population in Central America."
    },
    "Guinea": {
        "flag": "🇬🇳",
        "fact": "Guinea has the world's largest reserves of bauxite, used to make aluminum."
    },
    "Guinea-Bissau": {
        "flag": "🇬🇼",
        "fact": "Guinea-Bissau is one of the poorest countries in the world but has rich biodiversity."
    },
    "Guyana": {
        "flag": "🇬🇾",
        "fact": "Guyana is the only English-speaking country in South America."
    },
    "Haiti": {
        "flag": "🇭🇹",
        "fact": "Haiti was the first independent nation in Latin America and the Caribbean."
    },
    "Honduras": {
        "flag": "🇭🇳",
        "fact": "Honduras is home to the ancient Mayan ruins of Copán."
    },
    "Hungary": {
        "flag": "🇭🇺",
        "fact": "Hungary is home to the world's largest thermal water cave system."
    },
    "Iceland": {
        "flag": "🇮🇸",
        "fact": "Iceland has no mosquitoes and is powered almost entirely by renewable energy."
    },
    "India:)": {
        "flag": "🇮🇳",
        "fact": "India is the world's largest democracy and home to over 1.3 billion people."
    },
    "Indonesia": {
        "flag": "🇮🇩",
        "fact": "Indonesia is the world's largest archipelago with over 17,000 islands."
    },
    "Iran": {
        "flag": "🇮🇷",
        "fact": "Iran (Persia) has one of the world's oldest civilizations, dating back over 5,000 years."
    },
    "Iraq": {
        "flag": "🇮🇶",
        "fact": "Iraq is home to ancient Mesopotamia, often called the 'Cradle of Civilization'."
    },
    "Ireland": {
        "flag": "🇮🇪",
        "fact": "Ireland is known as the 'Emerald Isle' due to its lush green landscapes."
    },
    "Israel": {
        "flag": "🇮🇱",
        "fact": "Israel has the world's highest concentration of high-tech companies outside of Silicon Valley."
    },
    "Italy": {
        "flag": "🇮🇹",
        "fact": "Italy is home to more UNESCO World Heritage sites than any other country."
    },
    "Ivory Coast": {
        "flag": "🇨🇮",
        "fact": "The Ivory Coast is the world's largest producer of cocoa beans."
    },
    "Jamaica": {
        "flag": "🇯🇲",
        "fact": "Jamaica is the birthplace of reggae music and the fastest sprinters in the world."
    },
    "Japan": {
        "flag": "🇯🇵",
        "fact": "Japan has the world's highest life expectancy and is known for its advanced technology."
    },
    "Jordan": {
        "flag": "🇯🇴",
        "fact": "Jordan is home to the ancient city of Petra, one of the New Seven Wonders of the World."
    },
    "Kazakhstan": {
        "flag": "🇰🇿",
        "fact": "Kazakhstan is the world's largest landlocked country and has the world's largest space launch facility."
    },
    "Kenya": {
        "flag": "🇰🇪",
        "fact": "Kenya is home to the Great Migration, the largest animal migration on Earth."
    },
    "Kiribati": {
        "flag": "🇰🇮",
        "fact": "Kiribati is the only country in the world that lies in all four hemispheres."
    },
    "Kuwait": {
        "flag": "🇰🇼",
        "fact": "Kuwait has the world's sixth-largest oil reserves."
    },
    "Kyrgyzstan": {
        "flag": "🇰🇬",
        "fact": "Kyrgyzstan is known as the 'Switzerland of Central Asia' due to its mountainous terrain."
    },
    "Laos": {
        "flag": "🇱🇦",
        "fact": "Laos is the most heavily bombed country in history per capita."
    },
    "Latvia": {
        "flag": "🇱🇻",
        "fact": "Latvia has one of the highest percentages of forest coverage in Europe."
    },
    "Lebanon": {
        "flag": "🇱🇧",
        "fact": "Lebanon is home to the ancient city of Byblos, one of the oldest continuously inhabited cities in the world."
    },
    "Lesotho": {
        "flag": "🇱🇸",
        "fact": "Lesotho is completely surrounded by South Africa and is the only country entirely above 1,000 meters elevation."
    },
    "Liberia": {
        "flag": "🇱🇷",
        "fact": "Liberia was founded by freed American slaves and has a flag similar to the United States."
    },
    "Libya": {
        "flag": "🇱🇾",
        "fact": "Libya is 90% desert and has the world's largest proven oil reserves in Africa."
    },
    "Liechtenstein": {
        "flag": "🇱🇮",
        "fact": "Liechtenstein is one of the world's smallest countries and has no army."
    },
    "Lithuania": {
        "flag": "🇱🇹",
        "fact": "Lithuania was the last European country to convert to Christianity in 1387."
    },
    "Luxembourg": {
        "flag": "🇱🇺",
        "fact": "Luxembourg has the highest GDP per capita in the world."
    },
    "Madagascar": {
        "flag": "🇲🇬",
        "fact": "Madagascar is home to unique wildlife found nowhere else on Earth, including lemurs."
    },
    "Malawi": {
        "flag": "🇲🇼",
        "fact": "Malawi is known as the 'Warm Heart of Africa' due to its friendly people."
    },
    "Malaysia": {
        "flag": "🇲🇾",
        "fact": "Malaysia is home to the world's largest flower, the Rafflesia arnoldii."
    },
    "Maldives": {
        "flag": "🇲🇻",
        "fact": "The Maldives is the world's lowest-lying country, with an average elevation of just 1.5 meters."
    },
    "Mali": {
        "flag": "🇲🇱",
        "fact": "Mali was home to the ancient city of Timbuktu, a center of Islamic learning."
    },
    "Malta": {
        "flag": "🇲🇹",
        "fact": "Malta has the world's highest concentration of historical sites per square kilometer."
    },
    "Marshall Islands": {
        "flag": "🇲🇭",
        "fact": "The Marshall Islands consists of 29 coral atolls and 5 islands."
    },
    "Mauritania": {
        "flag": "🇲🇷",
        "fact": "Mauritania is one of the least densely populated countries in the world."
    },
    "Mauritius": {
        "flag": "🇲🇺",
        "fact": "Mauritius is the only known habitat of the extinct dodo bird."
    },
    "Mexico": {
        "flag": "🇲🇽",
        "fact": "Mexico is home to the world's largest pyramid, the Great Pyramid of Cholula."
    },
    "Micronesia": {
        "flag": "🇫🇲",
        "fact": "Micronesia consists of over 600 islands spread across the western Pacific Ocean."
    },
    "Moldova": {
        "flag": "🇲🇩",
        "fact": "Moldova is known for its wine production and has the world's largest wine cellar."
    },
    "Monaco": {
        "flag": "🇲🇨",
        "fact": "Monaco is the second-smallest country in the world and has the world's highest population density."
    },
    "Mongolia": {
        "flag": "🇲🇳",
        "fact": "Mongolia is the world's most sparsely populated country."
    },
    "Montenegro": {
        "flag": "🇲🇪",
        "fact": "Montenegro means 'Black Mountain' and is known for its stunning Adriatic coastline."
    },
    "Morocco": {
        "flag": "🇲🇦",
        "fact": "Morocco is home to the world's largest desert, the Sahara, and the ancient city of Marrakech."
    },
    "Mozambique": {
        "flag": "🇲🇿",
        "fact": "Mozambique has a coastline of over 2,500 kilometers along the Indian Ocean."
    },
    "Myanmar": {
        "flag": "🇲🇲",
        "fact": "Myanmar is home to the world's largest book, the Kuthodaw Pagoda with 729 stone tablets."
    },
    "Namibia": {
        "flag": "🇳🇦",
        "fact": "Namibia has the world's oldest desert, the Namib, which is over 55 million years old."
    },
    "Nauru": {
        "flag": "🇳🇷",
        "fact": "Nauru is the world's smallest island nation and was once the richest country per capita due to phosphate mining."
    },
    "Nepal": {
        "flag": "🇳🇵",
        "fact": "Nepal is home to Mount Everest, the world's highest peak, and is the only country with a non-rectangular flag."
    },
    "Netherlands": {
        "flag": "🇳🇱",
        "fact": "The Netherlands is famous for its tulips, windmills, and being one of the world's most bicycle-friendly countries."
    },
    "New Zealand": {
        "flag": "🇳🇿",
        "fact": "New Zealand was the first country to give women the right to vote in 1893."
    },
    "Nicaragua": {
        "flag": "🇳🇮",
        "fact": "Nicaragua is home to the largest lake in Central America, Lake Nicaragua."
    },
    "Niger": {
        "flag": "🇳🇪",
        "fact": "Niger is one of the hottest countries in the world and has the world's highest fertility rate."
    },
    "Nigeria": {
        "flag": "🇳🇬",
        "fact": "Nigeria is Africa's most populous country and largest economy."
    },
    "North Korea": {
        "flag": "🇰🇵",
        "fact": "North Korea is one of the most isolated countries in the world."
    },
    "North Macedonia": {
        "flag": "🇲🇰",
        "fact": "North Macedonia is home to Lake Ohrid, one of the oldest lakes in the world."
    },
    "Norway": {
        "flag": "🇳🇴",
        "fact": "Norway has the world's longest coastline and is known for its fjords and northern lights."
    },
    "Oman": {
        "flag": "🇴🇲",
        "fact": "Oman was once a major trading power and has a rich maritime history."
    },
    "Pakistan": {
        "flag": "🇵🇰",
        "fact": "Pakistan is home to K2, the world's second-highest peak, and has the world's highest paved international border."
    },
    "Palau": {
        "flag": "🇵🇼",
        "fact": "Palau is home to the world's first shark sanctuary and has some of the best diving spots in the world."
    },
    "Panama": {
        "flag": "🇵🇦",
        "fact": "Panama is home to the Panama Canal, one of the most important shipping routes in the world."
    },
    "Papua New Guinea": {
        "flag": "🇵🇬",
        "fact": "Papua New Guinea is one of the most linguistically diverse countries with over 800 languages spoken."
    },
    "Paraguay": {
        "flag": "🇵🇾",
        "fact": "Paraguay is one of only two landlocked countries in South America."
    },
    "Peru": {
        "flag": "🇵🇪",
        "fact": "Peru is home to Machu Picchu, one of the New Seven Wonders of the World."
    },
    "Philippines": {
        "flag": "🇵🇭",
        "fact": "The Philippines consists of over 7,000 islands and is the world's largest producer of coconuts."
    },
    "Poland": {
        "flag": "🇵🇱",
        "fact": "Poland is home to the world's largest castle by land area, Malbork Castle."
    },
    "Portugal": {
        "flag": "🇵🇹",
        "fact": "Portugal is the oldest nation-state in Europe and was a major maritime power during the Age of Discovery."
    },
    "Qatar": {
        "flag": "🇶🇦",
        "fact": "Qatar has the world's highest GDP per capita and will host the 2022 FIFA World Cup."
    },
    "Romania": {
        "flag": "🇷🇴",
        "fact": "Romania is home to Transylvania, the legendary home of Count Dracula."
    },
    "Russia": {
        "flag": "🇷🇺",
        "fact": "Russia is the largest country in the world, spanning 11 time zones."
    },
    "Rwanda": {
        "flag": "🇷🇼",
        "fact": "Rwanda is known as the 'Land of a Thousand Hills' and has made remarkable progress since the 1994 genocide."
    },
    "Saint Kitts and Nevis": {
        "flag": "🇰🇳",
        "fact": "Saint Kitts and Nevis is the smallest country in the Western Hemisphere."
    },
    "Saint Lucia": {
        "flag": "🇱🇨",
        "fact": "Saint Lucia is the only country named after a woman, Saint Lucy of Syracuse."
    },
    "Saint Vincent and the Grenadines": {
        "flag": "🇻🇨",
        "fact": "Saint Vincent and the Grenadines consists of 32 islands and is known for its beautiful beaches."
    },
    "Samoa": {
        "flag": "🇼🇸",
        "fact": "Samoa is the first country to see the sunrise each day due to its location near the International Date Line."
    },
    "San Marino": {
        "flag": "🇸🇲",
        "fact": "San Marino is the world's oldest republic, founded in 301 AD."
    },
    "Sao Tome and Principe": {
        "flag": "🇸🇹",
        "fact": "Sao Tome and Principe is Africa's smallest country and was once the world's largest producer of cocoa."
    },
    "Saudi Arabia": {
        "flag": "🇸🇦",
        "fact": "Saudi Arabia has the world's largest oil reserves and is home to the two holiest sites in Islam."
    },
    "Senegal": {
        "flag": "🇸🇳",
        "fact": "Senegal is known as the 'Gateway to Africa' and has a rich cultural heritage."
    },
    "Serbia": {
        "flag": "🇷🇸",
        "fact": "Serbia is home to the world's largest raspberry exporter and has a rich Orthodox Christian heritage."
    },
    "Seychelles": {
        "flag": "🇸🇨",
        "fact": "Seychelles is an archipelago of 115 islands and has the smallest population of any African country."
    },
    "Sierra Leone": {
        "flag": "🇸🇱",
        "fact": "Sierra Leone is known for its diamond mines and was the first country to have a female president in Africa."
    },
    "Singapore": {
        "flag": "🇸🇬",
        "fact": "Singapore is one of the world's most densely populated countries and a major financial center."
    },
    "Slovakia": {
        "flag": "🇸🇰",
        "fact": "Slovakia has the world's highest number of castles and chateaux per capita."
    },
    "Slovenia": {
        "flag": "🇸🇮",
        "fact": "Slovenia is home to Lake Bled, one of the most beautiful lakes in Europe."
    },
    "Solomon Islands": {
        "flag": "🇸🇧",
        "fact": "The Solomon Islands consists of over 900 islands and is known for its World War II history."
    },
    "Somalia": {
        "flag": "🇸🇴",
        "fact": "Somalia has the longest coastline in mainland Africa."
    },
    "South Africa": {
        "flag": "🇿🇦",
        "fact": "South Africa is the only country in the world with three capital cities."
    },
    "South Korea": {
        "flag": "🇰🇷",
        "fact": "South Korea has the world's fastest internet speeds and is a global leader in technology."
    },
    "South Sudan": {
        "flag": "🇸🇸",
        "fact": "South Sudan is the world's newest country, gaining independence in 2011."
    },
    "Spain": {
        "flag": "🇪🇸",
        "fact": "Spain is home to the world's largest tomato fight, La Tomatina, held annually in Buñol."
    },
    "Sri Lanka": {
        "flag": "🇱🇰",
        "fact": "Sri Lanka is the world's fourth-largest producer of tea and was the first country to have a female prime minister."
    },
    "Sudan": {
        "flag": "🇸🇩",
        "fact": "Sudan is home to more pyramids than Egypt, with over 200 ancient pyramids."
    },
    "Suriname": {
        "flag": "🇸🇷",
        "fact": "Suriname is the smallest country in South America and has the highest percentage of forest coverage."
    },
    "Sweden": {
        "flag": "🇸🇪",
        "fact": "Sweden is home to the Nobel Prize and has one of the world's most generous welfare systems."
    },
    "Switzerland": {
        "flag": "🇨🇭",
        "fact": "Switzerland is known for its neutrality, chocolate, watches, and the Swiss Alps."
    },
    "Syria": {
        "flag": "🇸🇾",
        "fact": "Syria is home to the ancient city of Damascus, one of the oldest continuously inhabited cities in the world."
    },
    "Taiwan": {
        "flag": "🇹🇼",
        "fact": "Taiwan is a global leader in semiconductor manufacturing and technology."
    },
    "Tajikistan": {
        "flag": "🇹🇯",
        "fact": "Tajikistan is the most mountainous country in Central Asia, with over 90% of its territory covered by mountains."
    },
    "Tanzania": {
        "flag": "🇹🇿",
        "fact": "Tanzania is home to Mount Kilimanjaro, Africa's highest peak, and the Serengeti National Park."
    },
    "Thailand": {
        "flag": "🇹🇭",
        "fact": "Thailand is the only Southeast Asian country never to have been colonized by European powers."
    },
    "Togo": {
        "flag": "🇹🇬",
        "fact": "Togo is a narrow strip of land in West Africa and was once a major center of the slave trade."
    },
    "Tonga": {
        "flag": "🇹🇴",
        "fact": "Tonga is the only Pacific island nation that was never colonized by European powers."
    },
    "Trinidad and Tobago": {
        "flag": "🇹🇹",
        "fact": "Trinidad and Tobago is the birthplace of calypso music and the steelpan, the only acoustic instrument invented in the 20th century."
    },
    "Tunisia": {
        "flag": "🇹🇳",
        "fact": "Tunisia is home to the ancient city of Carthage and was the starting point of the Arab Spring in 2011."
    },
    "Turkey": {
        "flag": "🇹🇷",
        "fact": "Turkey is the only country that spans two continents, Europe and Asia."
    },
    "Turkmenistan": {
        "flag": "🇹🇲",
        "fact": "Turkmenistan has the world's largest natural gas reserves and is known for its marble cities."
    },
    "Tuvalu": {
        "flag": "🇹🇻",
        "fact": "Tuvalu is one of the smallest countries in the world and is threatened by rising sea levels."
    },
    "Uganda": {
        "flag": "🇺🇬",
        "fact": "Uganda is home to half of the world's remaining mountain gorillas."
    },
    "Ukraine": {
        "flag": "🇺🇦",
        "fact": "Ukraine is the largest country entirely in Europe and is known as the 'Breadbasket of Europe'."
    },
    "United Arab Emirates": {
        "flag": "🇦🇪",
        "fact": "The UAE is home to the world's tallest building, the Burj Khalifa, and has the world's largest artificial island."
    },
    "United Kingdom": {
        "flag": "🇬🇧",
        "fact": "The United Kingdom is home to the world's oldest parliament and the world's largest library."
    },
    "United States": {
        "flag": "🇺🇸",
        "fact": "The United States has the world's largest economy and is home to the world's most visited national park, Great Smoky Mountains."
    },
    "Uruguay": {
        "flag": "🇺🇾",
        "fact": "Uruguay is the only country in South America that is entirely south of the Tropic of Capricorn."
    },
    "Uzbekistan": {
        "flag": "🇺🇿",
        "fact": "Uzbekistan is one of only two doubly landlocked countries in the world."
    },
    "Vanuatu": {
        "flag": "🇻🇺",
        "fact": "Vanuatu is home to the world's most accessible active volcano, Mount Yasur."
    },
    "Vatican City": {
        "flag": "🇻🇦",
        "fact": "Vatican City is the smallest country in the world and the headquarters of the Roman Catholic Church."
    },
    "Venezuela": {
        "flag": "🇻🇪",
        "fact": "Venezuela is home to Angel Falls, the world's highest uninterrupted waterfall."
    },
    "Vietnam": {
        "flag": "🇻🇳",
        "fact": "Vietnam is the world's second-largest coffee producer and has the world's largest cave, Son Doong."
    },
    "Yemen": {
        "flag": "🇾🇪",
        "fact": "Yemen is home to the ancient city of Sana'a, a UNESCO World Heritage site."
    },
    "Zambia": {
        "flag": "🇿🇲",
        "fact": "Zambia is home to Victoria Falls, one of the largest waterfalls in the world."
    },
    "Zimbabwe": {
        "flag": "🇿🇼",
        "fact": "Zimbabwe is home to the ancient city of Great Zimbabwe, a UNESCO World Heritage site."
    }
}

def get_background_image():
    """Get the background image as base64 string"""
    try:
        with open("ChatGPT Image Jul 28, 2025, 11_58_24 PM.png", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        return encoded_string
    except:
        return None

def get_flag_image_url(country_name):
    """Get flag image URL from flagcdn.com"""
    # Convert country name to ISO code (simplified mapping)
    country_codes = {
        "Afghanistan": "af", "Albania": "al", "Algeria": "dz", "Andorra": "ad", "Angola": "ao",
        "Antigua and Barbuda": "ag", "Argentina": "ar", "Armenia": "am", "Australia": "au", "Austria": "at",
        "Azerbaijan": "az", "Bahamas": "bs", "Bahrain": "bh", "Bangladesh": "bd", "Barbados": "bb",
        "Belarus": "by", "Belgium": "be", "Belize": "bz", "Benin": "bj", "Bhutan": "bt",
        "Bolivia": "bo", "Bosnia and Herzegovina": "ba", "Botswana": "bw", "Brazil": "br", "Brunei": "bn",
        "Bulgaria": "bg", "Burkina Faso": "bf", "Burundi": "bi", "Cambodia": "kh", "Cameroon": "cm",
        "Canada": "ca", "Cape Verde": "cv", "Central African Republic": "cf", "Chad": "td", "Chile": "cl",
        "China": "cn", "Colombia": "co", "Comoros": "km", "Congo": "cg", "Costa Rica": "cr",
        "Croatia": "hr", "Cuba": "cu", "Cyprus": "cy", "Czech Republic": "cz", "Denmark": "dk",
        "Djibouti": "dj", "Dominica": "dm", "Dominican Republic": "do", "East Timor": "tl", "Ecuador": "ec",
        "Egypt": "eg", "El Salvador": "sv", "Equatorial Guinea": "gq", "Eritrea": "er", "Estonia": "ee",
        "Eswatini": "sz", "Ethiopia": "et", "Fiji": "fj", "Finland": "fi", "France": "fr",
        "Gabon": "ga", "Gambia": "gm", "Georgia": "ge", "Germany": "de", "Ghana": "gh",
        "Greece": "gr", "Grenada": "gd", "Guatemala": "gt", "Guinea": "gn", "Guinea-Bissau": "gw",
        "Guyana": "gy", "Haiti": "ht", "Honduras": "hn", "Hungary": "hu", "Iceland": "is",
        "India": "in", "Indonesia": "id", "Iran": "ir", "Iraq": "iq", "Ireland": "ie",
        "Israel": "il", "Italy": "it", "Ivory Coast": "ci", "Jamaica": "jm", "Japan": "jp",
        "Jordan": "jo", "Kazakhstan": "kz", "Kenya": "ke", "Kiribati": "ki", "Kuwait": "kw",
        "Kyrgyzstan": "kg", "Laos": "la", "Latvia": "lv", "Lebanon": "lb", "Lesotho": "ls",
        "Liberia": "lr", "Libya": "ly", "Liechtenstein": "li", "Lithuania": "lt", "Luxembourg": "lu",
        "Madagascar": "mg", "Malawi": "mw", "Malaysia": "my", "Maldives": "mv", "Mali": "ml",
        "Malta": "mt", "Marshall Islands": "mh", "Mauritania": "mr", "Mauritius": "mu", "Mexico": "mx",
        "Micronesia": "fm", "Moldova": "md", "Monaco": "mc", "Mongolia": "mn", "Montenegro": "me",
        "Morocco": "ma", "Mozambique": "mz", "Myanmar": "mm", "Namibia": "na", "Nauru": "nr",
        "Nepal": "np", "Netherlands": "nl", "New Zealand": "nz", "Nicaragua": "ni", "Niger": "ne",
        "Nigeria": "ng", "North Korea": "kp", "North Macedonia": "mk", "Norway": "no", "Oman": "om",
        "Pakistan": "pk", "Palau": "pw", "Panama": "pa", "Papua New Guinea": "pg", "Paraguay": "py",
        "Peru": "pe", "Philippines": "ph", "Poland": "pl", "Portugal": "pt", "Qatar": "qa",
        "Romania": "ro", "Russia": "ru", "Rwanda": "rw", "Saint Kitts and Nevis": "kn", "Saint Lucia": "lc",
        "Saint Vincent and the Grenadines": "vc", "Samoa": "ws", "San Marino": "sm", "Sao Tome and Principe": "st", "Saudi Arabia": "sa",
        "Senegal": "sn", "Serbia": "rs", "Seychelles": "sc", "Sierra Leone": "sl", "Singapore": "sg",
        "Slovakia": "sk", "Slovenia": "si", "Solomon Islands": "sb", "Somalia": "so", "South Africa": "za",
        "South Korea": "kr", "South Sudan": "ss", "Spain": "es", "Sri Lanka": "lk", "Sudan": "sd",
        "Suriname": "sr", "Sweden": "se", "Switzerland": "ch", "Syria": "sy", "Taiwan": "tw",
        "Tajikistan": "tj", "Tanzania": "tz", "Thailand": "th", "Togo": "tg", "Tonga": "to",
        "Trinidad and Tobago": "tt", "Tunisia": "tn", "Turkey": "tr", "Turkmenistan": "tm", "Tuvalu": "tv",
        "Uganda": "ug", "Ukraine": "ua", "United Arab Emirates": "ae", "United Kingdom": "gb", "United States": "us",
        "Uruguay": "uy", "Uzbekistan": "uz", "Vanuatu": "vu", "Vatican City": "va", "Venezuela": "ve",
        "Vietnam": "vn", "Yemen": "ye", "Zambia": "zm", "Zimbabwe": "zw"
    }
    
    country_code = country_codes.get(country_name, "un")
    return f"https://flagcdn.com/w320/{country_code}.png"

def get_hint(country_name):
    """Generate an additional fact about the country"""
    # Additional facts for countries (different from the main facts)
    additional_facts = {
        "Afghanistan": "They are home to the ancient city of Kabul and have been a crossroads of civilizations for thousands of years.",
        "Albania": "They have one of the highest numbers of bunkers per capita in the world, built during the communist era.",
        "Algeria": "They are the largest country in Africa by land area and have the world's largest desert, the Sahara.",
        "Argentina": "They are famous for tango dancing and have the world's highest waterfall, Iguazu Falls.",
        "Australia": "They are home to unique wildlife like kangaroos and koalas, and have the world's largest coral reef system.",
        "Brazil": "They are the world's largest producer of coffee and are home to the Amazon Rainforest.",
        "Canada": "They have the world's longest coastline and are known for their maple syrup production.",
        "China": "They are home to the Great Wall, which is over 13,000 miles long, and have the world's largest population.",
        "France": "They are famous for their wine, cheese, and the Eiffel Tower in Paris.",
        "Germany": "They are known for their beer, sausages, and the famous Oktoberfest celebration.",
        "India": "They are the world's largest democracy and are famous for their Bollywood film industry.",
        "Italy": "They are home to more UNESCO World Heritage sites than any other country in the world.",
        "Japan": "They have the world's highest life expectancy and are famous for their bullet trains.",
        "Mexico": "They are the birthplace of chocolate and have the world's largest pyramid, the Great Pyramid of Cholula.",
        "Netherlands": "They are famous for their tulips, windmills, and being one of the most bicycle-friendly countries.",
        "Russia": "They span 11 time zones and are the largest country in the world by land area.",
        "South Africa": "They are the world's largest producer of platinum and have three capital cities.",
        "Spain": "They are famous for flamenco dancing and have the world's largest tomato fight, La Tomatina.",
        "United Kingdom": "They have the world's oldest parliament and are home to the world's largest library.",
        "United States": "They have the world's largest economy and are home to the world's most visited national park."
    }
    
    # Return additional fact if available, otherwise generate a diverse fact
    if country_name in additional_facts:
        return additional_facts[country_name]
    else:
        # Generate diverse facts based on country characteristics
        diverse_facts = [
            f"They are known for their beautiful landscapes and natural wonders.",
            f"They have a fascinating history that spans many centuries.",
            f"They are famous for their delicious traditional cuisine.",
            f"They have produced many famous artists and musicians.",
            f"They are home to ancient historical sites and monuments.",
            f"They have unique festivals and celebrations throughout the year.",
            f"They are known for their traditional crafts and handmade goods.",
            f"They have diverse wildlife and natural ecosystems.",
            f"They are famous for their traditional dances and music.",
            f"They have important archaeological discoveries.",
            f"They are known for their traditional clothing and textiles.",
            f"They have beautiful beaches and coastal areas.",
            f"They are famous for their traditional sports and games.",
            f"They have important religious and spiritual sites.",
            f"They are known for their traditional medicine and healing practices.",
            f"They have unique architectural styles and buildings.",
            f"They are famous for their traditional storytelling and literature.",
            f"They have important trade routes and commercial history.",
            f"They are known for their traditional farming and agriculture.",
            f"They have beautiful mountain ranges and hiking trails."
        ]
        return random.choice(diverse_facts)

def set_background():
    """Set background with countries flags"""
    # Set page background to black
    st.set_page_config(
        page_title="Flag Guessing Game",
        page_icon="🏳️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Load the countries flags background with heavy tinting
    try:
        background_image = get_background_image()
        if background_image:
            st.markdown(
                f"""
                <style>
                .stApp {{
                    background-image: url("data:image/png;base64,{background_image}");
                    background-size: cover;
                    background-repeat: no-repeat;
                    background-attachment: fixed;
                }}
                .stApp::before {{
                    content: '';
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background-color: rgba(0, 0, 0, 0.9);
                    z-index: -1;
                }}
                .content-container {{
                    background-color: white;
                    padding: 8px;
                    border-radius: 6px;
                    margin: 3px 0;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.3);
                    max-width: 85vw;
                    width: 100%;
                    margin-left: auto;
                    margin-right: auto;
                }}
                .score-container {{
                    background-color: white;
                    padding: 6px;
                    border-radius: 6px;
                    margin: 3px 0;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.3);
                    max-width: 85vw;
                    width: 100%;
                    margin-left: auto;
                    margin-right: auto;
                }}
                .flag-container {{
                    background-color: white;
                    padding: 6px;
                    border-radius: 6px;
                    margin: 3px 0;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.3);
                    max-width: 85vw;
                    width: 100%;
                    margin-left: auto;
                    margin-right: auto;
                    text-align: center;
                }}
                .options-container {{
                    background-color: white;
                    padding: 6px;
                    border-radius: 6px;
                    margin: 3px 0;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.3);
                    max-width: 85vw;
                    width: 100%;
                    margin-left: auto;
                    margin-right: auto;
                }}
                .result-container {{
                    background-color: white;
                    padding: 6px;
                    border-radius: 6px;
                    margin: 3px 0;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.3);
                    max-width: 85vw;
                    width: 100%;
                    margin-left: auto;
                    margin-right: auto;
                }}
                .user-choice {{
                    background-color: #e3f2fd;
                    border: 1px solid #2196f3;
                    border-radius: 4px;
                    padding: 4px;
                    margin: 2px 0;
                    text-align: center;
                    font-weight: bold;
                    color: #1976d2;
                    font-size: 12px;
                }}
                .stButton > button {{
                    width: 100%;
                    margin: 1px 0;
                    padding: 6px 12px;
                    font-size: 13px;
                    min-height: 35px;
                }}
                @media (max-width: 768px) {{
                    .content-container, .score-container, .flag-container, .options-container, .result-container {{
                        max-width: 92vw;
                        padding: 4px;
                    }}
                    h1 {{
                        font-size: 18px !important;
                    }}
                    h2 {{
                        font-size: 16px !important;
                    }}
                    h3 {{
                        font-size: 12px !important;
                    }}
                    p {{
                        font-size: 11px !important;
                    }}
                    .stButton > button {{
                        font-size: 11px;
                        padding: 4px 8px;
                        min-height: 30px;
                    }}
                }}
                @media (max-width: 480px) {{
                    .content-container, .score-container, .flag-container, .options-container, .result-container {{
                        max-width: 96vw;
                        padding: 3px;
                    }}
                    h1 {{
                        font-size: 16px !important;
                    }}
                    h2 {{
                        font-size: 14px !important;
                    }}
                    h3 {{
                        font-size: 10px !important;
                    }}
                    p {{
                        font-size: 10px !important;
                    }}
                    .stButton > button {{
                        font-size: 10px;
                        padding: 3px 6px;
                        min-height: 28px;
                    }}
                }}
                h1 {{
                    font-size: 20px !important;
                    margin: 6px 0 !important;
                }}
                h2 {{
                    font-size: 16px !important;
                    margin: 4px 0 !important;
                }}
                h3 {{
                    font-size: 14px !important;
                    margin: 3px 0 !important;
                }}
                p {{
                    font-size: 12px !important;
                    margin: 3px 0 !important;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
        else:
            # Fallback to black background
            st.markdown(
                """
                <style>
                .stApp {
                    background: #000000 !important;
                }
                            .content-container {
                background-color: white;
                padding: 8px;
                border-radius: 6px;
                margin: 3px 0;
                box-shadow: 0 1px 3px rgba(0,0,0,0.3);
                max-width: 85vw;
                width: 100%;
                margin-left: auto;
                margin-right: auto;
            }
            .score-container {
                background-color: white;
                padding: 6px;
                border-radius: 6px;
                margin: 3px 0;
                box-shadow: 0 1px 3px rgba(0,0,0,0.3);
                max-width: 85vw;
                width: 100%;
                margin-left: auto;
                margin-right: auto;
            }
            .flag-container {
                background-color: white;
                padding: 6px;
                border-radius: 6px;
                margin: 3px 0;
                box-shadow: 0 1px 3px rgba(0,0,0,0.3);
                max-width: 85vw;
                width: 100%;
                margin-left: auto;
                margin-right: auto;
                text-align: center;
            }
            .options-container {
                background-color: white;
                padding: 6px;
                border-radius: 6px;
                margin: 3px 0;
                box-shadow: 0 1px 3px rgba(0,0,0,0.3);
                max-width: 85vw;
                width: 100%;
                margin-left: auto;
                margin-right: auto;
            }
            .result-container {
                background-color: white;
                padding: 6px;
                border-radius: 6px;
                margin: 3px 0;
                box-shadow: 0 1px 3px rgba(0,0,0,0.3);
                max-width: 85vw;
                width: 100%;
                margin-left: auto;
                margin-right: auto;
            }
                            .user-choice {
                background-color: #e3f2fd;
                border: 1px solid #2196f3;
                border-radius: 4px;
                padding: 4px;
                margin: 2px 0;
                text-align: center;
                font-weight: bold;
                color: #1976d2;
                font-size: 12px;
            }
            .stButton > button {
                width: 100%;
                margin: 1px 0;
                padding: 6px 12px;
                font-size: 13px;
                min-height: 35px;
            }
                            @media (max-width: 768px) {
                .content-container, .score-container, .flag-container, .options-container, .result-container {
                    max-width: 92vw;
                    padding: 4px;
                }
                h1 {
                    font-size: 18px !important;
                }
                h2 {
                    font-size: 16px !important;
                }
                h3 {
                    font-size: 12px !important;
                }
                p {
                    font-size: 11px !important;
                }
                .stButton > button {
                    font-size: 11px;
                    padding: 4px 8px;
                    min-height: 30px;
                }
            }
            @media (max-width: 480px) {
                .content-container, .score-container, .flag-container, .options-container, .result-container {
                    max-width: 96vw;
                    padding: 3px;
                }
                h1 {
                    font-size: 16px !important;
                }
                h2 {
                    font-size: 14px !important;
                }
                h3 {
                    font-size: 10px !important;
                }
                p {
                    font-size: 10px !important;
                }
                .stButton > button {
                    font-size: 10px;
                    padding: 3px 6px;
                    min-height: 28px;
                }
            }
                h1 {
                    font-size: 24px !important;
                    margin: 10px 0 !important;
                }
                h2 {
                    font-size: 20px !important;
                    margin: 8px 0 !important;
                }
                h3 {
                    font-size: 16px !important;
                    margin: 6px 0 !important;
                }
                p {
                    font-size: 14px !important;
                    margin: 5px 0 !important;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
    except:
        # Fallback to black background
        st.markdown(
            """
            <style>
            .stApp {
                background: #000000 !important;
            }
            .content-container {
                background-color: white;
                padding: 15px;
                border-radius: 8px;
                margin: 5px 0;
                box-shadow: 0 2px 4px rgba(0,0,0,0.3);
                max-width: 800px;
                margin-left: auto;
                margin-right: auto;
            }
            .score-container {
                background-color: white;
                padding: 10px;
                border-radius: 8px;
                margin: 5px 0;
                box-shadow: 0 2px 4px rgba(0,0,0,0.3);
                max-width: 600px;
                margin-left: auto;
                margin-right: auto;
            }
            .flag-container {
                background-color: white;
                padding: 10px;
                border-radius: 8px;
                margin: 5px 0;
                box-shadow: 0 2px 4px rgba(0,0,0,0.3);
                max-width: 400px;
                margin-left: auto;
                margin-right: auto;
                text-align: center;
            }
            .options-container {
                background-color: white;
                padding: 10px;
                border-radius: 8px;
                margin: 5px 0;
                box-shadow: 0 2px 4px rgba(0,0,0,0.3);
                max-width: 500px;
                margin-left: auto;
                margin-right: auto;
            }
            .result-container {
                background-color: white;
                padding: 10px;
                border-radius: 8px;
                margin: 5px 0;
                box-shadow: 0 2px 4px rgba(0,0,0,0.3);
                max-width: 600px;
                margin-left: auto;
                margin-right: auto;
            }
            .stButton > button {
                width: 100%;
                margin: 2px 0;
                padding: 8px 16px;
                font-size: 14px;
            }
            h1 {
                font-size: 20px !important;
                margin: 6px 0 !important;
            }
            h2 {
                font-size: 16px !important;
                margin: 4px 0 !important;
            }
            h3 {
                font-size: 14px !important;
                margin: 3px 0 !important;
            }
            p {
                font-size: 12px !important;
                margin: 3px 0 !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

def main():
    st.set_page_config(
        page_title="Country Flag Guessing Game",
        page_icon="🏳️",
        layout="wide"
    )
    
    set_background()
    
    # Initialize session state
    if 'current_flag' not in st.session_state:
        st.session_state.current_flag = None
    if 'options' not in st.session_state:
        st.session_state.options = []
    if 'correct_answer' not in st.session_state:
        st.session_state.correct_answer = None
    if 'show_result' not in st.session_state:
        st.session_state.show_result = False
    if 'user_answer' not in st.session_state:
        st.session_state.user_answer = None
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'total_questions' not in st.session_state:
        st.session_state.total_questions = 0
    if 'show_hint' not in st.session_state:
        st.session_state.show_hint = False
    
    # Header
    st.markdown(
        """
        <div class="content-container">
            <h1 style="text-align: center; color: #333;">🏳️ Country Flag Guessing Game 🏳️</h1>
            <p style="text-align: center; color: #666; font-size: 18px;"><strong>Test your knowledge of world flags!</strong></p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Score display
    st.markdown(
        f"""
        <div class="score-container">
            <div style="display: flex; justify-content: space-around; text-align: center;">
                <div>
                    <h3 style="color: #000000;">Score</h3>
                    <h2 style="color: #007bff;">{st.session_state.score}</h2>
                </div>
                <div>
                    <h3 style="color: #000000;">Total Questions</h3>
                    <h2 style="color: #28a745;">{st.session_state.total_questions}</h2>
                </div>
                <div>
                    <h3 style="color: #000000;">Accuracy</h3>
                    <h2 style="color: #ffc107;">{(st.session_state.score / max(st.session_state.total_questions, 1)) * 100:.1f}%</h2>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Main game area
    if st.session_state.current_flag is None or st.button("🎯 Guess the Country Flag", key="new_game"):
        # Generate new question
        st.session_state.correct_answer = random.choice(list(COUNTRIES_DATA.keys()))
        st.session_state.current_flag = COUNTRIES_DATA[st.session_state.correct_answer]["flag"]
        
        # Generate 3 wrong options
        wrong_options = [country for country in COUNTRIES_DATA.keys() if country != st.session_state.correct_answer]
        wrong_options = random.sample(wrong_options, 3)
        
        # Create options list and shuffle
        st.session_state.options = [st.session_state.correct_answer] + wrong_options
        random.shuffle(st.session_state.options)
        
        st.session_state.show_result = False
        st.session_state.user_answer = None
        st.session_state.show_hint = False
    
    # Display current flag
    if st.session_state.current_flag and st.session_state.correct_answer:
        st.markdown(
            """
            <div class="content-container">
                <h2 style="text-align: center; color: #333;">Which country does this flag belong to?</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Display flag image
        st.markdown(
            """
            <div class="flag-container">
            """,
            unsafe_allow_html=True
        )
        
        try:
            flag_url = get_flag_image_url(st.session_state.correct_answer)
            # Use smaller, responsive image sizing
            st.image(flag_url, width=200)
        except:
            # Fallback to emoji
            st.markdown(f"**Flag:** {st.session_state.current_flag}")
            st.markdown(f"**Flag Emoji:** {st.session_state.current_flag}")
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Display hint button and options
        if not st.session_state.show_result:
            st.markdown(
                """
                <div class="options-container">
                """,
                unsafe_allow_html=True
            )
            
            # Hint button
            if st.button("💡 Hint", key="hint_button"):
                st.session_state.show_hint = True
                st.rerun()
            
            # Show hint if requested
            if st.session_state.show_hint:
                hint_text = get_hint(st.session_state.correct_answer)
                st.markdown(
                    f"""
                    <div style="background-color: #d1ecf1; border: 1px solid white; border-radius: 4px; padding: 6px; margin: 3px 0;">
                        <h4 style="color: #0c5460; margin: 0 0 3px 0; font-size: 12px;">💡 Hint</h4>
                        <p style="color: #333; margin: 0; font-size: 11px;">{hint_text}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            # Display options
            for i, option in enumerate(st.session_state.options):
                if st.button(option, key=f"option_{i}"):
                    st.session_state.user_answer = option
                    st.session_state.show_result = True
                    st.session_state.total_questions += 1
                    if option == st.session_state.correct_answer:
                        st.session_state.score += 1
                    st.rerun()
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Show result
        if st.session_state.show_result and st.session_state.user_answer:
            st.markdown(
                """
                <div class="result-container">
                """,
                unsafe_allow_html=True
            )
            
            # Show user's choice
            st.markdown(
                f"""
                <div class="user-choice">
                    <p style="margin: 0; font-size: 14px;">You chose: <strong>{st.session_state.user_answer}</strong></p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            if st.session_state.user_answer == st.session_state.correct_answer:
                st.markdown(
                    """
                    <div style="background-color: #d4edda; border: 1px solid white; border-radius: 4px; padding: 6px; margin: 3px 0; text-align: center;">
                        <h3 style="color: #155724; margin: 0; font-size: 14px;">🎉 Correct! Well done!</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"""
                    <div style="background-color: #f8d7da; border: 1px solid white; border-radius: 4px; padding: 6px; margin: 3px 0; text-align: center;">
                        <h3 style="color: #721c24; margin: 0; font-size: 14px;">❌ Wrong! The correct answer is: <strong>{st.session_state.correct_answer}</strong></h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            # Show fact
            fact = COUNTRIES_DATA[st.session_state.correct_answer]["fact"]
            st.markdown(
                f"""
                <div style="background-color: #fff3cd; border: 1px solid white; border-radius: 4px; padding: 6px; margin: 3px 0;">
                    <h4 style="color: #856404; margin: 0 0 3px 0; font-size: 12px;">💡 Did you know?</h4>
                    <p style="color: #333; margin: 0; font-size: 11px;"><strong>{st.session_state.correct_answer}:</strong> {fact}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Next question button
            if st.button("🔄 Next Question"):
                st.session_state.current_flag = None
                st.rerun()
            
            st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main() 