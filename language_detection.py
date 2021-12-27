from langdetect import detect

all_language_codes ={
    "en": "English",
    "hi": "Hindi",
    "mr": "Marathi",
    "pa": "Punjabi",
    "ur": "Urdu",
    "urd": "Urdu",
    "gu": "Gujarati",
    "guj": "Gujarati",
    "te": "Telegu"

}

input_sentences = [
    "मैं एक नया मोबाइल खरीदने की योजना बना रहा हूँ",
    "मी नवीन मोबाईल घेण्याचा विचार करत आहे",
    "నేను కొత్త మొబైల్ కొనాలని ప్లాన్ చేస్తున్నాను",
    "I am planning to buy a new mobile",
    "હું નવો મોબાઈલ ખરીદવાનું વિચારી રહ્યો છું",
    "ਮੈਂ ਇੱਕ ਨਵਾਂ ਮੋਬਾਈਲ ਖਰੀਦਣ ਦੀ ਯੋਜਨਾ ਬਣਾ ਰਿਹਾ ਹਾਂ"
]

lemmatizer_names = ["Language Code","Input Sentences"]
format_text = '{:24}' *(len(lemmatizer_names)+ 1)
print ("\n", format_text.format("Language Name", *lemmatizer_names), '\n' '='*0)
for data in input_sentences:
    language_code = detect(data)
    sentence = [all_language_codes.get(language_code), language_code, data]
    print (format_text.format(*sentence))